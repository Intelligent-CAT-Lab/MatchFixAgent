from __future__ import annotations
import re
import random
import decimal
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class HexTest(unittest.TestCase):

    __LOG: bool = False
    __BAD_ENCODING_NAME: str = "UNKNOWN"

    def testRequiredCharset_test0_decomposed(self) -> None:
        self.__testCustomCharset1("UTF-8", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16BE", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16LE", "testRequiredCharset")
        self.__testCustomCharset1("US-ASCII", "testRequiredCharset")
        self.__testCustomCharset1("ISO8859_1", "testRequiredCharset")

    def testGetCharsetName_test0_decomposed(self) -> None:
        self.assertEqual("UTF-8", Hex(1, None, "UTF-8").getCharsetName())

    def testGetCharset_test0_decomposed(self) -> None:
        self.assertEqual("UTF-8", Hex(1, None, "UTF-8").getCharset())

    def testEncodeStringEmpty_test0_decomposed(self) -> None:
        hex_instance = Hex(2, None, None)
        result = hex_instance.encode2("")
        self.assertEqual(
            [], list(result), "Encoded result does not match the expected empty list"
        )

    def testEncodeHexReadOnlyByteBuffer_test1_decomposed(self) -> None:
        chars = Hex.encodeHex6(memoryview(bytearray([10])))
        self.assertEqual("0a", "".join(chars))

    def testEncodeHexReadOnlyByteBuffer_test0_decomposed(self) -> None:
        chars = Hex.encodeHex6(memoryview(bytearray([10])))

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test3_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)  # Allocate a byte buffer with a capacity of 4
        bb[1] = 10  # Set the second byte (index 1) to 10
        bb_view = memoryview(bb)[
            1:2
        ]  # Create a view of the buffer from position 1 to limit 2
        result = Hex.encodeHexString3(
            bb_view, False
        )  # Call the encodeHexString3 method
        self.assertEqual(
            "0A", result
        )  # Assert that the result matches the expected value
        self.assertEqual(
            0, len(bb_view)
        )  # Assert that the remaining bytes in the view are 0

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test2_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)  # Allocate a byte buffer with a capacity of 4
        bb[1] = 10  # Put the value 10 (0x0A) at index 1
        bb_view = memoryview(bb)[
            1:2
        ]  # Create a view of the buffer from position 1 to limit 2
        result = Hex.encodeHexString3(
            bb_view, False
        )  # Call the encodeHexString3 method
        self.assertEqual(
            "0A", result
        )  # Assert that the result matches the expected value

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test1_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)
        bb[1] = 10

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test0_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test3_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)  # Allocate a byte buffer with a capacity of 4
        bb[1] = 10  # Set the value at index 1 to 10 (0x0A in hexadecimal)
        bb_view = memoryview(bb)  # Create a memoryview for slicing
        bb_view = bb_view[
            1:2
        ]  # Set position to 1 and limit to 2 (slice from index 1 to 2)

        # Assert that the encoded hex string matches the expected value
        self.assertEqual("0a", Hex.encodeHexString3(bb_view, True))

        # Assert that the remaining bytes in the buffer are 0
        self.assertEqual(0, len(bb_view))

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test2_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)  # Allocate a byte buffer with a capacity of 4
        bb[1] = 10  # Set the value at index 1 to 10 (0x0A in hexadecimal)
        bb_view = memoryview(bb)[
            1:2
        ]  # Create a view of the buffer from position 1 to limit 2
        result = Hex.encodeHexString3(
            bb_view, True
        )  # Encode the buffer to a hex string in lowercase
        self.assertEqual(
            "0a", result
        )  # Assert that the result matches the expected value

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test1_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)
        bb[1] = 10

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test0_decomposed(
        self,
    ) -> None:
        bb = self._allocate(4)

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test2_decomposed(
        self,
    ) -> None:
        bb = self._allocate(1)  # Allocate a byte buffer with capacity 1
        bb[0] = 10  # Put the byte value 10 into the buffer
        # No need to flip in Python, as we directly manipulate the buffer
        result = Hex.encodeHexString3(bb, False)  # Call the encodeHexString3 method
        self.assertEqual(
            "0A", result
        )  # Assert that the result matches the expected value

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test1_decomposed(
        self,
    ) -> None:
        bb = self._allocate(1)
        bb[0] = 10

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test0_decomposed(
        self,
    ) -> None:
        bb = self._allocate(1)

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test2_decomposed(
        self,
    ) -> None:
        bb = self._allocate(1)  # Allocate a byte buffer with capacity 1
        bb[0] = 10  # Put the byte value 10 into the buffer
        # No need to flip in Python, as we directly manipulate the buffer
        result = Hex.encodeHexString3(
            bb, True
        )  # Call the encodeHexString3 method with toLowerCase=True
        self.assertEqual(
            "0a", result
        )  # Assert that the result matches the expected value

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test1_decomposed(
        self,
    ) -> None:
        bb = self._allocate(1)
        bb[0] = 10

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test0_decomposed(
        self,
    ) -> None:
        bb = self._allocate(1)

    def testEncodeHexByteString_ByteArrayBoolean_ToUpperCase_test0_decomposed(
        self,
    ) -> None:
        self.assertEqual(
            "0A",
            Hex.encodeHexString1([10], False),
            "Hex encoding did not match expected value",
        )

    def testEncodeHexByteString_ByteArrayBoolean_ToLowerCase_test0_decomposed(
        self,
    ) -> None:
        self.assertEqual("0a", Hex.encodeHexString1([10], True))

    def testEncodeHexByteString_ByteArrayOfZeroes_test1_decomposed(self) -> None:
        c = Hex.encodeHexString0([0] * 36)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexByteString_ByteArrayOfZeroes_test0_decomposed(self) -> None:
        c = Hex.encodeHexString0([0] * 36)

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test3_decomposed(
        self,
    ) -> None:
        bb = self._allocate(36)  # Allocate a byte buffer of size 36
        bb[:3] = b"\x00" * 3  # Set the first 3 bytes to zero
        bb_view = memoryview(bb)[:3]  # Simulate a limit of 3 bytes
        self.assertEqual(
            "000000", Hex.encodeHexString2(bb_view)
        )  # Check the encoded string
        self.assertEqual(0, len(bb_view))  # Check remaining bytes (should be 0)

        bb[1:3] = b"\x00" * 2  # Reset bytes 1 and 2 to zero
        bb_view = memoryview(bb)[1:3]  # Simulate a new position and limit
        self.assertEqual(
            "0000", Hex.encodeHexString2(bb_view)
        )  # Check the encoded string
        self.assertEqual(0, len(bb_view))  # Check remaining bytes (should be 0)

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test2_decomposed(
        self,
    ) -> None:
        bb = self._allocate(36)  # Allocate a byte buffer of size 36
        bb[:3] = b"\x00" * 3  # Set the first 3 bytes to zero
        bb_view = memoryview(bb)[:3]  # Simulate setting a limit of 3
        self.assertEqual(
            "000000", Hex.encodeHexString2(bb_view)
        )  # Assert the encoded string is "000000"
        self.assertEqual(0, len(bb_view))  # Assert remaining bytes in the view is 0

        bb[1:3] = b"\x00" * 2  # Reset bytes 1 and 2 to zero
        bb_view = memoryview(bb)[1:3]  # Simulate setting position to 1 and limit to 3
        self.assertEqual(
            "0000", Hex.encodeHexString2(bb_view)
        )  # Assert the encoded string is "0000"

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test1_decomposed(
        self,
    ) -> None:
        bb = self._allocate(36)  # Allocate a byte buffer of size 36
        bb = memoryview(bb)[:3]  # Set a limit of 3 by slicing the buffer
        self.assertEqual(
            "000000", Hex.encodeHexString2(bb)
        )  # Assert the encoded string matches "000000"

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test0_decomposed(
        self,
    ) -> None:
        bb = self._allocate(36)

    def testEncodeHexByteString_ByteBufferOfZeroes_test2_decomposed(self) -> None:
        buffer = self._allocate(36)
        c = Hex.encodeHexString2(buffer)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexByteString_ByteBufferOfZeroes_test1_decomposed(self) -> None:
        self._allocate(36)
        c = Hex.encodeHexString2(self._allocate(36))

    def testEncodeHexByteString_ByteBufferOfZeroes_test0_decomposed(self) -> None:
        self._allocate(36)

    def testEncodeHexPartialInputOverbounds_test2_decomposed(self) -> None:
        data = "hello world".encode("utf-8")
        with self.assertRaises(
            IndexError
        ):  # IndexError in Java maps to IndexError in Python
            hex_result = Hex.encodeHex3(data, 9, 10, True)
        self.assertEqual(list("64"), hex_result)

    def testEncodeHexPartialInputOverbounds_test1_decomposed(self) -> None:
        data = "hello world".encode("utf-8")
        with self.assertRaises(
            IndexError
        ):  # IndexError in Java maps to IndexError in Python
            Hex.encodeHex3(data, 9, 10, True)

    def testEncodeHexPartialInputOverbounds_test0_decomposed(self) -> None:
        data: bytes = "hello world".encode("utf-8")

    def testEncodeHexPartialInputUnderbounds_test2_decomposed(self) -> None:
        data = "hello world".encode("utf-8")
        with self.assertRaises(
            IndexError
        ):  # IndexError in Java maps to IndexError in Python
            hex_result = Hex.encodeHex3(data, -2, 10, True)
        self.assertEqual(list("64"), hex_result)

    def testEncodeHexPartialInputUnderbounds_test1_decomposed(self) -> None:
        data = "hello world".encode("utf-8")
        with self.assertRaises(
            IndexError
        ):  # IndexError in Java maps to IndexError in Python
            Hex.encodeHex3(data, -2, 10, True)

    def testEncodeHexPartialInputUnderbounds_test0_decomposed(self) -> None:
        data: bytes = "hello world".encode("utf-8")

    def testEncodeHexPartialInput_test8_decomposed(self) -> None:
        data = "hello world".encode("utf-8")

        hex_result = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual([], hex_result)

        hex_result = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(list("68"), hex_result)

        hex_result = Hex.encodeHex3(data, 0, 1, False)
        self.assertEqual(list("68"), hex_result)

        hex_result = Hex.encodeHex3(data, 2, 4, True)
        self.assertEqual(list("6c6c6f20"), hex_result)

        hex_result = Hex.encodeHex3(data, 2, 4, False)
        self.assertEqual(list("6C6C6F20"), hex_result)

        hex_result = Hex.encodeHex3(data, 10, 1, True)
        self.assertEqual(list("64"), hex_result)

        hex_result = Hex.encodeHex3(data, 10, 1, False)
        self.assertEqual(list("64"), hex_result)

    def testEncodeHexPartialInput_test7_decomposed(self) -> None:
        data = "hello world".encode("utf-8")

        hex_result = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual([], hex_result)

        hex_result = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(list("68"), hex_result)

        hex_result = Hex.encodeHex3(data, 0, 1, False)
        self.assertEqual(list("68"), hex_result)

        hex_result = Hex.encodeHex3(data, 2, 4, True)
        self.assertEqual(list("6c6c6f20"), hex_result)

        hex_result = Hex.encodeHex3(data, 2, 4, False)
        self.assertEqual(list("6C6C6F20"), hex_result)

        hex_result = Hex.encodeHex3(data, 10, 1, True)
        self.assertEqual(list("64"), hex_result)

        hex_result = Hex.encodeHex3(data, 10, 1, False)
        self.assertEqual(list("64"), hex_result)

    def testEncodeHexPartialInput_test6_decomposed(self) -> None:
        data = "hello world".encode("utf-8")

        # Test case 1
        hex_result = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual([], hex_result)

        # Test case 2
        hex_result = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(list("68"), hex_result)

        # Test case 3
        hex_result = Hex.encodeHex3(data, 0, 1, False)
        self.assertEqual(list("68"), hex_result)

        # Test case 4
        hex_result = Hex.encodeHex3(data, 2, 4, True)
        self.assertEqual(list("6c6c6f20"), hex_result)

        # Test case 5
        hex_result = Hex.encodeHex3(data, 2, 4, False)
        self.assertEqual(list("6C6C6F20"), hex_result)

        # Test case 6
        hex_result = Hex.encodeHex3(data, 10, 1, True)

    def testEncodeHexPartialInput_test5_decomposed(self) -> None:
        data = "hello world".encode("utf-8")

        # Test case 1: Encoding with offset 0, length 0, toLowerCase=True
        hex_result = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual([], hex_result)

        # Test case 2: Encoding with offset 0, length 1, toLowerCase=True
        hex_result = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(list("68"), hex_result)

        # Test case 3: Encoding with offset 0, length 1, toLowerCase=False
        hex_result = Hex.encodeHex3(data, 0, 1, False)
        self.assertEqual(list("68"), hex_result)

        # Test case 4: Encoding with offset 2, length 4, toLowerCase=True
        hex_result = Hex.encodeHex3(data, 2, 4, True)
        self.assertEqual(list("6c6c6f20"), hex_result)

        # Test case 5: Encoding with offset 2, length 4, toLowerCase=False
        hex_result = Hex.encodeHex3(data, 2, 4, False)
        self.assertEqual(list("6C6C6F20"), hex_result)

    def testEncodeHexPartialInput_test4_decomposed(self) -> None:
        data = "hello world".encode(
            "utf-8"
        )  # Equivalent to getBytes(StandardCharsets.UTF_8)

        # Test case 1: dataOffset=0, dataLen=0, toLowerCase=True
        hex_result = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual(
            [], hex_result
        )  # Equivalent to assertArrayEquals(new char[0], hex)

        # Test case 2: dataOffset=0, dataLen=1, toLowerCase=True
        hex_result = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(
            list("68"), hex_result
        )  # Equivalent to assertArrayEquals("68".toCharArray(), hex)

        # Test case 3: dataOffset=0, dataLen=1, toLowerCase=False
        hex_result = Hex.encodeHex3(data, 0, 1, False)
        self.assertEqual(
            list("68"), hex_result
        )  # Equivalent to assertArrayEquals("68".toCharArray(), hex)

        # Test case 4: dataOffset=2, dataLen=4, toLowerCase=True
        hex_result = Hex.encodeHex3(data, 2, 4, True)
        # No assertion provided in the original Java code for this case

    def testEncodeHexPartialInput_test3_decomposed(self) -> None:
        data = "hello world".encode(
            "utf-8"
        )  # Equivalent to getBytes(StandardCharsets.UTF_8)
        hex_result = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual(
            [], hex_result
        )  # Equivalent to assertArrayEquals(new char[0], hex)

        hex_result = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(
            list("68"), hex_result
        )  # Equivalent to assertArrayEquals("68".toCharArray(), hex)

        hex_result = Hex.encodeHex3(data, 0, 1, False)
        # No assertion provided in the original Java code for this line

    def testEncodeHexPartialInput_test2_decomposed(self) -> None:
        data = "hello world".encode(
            "utf-8"
        )  # Equivalent to getBytes(StandardCharsets.UTF_8)
        hex_result = Hex.encodeHex3(data, 0, 0, True)  # Call the encodeHex3 method
        self.assertEqual(
            [], hex_result
        )  # Assert that the result is an empty list (equivalent to new char[0])

        hex_result = Hex.encodeHex3(
            data, 0, 1, True
        )  # Call the encodeHex3 method with different parameters

    def testEncodeHexPartialInput_test1_decomposed(self) -> None:
        data = "hello world".encode(
            "utf-8"
        )  # Equivalent to getBytes(StandardCharsets.UTF_8) in Java
        hex_result = Hex.encodeHex3(
            data, 0, 0, True
        )  # Call the encodeHex3 method with the same parameters

    def testEncodeHexPartialInput_test0_decomposed(self) -> None:
        data: bytes = "hello world".encode("utf-8")

    def testEncodeHex_ByteBufferWithLimit_test2_decomposed(self) -> None:
        bb = self._allocate(16)  # Allocate a byte buffer with a capacity of 16
        for i in range(16):
            bb[i] = i  # Populate the buffer with values 0 to 15

        expected = "000102030405060708090a0b0c0d0e0f"  # Expected hexadecimal string

        for i in range(15):
            # Simulate setting position and limit in the buffer
            position = i
            limit = i + 2
            sliced_bb = memoryview(bb)[
                position:limit
            ]  # Slice the buffer to simulate position and limit

            # Assert that the encoded hex matches the expected substring
            self.assertEqual(
                expected[i * 2 : i * 2 + 4], "".join(Hex.encodeHex6(sliced_bb))
            )

            # Assert that the remaining bytes in the sliced buffer are 0
            self.assertEqual(0, len(sliced_bb) - (limit - position))

    def testEncodeHex_ByteBufferWithLimit_test1_decomposed(self) -> None:
        bb = self._allocate(16)
        for i in range(16):
            bb[i] = i

    def testEncodeHex_ByteBufferWithLimit_test0_decomposed(self) -> None:
        bb = self._allocate(16)

    def testEncodeHex_ByteBufferOfZeroes_test2_decomposed(self) -> None:
        buffer = self._allocate(36)
        c = Hex.encodeHex6(buffer)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            "".join(c),
        )

    def testEncodeHex_ByteBufferOfZeroes_test1_decomposed(self) -> None:
        buffer = self._allocate(36)
        c = Hex.encodeHex6(buffer)

    def testEncodeHex_ByteBufferOfZeroes_test0_decomposed(self) -> None:
        self._allocate(36)

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test6_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"

        # Test encodeHex6
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected.lower(), "".join(actual))
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes
        b.obj.seek(0)  # Reset the buffer position

        # Test encodeHex7 with toLowerCase=True
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected.lower(), "".join(actual))
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes
        b.obj.seek(0)  # Reset the buffer position

        # Test encodeHex7 with toLowerCase=False
        actual = Hex.encodeHex7(b, False)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test5_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")
        expected = (
            "48656c6c6f20576f726c64"  # Lowercase version of the expected hex string
        )

        # Test Hex.encodeHex6
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected, "".join(actual))  # Convert list of chars to string
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes in buffer
        b.obj.seek(0)  # Reset buffer position

        # Test Hex.encodeHex7 with toLowerCase=True
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected, "".join(actual))  # Convert list of chars to string
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes in buffer
        b.obj.seek(0)  # Reset buffer position

        # Test Hex.encodeHex7 with toLowerCase=False
        actual = Hex.encodeHex7(b, False)
        # No assertion here as the original Java code does not include one

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test4_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")
        expected = (
            "48656c6c6f20576f726c64"  # Lowercase hex representation of "Hello World"
        )

        # Test encodeHex6
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected, "".join(actual))  # Convert list of chars to string
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes in buffer

        # Reset buffer
        b.obj.seek(0)  # Equivalent to ByteBuffer.flip() in Java

        # Test encodeHex7
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected, "".join(actual))  # Convert list of chars to string
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes in buffer

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test3_decomposed(self) -> None:
        b = self.__getByteBufferUtf8(
            "Hello World"
        )  # Get a ByteBuffer-like object for "Hello World"
        expected = "48656c6c6f20576f726c64"  # Expected result in lowercase hex

        # Test Hex.encodeHex6
        actual = Hex.encodeHex6(b)
        self.assertEqual(
            expected, "".join(actual)
        )  # Compare expected with the actual result
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Ensure no remaining bytes in the buffer

        # Reset the buffer for reuse
        b.obj.seek(0)  # Equivalent to ByteBuffer.flip()

        # Test Hex.encodeHex7 with uppercase
        actual = Hex.encodeHex7(b, True)

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test2_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")  # Get the ByteBuffer equivalent
        expected = "48656c6c6f20576f726c64"  # Expected result in lowercase
        actual = Hex.encodeHex6(b)  # Call the encodeHex6 method
        self.assertEqual(
            expected, "".join(actual)
        )  # Assert the expected and actual values match
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Assert that the buffer has no remaining bytes

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test1_decomposed(self) -> None:
        b = self.__getByteBufferUtf8(
            "Hello World"
        )  # Get the ByteBuffer equivalent in Python
        expected = "48656C6C6F20576F726C64"  # Expected hexadecimal string
        actual = Hex.encodeHex6(b)  # Call the encodeHex6 method
        self.assertEqual(
            "".join(actual), expected
        )  # Assert that the actual result matches the expected result

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test0_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test6_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"

        # Test encodeHex6
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes
        b.obj.seek(0)  # Reset buffer position

        # Test encodeHex7 with toLowerCase=True
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes
        b.obj.seek(0)  # Reset buffer position

        # Test encodeHex7 with toLowerCase=False
        actual = Hex.encodeHex7(b, False)
        self.assertEqual(expected.upper(), "".join(actual))
        self.assertEqual(0, b.nbytes - b.obj.tell())  # Check remaining bytes

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test5_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"

        # Test Hex.encodeHex6
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Check remaining bytes in the buffer
        b.obj.seek(0)  # Reset the buffer position (equivalent to flip in Java)

        # Test Hex.encodeHex7 with toLowerCase=True
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Check remaining bytes in the buffer
        b.obj.seek(0)  # Reset the buffer position (equivalent to flip in Java)

        # Test Hex.encodeHex7 with toLowerCase=False
        actual = Hex.encodeHex7(b, False)

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test4_decomposed(self) -> None:
        b = self.__getByteBufferUtf8(
            "Hello World"
        )  # Get the ByteBuffer equivalent in Python
        expected = "48656c6c6f20576f726c64"  # Expected hex string

        # Test Hex.encodeHex6
        actual = Hex.encodeHex6(b)
        self.assertEqual(
            expected, "".join(actual)
        )  # Convert list of chars to string and compare
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Check remaining bytes in the buffer

        # Reset the buffer (equivalent to flip in Java)
        b.obj.seek(0)

        # Test Hex.encodeHex7 with toLowerCase=True
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(
            expected, "".join(actual)
        )  # Convert list of chars to string and compare
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Check remaining bytes in the buffer

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test3_decomposed(self) -> None:
        b = self.__getByteBufferUtf8(
            "Hello World"
        )  # Get a ByteBuffer-like object for "Hello World"
        expected = "48656c6c6f20576f726c64"  # Expected hex string
        actual = Hex.encodeHex6(b)  # Call encodeHex6 to get the hex representation
        self.assertEqual(
            expected, "".join(actual)
        )  # Assert that the actual matches the expected
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Assert that the buffer has no remaining bytes
        b.obj.seek(0)  # Reset the buffer position (equivalent to flip in Java)
        actual = Hex.encodeHex7(b, True)  # Call encodeHex7 with toLowerCase=True

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test2_decomposed(self) -> None:
        b = self.__getByteBufferUtf8(
            "Hello World"
        )  # Get the ByteBuffer equivalent in Python
        expected = "48656c6c6f20576f726c64"  # Expected hex string
        actual = Hex.encodeHex6(b)  # Call the encodeHex6 method
        self.assertEqual(
            expected, "".join(actual)
        )  # Assert the expected and actual values match
        self.assertEqual(
            0, b.nbytes - b.obj.tell()
        )  # Assert that the buffer has no remaining bytes

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test1_decomposed(self) -> None:
        b = self.__getByteBufferUtf8(
            "Hello World"
        )  # Get the ByteBuffer equivalent in Python
        expected = "48656c6c6f20576f726c64"  # Expected hex string
        actual = Hex.encodeHex6(b)  # Call the encodeHex6 method
        self.assertEqual(
            "".join(actual), expected
        )  # Assert that the actual result matches the expected result

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test0_decomposed(self) -> None:
        b = self.__getByteBufferUtf8("Hello World")

    def testEncodeHexByteBufferEmpty_test3_decomposed(self) -> None:
        self._allocate(0)
        self.assertEqual([], Hex.encodeHex6(self._allocate(0)))
        self._allocate(0)
        self.assertEqual([], Hex(2, None, None).encode1(self._allocate(0)))

    def testEncodeHexByteBufferEmpty_test2_decomposed(self) -> None:
        self._allocate(0)
        self.assertEqual([], Hex.encodeHex6(self._allocate(0)))
        self._allocate(0)

    def testEncodeHexByteBufferEmpty_test1_decomposed(self) -> None:
        buffer = self._allocate(0)
        self.assertEqual([], Hex.encodeHex6(buffer))

    def testEncodeHexByteBufferEmpty_test0_decomposed(self) -> None:
        self._allocate(0)

    def testEncodeHexByteArrayZeroes_test1_decomposed(self) -> None:
        c = Hex.encodeHex0([0] * 36)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            "".join(c),
        )

    def testEncodeHexByteArrayZeroes_test0_decomposed(self) -> None:
        c = Hex.encodeHex0([0] * 36)

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test4_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"

        # Test with encodeHex0
        actual = Hex.encodeHex0(b)
        self.assertNotEqual(expected, "".join(actual))

        # Test with encodeHex1 (uppercase)
        actual = Hex.encodeHex1(b, True)
        self.assertNotEqual(expected, "".join(actual))

        # Test with encodeHex1 (lowercase)
        actual = Hex.encodeHex1(b, False)
        self.assertEqual(expected, "".join(actual))

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test3_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"

        # Test encodeHex0
        actual = Hex.encodeHex0(b)
        self.assertNotEqual(expected, "".join(actual))

        # Test encodeHex1 with toLowerCase=True
        actual = Hex.encodeHex1(b, True)
        self.assertNotEqual(expected, "".join(actual))

        # Test encodeHex1 with toLowerCase=False
        actual = Hex.encodeHex1(b, False)

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test2_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"
        actual = Hex.encodeHex0(b)
        self.assertNotEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, True)

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test1_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"
        actual = Hex.encodeHex0(b)
        self.assertEqual("".join(actual), expected)

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test0_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test4_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"

        # Test encodeHex0
        actual = Hex.encodeHex0(b)
        self.assertEqual(expected, "".join(actual))

        # Test encodeHex1 with toLowerCase=True
        actual = Hex.encodeHex1(b, True)
        self.assertEqual(expected, "".join(actual))

        # Test encodeHex1 with toLowerCase=False
        actual = Hex.encodeHex1(b, False)
        self.assertNotEqual(expected, "".join(actual))

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test3_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"

        # Test encodeHex0
        actual = Hex.encodeHex0(b)
        self.assertEqual(expected, "".join(actual))

        # Test encodeHex1 with toLowerCase=True
        actual = Hex.encodeHex1(b, True)
        self.assertEqual(expected, "".join(actual))

        # Test encodeHex1 with toLowerCase=False
        actual = Hex.encodeHex1(b, False)
        # No assertion here as the original Java code does not assert this case

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test2_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"

        # Test encodeHex0
        actual = Hex.encodeHex0(b)
        self.assertEqual(expected, "".join(actual))

        # Test encodeHex1 with toLowerCase=True
        actual = Hex.encodeHex1(b, True)
        self.assertEqual(expected, "".join(actual))

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test1_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"
        actual = "".join(Hex.encodeHex0(b))
        self.assertEqual(expected, actual)

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test0_decomposed(self) -> None:
        b = StringUtils.getBytesUtf8("Hello World")

    def testEncodeHexByteArrayEmpty_test1_decomposed(self) -> None:
        self.assertEqual([], Hex.encodeHex0([]))
        self.assertEqual([], Hex(2, None, None).encode0([]))

    def testEncodeHexByteArrayEmpty_test0_decomposed(self) -> None:
        self.assertEqual(
            [],
            Hex.encodeHex0([]),
            "Encoded hex array for empty byte array does not match expected result",
        )

    def testEncodeDecodeHexCharArrayRandomToOutput_test0_decomposed(self) -> None:
        for _ in range(5, 0, -1):  # Loop from 5 to 1
            # Generate random byte array
            data = os.urandom(ThreadLocalRandom.current().nextInt(10000) + 1)

            # Encode to lower case hex characters
            lower_encoded_chars = [""] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), True, lower_encoded_chars, 0)
            decoded_lower_case_bytes = Hex.decodeHex0(lower_encoded_chars)
            self.assertEqual(data, decoded_lower_case_bytes)

            # Encode to upper case hex characters
            upper_encoded_chars = [""] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), False, upper_encoded_chars, 0)
            decoded_upper_case_bytes = Hex.decodeHex0(upper_encoded_chars)
            self.assertEqual(data, decoded_upper_case_bytes)

    def testEncodeDecodeHexCharArrayRandom_test1_decomposed(self) -> None:
        hex = Hex(2, None, None)
        for _ in range(5, 0, -1):
            data = bytearray(os.urandom(ThreadLocalRandom.current().nextInt(10000) + 1))

            # Encode and decode using encodeHex0 and decodeHex0
            encoded_chars = Hex.encodeHex0(data)
            decoded_bytes = Hex.decodeHex0(encoded_chars)
            self.assertEqual(data, decoded_bytes)

            # Encode and decode using encode0 and decode0
            encoded_string_bytes = hex.encode0(data)
            decoded_bytes = hex.decode0(encoded_string_bytes)
            self.assertEqual(data, decoded_bytes)

            # Encode and decode using encode2 and decode2 with a string
            data_string = "".join(encoded_chars)
            encoded_string_chars = hex.encode2(data_string)
            decoded_bytes = hex.decode2(encoded_string_chars)
            self.assertEqual(StringUtils.getBytesUtf8(data_string), decoded_bytes)

            # Encode and decode using encode2 and decode2 with a string of encoded characters
            data_string = "".join(encoded_chars)
            encoded_string_chars = hex.encode2(data_string)
            decoded_bytes = hex.decode2("".join(encoded_string_chars))
            self.assertEqual(StringUtils.getBytesUtf8(data_string), decoded_bytes)

    def testEncodeDecodeHexCharArrayRandom_test0_decomposed(self) -> None:
        hex_instance = Hex(2, None, None)

    def testEncodeTypeError_test0_decomposed(self) -> None:
        with self.assertRaises(
            EncoderException, msg="An exception wasn't thrown when trying to encode."
        ):
            Hex(2, None, None).encode2([65])

    def testEncodeByteBufferObjectEmpty_test1_decomposed(self) -> None:
        buffer = self._allocate(0)
        hex_encoder = Hex(2, None, None)
        result = hex_encoder.encode2(buffer)
        self.assertEqual(list(result), [])

    def testEncodeByteBufferObjectEmpty_test0_decomposed(self) -> None:
        self._allocate(0)

    def testEncodeByteBufferAllocatedButEmpty_test2_decomposed(self) -> None:
        bb = self._allocate(10)  # Allocate a byte buffer with capacity 10
        bb = memoryview(bb)[:0]  # Simulate flipping the buffer to make it empty
        hex_encoder = Hex(2, None, None)  # Create a Hex instance
        self.assertEqual(
            [], hex_encoder.encode1(bb)
        )  # Assert the encoded result is an empty list
        self.assertEqual(0, len(bb))  # Assert the remaining length of the buffer is 0

    def testEncodeByteBufferAllocatedButEmpty_test1_decomposed(self) -> None:
        bb = self._allocate(10)  # Allocate a byte buffer with capacity 10
        bb = memoryview(bb)[:0]  # Simulate flipping the buffer to make it empty
        hex_encoder = Hex(2, None, None)  # Create a Hex instance
        self.assertEqual(
            [], hex_encoder.encode1(bb)
        )  # Assert that the encoded result is an empty list

    def testEncodeByteBufferAllocatedButEmpty_test0_decomposed(self) -> None:
        bb = self._allocate(10)

    def testEncodeByteBufferEmpty_test1_decomposed(self) -> None:
        empty_buffer = self._allocate(0)
        hex_instance = Hex(2, None, None)
        self.assertEqual(list(bytearray(0)), hex_instance.encode1(empty_buffer))

    def testEncodeByteBufferEmpty_test0_decomposed(self) -> None:
        self._allocate(0)

    def testEncodeByteArrayObjectEmpty_test0_decomposed(self) -> None:
        expected = []
        actual = Hex(2, None, None).encode2(bytearray())
        self.assertEqual(
            expected,
            list(actual),
            "Encoded result does not match the expected empty list",
        )

    def testEncodeByteArrayEmpty_test0_decomposed(self) -> None:
        self.assertEqual(Hex(2, None, None).encode0([]), [])

    def testDecodeByteBufferWithLimit_test1_decomposed(self) -> None:
        bb = self.__getByteBufferUtf8("000102030405060708090a0b0c0d0e0f")
        expected = bytearray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        for i in range(15):
            bb = bb.obj  # Access the underlying bytearray
            bb_view = memoryview(bb)  # Create a memoryview for slicing
            position = i * 2
            limit = i * 2 + 4
            sliced_bb = bb_view[
                position:limit
            ]  # Slice the buffer based on position and limit

            decoded = Hex(2, None, None).decode1(sliced_bb)
            expected_slice = expected[i : i + 2]

            self.assertEqual(
                str(bytearray(expected_slice), "utf-8"),
                str(bytearray(decoded), "utf-8"),
            )
            self.assertEqual(0, len(sliced_bb) - len(decoded))

    def testDecodeByteBufferWithLimit_test0_decomposed(self) -> None:
        bb = self.__getByteBufferUtf8("000102030405060708090a0b0c0d0e0f")

    def testDecodeStringEmpty_test0_decomposed(self) -> None:
        self.assertEqual(
            [],
            Hex(2, None, None).decode2(""),
            "Decoded output does not match the expected empty list",
        )

    def testDecodeHexStringOddCharacters_test0_decomposed(self) -> None:
        with pytest.raises(DecoderException):
            Hex(2, None, None).decode2("6")

    def testDecodeHexCharArrayOutBufferUnderSizedByOffset_test0_decomposed(
        self,
    ) -> None:
        out = bytearray(6)  # Create a byte array with size 6
        with self.assertRaises(
            DecoderException
        ):  # Expect a DecoderException to be raised
            Hex.decodeHex1(list("aabbccddeeff"), out, 1)  # Call the decodeHex1 method

    def testDecodeHexCharArrayOutBufferUnderSized_test0_decomposed(self) -> None:
        out = bytearray(4)  # Create a byte array with size 4
        with self.assertRaises(
            DecoderException
        ):  # Expect a DecoderException to be raised
            Hex.decodeHex1(list("aabbccddeeff"), out, 0)

    def testDecodeHexCharArrayOddCharacters5_test0_decomposed(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C", "D", "E"])

    def testDecodeHexCharArrayOddCharacters3_test0_decomposed(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C"])

    def testDecodeHexStringOddCharacters1_test0_decomposed(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters1("A")

    def testDecodeHexCharArrayOddCharacters1_test0_decomposed(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A"])

    def testDecodeTypeError_test0_decomposed(self) -> None:
        with self.assertRaises(
            DecoderException, msg="An exception wasn't thrown when trying to decode."
        ):
            Hex(2, None, None).decode2([65])

    def testDecodeHexStringEmpty_test0_decomposed(self) -> None:
        self.assertEqual([], Hex.decodeHex2(""))

    def testDecodeHexCharArrayEmpty_test0_decomposed(self) -> None:
        self.assertEqual([], Hex.decodeHex0([]))

    def testDecodeByteBufferWithLimitOddCharacters_test2_decomposed(self) -> None:
        bb = self._allocate(10)  # Allocate a byte buffer with a capacity of 10
        bb[1] = 65  # Set the value at index 1 to 65 (ASCII for 'A')
        bb_view = memoryview(bb)[1:2]  # Create a view from position 1 to limit 2
        self.__checkDecodeHexByteBufferOddCharacters(bb_view)  # Call the check method

    def testDecodeByteBufferWithLimitOddCharacters_test1_decomposed(self) -> None:
        bb = self._allocate(10)
        bb[1] = 65

    def testDecodeByteBufferWithLimitOddCharacters_test0_decomposed(self) -> None:
        bb = self._allocate(10)

    def testDecodeByteBufferOddCharacters_test2_decomposed(self) -> None:
        bb = self._allocate(1)
        bb[0] = 65  # Equivalent to bb.put((byte) 65) in Java
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferOddCharacters_test1_decomposed(self) -> None:
        bb = self._allocate(1)
        bb[0] = 65

    def testDecodeByteBufferOddCharacters_test0_decomposed(self) -> None:
        bb = self._allocate(1)

    def testDecodeByteBufferObjectEmpty_test1_decomposed(self) -> None:
        self._allocate(0)
        self.assertEqual(bytearray(0), Hex(2, None, None).decode2(self._allocate(0)))

    def testDecodeByteBufferObjectEmpty_test0_decomposed(self) -> None:
        self._allocate(0)

    def testDecodeByteBufferAllocatedButEmpty_test2_decomposed(self) -> None:
        bb = self._allocate(10)  # Allocate a byte buffer with capacity 10
        bb = memoryview(bb)[
            :0
        ]  # Flip the buffer (simulate empty buffer by slicing to 0 length)
        hex_decoder = Hex(2, None, None)  # Create a Hex instance
        self.assertEqual(
            [], hex_decoder.decode1(bb)
        )  # Assert the decoded result is an empty list
        self.assertEqual(0, len(bb))  # Assert the remaining length of the buffer is 0

    def testDecodeByteBufferAllocatedButEmpty_test1_decomposed(self) -> None:
        bb = self._allocate(10)  # Allocate a byte buffer with capacity 10
        bb = memoryview(bb)[:0]  # Simulate flipping the buffer to make it empty
        hex_decoder = Hex(2, None, None)  # Create a Hex instance
        self.assertEqual(
            [], hex_decoder.decode1(bb)
        )  # Assert that decoding an empty buffer returns an empty list

    def testDecodeByteBufferAllocatedButEmpty_test0_decomposed(self) -> None:
        bb = self._allocate(10)

    def testDecodeByteBufferEmpty_test1_decomposed(self) -> None:
        buffer = self._allocate(0)
        hex_instance = Hex(2, None, None)
        self.assertEqual(bytearray(0), hex_instance.decode1(buffer))

    def testDecodeByteBufferEmpty_test0_decomposed(self) -> None:
        self._allocate(0)

    def testDecodeByteArrayOddCharacters_test0_decomposed(self) -> None:
        with pytest.raises(DecoderException):
            Hex(2, None, None).decode0([65])

    def testDecodeByteArrayObjectEmpty_test0_decomposed(self) -> None:
        self.assertEqual(
            bytearray(0),
            Hex(2, None, None).decode2(bytearray(0)),
            "Decoded result does not match the expected empty byte array",
        )

    def testDecodeByteArrayEmpty_test0_decomposed(self) -> None:
        self.assertEqual(bytearray([]), Hex(2, None, None).decode0(bytearray([])))

    def testDecodeBadCharacterPos1_test0_decomposed(self) -> None:
        with pytest.raises(DecoderException):
            Hex(2, None, None).decode2("0q")

    def testDecodeBadCharacterPos0_test0_decomposed(self) -> None:
        with pytest.raises(DecoderException):
            Hex(2, None, None).decode2("q0")

    def testCustomCharsetToString_test0_decomposed(self) -> None:
        self.assertTrue(
            Hex(2, None, None).toString().find(Hex.DEFAULT_CHARSET_NAME) >= 0
        )

    def testCustomCharsetBadName_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Hex.Hex0(self.__BAD_ENCODING_NAME)

    def testCustomCharset0_test0_decomposed(self) -> None:
        for name in Charset.availableCharsets().keys():
            self.__testCustomCharset1(name, "testCustomCharset")

    def _allocate(self, capacity: int) -> typing.Union[bytearray, memoryview]:
        return bytearray(capacity)

    def __testCustomCharset1(self, name: str, parent: str) -> None:
        if not self.__charsetSanityCheck(name):
            return
        self.__log0(f"{parent}={name}")
        custom_codec = Hex.Hex0(name)
        source_string = "Hello World"
        source_bytes = source_string.encode(name)
        actual_encoded_bytes = custom_codec.encode0(source_bytes)
        expected_hex_string = Hex.encodeHexString0(source_bytes)
        expected_hex_string_bytes = expected_hex_string.encode(name)
        self.assertEqual(expected_hex_string_bytes, actual_encoded_bytes)
        actual_string_from_bytes = actual_encoded_bytes.decode(name)
        self.assertEqual(
            f"{name}, expectedHexString={expected_hex_string}, actualStringFromBytes={actual_string_from_bytes}",
            expected_hex_string,
            actual_string_from_bytes,
        )
        utf8_codec = Hex(2, None, None)
        expected_hex_string = "48656c6c6f20576f726c64"
        decoded_utf8_bytes = utf8_codec.decode2(expected_hex_string)
        actual_string_from_bytes = decoded_utf8_bytes.decode(utf8_codec.getCharset())
        self.assertEqual(name, source_string, actual_string_from_bytes)
        decoded_custom_bytes = custom_codec.decode0(actual_encoded_bytes)
        actual_string_from_bytes = decoded_custom_bytes.decode(name)
        self.assertEqual(name, source_string, actual_string_from_bytes)

    def __log1(self, t: BaseException) -> None:
        if self.__LOG:
            import sys

            print(t, file=sys.stdout)
            sys.stdout.flush()

    def __log0(self, s: str) -> None:
        if self.__LOG:
            print(s, flush=True)

    def __checkDecodeHexCharArrayOddCharacters1(self, data: str) -> None:
        try:
            Hex.decodeHex2(data)
            pytest.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def __checkDecodeHexByteBufferOddCharacters(
        self, data: typing.Union[bytearray, memoryview]
    ) -> None:
        try:
            Hex(2, None, None).decode1(data)
            pytest.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def __checkDecodeHexCharArrayOddCharacters0(self, data: typing.List[str]) -> None:
        try:
            Hex.decodeHex0(data)
            pytest.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def __charsetSanityCheck(self, name: str) -> bool:
        source = "the quick brown dog jumped over the lazy fox"
        try:
            # Encode the source string to bytes using the given charset
            bytes_ = source.encode(name)
            # Decode the bytes back to a string using the same charset
            str_ = bytes_.decode(name)
            # Check if the roundtrip conversion is successful
            equals = source == str_
            if not equals:
                self.__log0(
                    f"FAILED charsetSanityCheck=Interesting Python charset oddity: Roundtrip"
                    f" failed for {name}"
                )
            return equals
        except (LookupError, UnicodeEncodeError, UnicodeDecodeError) as e:
            if self.__LOG:
                self.__log0(f"FAILED charsetSanityCheck={name}, e={e}")
                self.__log1(e)
            return False

    def __getByteBufferUtf8(self, string: str) -> typing.Union[bytearray, memoryview]:
        bytes_utf8 = string.encode("utf-8")  # Convert the string to UTF-8 encoded bytes
        bb = self._allocate(
            len(bytes_utf8)
        )  # Allocate a buffer with the required capacity
        bb[: len(bytes_utf8)] = bytes_utf8  # Put the bytes into the buffer
        return memoryview(bb)  # Return a memoryview of the buffer
