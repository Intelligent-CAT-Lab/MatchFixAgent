from __future__ import annotations
import collections
import sys
import datetime
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
import unittest
import enum
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class DomainValidatorTest(unittest.TestCase):

    __validator: DomainValidator = None

    def testGetArray_test0_decomposed(self) -> None:
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_MINUS)
        )
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_PLUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.GENERIC_MINUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.GENERIC_PLUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.LOCAL_MINUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.LOCAL_PLUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_RO))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.GENERIC_RO))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.INFRASTRUCTURE_RO))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.LOCAL_RO))

    def testEnumIsPublic_test0_decomposed(self) -> None:
        self.assertTrue(
            Modifier.isPublic(
                DomainValidator.ArrayType.__class__.__dict__.get("__module__")
            )
        )

    def test_LOCAL_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        sorted_result = self.__isSortedLowerCase0("LOCAL_TLDS")
        self.assertTrue(sorted_result)

    def test_LOCAL_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        sorted_result = self.__isSortedLowerCase0("_DomainValidator__LOCAL_TLDS")
        self.assertTrue(sorted_result)

    def test_GENERIC_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        sorted = self.__isSortedLowerCase0("GENERIC_TLDS")
        self.assertTrue(sorted)

    def test_GENERIC_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        sorted_result = self.__isSortedLowerCase0("GENERIC_TLDS")

    def test_COUNTRY_CODE_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        sorted = self.__isSortedLowerCase0("COUNTRY_CODE_TLDS")
        self.assertTrue(sorted)

    def test_COUNTRY_CODE_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        sorted_result = self.__isSortedLowerCase0("COUNTRY_CODE_TLDS")
        # You can add assertions here if needed, for example:
        # self.assertTrue(sorted_result)

    def test_INFRASTRUCTURE_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        sorted = self.__isSortedLowerCase0("INFRASTRUCTURE_TLDS")
        self.assertTrue(sorted)

    def test_INFRASTRUCTURE_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        sorted_result = self.__isSortedLowerCase0("INFRASTRUCTURE_TLDS")

    def testIsIDNtoASCIIBroken_test2_decomposed(self) -> None:
        print(">>DomainValidatorTest.testIsIDNtoASCIIBroken()")
        input_str = "."
        ok = input_str == IDN.toASCII(input_str)
        print(f"IDN.toASCII is {'OK' if ok else 'BROKEN'}")

        props = [
            "java.version",  # Java Runtime Environment version
            "java.vendor",  # Java Runtime Environment vendor
            "java.vm.specification.version",  # Java Virtual Machine specification version
            "java.vm.specification.vendor",  # Java Virtual Machine specification vendor
            "java.vm.specification.name",  # Java Virtual Machine specification name
            "java.vm.version",  # Java Virtual Machine implementation version
            "java.vm.vendor",  # Java Virtual Machine implementation vendor
            "java.vm.name",  # Java Virtual Machine implementation name
            "java.specification.version",  # Java Runtime Environment specification version
            "java.specification.vendor",  # Java Runtime Environment specification vendor
            "java.specification.name",  # Java Runtime Environment specification name
            "java.class.version",  # Java class format version number
        ]

        for prop in props:
            print(f"{prop}={os.getenv(prop, 'N/A')}")

        print("<<DomainValidatorTest.testIsIDNtoASCIIBroken()")
        self.assertTrue(True)

    def testIsIDNtoASCIIBroken_test1_decomposed(self) -> None:
        print(">>DomainValidatorTest.testIsIDNtoASCIIBroken()")
        input_str = "."
        ok = input_str == IDN.toASCII(input_str)
        print(f"IDN.toASCII is {'OK' if ok else 'BROKEN'}")

        props = [
            "java.version",  # Java Runtime Environment version
            "java.vendor",  # Java Runtime Environment vendor
            "java.vm.specification.version",  # Java Virtual Machine specification version
            "java.vm.specification.vendor",  # Java Virtual Machine specification vendor
            "java.vm.specification.name",  # Java Virtual Machine specification name
            "java.vm.version",  # Java Virtual Machine implementation version
            "java.vm.vendor",  # Java Virtual Machine implementation vendor
            "java.vm.name",  # Java Virtual Machine implementation name
            "java.specification.version",  # Java Runtime Environment specification version
            "java.specification.vendor",  # Java Runtime Environment specification vendor
            "java.specification.name",  # Java Runtime Environment specification name
            "java.class.version",  # Java class format version number
        ]

        for prop in props:
            print(f"{prop}={os.getenv(prop, 'Unknown')}")

    def testIsIDNtoASCIIBroken_test0_decomposed(self) -> None:
        print(">>DomainValidatorTest.testIsIDNtoASCIIBroken()")
        input = "."
        ok = input == IDN.toASCII(input)

    def testUnicodeToASCII_test1_decomposed(self) -> None:
        asciidots = [
            "",
            ",",
            ".",  # fails IDN.toASCII, but should pass wrapped version
            "a.",  # ditto
            "a.b",
            "a..b",
            "a...b",
            ".a",
            "..a",
        ]
        for s in asciidots:
            self.assertEqual(s, DomainValidator.unicodeToASCII(s))

        otherDots = [
            ["b\u3002", "b."],
            ["b\uff0e", "b."],
            ["b\uff61", "b."],
            ["\u3002", "."],
            ["\uff0e", "."],
            ["\uff61", "."],
        ]
        for s in otherDots:
            self.assertEqual(s[1], DomainValidator.unicodeToASCII(s[0]))

    def testUnicodeToASCII_test0_decomposed(self) -> None:
        asciidots = [
            "",
            ",",
            ".",  # fails IDN.toASCII, but should pass wrapped version
            "a.",  # ditto
            "a.b",
            "a..b",
            "a...b",
            ".a",
            "..a",
        ]
        for s in asciidots:
            self.assertEqual(s, DomainValidator.unicodeToASCII(s))

    def testValidator306_test3_decomposed(self) -> None:
        long_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A"
        self.assertEqual(63, len(long_string))

        self.assertTrue(
            self.__validator.isValidDomainSyntax(long_string + ".com"),
            "63 chars label should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax(long_string + "x.com"),
            "64 chars label should fail",
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("test." + long_string),
            "63 chars TLD should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("test.x" + long_string),
            "64 chars TLD should fail",
        )

        long_domain = (
            long_string + "." + long_string + "." + long_string + "." + long_string[:61]
        )
        self.assertEqual(253, len(long_domain))

        self.assertTrue(
            self.__validator.isValidDomainSyntax(long_domain),
            "253 chars domain should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax(long_domain + "x"),
            "254 chars domain should fail",
        )

    def testValidator306_test2_decomposed(self) -> None:
        long_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A"
        self.assertEqual(63, len(long_string))

        self.assertTrue(
            self.__validator.isValidDomainSyntax(long_string + ".com"),
            "63 chars label should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax(long_string + "x.com"),
            "64 chars label should fail",
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("test." + long_string),
            "63 chars TLD should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("test.x" + long_string),
            "64 chars TLD should fail",
        )

        long_domain = (
            long_string + "." + long_string + "." + long_string + "." + long_string[:61]
        )
        self.assertEqual(253, len(long_domain))

    def testValidator306_test1_decomposed(self) -> None:
        long_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A"
        self.assertEqual(63, len(long_string))
        self.assertTrue(
            self.__validator.isValidDomainSyntax(long_string + ".com"),
            "63 chars label should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax(long_string + "x.com"),
            "64 chars label should fail",
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("test." + long_string),
            "63 chars TLD should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("test.x" + long_string),
            "64 chars TLD should fail",
        )

    def testValidator306_test0_decomposed(self) -> None:
        long_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A"
        self.assertEqual(63, len(long_string))

    def testValidator297_test0_decomposed(self) -> None:
        self.assertTrue(
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
            self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
        )

    def testDomainNoDots_test0_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a"), "a (alpha) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("9"), "9 (alphanum) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("c-z"),
            "c-z (alpha - alpha) should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("c-"), "c- (alpha -) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("-c"), "-c (- alpha) should fail"
        )
        self.assertFalse(self.__validator.isValidDomainSyntax("-"), "- (-) should fail")

    def testRFC2396toplabel_test0_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c"), "a.c (alpha) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.cc"),
            "a.cc (alpha alpha) should validate",
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c9"),
            "a.c9 (alpha alphanum) should validate",
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c-9"),
            "a.c-9 (alpha - alphanum) should validate",
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c-z"),
            "a.c-z (alpha - alpha) should validate",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.9c"),
            "a.9c (alphanum alpha) should fail",
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.c-"), "a.c- (alpha -) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.-"), "a.- (-) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.-9"),
            "a.-9 (- alphanum) should fail",
        )

    def testRFC2396domainlabel_test0_decomposed(self) -> None:
        self.assertTrue(self.__validator.isValid("a.ch"), "a.ch should validate")
        self.assertTrue(self.__validator.isValid("9.ch"), "9.ch should validate")
        self.assertTrue(self.__validator.isValid("az.ch"), "az.ch should validate")
        self.assertTrue(self.__validator.isValid("09.ch"), "09.ch should validate")
        self.assertTrue(self.__validator.isValid("9-1.ch"), "9-1.ch should validate")
        self.assertFalse(
            self.__validator.isValid("91-.ch"), "91-.ch should not validate"
        )
        self.assertFalse(self.__validator.isValid("-.ch"), "-.ch should not validate")

    def testIDNJava6OrLater_test2_decomposed(self) -> None:
        version = os.getenv("JAVA_VERSION", "1.6")  # Simulating Java version check
        if version < "1.6":
            print("Cannot run Unicode IDN tests")
            return  # Cannot run the test

        self.assertTrue(
            self.__validator.isValid("www.bücher.ch"), "bücher.ch should validate"
        )
        self.assertTrue(
            self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
        )
        self.assertTrue(
            self.__validator.isValid("президент.рф"), "президент.рф should validate"
        )
        self.assertFalse(
            self.__validator.isValid("www.\ufffd.ch"), "www.\ufffd.ch FFFD should fail"
        )

    def testIDNJava6OrLater_test1_decomposed(self) -> None:
        version = os.getenv("JAVA_VERSION", "1.6")  # Simulating Java version check
        if version < "1.6":
            print("Cannot run Unicode IDN tests")
            return  # Cannot run the test
        self.assertTrue(
            self.__validator.isValid("www.bücher.ch"), "www.bücher.ch should validate"
        )

    def testIDNJava6OrLater_test0_decomposed(self) -> None:
        version = os.getenv("JAVA_VERSION")

    def testIDN_test0_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValid("www.xn--bcher-kva.ch"),
            "b\u00fccher.ch in IDN should validate",
        )

    def testAllowLocal_test2_decomposed(self) -> None:
        noLocal = DomainValidator.getInstance1(False)
        allowLocal = DomainValidator.getInstance1(True)

        self.assertEqual(noLocal, self.__validator)

        self.assertFalse(
            noLocal.isValid("localhost.localdomain"),
            "localhost.localdomain should validate",
        )
        self.assertFalse(noLocal.isValid("localhost"), "localhost should validate")
        self.assertTrue(
            allowLocal.isValid("localhost.localdomain"),
            "localhost.localdomain should validate",
        )
        self.assertTrue(allowLocal.isValid("localhost"), "localhost should validate")
        self.assertTrue(allowLocal.isValid("hostname"), "hostname should validate")
        self.assertTrue(
            allowLocal.isValid("machinename"), "machinename should validate"
        )
        self.assertTrue(allowLocal.isValid("apache.org"), "apache.org should validate")
        self.assertFalse(
            allowLocal.isValid(" apache.org "),
            "domain name with spaces shouldn't validate",
        )

    def testAllowLocal_test1_decomposed(self) -> None:
        noLocal = DomainValidator.getInstance1(False)
        allowLocal = DomainValidator.getInstance1(True)
        self.assertEqual(noLocal, self.__validator)
        self.assertFalse(
            noLocal.isValid("localhost.localdomain"),
            "localhost.localdomain should validate",
        )

    def testAllowLocal_test0_decomposed(self) -> None:
        noLocal = DomainValidator.getInstance1(False)
        allowLocal = DomainValidator.getInstance1(True)

    def testTopLevelDomains_test4_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValidInfrastructureTld(".arpa"),
            ".arpa should validate as iTLD",
        )
        self.assertFalse(
            self.__validator.isValidInfrastructureTld(".com"),
            ".com shouldn't validate as iTLD",
        )
        self.assertTrue(
            self.__validator.isValidGenericTld(".name"), ".name should validate as gTLD"
        )
        self.assertFalse(
            self.__validator.isValidGenericTld(".us"), ".us shouldn't validate as gTLD"
        )
        self.assertTrue(
            self.__validator.isValidCountryCodeTld(".uk"),
            ".uk should validate as ccTLD",
        )
        self.assertFalse(
            self.__validator.isValidCountryCodeTld(".org"),
            ".org shouldn't validate as ccTLD",
        )
        self.assertTrue(
            self.__validator.isValidTld(".COM"), ".COM should validate as TLD"
        )
        self.assertTrue(
            self.__validator.isValidTld(".BiZ"), ".BiZ should validate as TLD"
        )
        self.assertFalse(
            self.__validator.isValid(".nope"), "invalid TLD shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid(""), "empty string shouldn't validate as TLD"
        )
        self.assertFalse(
            self.__validator.isValid(None), "null shouldn't validate as TLD"
        )

    def testTopLevelDomains_test3_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValidInfrastructureTld(".arpa"),
            ".arpa should validate as iTLD",
        )
        self.assertFalse(
            self.__validator.isValidInfrastructureTld(".com"),
            ".com shouldn't validate as iTLD",
        )
        self.assertTrue(
            self.__validator.isValidGenericTld(".name"), ".name should validate as gTLD"
        )
        self.assertFalse(
            self.__validator.isValidGenericTld(".us"), ".us shouldn't validate as gTLD"
        )
        self.assertTrue(
            self.__validator.isValidCountryCodeTld(".uk"),
            ".uk should validate as ccTLD",
        )
        self.assertFalse(
            self.__validator.isValidCountryCodeTld(".org"),
            ".org shouldn't validate as ccTLD",
        )
        self.assertTrue(
            self.__validator.isValidTld(".COM"), ".COM should validate as TLD"
        )
        self.assertTrue(
            self.__validator.isValidTld(".BiZ"), ".BiZ should validate as TLD"
        )

    def testTopLevelDomains_test2_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValidInfrastructureTld(".arpa"),
            ".arpa should validate as iTLD",
        )
        self.assertFalse(
            self.__validator.isValidInfrastructureTld(".com"),
            ".com shouldn't validate as iTLD",
        )
        self.assertTrue(
            self.__validator.isValidGenericTld(".name"), ".name should validate as gTLD"
        )
        self.assertFalse(
            self.__validator.isValidGenericTld(".us"), ".us shouldn't validate as gTLD"
        )
        self.assertTrue(
            self.__validator.isValidCountryCodeTld(".uk"),
            ".uk should validate as ccTLD",
        )
        self.assertFalse(
            self.__validator.isValidCountryCodeTld(".org"),
            ".org shouldn't validate as ccTLD",
        )

    def testTopLevelDomains_test1_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValidInfrastructureTld(".arpa"),
            ".arpa should validate as iTLD",
        )
        self.assertFalse(
            self.__validator.isValidInfrastructureTld(".com"),
            ".com shouldn't validate as iTLD",
        )
        self.assertTrue(
            self.__validator.isValidGenericTld(".name"), ".name should validate as gTLD"
        )
        self.assertFalse(
            self.__validator.isValidGenericTld(".us"), ".us shouldn't validate as gTLD"
        )

    def testTopLevelDomains_test0_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValidInfrastructureTld(".arpa"),
            ".arpa should validate as iTLD",
        )
        self.assertFalse(
            self.__validator.isValidInfrastructureTld(".com"),
            ".com shouldn't validate as iTLD",
        )

    def testInvalidDomains_test0_decomposed(self) -> None:
        self.assertFalse(
            self.__validator.isValid(".org"), "bare TLD .org shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid(" apache.org "),
            "domain name with spaces shouldn't validate",
        )
        self.assertFalse(
            self.__validator.isValid("apa che.org"),
            "domain name containing spaces shouldn't validate",
        )
        self.assertFalse(
            self.__validator.isValid("-testdomain.name"),
            "domain name starting with dash shouldn't validate",
        )
        self.assertFalse(
            self.__validator.isValid("testdomain-.name"),
            "domain name ending with dash shouldn't validate",
        )
        self.assertFalse(
            self.__validator.isValid("---c.com"),
            "domain name starting with multiple dashes shouldn't validate",
        )
        self.assertFalse(
            self.__validator.isValid("c--.com"),
            "domain name ending with multiple dashes shouldn't validate",
        )
        self.assertFalse(
            self.__validator.isValid("apache.rog"),
            "domain name with invalid TLD shouldn't validate",
        )
        self.assertFalse(
            self.__validator.isValid("http://www.apache.org"), "URL shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid(" "),
            "Empty string shouldn't validate as domain name",
        )
        self.assertFalse(
            self.__validator.isValid(None), "Null shouldn't validate as domain name"
        )

    def testValidDomains_test0_decomposed(self) -> None:
        self.assertTrue(
            self.__validator.isValid("apache.org"), "apache.org should validate"
        )
        self.assertTrue(
            self.__validator.isValid("www.google.com"), "www.google.com should validate"
        )
        self.assertTrue(
            self.__validator.isValid("test-domain.com"),
            "test-domain.com should validate",
        )
        self.assertTrue(
            self.__validator.isValid("test---domain.com"),
            "test---domain.com should validate",
        )
        self.assertTrue(
            self.__validator.isValid("test-d-o-m-ain.com"),
            "test-d-o-m-ain.com should validate",
        )
        self.assertTrue(
            self.__validator.isValid("as.uk"), "two-letter domain label should validate"
        )
        self.assertTrue(
            self.__validator.isValid("ApAchE.Org"),
            "case-insensitive ApAchE.Org should validate",
        )
        self.assertTrue(
            self.__validator.isValid("z.com"),
            "single-character domain label should validate",
        )
        self.assertTrue(
            self.__validator.isValid("i.have.an-example.domain.name"),
            "i.have.an-example.domain.name should validate",
        )

    def setUp(self) -> None:
        self.validator = DomainValidator.getInstance0()

    @staticmethod
    def main(a: typing.List[str]) -> None:
        OK = True
        for list_name in [
            "INFRASTRUCTURE_TLDS",
            "COUNTRY_CODE_TLDS",
            "GENERIC_TLDS",
            "LOCAL_TLDS",
        ]:
            OK &= DomainValidatorTest.__isSortedLowerCase0(list_name)

        if not OK:
            print("Fix arrays before retrying; cannot continue")
            return

        iana_tlds = set()  # Keep for comparison with array contents
        dv = DomainValidator.getInstance0()
        txt_file = pathlib.Path("target/tlds-alpha-by-domain.txt")
        timestamp = DomainValidatorTest.__download(
            txt_file, "https://data.iana.org/TLD/tlds-alpha-by-domain.txt", 0
        )
        html_file = pathlib.Path("target/tlds-alpha-by-domain.html")
        DomainValidatorTest.__download(
            html_file, "https://www.iana.org/domains/root/db", timestamp
        )

        with txt_file.open("r", encoding="utf-8") as br:
            line = br.readline()  # Header
            if line.startswith("# Version "):
                header = line[2:]
            else:
                raise IOError("File does not have expected Version header")

            generate_unicode_tlds = (
                False  # Change this to generate Unicode TLDs as well
            )

            html_info = DomainValidatorTest.__getHtmlInfo(html_file)
            missing_tld = {}  # Stores entry and comments as strings
            missing_cc = {}

            for line in br:
                if not line.startswith("#"):
                    line = line.strip()
                    unicode_tld = (
                        None  # Only different from ascii_tld if that was punycode
                    )
                    ascii_tld = line.lower()
                    if line.startswith("XN--"):
                        unicode_tld = str(IDN.toUnicode(line))
                    else:
                        unicode_tld = ascii_tld

                    if not dv.isValidTld(ascii_tld):
                        info = html_info.get(ascii_tld)
                        if info is not None:
                            type_, comment = info
                            if type_ == "country-code":  # Which list to use?
                                missing_cc[ascii_tld] = f"{unicode_tld} {comment}"
                                if generate_unicode_tlds:
                                    missing_cc[unicode_tld] = f"{ascii_tld} {comment}"
                            else:
                                missing_tld[ascii_tld] = f"{unicode_tld} {comment}"
                                if generate_unicode_tlds:
                                    missing_tld[unicode_tld] = f"{ascii_tld} {comment}"
                        else:
                            print(
                                f"Expected to find HTML info for {ascii_tld}",
                                file=sys.stderr,
                            )

                    iana_tlds.add(ascii_tld)
                    if generate_unicode_tlds and unicode_tld != ascii_tld:
                        iana_tlds.add(unicode_tld)

        for key in sorted(html_info.keys()):
            if key not in iana_tlds:
                if DomainValidatorTest.__isNotInRootZone(key):
                    print(f"INFO: HTML entry not yet in root zone: {key}")
                else:
                    print(
                        f"WARN: Expected to find text entry for html: {key}",
                        file=sys.stderr,
                    )

        if missing_tld:
            DomainValidatorTest.__printMap(header, missing_tld, "TLD")
        if missing_cc:
            DomainValidatorTest.__printMap(header, missing_cc, "CC")

        DomainValidatorTest.__isInIanaList0("INFRASTRUCTURE_TLDS", iana_tlds)
        DomainValidatorTest.__isInIanaList0("COUNTRY_CODE_TLDS", iana_tlds)
        DomainValidatorTest.__isInIanaList0("GENERIC_TLDS", iana_tlds)

        print("Finished checks")

    @staticmethod
    def __isSortedLowerCase1(name: str, array: List[str]) -> bool:
        sorted = True
        strictly_sorted = True
        length = len(array)
        lower_case = DomainValidatorTest.__isLowerCase(
            array[length - 1]
        )  # Check the last entry

        for i in range(length - 1):  # compare all but last entry with next
            entry = array[i]
            next_entry = array[i + 1]
            cmp = (entry > next_entry) - (
                entry < next_entry
            )  # Simulate Java's compareTo

            if cmp > 0:  # out of order
                print(f"Out of order entry: {entry} < {next_entry} in {name}")
                sorted = False
            elif cmp == 0:
                strictly_sorted = False
                print(f"Duplicated entry: {entry} in {name}")

            if not DomainValidatorTest.__isLowerCase(entry):
                print(f"Non lowerCase entry: {entry} in {name}")
                lower_case = False

        return sorted and strictly_sorted and lower_case

    @staticmethod
    def __isLowerCase(string: str) -> bool:
        return string == string.lower()

    @staticmethod
    def __isSortedLowerCase0(arrayName: str) -> bool:
        from src.main.org.apache.commons.validator.routines.DomainValidator import (
            DomainValidator,
        )
        import inspect

        # Get the field from the DomainValidator class
        f = getattr(DomainValidator, arrayName, None)
        if f is None:
            raise AttributeError(f"Field '{arrayName}' not found in DomainValidator")

        # Check if the field is private
        is_private = arrayName.startswith("_")
        if is_private:
            # Python doesn't have direct access modifiers like Java, but we assume private fields start with '_'
            pass  # No need to explicitly set accessibility in Python

        # Get the value of the field
        array = f

        # Call the helper method to check if the array is sorted and lowercase
        try:
            return DomainValidatorTest.__isSortedLowerCase1(arrayName, array)
        finally:
            # No need to reset accessibility in Python
            pass

    @staticmethod
    def __isInIanaList1(
        name: str, array: typing.List[str], ianaTlds: typing.Set[str]
    ) -> bool:
        for item in array:
            if item not in ianaTlds:
                print(f"{name} contains unexpected value: {item}")
        return True

    @staticmethod
    def __isInIanaList0(arrayName: str, ianaTlds: typing.Set[str]) -> bool:
        # Get the field from the DomainValidator class
        f = getattr(DomainValidator, arrayName, None)
        if f is None:
            raise AttributeError(f"Field '{arrayName}' not found in DomainValidator")

        # Check if the field is private (simulated by checking if it starts with an underscore)
        is_private = arrayName.startswith("_")
        if is_private:
            # Simulate making the field accessible (not needed in Python, but included for clarity)
            pass

        # Assume the field is a list of strings
        array = f

        try:
            # Call the helper method __isInIanaList1
            return DomainValidatorTest.__isInIanaList1(arrayName, array, ianaTlds)
        finally:
            if is_private:
                # Simulate restoring the field's accessibility (not needed in Python)
                pass

    @staticmethod
    def __closeQuietly(in_: Closeable) -> None:
        if in_ is not None:
            try:
                in_.close()
            except IOError:
                pass

    @staticmethod
    def __isNotInRootZone(domain: str) -> bool:
        tldurl = f"http://www.iana.org/domains/root/db/{domain}.html"
        root_check = pathlib.Path("target") / f"tld_{domain}.html"
        in_ = None
        try:
            DomainValidatorTest.__download(root_check, tldurl, 0)
            with root_check.open("r", encoding="utf-8") as in_:
                for input_line in in_:
                    if (
                        "This domain is not present in the root zone at this time."
                        in input_line
                    ):
                        return True
        except IOError:
            pass
        finally:
            DomainValidatorTest.__closeQuietly(in_)
        return False

    @staticmethod
    def __download(f: pathlib.Path, tldurl: str, timestamp: int) -> int:
        import time
        import requests
        from datetime import datetime, timezone

        HOUR = 60 * 60 * 1000  # an hour in ms
        mod_time = 0

        if f.exists() and f.is_file():
            mod_time = int(f.stat().st_mtime * 1000)  # Convert seconds to milliseconds
            if mod_time > int(time.time() * 1000) - HOUR:
                print(f"Skipping download - found recent {f}")
                return mod_time

        headers = {}
        if mod_time > 0:
            since = datetime.fromtimestamp(mod_time / 1000, tz=timezone.utc).strftime(
                "%a, %d %b %Y %H:%M:%S GMT"
            )
            headers["If-Modified-Since"] = since
            print(f"Found {f} with date {since}")

        response = requests.get(tldurl, headers=headers, stream=True)

        if response.status_code == 304:
            print(f"Already have most recent {tldurl}")
        else:
            print(f"Downloading {tldurl}")
            with open(f, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print("Done")

        return int(f.stat().st_mtime * 1000)  # Return last modified time in ms

    @staticmethod
    def __getHtmlInfo(f: pathlib.Path) -> typing.Dict[str, typing.List[str]]:
        import re
        from collections import defaultdict

        info = {}

        domain_pattern = re.compile(r".*<a href=\"/domains/root/db/([^.]+)\.html")
        type_pattern = re.compile(r"\s+<td>([^<]+)</td>")
        comment_pattern = re.compile(r"\s+<td>([^<]+)</td>")

        with f.open("r", encoding="utf-8") as br:
            lines = br.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                domain_match = domain_pattern.match(line)
                if domain_match:
                    dom = domain_match.group(1)
                    typ = "??"
                    com = "??"
                    i += 1
                    while (
                        i < len(lines) and lines[i].strip() == ""
                    ):  # Skip extra blank lines
                        i += 1
                    if i < len(lines):
                        line = lines[i].strip()
                        type_match = type_pattern.match(line)
                        if type_match:
                            typ = type_match.group(1)
                            i += 1
                            if i < len(lines) and re.match(
                                r"\s+<!--.*", lines[i].strip()
                            ):
                                while i < len(lines) and not re.match(
                                    r".*-->.*", lines[i].strip()
                                ):
                                    i += 1
                                i += 1
                            while i < len(lines) and not re.match(
                                r".*</td>.*", lines[i].strip()
                            ):
                                line += " " + lines[i].strip()
                                i += 1
                            comment_match = comment_pattern.match(line)
                            if comment_match:
                                com = comment_match.group(1)
                            if (
                                "Not assigned" in com
                                or "Retired" in com
                                or typ == "test"
                            ):
                                pass
                            else:
                                info[dom.lower()] = [typ, com]
                        else:
                            print(f"Unexpected type: {line}")
                i += 1
        return info

    @staticmethod
    def __printMap(header: str, map_: typing.Dict[str, str], string: str) -> None:
        print(f"Entries missing from {string} List\n")
        if header is not None:
            print(f"        // Taken from {header}")
        for key, value in map_.items():
            print(f'        "{key}", // {value}')
        print("\nDone")
