from __future__ import annotations
import time
import re
import sys
import os
from abc import ABC
import io
import threading
import typing
from typing import *
import datetime
import pickle
from src.main.org.apache.commons.pool2.impl.InterruptibleReentrantLock import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class LinkedBlockingDeque(Deque):

    __notFull: threading.Condition = None

    __notEmpty: threading.Condition = None

    __lock: InterruptibleReentrantLock = None

    __capacity: int = 0

    __count: int = 0

    __last: Node[typing.Any] = None

    __first: Node[typing.Any] = None

    __serialVersionUID: int = -387911632671998426

    def toString(self) -> str:
        self.__lock.lock()
        try:
            return super().__str__()
        finally:
            self.__lock.unlock()

    def toArray1(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:
        self.__lock.lock()
        try:
            if len(a) < self.__count:
                a = [None] * self.__count  # Create a new list with the required size
            k = 0
            p = self.__first
            while p is not None:
                a[k] = p.item
                k += 1
                p = p.next
            if len(a) > k:
                a[k] = None
            return a
        finally:
            self.__lock.unlock()

    def size(self) -> int:
        self.__lock.lock()
        try:
            return self.__count
        finally:
            self.__lock.unlock()

    def removeLastOccurrence(self, o: typing.Any) -> bool:
        if o is None:
            return False
        self.__lock.lock()
        try:
            p = self.__last
            while p is not None:
                if o == p.item:
                    self.__unlink(p)
                    return True
                p = p.prev
            return False
        finally:
            self.__lock.unlock()

    def removeLast(self) -> typing.Any:
        x = self.pollLast0()
        if x is None:
            raise RuntimeError()
        return x

    def removeFirstOccurrence(self, o: typing.Any) -> bool:
        if o is None:
            return False
        self.__lock.lock()
        try:
            p = self.__first
            while p is not None:
                if o == p.item:
                    self.__unlink(p)
                    return True
                p = p.next
            return False
        finally:
            self.__lock.unlock()

    def removeFirst(self) -> typing.Any:
        x = self.pollFirst0()
        if x is None:
            raise RuntimeError()
        return x

    def push(self, e: typing.Any) -> None:
        self.addFirst(e)

    def pop(self) -> typing.Any:
        return self.removeFirst()

    def pollLast(self) -> typing.Any:
        return self.pollLast0()

    def pollFirst(self) -> typing.Any:
        return self.pollFirst0()

    def poll(self) -> typing.Any:
        return self.poll0()

    def peekLast(self) -> typing.Any:
        self.__lock.lock()
        try:
            return None if self.__last is None else self.__last.item
        finally:
            self.__lock.unlock()

    def peekFirst(self) -> typing.Any:
        self.__lock.lock()
        try:
            return None if self.__first is None else self.__first.item
        finally:
            self.__lock.unlock()

    def peek(self) -> typing.Any:
        return self.peekFirst()

    def offerFirst(self, e: typing.Any) -> bool:
        return self.offerFirst0(e)

    def offer(self, e: typing.Any) -> bool:
        return self.offer0(e)

    def iterator(self) -> typing.Iterator[typing.Any]:
        return self.Itr()

    def getLast(self) -> typing.Any:
        x = self.peekLast()
        if x is None:
            raise RuntimeError()
        return x

    def getFirst(self) -> typing.Any:
        x = self.peekFirst()
        if x is None:
            raise RuntimeError()
        return x

    def element(self) -> typing.Any:
        return self.getFirst()

    def descendingIterator(self) -> typing.Iterator[typing.Any]:
        return self.__reversed__()

    def contains(self, o: typing.Any) -> bool:
        if o is None:
            return False
        self.__lock.lock()
        try:
            p = self.__first
            while p is not None:
                if o == p.item:
                    return True
                p = p.next
            return False
        finally:
            self.__lock.unlock()

    def clear(self) -> None:
        self.__lock.lock()
        try:
            f = self.__first
            while f is not None:
                f.item = None
                n = f.next
                f.prev = None
                f.next = None
                f = n
            self.__first = self.__last = None
            self.__count = 0
            self.__notFull.notify_all()
        finally:
            self.__lock.unlock()

    def addLast(self, e: typing.Any) -> None:
        if not self.offerLast0(e):
            raise RuntimeError("Deque full")

    def addFirst(self, e: typing.Any) -> None:
        if not self.offerFirst0(e):
            raise RuntimeError("Deque full")

    def add(self, e: typing.Any) -> bool:
        self.addLast(e)
        return True

    def toArray0(self) -> typing.List[typing.Any]:
        self.__lock.lock()
        try:
            a = [None] * self.__count  # Create a list with the size of __count
            k = 0
            p = self.__first
            while p is not None:
                a[k] = p.item
                k += 1
                p = p.next
            return a
        finally:
            self.__lock.unlock()

    def takeLast(self) -> typing.Any:
        self.__lock.lock()
        try:
            x = None
            while (x := self.__unlinkLast()) is None:
                self.__notEmpty.wait()
            return x
        finally:
            self.__lock.unlock()

    def takeFirst(self) -> typing.Any:
        self.__lock.lock()
        try:
            x = None
            while (x := self.__unlinkFirst()) is None:
                self.__notEmpty.wait()
            return x
        finally:
            self.__lock.unlock()

    def take(self) -> typing.Any:
        return self.takeFirst()

    def remove1(self, o: typing.Any) -> bool:
        return self.removeFirstOccurrence(o)

    def remove0(self) -> typing.Any:
        return self.removeFirst()

    def remainingCapacity(self) -> int:
        self.__lock.lock()
        try:
            return self.__capacity - self.__count
        finally:
            self.__lock.unlock()

    def putLast(self, e: typing.Any) -> None:
        if e is None:
            raise ValueError("e must not be None")
        self.__lock.lock()
        try:
            while not self.__linkLast(e):
                self.__notFull.wait()
        finally:
            self.__lock.unlock()

    def putFirst(self, e: typing.Any) -> None:
        if e is None:
            raise ValueError("e must not be None")
        self.__lock.lock()
        try:
            while not self.__linkFirst(e):
                self.__notFull.wait()
        finally:
            self.__lock.unlock()

    def put(self, e: typing.Any) -> None:
        self.putLast(e)

    def pollLast2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        return self.pollLast1(PoolImplUtils.toDuration(timeout, unit))

    def pollLast1(self, timeout: datetime.timedelta) -> typing.Any:
        nanos = int(timeout.total_seconds() * 1e9)  # Convert timeout to nanoseconds
        self.__lock.lockInterruptibly()
        try:
            x = None
            while (x := self.__unlinkLast()) is None:
                if nanos <= 0:
                    return None
                nanos = (
                    self.__notEmpty.wait_for(
                        lambda: self.__unlinkLast() is not None, timeout.total_seconds()
                    )
                    * 1e9
                )
            return x
        finally:
            self.__lock.unlock()

    def pollLast0(self) -> typing.Any:
        self.__lock.lock()
        try:
            return self.__unlinkLast()
        finally:
            self.__lock.unlock()

    def pollFirst2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        return self.pollFirst1(PoolImplUtils.toDuration(timeout, unit))

    def pollFirst0(self) -> typing.Any:
        self.__lock.lock()
        try:
            return self.__unlinkFirst()
        finally:
            self.__lock.unlock()

    def poll2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        return self.pollFirst2(timeout, unit)

    def poll0(self) -> typing.Any:
        return self.pollFirst0()

    def offerLast2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:
        return self.offerLast1(e, PoolImplUtils.toDuration(timeout, unit))

    def offerLast0(self, e: typing.Any) -> bool:
        if e is None:
            raise ValueError("e must not be None")
        self.__lock.lock()
        try:
            return self.__linkLast(e)
        finally:
            self.__lock.unlock()

    def offerLast(self, e: typing.Any) -> bool:
        return self.offerLast0(e)

    def offerFirst2(
        self, e: typing.Any, timeout: int, unit: datetime.timedelta
    ) -> bool:
        return self.offerFirst1(e, PoolImplUtils.toDuration(timeout, unit))

    def offerFirst1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        if e is None:
            raise ValueError("e must not be None")

        nanos = int(timeout.total_seconds() * 1e9)  # Convert timeout to nanoseconds
        self.__lock.lockInterruptibly()
        try:
            while not self.__linkFirst(e):
                if nanos <= 0:
                    return False
                nanos = (
                    self.__notFull.wait_for(lambda: False, timeout.total_seconds())
                    * 1e9
                )
            return True
        finally:
            self.__lock.unlock()

    def offerFirst0(self, e: typing.Any) -> bool:
        if e is None:
            raise ValueError("e must not be None")
        self.__lock.lock()
        try:
            return self.__linkFirst(e)
        finally:
            self.__lock.unlock()

    def offer2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:
        return self.offerLast2(e, timeout, unit)

    def offer0(self, e: typing.Any) -> bool:
        return self.offerLast0(e)

    def interuptTakeWaiters(self) -> None:
        self.__lock.lock()
        try:
            self.__lock.interruptWaiters(self.__notEmpty)
        finally:
            self.__lock.unlock()

    def hasTakeWaiters(self) -> bool:
        self.__lock.lock()
        try:
            return self.__lock.has_waiters(self.__notEmpty)
        finally:
            self.__lock.unlock()

    def getTakeQueueLength(self) -> int:
        self.__lock.lock()
        try:
            return self.__lock.getWaitQueueLength(self.__notEmpty)
        finally:
            self.__lock.unlock()

    def drainTo1(self, c: typing.Collection[typing.Any], maxElements: int) -> int:
        if c is self:
            raise ValueError("c cannot be the same as this deque")

        self.__lock.lock()
        try:
            n = min(maxElements, self.__count)
            for _ in range(n):
                c.add(self.__first.item)  # Add the item to the collection
                self.__unlinkFirst()  # Remove the first node
            return n
        finally:
            self.__lock.unlock()

    def drainTo0(self, c: typing.Collection[typing.Any]) -> int:
        return self.drainTo1(c, float("inf"))

    def __init__(
        self,
        constructorId: int,
        capacity: int,
        fairness: bool,
        c: typing.Optional[typing.Collection[typing.Any]] = None,
    ) -> None:
        if constructorId == 0:
            if capacity <= 0:
                raise ValueError("Capacity must be greater than 0")
            self.__capacity = capacity
            self.__lock = InterruptibleReentrantLock(fairness)
            self.__notEmpty = threading.Condition(self.__lock)
            self.__notFull = threading.Condition(self.__lock)

            if c is not None:
                with self.__lock:  # Lock for thread safety and visibility
                    for e in c:
                        if e is None:
                            raise ValueError("Collection contains None")
                        if not self.__linkLast(e):
                            raise RuntimeError("Deque full")
        else:
            self.__capacity = capacity
            self.__lock = InterruptibleReentrantLock(fairness)
            self.__notEmpty = threading.Condition(self.__lock)
            self.__notFull = threading.Condition(self.__lock)

    @staticmethod
    def LinkedBlockingDeque3(capacity: int) -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, capacity, False, None)

    @staticmethod
    def LinkedBlockingDeque2(
        c: typing.Collection[typing.Any],
    ) -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, int(1e9), False, c)

    @staticmethod
    def LinkedBlockingDeque1(fairness: bool) -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, float("inf"), fairness, None)

    @staticmethod
    def LinkedBlockingDeque0() -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, sys.maxsize, False, None)

    def __writeObject(self, s: pickle.Pickler) -> None:
        self.__lock.lock()
        try:
            s.dump(self)  # Equivalent to s.defaultWriteObject() in Java
            current = self.__first
            while current is not None:
                s.dump(current.item)
                current = current.next
            s.dump(None)  # Write a null marker at the end
        finally:
            self.__lock.unlock()

    def __unlinkLast(self) -> typing.Any:
        l = self.__last
        if l is None:
            return None
        p = l.prev
        item = l.item
        l.item = None
        l.prev = l  # help GC
        self.__last = p
        if p is None:
            self.__first = None
        else:
            p.next = None
        self.__count -= 1
        self.__notFull.notify()  # Signal the condition variable
        return item

    def __unlinkFirst(self) -> typing.Any:
        f = self.__first
        if f is None:
            return None
        n = f.next
        item = f.item
        f.item = None
        f.next = f  # help GC
        self.__first = n
        if n is None:
            self.__last = None
        else:
            n.prev = None
        self.__count -= 1
        self.__notFull.notify()  # Equivalent to `signal()` in Java
        return item

    def __unlink(self, x: Node[typing.Any]) -> None:
        p = x.prev
        n = x.next
        if p is None:
            self.__unlinkFirst()
        elif n is None:
            self.__unlinkLast()
        else:
            p.next = n
            n.prev = p
            x.item = None
            self.__count -= 1
            self.__notFull.notify()  # Equivalent to `signal()` in Java

    def __readObject(self, s: pickle.Unpickler) -> None:
        # Read the non-transient fields
        s.default_load()

        # Initialize transient fields
        self.__count = 0
        self.__first = None
        self.__last = None

        # Read and add items until a None is encountered
        while True:
            item = s.load()
            if item is None:
                break
            self.add(item)

    def __linkLast(self, e: typing.Any) -> bool:
        if self.__count >= self.__capacity:
            return False
        l = self.__last
        x = Node()
        x.value = e  # Assuming Node has a `value` attribute to store the element
        x.prev = l  # Assuming Node has a `prev` attribute for the previous node
        x.next = None
        self.__last = x
        if self.__first is None:
            self.__first = x
        else:
            l.next = x
        self.__count += 1
        self.__notEmpty.notify()  # Notify a thread waiting on the condition
        return True

    def __linkFirst(self, e: typing.Any) -> bool:
        if self.__count >= self.__capacity:
            return False
        f = self.__first
        x = Node()
        x.item = e
        x.next = f
        self.__first = x
        if self.__last is None:
            self.__last = x
        else:
            f.prev = x
        self.__count += 1
        self.__notEmpty.notify()  # Notify a thread waiting on the condition
        return True

    def pollFirst1(self, timeout: datetime.timedelta) -> typing.Any:
        nanos = int(timeout.total_seconds() * 1e9)  # Convert timeout to nanoseconds
        self.__lock.lockInterruptibly()
        try:
            x = None
            while (x := self.__unlinkFirst()) is None:
                if nanos <= 0:
                    return None
                nanos = (
                    self.__notEmpty.wait_for(
                        lambda: self.__unlinkFirst() is not None,
                        timeout.total_seconds(),
                    )
                    * 1e9
                )
            return x
        finally:
            self.__lock.unlock()

    def poll1(self, timeout: datetime.timedelta) -> typing.Any:
        return self.pollFirst1(timeout)

    def offerLast1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        if e is None:
            raise ValueError("e must not be None")

        nanos = int(timeout.total_seconds() * 1e9)  # Convert timeout to nanoseconds
        self.__lock.lockInterruptibly()
        try:
            while not self.__linkLast(e):
                if nanos <= 0:
                    return False
                nanos = (
                    self.__notFull.wait_for(lambda: False, timeout=nanos / 1e9) * 1e9
                )
            return True
        finally:
            self.__lock.unlock()

    def offer1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        return self.offerLast1(e, timeout)


