from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.digest.Blake3 import *


class Blake3TestVectorsTest(unittest.TestCase):

    __deriveKey: typing.List[int] = None

    __keyedHash: typing.List[int] = None

    __hash: typing.List[int] = None

    __input: typing.List[int] = None

    __hasher: Blake3 = Blake3.initHash()
    __CTX: typing.List[int] = list(b"BLAKE3 2019-12-27 16:29:52 test vectors context")
    __KEY: typing.List[int] = list(b"whats the Elvish word for friend")
    __kdfHasher: Blake3 = Blake3.initKeyDerivationFunction(__CTX)
    __keyedHasher: Blake3 = Blake3.initKeyedHash(__KEY)

    def testkeyDerivation_test5_decomposed(self) -> None:
        self.__kdfHasher.update0(self.__input)
        actual = self.__kdfHasher.doFinalize2(len(self.__deriveKey))
        self.assertEqual(self.__deriveKey, actual)

        self.__kdfHasher.reset()
        self.__kdfHasher.update0(self.__input)
        truncated = self.__kdfHasher.doFinalize2(32)
        self.assertEqual(self.__deriveKey[:32], truncated)

    def testkeyDerivation_test4_decomposed(self) -> None:
        self.__kdfHasher.update0(self.__input)
        actual = self.__kdfHasher.doFinalize2(len(self.__deriveKey))
        self.assertEqual(self.__deriveKey, actual)
        self.__kdfHasher.reset()
        self.__kdfHasher.update0(self.__input)
        truncated = self.__kdfHasher.doFinalize2(32)

    def testkeyDerivation_test3_decomposed(self) -> None:
        self.__kdfHasher.update0(self.__input)
        actual = self.__kdfHasher.doFinalize2(len(self.__deriveKey))
        self.assertEqual(self.__deriveKey, actual)
        self.__kdfHasher.reset()
        self.__kdfHasher.update0(self.__input)

    def testkeyDerivation_test2_decomposed(self) -> None:
        self.__kdfHasher.update0(self.__input)
        actual = self.__kdfHasher.doFinalize2(len(self.__deriveKey))
        self.assertEqual(self.__deriveKey, actual)
        self.__kdfHasher.reset()

    def testkeyDerivation_test1_decomposed(self) -> None:
        self.__kdfHasher.update0(self.__input)
        actual = self.__kdfHasher.doFinalize2(len(self.__deriveKey))

    def testkeyDerivation_test0_decomposed(self) -> None:
        self.__kdfHasher.update0(self.__input)

    def testkeyedHashTruncatedOutput_test1_decomposed(self) -> None:
        actual = Blake3.keyedHash(self.__KEY, self.__input)
        self.assertEqual(self.__keyedHash[:32], actual)

    def testkeyedHashTruncatedOutput_test0_decomposed(self) -> None:
        actual = Blake3.keyedHash(self.__KEY, self.__input)

    def testkeyedHashArbitraryOutputLength_test2_decomposed(self) -> None:
        self.__keyedHasher.update0(self.__input)
        actual = self.__keyedHasher.doFinalize2(len(self.__keyedHash))
        self.assertEqual(self.__keyedHash, actual)

    def testkeyedHashArbitraryOutputLength_test1_decomposed(self) -> None:
        self.__keyedHasher.update0(self.__input)
        actual = self.__keyedHasher.doFinalize2(len(self.__keyedHash))

    def testkeyedHashArbitraryOutputLength_test0_decomposed(self) -> None:
        self.__keyedHasher.update0(self.__input)

    def testhashTruncatedOutput_test1_decomposed(self) -> None:
        actual = Blake3.hash_(self.__input)
        self.assertEqual(self.__hash[:32], actual)

    def testhashTruncatedOutput_test0_decomposed(self) -> None:
        actual = Blake3.hash_(self.__input)

    def testhashArbitraryOutputLength_test2_decomposed(self) -> None:
        self.__hasher.update0(self.__input)
        actual = self.__hasher.doFinalize2(len(self.__hash))
        self.assertEqual(self.__hash, actual)

    def testhashArbitraryOutputLength_test1_decomposed(self) -> None:
        self.__hasher.update0(self.__input)
        actual = self.__hasher.doFinalize2(len(self.__hash))

    def testhashArbitraryOutputLength_test0_decomposed(self) -> None:
        self.__hasher.update0(self.__input)

    @staticmethod
    def testCases() -> typing.List[typing.List[typing.Any]]:
        return [
            [
                0,
                "af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262e00f03e7b69af26b7faaf09fcd333050338ddfe085b8cc869ca98b206c08243a26f5487789e8f660afe6c99ef9e0c52b92e7393024a80459cf91f476f9ffdbda7001c22e159b402631f277ca96f2defdf1078282314e763699a31c5363165421cce14d",
                "92b2b75604ed3c761f9d6f62392c8a9227ad0ea3f09573e783f1498a4ed60d26b18171a2f22a4b94822c701f107153dba24918c4bae4d2945c20ece13387627d3b73cbf97b797d5e59948c7ef788f54372df45e45e4293c7dc18c1d41144a9758be58960856be1eabbe22c2653190de560ca3b2ac4aa692a9210694254c371e851bc8f",
                "2cc39783c223154fea8dfb7c1b1660f2ac2dcbd1c1de8277b0b0dd39b7e50d7d905630c8be290dfcf3e6842f13bddd573c098c3f17361f1f206b8cad9d088aa4a3f746752c6b0ce6a83b0da81d59649257cdf8eb3e9f7d4998e41021fac119deefb896224ac99f860011f73609e6e0e4540f93b273e56547dfd3aa1a035ba6689d89a0",
            ],
            [
                1,
                "2d3adedff11b61f14c886e35afa036736dcd87a74d27b5c1510225d0f592e213c3a6cb8bf623e20cdb535f8d1a5ffb86342d9c0b64aca3bce1d31f60adfa137b358ad4d79f97b47c3d5e79f179df87a3b9776ef8325f8329886ba42f07fb138bb502f4081cbcec3195c5871e6c23e2cc97d3c69a613eba131e5f1351f3f1da786545e5",
                "6d7878dfff2f485635d39013278ae14f1454b8c0a3a2d34bc1ab38228a80c95b6568c0490609413006fbd428eb3fd14e7756d90f73a4725fad147f7bf70fd61c4e0cf7074885e92b0e3f125978b4154986d4fb202a3f331a3fb6cf349a3a70e49990f98fe4289761c8602c4e6ab1138d31d3b62218078b2f3ba9a88e1d08d0dd4cea11",
                "b3e2e340a117a499c6cf2398a19ee0d29cca2bb7404c73063382693bf66cb06c5827b91bf889b6b97c5477f535361caefca0b5d8c4746441c57617111933158950670f9aa8a05d791daae10ac683cbef8faf897c84e6114a59d2173c3f417023a35d6983f2c7dfa57e7fc559ad751dbfb9ffab39c2ef8c4aafebc9ae973a64f0c76551",
            ],
            [
                2,
                "7b7015bb92cf0b318037702a6cdd81dee41224f734684c2c122cd6359cb1ee63d8386b22e2ddc05836b7c1bb693d92af006deb5ffbc4c70fb44d0195d0c6f252faac61659ef86523aa16517f87cb5f1340e723756ab65efb2f91964e14391de2a432263a6faf1d146937b35a33621c12d00be8223a7f1919cec0acd12097ff3ab00ab1",
                "5392ddae0e0a69d5f40160462cbd9bd889375082ff224ac9c758802b7a6fd20a9ffbf7efd13e989a6c246f96d3a96b9d279f2c4e63fb0bdff633957acf50ee1a5f658be144bab0f6f16500dee4aa5967fc2c586d85a04caddec90fffb7633f46a60786024353b9e5cebe277fcd9514217fee2267dcda8f7b31697b7c54fab6a939bf8f",
                "1f166565a7df0098ee65922d7fea425fb18b9943f19d6161e2d17939356168e6daa59cae19892b2d54f6fc9f475d26031fd1c22ae0a3e8ef7bdb23f452a15e0027629d2e867b1bb1e6ab21c71297377750826c404dfccc2406bd57a83775f89e0b075e59a7732326715ef912078e213944f490ad68037557518b79c0086de6d6f6cdd2",
            ],
            # Add the remaining test cases here in the same format
        ]
