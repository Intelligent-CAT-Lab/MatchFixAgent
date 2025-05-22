from __future__ import annotations
import time
import re
import sys
import unittest
import pytest
import io
import typing
from typing import *
import datetime
import os
import unittest
from src.main.org.apache.commons.pool2.impl.LinkedBlockingDeque import *


class TestLinkedBlockingDeque(unittest.TestCase):

    __THREE: int = 3
    __TWO: int = 2
    __ONE: int = 1
    __TIMEOUT_50_MILLIS: datetime.timedelta = datetime.timedelta(milliseconds=50)
    deque: LinkedBlockingDeque[int] = None

    def testToArray_test4_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        arr = self.deque.toArray()
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])
        arr = self.deque.toArray([])
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])
        arr = self.deque.toArray([])
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])

    def testToArray_test3_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        arr = self.deque.toArray()
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])
        arr = self.deque.toArray([])
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])
        arr = self.deque.toArray([])
        self.assertEqual(1, arr[0])

    def testToArray_test2_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        arr = self.deque.toArray()
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])
        arr = self.deque.toArray([])
        self.assertEqual(1, arr[0])

    def testToArray_test1_decomposed(self) -> None:
        self.deque = LinkedBlockingDeque[int]()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        arr = self.deque.toArray()
        self.assertEqual(self.__ONE, arr[0])

    def testToArray_test0_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testTakeLast_test1_decomposed(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(self.__ONE, self.deque.takeLast())

    def testTakeLast_test0_decomposed(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))

    def testTakeFirst_test1_decomposed(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(self.__TWO, self.deque.takeFirst())

    def testTakeFirst_test0_decomposed(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))

    def testTake_test1_decomposed(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(self.__TWO, self.deque.take())

    def testTake_test0_decomposed(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))

    def testRemoveLastOccurrence_test3_decomposed(self) -> None:
        self.assertFalse(self.deque.removeLastOccurrence(None))
        self.assertFalse(self.deque.removeLastOccurrence(self.__ONE))
        self.deque.add(self.__ONE)
        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.removeLastOccurrence(self.__ONE))
        self.assertEqual(1, self.deque.size())

    def testRemoveLastOccurrence_test2_decomposed(self) -> None:
        self.assertFalse(self.deque.removeLastOccurrence(None))
        self.assertFalse(self.deque.removeLastOccurrence(self.__ONE))
        self.deque.add(self.__ONE)
        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.removeLastOccurrence(self.__ONE))

    def testRemoveLastOccurrence_test1_decomposed(self) -> None:
        self.assertFalse(self.deque.removeLastOccurrence(None))
        self.assertFalse(self.deque.removeLastOccurrence(self.__ONE))
        self.deque.add(self.__ONE)
        self.deque.add(self.__ONE)

    def testRemoveLastOccurrence_test0_decomposed(self) -> None:
        self.assertFalse(self.deque.removeLastOccurrence(None))
        self.assertFalse(self.deque.removeLastOccurrence(self.__ONE))

    def testRemoveLast_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.removeLast()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        self.assertEqual(self.__TWO, self.deque.removeLast())

        with self.assertRaises(RuntimeError):
            self.deque.removeLast()
            self.deque.removeLast()

    def testRemoveLast_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.removeLast()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testRemoveLast_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.remove_last()
        self.deque.add(self.__ONE)

    def testRemoveFirst_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.removeFirst()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__ONE, self.deque.removeFirst())
        with self.assertRaises(RuntimeError):
            self.deque.removeFirst()
            self.deque.removeFirst()

    def testRemoveFirst_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.removeFirst()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testRemoveFirst_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.removeFirst()
        self.deque.add(self.__ONE)

    def testRemove_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.remove()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__ONE, self.deque.remove())

    def testRemove_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.remove()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testRemove_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.remove()
        self.deque.add(self.__ONE)

    def testPutLast_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putLast(None)
        self.deque.putLast(self.__ONE)
        self.deque.putLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        self.assertEqual(self.__ONE, self.deque.pop())

    def testPutLast_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putLast(None)
        self.deque.putLast(self.__ONE)
        self.deque.putLast(self.__TWO)
        self.assertEqual(2, self.deque.size())

    def testPutLast_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putLast(None)
        self.deque.putLast(self.__ONE)
        self.deque.putLast(self.__TWO)

    def testPutFirst_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putFirst(None)
        self.deque.putFirst(self.__ONE)
        self.deque.putFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        self.assertEqual(self.__TWO, self.deque.pop())

    def testPutFirst_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putFirst(None)
        self.deque.putFirst(self.__ONE)
        self.deque.putFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())

    def testPutFirst_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putFirst(None)
        self.deque.putFirst(self.__ONE)
        self.deque.putFirst(self.__TWO)

    def testPut_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.put(None)
        self.deque.put(self.__ONE)
        self.deque.put(self.__TWO)

    def testPush_test3_decomposed(self) -> None:
        self.deque.push(self.__ONE)
        self.deque.push(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.push(self.__THREE)
        self.assertEqual(self.__TWO, self.deque.pop())

    def testPush_test2_decomposed(self) -> None:
        self.deque.push(self.__ONE)
        self.deque.push(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.push(self.__THREE)

    def testPush_test1_decomposed(self) -> None:
        self.deque.push(self.__ONE)
        self.deque.push(self.__TWO)
        self.assertEqual(2, self.deque.size())

    def testPush_test0_decomposed(self) -> None:
        self.deque.push(self.__ONE)
        self.deque.push(self.__TWO)

    def testPossibleBug_test5_decomposed(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            self.deque.add(int(i))
        iter = iter(self.deque)
        next(iter)
        self.deque.remove(int(1))
        self.deque.remove(int(0))
        self.deque.remove(int(2))
        next(iter)

    def testPossibleBug_test4_decomposed(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            self.deque.add(int(i))
        iter = iter(self.deque)
        next(iter)
        self.deque.remove(1)
        self.deque.remove(0)
        self.deque.remove(2)

    def testPossibleBug_test3_decomposed(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            self.deque.add(int(i))
        iter = iter(self.deque)
        next(iter)

    def testPossibleBug_test2_decomposed(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            self.deque.add(int(i))
        iter_ = iter(self.deque)

    def testPossibleBug_test1_decomposed(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            self.deque.add(int(i))

    def testPossibleBug_test0_decomposed(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()

    def testPop_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.pop()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        self.assertEqual(self.__ONE, self.deque.pop())

        with self.assertRaises(RuntimeError):
            self.deque.pop()
            self.deque.pop()

    def testPop_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.pop()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testPop_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.pop()

    def testPollWithTimeout_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.poll1(self.__TIMEOUT_50_MILLIS))
        self.assertIsNone(self.deque.poll1(self.__TIMEOUT_50_MILLIS))

    def testPollLastWithTimeout_test1_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollLast())
        self.assertIsNone(self.deque.pollLast1(self.__TIMEOUT_50_MILLIS))

    def testPollLastWithTimeout_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollLast())

    def testPollLast_test2_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollLast())
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(self.__ONE, self.deque.pollLast())

    def testPollLast_test1_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollLast())
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))

    def testPollLast_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollLast())

    def testPollFirstWithTimeout_test1_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollFirst())
        self.assertIsNone(self.deque.pollFirst1(self.__TIMEOUT_50_MILLIS))

    def testPollFirstWithTimeout_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollFirst())

    def testPollFirst_test2_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollFirst())
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(self.__TWO, self.deque.pollFirst())

    def testPollFirst_test1_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollFirst())
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))

    def testPollFirst_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.pollFirst())

    def testPeekLast_test2_decomposed(self) -> None:
        self.assertIsNone(self.deque.peek_last())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__TWO, self.deque.peek_last())

    def testPeekLast_test1_decomposed(self) -> None:
        self.assertIsNone(self.deque.peekLast())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testPeekLast_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.peekLast())

    def testPeekFirst_test2_decomposed(self) -> None:
        self.assertIsNone(self.deque.peekFirst())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__ONE, self.deque.peekFirst())

    def testPeekFirst_test1_decomposed(self) -> None:
        self.assertIsNone(self.deque.peekFirst())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testPeekFirst_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.peekFirst())

    def testPeek_test2_decomposed(self) -> None:
        self.assertIsNone(self.deque.peek())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__ONE, self.deque.peek())

    def testPeek_test1_decomposed(self) -> None:
        self.assertIsNone(self.deque.peek())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testPeek_test0_decomposed(self) -> None:
        self.assertIsNone(self.deque.peek())

    def testOfferWithTimeout_test0_decomposed(self) -> None:
        self.assertTrue(self.deque.offer1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offer1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offer1(self.__THREE, self.__TIMEOUT_50_MILLIS))
        with self.assertRaises(RuntimeError):
            self.deque.offer1(None, self.__TIMEOUT_50_MILLIS)

    def testOfferLastWithTimeout_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.offerLast1(None, self.__TIMEOUT_50_MILLIS)
        self.assertTrue(self.deque.offerLast1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offerLast1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offerLast1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferLast_test3_decomposed(self) -> None:
        self.deque.offerLast(self.__ONE)
        self.deque.offerLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.offerLast(None)
        self.assertEqual(self.__ONE, self.deque.pop())

    def testOfferLast_test2_decomposed(self) -> None:
        self.deque.offerLast(self.__ONE)
        self.deque.offerLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.offerLast(None)

    def testOfferLast_test1_decomposed(self) -> None:
        self.deque.offerLast(self.__ONE)
        self.deque.offerLast(self.__TWO)
        self.assertEqual(2, self.deque.size())

    def testOfferLast_test0_decomposed(self) -> None:
        self.deque.offerLast(self.__ONE)
        self.deque.offerLast(self.__TWO)

    def testOfferFirstWithTimeout_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.offerFirst1(None, self.__TIMEOUT_50_MILLIS)
        self.assertTrue(self.deque.offerFirst1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offerFirst1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offerFirst1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferFirst_test3_decomposed(self) -> None:
        self.deque.offerFirst(self.__ONE)
        self.deque.offerFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.offerFirst(None)
        self.assertEqual(self.__TWO, self.deque.pop())

    def testOfferFirst_test2_decomposed(self) -> None:
        self.deque.offerFirst(self.__ONE)
        self.deque.offerFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.offerFirst(None)

    def testOfferFirst_test1_decomposed(self) -> None:
        self.deque.offerFirst(self.__ONE)
        self.deque.offerFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())

    def testOfferFirst_test0_decomposed(self) -> None:
        self.deque.offerFirst(self.__ONE)
        self.deque.offerFirst(self.__TWO)

    def testOffer_test0_decomposed(self) -> None:
        self.assertTrue(self.deque.offer(self.__ONE))
        self.assertTrue(self.deque.offer(self.__TWO))
        self.assertFalse(self.deque.offer(self.__THREE))
        with self.assertRaises(RuntimeError):
            self.deque.offer(None)

    def testIterator_test5_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.iterator().next()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.iterator()
        self.assertEqual(self.__ONE, iter.next())
        iter.remove()
        self.assertEqual(self.__TWO, iter.next())

    def testIterator_test4_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            next(self.deque.iterator())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.iterator()
        self.assertEqual(self.__ONE, next(iter))
        iter.remove()

    def testIterator_test3_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.iterator().next()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.iterator()
        self.assertEqual(self.__ONE, iter.next())

    def testIterator_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            next(self.deque.iterator())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.iterator()

    def testIterator_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            next(self.deque.iterator())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testIterator_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.iterator().next()

    def testGetLast_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.getLast()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__TWO, self.deque.getLast())

    def testGetLast_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.getLast()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testGetLast_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.getLast()

    def testGetFirst_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.getFirst()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__ONE, self.deque.getFirst())

    def testGetFirst_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.getFirst()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testGetFirst_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.getFirst()

    def testElement_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.element()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(self.__ONE, self.deque.element())

    def testElement_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.element()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testElement_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.element()

    def testDrainTo_test10_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))
        self.assertEqual(1, self.deque.size())
        self.assertEqual(1, len(c))

        iterator = iter(c)
        self.assertEqual(self.__ONE, next(iterator))

    def testDrainTo_test9_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))
        self.assertEqual(1, self.deque.size())
        self.assertEqual(1, len(c))

        iter(c)  # Equivalent to calling `c.iterator()` in Java
        int(1)  # Equivalent to `Integer.valueOf(1)` in Java

    def testDrainTo_test8_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))
        self.assertEqual(1, self.deque.size())
        self.assertEqual(1, len(c))
        iter(c)  # Equivalent to calling `c.iterator()` in Java

    def testDrainTo_test7_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))
        self.assertEqual(1, self.deque.size())
        self.assertEqual(1, len(c))

    def testDrainTo_test6_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))

    def testDrainTo_test5_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))
        c = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testDrainTo_test4_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))
        c = []
        self.deque.add(self.__ONE)

    def testDrainTo_test3_decomposed(self) -> None:
        c: List[int] = []  # Using a list to mimic the Collection in Java
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo(c))
        self.assertEqual(2, len(c))

    def testDrainTo_test2_decomposed(self) -> None:
        c: List[int] = []  # Using a list to represent the collection
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo(c))

    def testDrainTo_test1_decomposed(self) -> None:
        c: List[int] = []  # Using a list to represent the Collection
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testDrainTo_test0_decomposed(self) -> None:
        c: List[int] = []
        self.deque.add(self.__ONE)

    def testDescendingIterator_test5_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.descendingIterator().next()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        iter = self.deque.descendingIterator()
        self.assertEqual(self.__TWO, iter.next())
        iter.remove()
        self.assertEqual(self.__ONE, iter.next())

    def testDescendingIterator_test4_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.descendingIterator().next()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.descendingIterator()
        self.assertEqual(2, iter.next())
        iter.remove()

    def testDescendingIterator_test3_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.descendingIterator().next()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.descendingIterator()
        self.assertEqual(self.__TWO, iter.next())

    def testDescendingIterator_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.descendingIterator().next()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.descendingIterator()

    def testDescendingIterator_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.descendingIterator().next()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testDescendingIterator_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.descendingIterator().next()

    def testContains_test3_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.contains(self.__ONE))
        self.assertFalse(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(None))
        self.deque.add(self.__TWO)
        self.assertTrue(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(self.__THREE))

    def testContains_test2_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.contains(self.__ONE))
        self.assertFalse(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(None))
        self.deque.add(self.__TWO)

    def testContains_test1_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.contains(self.__ONE))
        self.assertFalse(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(None))

    def testContains_test0_decomposed(self) -> None:
        self.deque.add(self.__ONE)

    def testConstructors_test6_decomposed(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remaining_capacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        self.assertEqual(2, deque.remaining_capacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, self.__TWO])
        self.assertEqual(2, deque.size())

        with self.assertRaises(RuntimeError):
            LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, None])

    def testConstructors_test5_decomposed(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remainingCapacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        self.assertEqual(2, deque.remainingCapacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, self.__TWO])
        self.assertEqual(2, deque.size())

    def testConstructors_test4_decomposed(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remainingCapacity())
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        self.assertEqual(2, deque.remainingCapacity())
        deque = LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, self.__TWO])

    def testConstructors_test3_decomposed(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remaining_capacity())
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        self.assertEqual(2, deque.remaining_capacity())

    def testConstructors_test2_decomposed(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remaining_capacity())
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)

    def testConstructors_test1_decomposed(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remaining_capacity())

    def testConstructors_test0_decomposed(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()

    def testClear_test3_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.deque.clear()
        self.deque.add(self.__ONE)
        self.assertEqual(1, self.deque.size())

    def testClear_test2_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.deque.clear()
        self.deque.add(self.__ONE)

    def testClear_test1_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.deque.clear()

    def testClear_test0_decomposed(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

    def testAddLast_test3_decomposed(self) -> None:
        self.deque.addLast(self.__ONE)
        self.deque.addLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)
        self.assertEqual(self.__ONE, self.deque.pop())

    def testAddLast_test2_decomposed(self) -> None:
        self.deque.addLast(self.__ONE)
        self.deque.addLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)

    def testAddLast_test1_decomposed(self) -> None:
        self.deque.addLast(self.__ONE)
        self.deque.addLast(self.__TWO)
        self.assertEqual(2, self.deque.size())

    def testAddLast_test0_decomposed(self) -> None:
        self.deque.addLast(self.__ONE)
        self.deque.addLast(self.__TWO)

    def testAddFirst_test3_decomposed(self) -> None:
        self.deque.addFirst(self.__ONE)
        self.deque.addFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)
        self.assertEqual(self.__TWO, self.deque.pop())

    def testAddFirst_test2_decomposed(self) -> None:
        self.deque.addFirst(self.__ONE)
        self.deque.addFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)

    def testAddFirst_test1_decomposed(self) -> None:
        self.deque.addFirst(self.__ONE)
        self.deque.addFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())

    def testAddFirst_test0_decomposed(self) -> None:
        self.deque.addFirst(self.__ONE)
        self.deque.addFirst(self.__TWO)

    def testAdd_test0_decomposed(self) -> None:
        self.assertTrue(self.deque.add(self.__ONE))
        self.assertTrue(self.deque.add(self.__TWO))
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)
        with self.assertRaises(RuntimeError):
            self.deque.add(None)

    def setUp(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