class AbstractItr(ABC):

    __lastRet: Node[typing.Any] = None

    nextItem: typing.Any = None

    next: Node[typing.Any] = None

    def remove(self) -> None:
        n = self.__lastRet
        if n is None:
            raise RuntimeError()
        self.__lastRet = None
        lock.lock()
        try:
            if n.item is not None:
                self.__unlink(n)
        finally:
            lock.unlock()

    def next_(self) -> typing.Any:
        if self.next is None:
            raise RuntimeError()
        self.__lastRet = self.next
        x = self.nextItem
        self.advance()
        return x

    def hasNext(self) -> bool:
        return self.next is not None

    def __succ(self, n: Node[typing.Any]) -> Node[typing.Any]:
        while True:
            s = self.nextNode(n)
            if s is None:
                return None
            if s.item is not None:
                return s
            if s == n:
                return self.firstNode()
            n = s

    def advance(self) -> None:
        self.__lock.lock()
        try:
            self.next = self.__succ(self.next)
            self.nextItem = None if self.next is None else self.next.item
        finally:
            self.__lock.unlock()

    def __init__(self) -> None:
        self.lock.lock()
        try:
            self.next = self.firstNode()
            self.nextItem = None if self.next is None else self.next.item
        finally:
            self.lock.unlock()

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        # This method is abstract in Java, so it should raise a NotImplementedError in Python
        raise NotImplementedError("Subclasses must implement this method")

    def firstNode(self) -> Node[typing.Any]:
        return self.__first


class DescendingItr(AbstractItr):

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        return n.prev

    def firstNode(self) -> Node[typing.Any]:
        return self._LinkedBlockingDeque__last


class Node:

    next: Node = None

    prev: Node = None

    item: typing.Any = None

    def __init__(self, x: typing.Any, p: Node, n: Node) -> None:
        self.item = x
        self.prev = p
        self.next = n


class Itr(AbstractItr):

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        return n.next

    def firstNode(self) -> Node[typing.Any]:
        return self._Itr__first
