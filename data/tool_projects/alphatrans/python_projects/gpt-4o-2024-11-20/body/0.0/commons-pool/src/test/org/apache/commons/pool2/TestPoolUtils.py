from __future__ import annotations
import time
import inspect
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PoolUtils import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *

# from src.main.org.opentest4j.AssertionFailedError import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class TestPoolUtils(unittest.TestCase):

    __CHECK_SLEEP_PERIOD: int = 300 * (4 - 1) + 300 // 2
    __CHECK_COUNT: int = 4
    __CHECK_PERIOD: int = 300

    def testTimerHolder_test1_decomposed(self) -> None:
        h = PoolUtils.TimerHolder()
        self.assertIsNotNone(h)
        self.assertIsNotNone(PoolUtils.TimerHolder.MIN_IDLE_TIMER)

    def testTimerHolder_test0_decomposed(self) -> None:
        h = PoolUtils.TimerHolder()

    def testSynchronizedPoolObjectPool_test1_decomposed(self) -> None:
        # Test that a ValueError is raised when passing None to synchronizedPool1
        with self.assertRaises(ValueError) as context:
            PoolUtils.synchronizedPool1(None)
        self.assertEqual(str(context.exception), "pool must not be null.")

        # Create a proxy object pool and a synchronized pool
        called_methods = []
        op = self.__createProxy1(ObjectPool, called_methods)
        sop = PoolUtils.synchronizedPool1(op)

        # Invoke every method on the synchronized pool
        expected_methods = self.__invokeEveryMethod2(sop)

        # Assert that the methods called match the expected methods
        self.assertEqual(expected_methods, called_methods)

    def testSynchronizedPoolObjectPool_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError) as context:
            PoolUtils.synchronizedPool1(None)
        self.assertEqual(
            str(context.exception),
            "PoolUtils.synchronizedPool(ObjectPool) must not allow a null pool.",
        )

    def testSynchronizedPoolKeyedObjectPool_test1_decomposed(self) -> None:
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.synchronizedPool(KeyedObjectPool) must not allow a null pool.",
        ):
            PoolUtils.synchronizedPool0(None)

        called_methods: List[str] = []
        with TestPoolUtils.__createProxy1(
            KeyedObjectPool, called_methods
        ) as kop, PoolUtils.synchronizedPool0(kop) as skop:
            expected_methods = TestPoolUtils.__invokeEveryMethod0(skop)
            self.assertEqual(expected_methods, called_methods)

    def testSynchronizedPoolKeyedObjectPool_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError) as context:
            PoolUtils.synchronizedPool0(None)
        self.assertEqual(
            str(context.exception),
            "PoolUtils.synchronizedPool(KeyedObjectPool) must not allow a null pool.",
        )

    def testPrefillObjectPool_test1_decomposed(self) -> None:
        with self.assertRaises(ValueError) as context:
            PoolUtils.prefill2(None, 1)
        self.assertEqual(
            str(context.exception),
            "pool must not be null.",
            "PoolUtils.prefill(ObjectPool,int) must not allow null pool.",
        )

        called_methods = []
        with TestPoolUtils.__createProxy1(ObjectPool, called_methods) as pool:
            # Test with count = 0
            PoolUtils.prefill2(pool, 0)
            expected_methods = ["addObjects"]
            self.assertEqual(expected_methods, called_methods)

            # Clear the called methods and test with count = 3
            called_methods.clear()
            PoolUtils.prefill2(pool, 3)
            self.assertEqual(expected_methods, called_methods)

    def testPrefillObjectPool_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError) as context:
            PoolUtils.prefill2(None, 1)
        self.assertEqual(
            str(context.exception),
            "PoolUtils.prefill(ObjectPool,int) must not allow null pool.",
        )

    def testPrefillKeyedObjectPoolCollection_test1_decomposed(self) -> None:
        # Test case 1: Ensure PoolUtils.prefill0 raises an exception for null keys
        with self.assertRaises(ValueError) as context:
            with TestPoolUtils.__createProxy1(KeyedObjectPool, None) as pool:
                PoolUtils.prefill0(pool, None, 1)
        self.assertEqual(
            str(context.exception),
            "keys must not be null.",
            "PoolUtils.prefill(KeyedObjectPool, Collection, int) must not accept null keys.",
        )

        # Test case 2: Verify method calls for valid keys and counts
        called_methods = []
        with TestPoolUtils.__createProxy1(KeyedObjectPool, called_methods) as pool:
            # Case 2.1: Empty keys set
            keys = set()
            PoolUtils.prefill0(pool, keys, 0)
            expected_methods = ["addObjects0"]
            self.assertEqual(expected_methods, called_methods)

            # Case 2.2: Non-empty keys set with a count
            called_methods.clear()
            keys.update(["one", "two", "three"])
            count = 3
            PoolUtils.prefill0(pool, keys, count)
            self.assertEqual(expected_methods, called_methods)

    def testPrefillKeyedObjectPoolCollection_test0_decomposed(self) -> None:
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.prefill(KeyedObjectPool,Collection,int) must not accept null keys.",
        ):
            pool = self.__createProxy1(KeyedObjectPool, None)
            PoolUtils.prefill0(pool, None, 1)

    def testJavaBeanInstantiation_test0_decomposed(self) -> None:
        self.assertIsNotNone(PoolUtils())

    def testErodingPoolKeyedObjectPoolDefaultFactor_test0_decomposed(self) -> None:
        internal_pool = self.__createProxy0(
            KeyedObjectPool, lambda arg0, arg1, arg2: None
        )
        pool = PoolUtils.erodingPool0(internal_pool)

        expected_to_string = (
            "ErodingKeyedObjectPool{factor=ErodingFactor{factor=1.0, idleHighWaterMark=1},"
            + " keyedPool="
            + str(internal_pool)
            + "}"
        )

        self.assertEqual(expected_to_string, str(pool))

    def testErodingObjectPoolDefaultFactor_test0_decomposed(self) -> None:
        internal_pool = self.__createProxy0(ObjectPool, lambda arg0, arg1, arg2: None)
        pool = PoolUtils.erodingPool3(internal_pool)
        expected_to_string = f"ErodingObjectPool{{factor=ErodingFactor{{factor=1.0, idleHighWaterMark=1}}, pool={internal_pool}}}"
        self.assertEqual(expected_to_string, str(pool))

    def testCheckRethrow_test0_decomposed(self) -> None:
        # Test case 1: Exception should not be rethrown
        try:
            PoolUtils.checkRethrow(Exception())
        except BaseException as t:
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only SystemExit and BaseException."
            )

        # Test case 2: SystemExit (equivalent to ThreadDeath) should be rethrown
        try:
            PoolUtils.checkRethrow(SystemExit())
            pytest.fail("PoolUtils.checkRethrow(Throwable) must rethrow SystemExit.")
        except SystemExit:
            pass
        except BaseException as t:
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only SystemExit and BaseException."
            )

        # Test case 3: BaseException (equivalent to VirtualMachineError) should be rethrown
        try:
            PoolUtils.checkRethrow(
                InternalError()
            )  # InternalError is a subclass of BaseException
            pytest.fail("PoolUtils.checkRethrow(Throwable) must rethrow BaseException.")
        except BaseException:
            pass
        except Exception as t:
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only SystemExit and BaseException."
            )

    def testCheckMinIdleKeyedObjectPoolKeysNulls_test1_decomposed(self) -> None:
        # First try block
        try:
            pool = self.__createProxy1(KeyedObjectPool, None)
            with pytest.raises(
                ValueError,
                match="PoolUtils.checkMinIdle\\(KeyedObjectPool,Collection,int,long\\) must not accept null keys.",
            ):
                PoolUtils.checkMinIdle1(pool, None, 1, 1)
        except Exception as e:
            pytest.fail(f"Unexpected exception raised: {e}")

        # Second try block
        try:
            pool = self.__createProxy1(KeyedObjectPool, None)
            PoolUtils.checkMinIdle1(pool, [], 1, 1)  # Passing an empty list
        except ValueError:
            pytest.fail(
                "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must accept empty lists."
            )

    def testCheckMinIdleKeyedObjectPoolKeysNulls_test0_decomposed(self) -> None:
        with self.__createProxy1(KeyedObjectPool, None) as pool:
            with self.assertRaises(ValueError) as context:
                PoolUtils.checkMinIdle1(pool, None, 1, 1)
            self.assertIn(
                "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must not accept null keys.",
                str(context.exception),
            )

    def testCheckMinIdleKeyedObjectPoolKeys_test1_decomposed(self) -> None:
        afe = None
        tries_left = 3
        while tries_left > 0 and afe is not None:
            afe = None
            called_methods: List[str] = []
            try:
                with self.__createProxy1(KeyedObjectPool, called_methods) as pool:
                    keys = ["one", "two"]
                    tasks = PoolUtils.checkMinIdle0(pool, keys, 1, self.__CHECK_PERIOD)

                    # Sleep to allow CHECK_COUNT checks to occur
                    time.sleep(
                        self.__CHECK_SLEEP_PERIOD / 1000
                    )  # Convert ms to seconds

                    # Cancel all tasks
                    for task in tasks.values():
                        task.cancel()

                    # Build the expected method calls
                    expected_methods = []
                    for _ in range(self.__CHECK_COUNT * len(keys)):
                        expected_methods.append("getNumIdle1")
                        expected_methods.append("addObject")

                    # Assert that the called methods match the expected methods
                    self.assertEqual(expected_methods, called_methods)

            except AssertionError as e:
                afe = e

            tries_left -= 1

        if afe is not None:
            raise afe

    def testCheckMinIdleKeyedObjectPoolKeys_test0_decomposed(self) -> None:
        afe = None
        tries_left = 3
        while tries_left > 0 and afe is not None:
            afe = None
            called_methods = []
            try:
                with self.__createProxy1(KeyedObjectPool, called_methods) as pool:
                    keys = ["one", "two"]
                    tasks = PoolUtils.checkMinIdle0(pool, keys, 1, self.__CHECK_PERIOD)

                    # Simulate the sleep period
                    time.sleep(
                        self.__CHECK_SLEEP_PERIOD / 1000
                    )  # Convert milliseconds to seconds

                    # Cancel all tasks
                    for task in tasks.values():
                        task.cancel()

                    # Create the expected methods list
                    expected_methods = []
                    for _ in range(self.__CHECK_COUNT * len(keys)):
                        expected_methods.append("getNumIdle1")
                        expected_methods.append("addObject")

                    # Assert that the called methods match the expected methods
                    self.assertEqual(expected_methods, called_methods)

            except AssertionError as e:
                afe = e

            tries_left -= 1

    @staticmethod
    def __createProxy0(
        clazz: typing.Type[typing.Any], handler: typing.Callable
    ) -> typing.Any:
        return type(
            f"Proxy_{clazz.__name__}",
            (clazz,),
            {
                "__init__": lambda self, *args, **kwargs: None,
                "__getattr__": lambda self, name: lambda *args, **kwargs: handler(
                    self, name, *args, **kwargs
                ),
            },
        )()

    @staticmethod
    def __invokeEveryMethod3(pof: PooledObjectFactory[typing.Any]) -> typing.List[str]:
        pof.activateObject(None)
        pof.destroyObject0(None)
        pof.makeObject()
        pof.passivateObject(None)
        pof.validateObject(None)
        str(pof)  # Equivalent to calling `toString()` in Java

        return [
            "activateObject",
            "destroyObject",
            "makeObject",
            "passivateObject",
            "validateObject",
            "toString",
        ]

    @staticmethod
    def __invokeEveryMethod2(op: ObjectPool[object]) -> typing.List[str]:
        op.addObject()
        op.borrowObject()
        op.clear()
        op.close()
        op.getNumActive()
        op.getNumIdle()
        op.invalidateObject0(object())
        op.returnObject(object())
        op.__str__()

        return [
            "addObject",
            "borrowObject",
            "clear",
            "close",
            "getNumActive",
            "getNumIdle",
            "invalidateObject0",
            "returnObject",
            "toString",
        ]

    @staticmethod
    def __invokeEveryMethod1(
        kpof: KeyedPooledObjectFactory[typing.Any, typing.Any],
    ) -> typing.List[str]:
        kpof.activateObject(None, None)
        kpof.destroyObject0(None, None)
        kpof.makeObject(None)
        kpof.passivateObject(None, None)
        kpof.validateObject(None, None)
        kpof.__str__()

        return [
            "activateObject",
            "destroyObject0",
            "makeObject",
            "passivateObject",
            "validateObject",
            "toString",
        ]

    @staticmethod
    def __invokeEveryMethod0(
        kop: KeyedObjectPool[object, typing.Any],
    ) -> typing.List[str]:
        kop.addObject(None)
        kop.borrowObject(None)
        kop.clear0()
        kop.clear1(None)
        kop.close()
        kop.getNumActive0()
        kop.getNumActive1(None)
        kop.getNumIdle0()
        kop.getNumIdle1(None)
        kop.invalidateObject0(None, object())
        kop.returnObject(None, object())
        kop.__str__()

        return [
            "addObject",
            "borrowObject",
            "clear0",
            "clear1",
            "close",
            "getNumActive0",
            "getNumActive1",
            "getNumIdle0",
            "getNumIdle1",
            "invalidateObject0",
            "returnObject",
            "toString",
        ]

    @staticmethod
    def __createProxy1(
        clazz: typing.Type[typing.Any], logger: typing.List[str]
    ) -> typing.Any:
        return TestPoolUtils.__createProxy0(clazz, MethodCallLogger(logger))


class MethodCallLogger:

    __calledMethods: typing.List[str] = None

    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:
        if self.__calledMethods is None:
            return None
        self.__calledMethods.append(method.__name__)

        if method.return_annotation == bool:
            return False
        if method.return_annotation == int:
            return 0
        if (
            method.return_annotation == int
        ):  # Python does not differentiate between int and long
            return 0
        if method.return_annotation == object:
            return object()
        if method.return_annotation == PooledObject:
            return DefaultPooledObject(object())

        return None

    def __init__(self, calledMethods: typing.List[str]) -> None:
        self.__calledMethods = calledMethods
