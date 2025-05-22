from __future__ import annotations
import time
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.impl.DefaultEvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class BaseObjectPoolConfig(BaseObject, ABC):

    DEFAULT_EVICTION_POLICY_CLASS_NAME: str = DefaultEvictionPolicy.__name__
    DEFAULT_JMX_NAME_BASE: str = None
    DEFAULT_JMX_NAME_PREFIX: str = "pool"
    DEFAULT_JMX_ENABLE: bool = True
    DEFAULT_BLOCK_WHEN_EXHAUSTED: bool = True
    DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS: int = -1
    DEFAULT_TEST_WHILE_IDLE: bool = False
    DEFAULT_TEST_ON_RETURN: bool = False
    DEFAULT_TEST_ON_BORROW: bool = False
    DEFAULT_TEST_ON_CREATE: bool = False
    DEFAULT_NUM_TESTS_PER_EVICTION_RUN: int = 3
    DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT_MILLIS: int = 10 * 1000
    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS: int = -1
    DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS: int = 1000 * 60 * 30

    DEFAULT_MIN_EVICTABLE_IDLE_DURATION: datetime.timedelta = (
        None  # LLM could not translate this field
    )

    DEFAULT_MAX_WAIT_MILLIS: int = -1
    DEFAULT_FAIRNESS: bool = False
    DEFAULT_LIFO: bool = True
    __jmxNameBase: str = DEFAULT_JMX_NAME_BASE
    __jmxNamePrefix: str = DEFAULT_JMX_NAME_PREFIX
    __jmxEnabled: bool = DEFAULT_JMX_ENABLE
    __blockWhenExhausted: bool = DEFAULT_BLOCK_WHEN_EXHAUSTED

    __durationBetweenEvictionRuns: datetime.timedelta = (
        None  # LLM could not translate this field
    )

    __testWhileIdle: bool = DEFAULT_TEST_WHILE_IDLE
    __testOnReturn: bool = None
    __testOnBorrow: bool = DEFAULT_TEST_ON_BORROW
    __testOnCreate: bool = DEFAULT_TEST_ON_CREATE
    __evictionPolicyClassName: str = None
    __evictionPolicy: EvictionPolicy[typing.Any] = None

    __numTestsPerEvictionRun: int = DEFAULT_NUM_TESTS_PER_EVICTION_RUN

    __softMinEvictableIdleDuration: datetime.timedelta = (
        None  # LLM could not translate this field
    )

    __evictorShutdownTimeoutDuration: datetime.timedelta = (
        None  # LLM could not translate this field
    )

    __minEvictableIdleDuration: datetime.timedelta = (
        None  # LLM could not translate this field
    )

    __maxWaitDuration: datetime.timedelta = None  # LLM could not translate this field

    __fairness: bool = DEFAULT_FAIRNESS
    __lifo: bool = DEFAULT_LIFO

    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION: datetime.timedelta = (
        None  # LLM could not translate this field
    )

    @staticmethod
    def initialize_fields() -> None:
        BaseObjectPoolConfig.__testOnReturn: bool = (
            BaseObjectPoolConfig.DEFAULT_TEST_ON_RETURN
        )

        BaseObjectPoolConfig.__evictionPolicyClassName: str = (
            BaseObjectPoolConfig.DEFAULT_EVICTION_POLICY_CLASS_NAME
        )

    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        if isinstance(builder, list):
            builder.append(f"lifo={self.__lifo}")
            builder.append(f", fairness={self.__fairness}")
            builder.append(f", maxWaitDuration={self.__maxWaitDuration}")
            builder.append(f", minEvictableIdleTime={self.__minEvictableIdleDuration}")
            builder.append(
                f", softMinEvictableIdleTime={self.__softMinEvictableIdleDuration}"
            )
            builder.append(f", numTestsPerEvictionRun={self.__numTestsPerEvictionRun}")
            builder.append(
                f", evictionPolicyClassName={self.__evictionPolicyClassName}"
            )
            builder.append(f", testOnCreate={self.__testOnCreate}")
            builder.append(f", testOnBorrow={self.__testOnBorrow}")
            builder.append(f", testOnReturn={self.__testOnReturn}")
            builder.append(f", testWhileIdle={self.__testWhileIdle}")
            builder.append(
                f", timeBetweenEvictionRuns={self.__durationBetweenEvictionRuns}"
            )
            builder.append(f", blockWhenExhausted={self.__blockWhenExhausted}")
            builder.append(f", jmxEnabled={self.__jmxEnabled}")
            builder.append(f", jmxNamePrefix={self.__jmxNamePrefix}")
            builder.append(f", jmxNameBase={self.__jmxNameBase}")
        elif isinstance(builder, io.StringIO):
            builder.write(f"lifo={self.__lifo}")
            builder.write(f", fairness={self.__fairness}")
            builder.write(f", maxWaitDuration={self.__maxWaitDuration}")
            builder.write(f", minEvictableIdleTime={self.__minEvictableIdleDuration}")
            builder.write(
                f", softMinEvictableIdleTime={self.__softMinEvictableIdleDuration}"
            )
            builder.write(f", numTestsPerEvictionRun={self.__numTestsPerEvictionRun}")
            builder.write(f", evictionPolicyClassName={self.__evictionPolicyClassName}")
            builder.write(f", testOnCreate={self.__testOnCreate}")
            builder.write(f", testOnBorrow={self.__testOnBorrow}")
            builder.write(f", testOnReturn={self.__testOnReturn}")
            builder.write(f", testWhileIdle={self.__testWhileIdle}")
            builder.write(
                f", timeBetweenEvictionRuns={self.__durationBetweenEvictionRuns}"
            )
            builder.write(f", blockWhenExhausted={self.__blockWhenExhausted}")
            builder.write(f", jmxEnabled={self.__jmxEnabled}")
            builder.write(f", jmxNamePrefix={self.__jmxNamePrefix}")
            builder.write(f", jmxNameBase={self.__jmxNameBase}")

    def setTimeBetweenEvictionRunsMillis(
        self, timeBetweenEvictionRunsMillis: int
    ) -> None:
        self.setTimeBetweenEvictionRuns(
            datetime.timedelta(milliseconds=timeBetweenEvictionRunsMillis)
        )

    def setSoftMinEvictableIdleTimeMillis(
        self, softMinEvictableIdleTimeMillis: int
    ) -> None:
        self.setSoftMinEvictableIdleTime(
            datetime.timedelta(milliseconds=softMinEvictableIdleTimeMillis)
        )

    def setMinEvictableIdleTimeMillis(self, minEvictableIdleTimeMillis: int) -> None:
        self.__minEvictableIdleDuration = datetime.timedelta(
            milliseconds=minEvictableIdleTimeMillis
        )

    def setMaxWaitMillis(self, maxWaitMillis: int) -> None:
        self.setMaxWait(datetime.timedelta(milliseconds=maxWaitMillis))

    def setEvictorShutdownTimeoutMillis1(
        self, evictorShutdownTimeoutMillis: int
    ) -> None:
        self.setEvictorShutdownTimeout(
            datetime.timedelta(milliseconds=evictorShutdownTimeoutMillis)
        )

    def setEvictorShutdownTimeoutMillis0(
        self, evictorShutdownTimeout: datetime.timedelta
    ) -> None:
        self.setEvictorShutdownTimeout(evictorShutdownTimeout)

    def getTimeBetweenEvictionRunsMillis(self) -> int:
        return int(self.__durationBetweenEvictionRuns.total_seconds() * 1000)

    def getTimeBetweenEvictionRuns(self) -> datetime.timedelta:
        return self.__durationBetweenEvictionRuns

    def getSoftMinEvictableIdleTimeMillis(self) -> int:
        return int(self.__softMinEvictableIdleDuration.total_seconds() * 1000)

    def getSoftMinEvictableIdleTime(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

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

    def setTimeBetweenEvictionRuns(
        self, timeBetweenEvictionRuns: datetime.timedelta
    ) -> None:
        self.__durationBetweenEvictionRuns = PoolImplUtils.nonNull(
            timeBetweenEvictionRuns, self.DEFAULT_TIME_BETWEEN_EVICTION_RUNS
        )

    def setTestWhileIdle(self, testWhileIdle: bool) -> None:
        self.__testWhileIdle = testWhileIdle

    def setTestOnReturn(self, testOnReturn: bool) -> None:
        self.__testOnReturn = testOnReturn

    def setTestOnCreate(self, testOnCreate: bool) -> None:
        self.__testOnCreate = testOnCreate

    def setTestOnBorrow(self, testOnBorrow: bool) -> None:
        self.__testOnBorrow = testOnBorrow

    def setSoftMinEvictableIdleTime(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        self.__softMinEvictableIdleDuration = PoolImplUtils.nonNull(
            softMinEvictableIdleTime, self.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME
        )

    def setNumTestsPerEvictionRun(self, numTestsPerEvictionRun: int) -> None:
        self.__numTestsPerEvictionRun = numTestsPerEvictionRun

    def setMinEvictableIdleTime(self, minEvictableIdleTime: datetime.timedelta) -> None:
        self.__minEvictableIdleDuration = PoolImplUtils.nonNull(
            minEvictableIdleTime, self.DEFAULT_MIN_EVICTABLE_IDLE_TIME
        )

    def setMaxWait(self, maxWaitDuration: datetime.timedelta) -> None:
        self.__maxWaitDuration = PoolImplUtils.nonNull(
            maxWaitDuration, self.DEFAULT_MAX_WAIT
        )

    def setLifo(self, lifo: bool) -> None:
        self.__lifo = lifo

    def setJmxNamePrefix(self, jmxNamePrefix: str) -> None:
        self.__jmxNamePrefix = jmxNamePrefix

    def setJmxNameBase(self, jmxNameBase: str) -> None:
        self.__jmxNameBase = jmxNameBase

    def setJmxEnabled(self, jmxEnabled: bool) -> None:
        self.__jmxEnabled = jmxEnabled

    def setFairness(self, fairness: bool) -> None:
        self.__fairness = fairness

    def setEvictorShutdownTimeout(
        self, evictorShutdownTimeoutDuration: datetime.timedelta
    ) -> None:
        self.__evictorShutdownTimeoutDuration = PoolImplUtils.nonNull(
            evictorShutdownTimeoutDuration, self.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
        )

    def setEvictionPolicyClassName(self, evictionPolicyClassName: str) -> None:
        self.__evictionPolicyClassName = evictionPolicyClassName

    def setEvictionPolicy(self, evictionPolicy: EvictionPolicy[typing.Any]) -> None:
        self.__evictionPolicy = evictionPolicy

    def setBlockWhenExhausted(self, blockWhenExhausted: bool) -> None:
        self.__blockWhenExhausted = blockWhenExhausted

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

    def getSoftMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

    def getNumTestsPerEvictionRun(self) -> int:
        return self.__numTestsPerEvictionRun

    def getMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__minEvictableIdleDuration

    def getMaxWaitDuration(self) -> datetime.timedelta:
        return self.__maxWaitDuration

    def getLifo(self) -> bool:
        return self.__lifo

    def getJmxNamePrefix(self) -> str:
        return self.__jmxNamePrefix

    def getJmxNameBase(self) -> str:
        return self.__jmxNameBase

    def getJmxEnabled(self) -> bool:
        return self.__jmxEnabled

    def getFairness(self) -> bool:
        return self.__fairness

    def getEvictorShutdownTimeoutDuration(self) -> datetime.timedelta:
        return self.__evictorShutdownTimeoutDuration

    def getEvictionPolicyClassName(self) -> str:
        return self.__evictionPolicyClassName

    def getEvictionPolicy(self) -> EvictionPolicy[typing.Any]:
        return self.__evictionPolicy

    def getBlockWhenExhausted(self) -> bool:
        return self.__blockWhenExhausted


BaseObjectPoolConfig.initialize_fields()
