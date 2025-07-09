from __future__ import annotations
import time
import copy
import re
import threading
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import datetime
import os
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.SwallowedExceptionListener import *
from src.main.org.apache.commons.pool2.impl.AbandonedConfig import *
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class BaseGenericObjectPool(BaseObject, ABC):

    _abandonedConfig: AbandonedConfig = None

    destroyedByBorrowValidationCount: int = 0
    destroyedByEvictorCount: int = 0
    destroyedCount: int = 0
    createdCount: int = 0
    evictionLock: typing.Any = object()
    closed: bool = False

    closeLock: typing.Any = object()
    MEAN_TIMING_STATS_CACHE_SIZE: int = 100
    __messageStatistics: bool = False

    __swallowedExceptionListener: SwallowedExceptionListener = None

    __maxBorrowWaitDuration: typing.Generic[
        typing.TypeVar("T", bound=datetime.timedelta)
    ] = None  # LLM could not translate this field

    __waitTimes: StatsStore = None  # LLM could not translate this field

    __idleTimes: StatsStore = None  # LLM could not translate this field

    __activeTimes: StatsStore = None  # LLM could not translate this field

    __returnedCount: int = 0
    __borrowedCount: int = 0
    __evictor: Evictor = None

    __evictorShutdownTimeoutDuration: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
    )
    __evictionPolicy: EvictionPolicy[typing.Any] = None

    __softMinEvictableIdleDuration: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION
    )
    __minEvictableIdleDuration: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION
    )
    __numTestsPerEvictionRun: int = (
        BaseObjectPoolConfig.DEFAULT_NUM_TESTS_PER_EVICTION_RUN
    )
    __durationBetweenEvictionRuns: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_TIME_BETWEEN_EVICTION_RUNS
    )
    __testWhileIdle: bool = BaseObjectPoolConfig.DEFAULT_TEST_WHILE_IDLE
    __testOnReturn: bool = BaseObjectPoolConfig.DEFAULT_TEST_ON_RETURN
    __testOnBorrow: bool = BaseObjectPoolConfig.DEFAULT_TEST_ON_BORROW
    __testOnCreate: bool = BaseObjectPoolConfig.DEFAULT_TEST_ON_CREATE
    __lifo: bool = BaseObjectPoolConfig.DEFAULT_LIFO
    __maxWaitDuration: datetime.timedelta = BaseObjectPoolConfig.DEFAULT_MAX_WAIT
    __blockWhenExhausted: bool = BaseObjectPoolConfig.DEFAULT_BLOCK_WHEN_EXHAUSTED
    __maxTotal: int = GenericKeyedObjectPoolConfig.DEFAULT_MAX_TOTAL
    __DEFAULT_REMOVE_ABANDONED_TIMEOUT: datetime.timedelta = datetime.timedelta(
        seconds=int(2**31 - 1)
    )
    __EVICTION_POLICY_TYPE_NAME: str = EvictionPolicy.__name__
    evictionIterator: EvictionIterator = None

    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        if isinstance(builder, list):
            append = builder.append
        elif isinstance(builder, io.StringIO):
            append = builder.write
        else:
            raise TypeError("builder must be a list or StringIO")

        append("maxTotal=")
        append(str(self.__maxTotal))
        append(", blockWhenExhausted=")
        append(str(self.__blockWhenExhausted))
        append(", maxWaitDuration=")
        append(str(self.__maxWaitDuration))
        append(", lifo=")
        append(str(self.__lifo))
        append(", fairness=")
        append(str(self.__fairness))
        append(", testOnCreate=")
        append(str(self.__testOnCreate))
        append(", testOnBorrow=")
        append(str(self.__testOnBorrow))
        append(", testOnReturn=")
        append(str(self.__testOnReturn))
        append(", testWhileIdle=")
        append(str(self.__testWhileIdle))
        append(", durationBetweenEvictionRuns=")
        append(str(self.__durationBetweenEvictionRuns))
        append(", numTestsPerEvictionRun=")
        append(str(self.__numTestsPerEvictionRun))
        append(", minEvictableIdleTimeDuration=")
        append(str(self.__minEvictableIdleDuration))
        append(", softMinEvictableIdleTimeDuration=")
        append(str(self.__softMinEvictableIdleDuration))
        append(", evictionPolicy=")
        append(str(self.__evictionPolicy))
        append(", closeLock=")
        append(str(self.closeLock))
        append(", closed=")
        append(str(self.closed))
        append(", evictionLock=")
        append(str(self.evictionLock))
        append(", evictor=")
        append(str(self.__evictor))
        append(", evictionIterator=")
        append(str(self.evictionIterator))
        append(", factoryClassLoader=")
        append("None")  # Placeholder for factoryClassLoader
        append(", oname=")
        append("None")  # Placeholder for oname
        append(", creationStackTrace=")
        append("None")  # Placeholder for creationStackTrace
        append(", borrowedCount=")
        append(str(self.__borrowedCount))
        append(", returnedCount=")
        append(str(self.__returnedCount))
        append(", createdCount=")
        append(str(self.createdCount))
        append(", destroyedCount=")
        append(str(self.destroyedCount))
        append(", destroyedByEvictorCount=")
        append(str(self.destroyedByEvictorCount))
        append(", destroyedByBorrowValidationCount=")
        append(str(self.destroyedByBorrowValidationCount))
        append(", activeTimes=")
        append(str(self.__activeTimes))
        append(", idleTimes=")
        append(str(self.__idleTimes))
        append(", waitTimes=")
        append(str(self.__waitTimes))
        append(", maxBorrowWaitDuration=")
        append(str(self.__maxBorrowWaitDuration))
        append(", swallowedExceptionListener=")
        append(str(self.__swallowedExceptionListener))

    def setSoftMinEvictableIdleTimeMillis(
        self, softMinEvictableIdleTimeMillis: int
    ) -> None:
        self.setSoftMinEvictableIdleTime(
            datetime.timedelta(milliseconds=softMinEvictableIdleTimeMillis)
        )

    def setSoftMinEvictableIdleTime(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        self.__softMinEvictableIdleDuration = PoolImplUtils.nonNull(
            softMinEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setMinEvictableIdleTimeMillis(self, minEvictableIdleTimeMillis: int) -> None:
        self.setMinEvictableIdleTime(
            datetime.timedelta(milliseconds=minEvictableIdleTimeMillis)
        )

    def setMinEvictableIdleTime(self, minEvictableIdleTime: datetime.timedelta) -> None:
        self.__minEvictableIdleDuration = PoolImplUtils.nonNull(
            minEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setMaxWaitMillis(self, maxWaitMillis: int) -> None:
        self.setMaxWait(datetime.timedelta(milliseconds=maxWaitMillis))

    def setEvictorShutdownTimeoutMillis(
        self, evictorShutdownTimeoutMillis: int
    ) -> None:
        self.setEvictorShutdownTimeout(
            datetime.timedelta(milliseconds=evictorShutdownTimeoutMillis)
        )

    def getTimeBetweenEvictionRunsMillis(self) -> int:
        return int(self.__durationBetweenEvictionRuns.total_seconds() * 1000)

    def getTimeBetweenEvictionRuns(self) -> datetime.timedelta:
        return self.__durationBetweenEvictionRuns

    def getSoftMinEvictableIdleTimeMillis(self) -> int:
        return int(self.__softMinEvictableIdleDuration.total_seconds() * 1000)

    def getSoftMinEvictableIdleTime(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

    def getRemoveAbandonedTimeout(self) -> int:
        return int(self.getRemoveAbandonedTimeoutDuration().total_seconds())

    def getMinEvictableIdleTimeMillis(self) -> int:
        return int(self.__minEvictableIdleDuration.total_seconds() * 1000)

    def getMinEvictableIdleTime(self) -> datetime.timedelta:
        return self.__minEvictableIdleDuration

    def getMaxWaitMillis(self) -> int:
        return int(self.__maxWaitDuration.total_seconds() * 1000)

    def getEvictorShutdownTimeoutMillis(self) -> int:
        return int(self.__evictorShutdownTimeoutDuration.total_seconds() * 1000)

    def getEvictorShutdownTimeout(self) -> datetime.timedelta:
        return self.__evictorShutdownTimeoutDuration

    def __setEvictionPolicy1(self, className: str, classLoader: typing.Any) -> None:
        clazz = getattr(__import__(className, fromlist=[""]), className.split(".")[-1])
        policy = clazz()
        self.__evictionPolicy = typing.cast(EvictionPolicy[typing.Any], policy)

    def updateStatsReturn(self, activeTime: datetime.timedelta) -> None:
        self.__returnedCount += 1
        self.__activeTimes.add0(activeTime)

    def updateStatsBorrow(
        self, p: PooledObject[typing.Any], waitDuration: datetime.timedelta
    ) -> None:
        self.__borrowedCount += 1
        self.__idleTimes.add0(p.getIdleDuration())
        self.__waitTimes.add0(waitDuration)

        currentMaxDuration = None
        while True:
            currentMaxDuration = self.__maxBorrowWaitDuration.get()
            if currentMaxDuration >= waitDuration:
                break
            if self.__maxBorrowWaitDuration.compareAndSet(
                currentMaxDuration, waitDuration
            ):
                break

    def swallowException(self, swallowException: Exception) -> None:
        listener = self.getSwallowedExceptionListener()

        if listener is None:
            return

        try:
            listener.onSwallowException(swallowException)
        except VirtualMachineError as e:
            raise e
        except Exception:
            pass

    def setTestWhileIdle(self, testWhileIdle: bool) -> None:
        self.__testWhileIdle = testWhileIdle

    def setTestOnReturn(self, testOnReturn: bool) -> None:
        self.__testOnReturn = testOnReturn

    def setTestOnCreate(self, testOnCreate: bool) -> None:
        self.__testOnCreate = testOnCreate

    def setTestOnBorrow(self, testOnBorrow: bool) -> None:
        self.__testOnBorrow = testOnBorrow

    def setSwallowedExceptionListener(
        self, swallowedExceptionListener: SwallowedExceptionListener
    ) -> None:
        self.__swallowedExceptionListener = swallowedExceptionListener

    def setSoftMinEvictableIdle(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        self.__softMinEvictableIdleDuration = PoolImplUtils.nonNull(
            softMinEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setNumTestsPerEvictionRun(self, numTestsPerEvictionRun: int) -> None:
        self.__numTestsPerEvictionRun = numTestsPerEvictionRun

    def setMinEvictableIdle(self, minEvictableIdleTime: datetime.timedelta) -> None:
        self.__minEvictableIdleDuration = PoolImplUtils.nonNull(
            minEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setMessagesStatistics(self, messagesDetails: bool) -> None:
        self.__messageStatistics = messagesDetails

    def setMaxWait(self, maxWaitDuration: datetime.timedelta) -> None:
        self.__maxWaitDuration = PoolImplUtils.nonNull(
            maxWaitDuration, BaseObjectPoolConfig.DEFAULT_MAX_WAIT
        )

    def setMaxTotal(self, maxTotal: int) -> None:
        self.__maxTotal = maxTotal

    def setLifo(self, lifo: bool) -> None:
        self.__lifo = lifo

    def setEvictorShutdownTimeout(
        self, evictorShutdownTimeout: datetime.timedelta
    ) -> None:
        self.__evictorShutdownTimeoutDuration = PoolImplUtils.nonNull(
            evictorShutdownTimeout,
            BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT,
        )

    def setEvictionPolicyClassName1(
        self, evictionPolicyClassName: str, classLoader: typing.Any
    ) -> None:
        epClass = EvictionPolicy
        epClassLoader = epClass.__module__
        try:
            try:
                self.__setEvictionPolicy1(evictionPolicyClassName, classLoader)
            except (TypeError, ModuleNotFoundError, AttributeError):
                self.__setEvictionPolicy1(evictionPolicyClassName, epClassLoader)
        except TypeError:
            raise ValueError(
                f"Class {evictionPolicyClassName} from class loaders [{classLoader}, {epClassLoader}] "
                f"do not implement {self.__EVICTION_POLICY_TYPE_NAME}"
            )
        except (ModuleNotFoundError, AttributeError, TypeError, Exception) as e:
            raise ValueError(
                f"Unable to create {self.__EVICTION_POLICY_TYPE_NAME} instance of type {evictionPolicyClassName}",
                e,
            )

    def setEvictionPolicyClassName0(self, evictionPolicyClassName: str) -> None:
        self.setEvictionPolicyClassName1(
            evictionPolicyClassName, threading.current_thread().context
        )

    def setEvictionPolicy0(self, evictionPolicy: EvictionPolicy[typing.Any]) -> None:
        self.__evictionPolicy = evictionPolicy

    def setBlockWhenExhausted(self, blockWhenExhausted: bool) -> None:
        self.__blockWhenExhausted = blockWhenExhausted

    def setAbandonedConfig(self, abandonedConfig: AbandonedConfig) -> None:
        self._abandonedConfig = AbandonedConfig.copy(abandonedConfig)

    def _markReturningState(self, pooledObject: PooledObject[typing.Any]) -> None:
        with pooledObject:  # Synchronized block equivalent in Python
            if pooledObject.getState() != PooledObjectState.ALLOCATED:
                raise RuntimeError(
                    "Object has already been returned to this pool or is invalid"
                )
            pooledObject.markReturning()  # Keep from being marked abandoned

    def isClosed(self) -> bool:
        return self.closed

    def isAbandonedConfig(self) -> bool:
        return self._abandonedConfig is not None

    def getDurationBetweenEvictionRuns(self) -> datetime.timedelta:
        return self.__durationBetweenEvictionRuns

    def getTestWhileIdle(self) -> bool:
        return self.__testWhileIdle

    def getTestOnReturn(self) -> bool:
        return self.__testOnReturn

    def getTestOnCreate(self) -> bool:
        return self.__testOnCreate

    def getTestOnBorrow(self) -> bool:
        return self.__testOnBorrow

    def getSwallowedExceptionListener(self) -> SwallowedExceptionListener:
        return self.__swallowedExceptionListener

    def getSoftMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

    def getReturnedCount(self) -> int:
        return self.__returnedCount

    def getRemoveAbandonedTimeoutDuration(self) -> datetime.timedelta:
        ac = self._abandonedConfig
        return (
            ac.getRemoveAbandonedTimeoutDuration()
            if ac is not None
            else self.__DEFAULT_REMOVE_ABANDONED_TIMEOUT
        )

    def getRemoveAbandonedOnMaintenance(self) -> bool:
        ac = self._abandonedConfig
        return ac is not None and ac.getRemoveAbandonedOnMaintenance()

    def getRemoveAbandonedOnBorrow(self) -> bool:
        ac = self._abandonedConfig
        return ac is not None and ac.getRemoveAbandonedOnBorrow()

    def getNumTestsPerEvictionRun(self) -> int:
        return self.__numTestsPerEvictionRun

    def getMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__minEvictableIdleDuration

    def getMessageStatistics(self) -> bool:
        return self.__messageStatistics

    def getMeanIdleTimeMillis(self) -> int:
        return self.__idleTimes.getMean()

    def getMeanBorrowWaitTimeMillis(self) -> int:
        return self.__waitTimes.getMean()

    def getMeanActiveTimeMillis(self) -> int:
        return self.__activeTimes.getMean()

    def getMaxWaitDuration(self) -> datetime.timedelta:
        return self.__maxWaitDuration

    def getMaxTotal(self) -> int:
        return self.__maxTotal

    def getMaxBorrowWaitTimeMillis(self) -> int:
        return int(self.__maxBorrowWaitDuration.get().total_seconds() * 1000)

    def getLogAbandoned(self) -> bool:
        ac = self._abandonedConfig
        return ac is not None and ac.getLogAbandoned()

    def getLifo(self) -> bool:
        return self.__lifo

    def getEvictorShutdownTimeoutDuration(self) -> datetime.timedelta:
        return self.__evictorShutdownTimeoutDuration

    def getEvictionPolicyClassName(self) -> str:
        return self.__evictionPolicy.__class__.__name__

    def getEvictionPolicy(self) -> EvictionPolicy[typing.Any]:
        return self.__evictionPolicy

    def getDestroyedCount(self) -> int:
        return self.destroyedCount

    def getDestroyedByEvictorCount(self) -> int:
        return self.destroyedByEvictorCount

    def getDestroyedByBorrowValidationCount(self) -> int:
        return self.destroyedByBorrowValidationCount

    def getCreatedCount(self) -> int:
        return self.createdCount

    def getBorrowedCount(self) -> int:
        return self.__borrowedCount

    def getBlockWhenExhausted(self) -> bool:
        return self.__blockWhenExhausted

    def assertOpen(self) -> None:
        if self.isClosed():
            raise RuntimeError("Pool not open")

    def __getStackTrace(self, e: Exception) -> str:
        w = StringIO()
        try:
            import traceback

            traceback.print_exception(type(e), e, e.__traceback__, file=w)
            return w.getvalue()
        finally:
            w.close()

    def createRemoveList(
        self,
        abandonedConfig: AbandonedConfig,
        allObjects: typing.Dict[IdentityWrapper[typing.Any], PooledObject[typing.Any]],
    ) -> typing.List[PooledObject[typing.Any]]:
        timeout = (
            datetime.datetime.now(datetime.timezone.utc)
            - abandonedConfig.getRemoveAbandonedTimeoutDuration()
        )
        remove = []
        for pooledObject in allObjects.values():
            with (
                pooledObject
            ):  # Assuming `pooledObject` supports context management for synchronization
                if (
                    pooledObject.getState() == PooledObjectState.ALLOCATED
                    and pooledObject.getLastUsedInstant() <= timeout
                ):
                    pooledObject.markAbandoned()
                    remove.append(pooledObject)
        return remove

    def getNumIdle(self) -> int:
        raise NotImplementedError("Subclasses must implement this method")

    def evict(self) -> None:
        raise Exception("This method must be implemented by a subclass")

    def ensureMinIdle(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    def close(self) -> None:
        raise NotImplementedError("Subclasses must implement the close method.")


class IdentityWrapper:

    __instance: typing.Any = None

    def toString(self) -> str:
        builder = []
        builder.append("IdentityWrapper [instance=")
        builder.append(str(self.__instance))
        builder.append("]")
        return "".join(builder)

    def hashCode(self) -> int:
        return id(self.__instance)

    def equals(self, other: typing.Any) -> bool:
        return (
            isinstance(other, IdentityWrapper) and other.__instance is self.__instance
        )

    def getObject(self) -> typing.Any:
        return self.__instance

    def __init__(self, instance: typing.Any) -> None:
        self.__instance = instance


class Evictor:

    __scheduledFuture: concurrent.futures.Future[typing.Any] = None

    def setScheduledFuture(
        self, scheduledFuture: concurrent.futures.Future[typing.Any]
    ) -> None:
        self.__scheduledFuture = scheduledFuture

    def cancel(self) -> None:
        self.__scheduledFuture.cancel(False)


class EvictionIterator:

    __idleObjectIterator: typing.Iterator[PooledObject[typing.Any]] = None

    __idleObjects: typing.Deque[PooledObject[typing.Any]] = None

    def remove(self) -> None:
        self.__idleObjectIterator.remove()

    def next_(self) -> PooledObject[typing.Any]:
        return next(self.__idleObjectIterator)

    def hasNext(self) -> bool:
        return self.__idleObjectIterator.__next__ is not None

    def getIdleObjects(self) -> typing.Deque[PooledObject[typing.Any]]:
        return self.__idleObjects

    def __init__(self, idleObjects: typing.Deque[PooledObject[typing.Any]]) -> None:
        self.__idleObjects = idleObjects

        if BaseGenericObjectPool.getLifo(self):
            self.__idleObjectIterator = reversed(idleObjects)
        else:
            self.__idleObjectIterator = iter(idleObjects)


class StatsStore:

    __index: int = 0

    __size: int = 0

    __values: typing.List[int] = None

    __NULL: int = -1

    def toString(self) -> str:
        builder = []
        builder.append("StatsStore [")
        builder.append(str(self.getCurrentValues()))
        builder.append("], size=")
        builder.append(str(self.__size))
        builder.append(", index=")
        builder.append(str(self.__index))
        builder.append("]")
        return "".join(builder)

    def getMean(self) -> int:
        result = 0.0
        counter = 0
        for i in range(self.__size):
            value = self.__values[i]
            if value != self.__NULL:
                counter += 1
                result = result * ((counter - 1) / counter) + value / counter
        return int(result)

    def getCurrentValues(self) -> typing.List[int]:
        return self.__values[: self.__index]

    def add1(self, value: int) -> None:
        self.__values[self.__index] = value
        self.__index += 1
        if self.__index == self.__size:
            self.__index = 0

    def add0(self, value: datetime.timedelta) -> None:
        self.add1(int(value.total_seconds() * 1000))

    def __init__(self, size: int) -> None:
        self.__size = size
        self.__values = [self.__NULL for _ in range(size)]
