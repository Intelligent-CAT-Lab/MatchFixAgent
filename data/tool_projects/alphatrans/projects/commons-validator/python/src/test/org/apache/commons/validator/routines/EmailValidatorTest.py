from __future__ import annotations
import re
import sys
import enum
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.test.org.apache.commons.validator.ResultPair import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.routines.EmailValidator import *


class EmailValidatorTest(unittest.TestCase):

    _ACTION: str = "email"
    _FORM_KEY: str = "emailForm"
    __testEmailFromPerl: typing.List[ResultPair] = [
        ResultPair("abigail@example.com", True),
        ResultPair("abigail@example.com ", True),
        ResultPair(" abigail@example.com", True),
        ResultPair("abigail @example.com ", True),
        ResultPair("*@example.net", True),
        ResultPair('"\\""@foo.bar', True),
        ResultPair("fred&barny@example.com", True),
        ResultPair("---@example.com", True),
        ResultPair("foo-bar@example.net", True),
        ResultPair('"127.0.0.1"@[127.0.0.1]', True),
        ResultPair("Abigail <abigail@example.com>", True),
        ResultPair("Abigail<abigail@example.com>", True),
        ResultPair("Abigail<@a,@b,@c:abigail@example.com>", True),
        ResultPair('"This is a phrase"<abigail@example.com>', True),
        ResultPair('"Abigail "<abigail@example.com>', True),
        ResultPair('"Joe & J. Harvey" <example @Org>', True),
        ResultPair("Abigail <abigail @ example.com>", True),
        ResultPair("Abigail made this <  abigail   @   example  .    com    >", True),
        ResultPair("Abigail(the bitch)@example.com", True),
        ResultPair("Abigail <abigail @ example . (bar) com >", True),
        ResultPair(
            "Abigail < (one)  abigail (two) @(three)example . (bar) com (quz) >", True
        ),
        ResultPair(
            "Abigail (foo) (((baz)(nested) (comment)) ! ) < (one)  abigail (two)"
            + " @(three)example . (bar) com (quz) >",
            True,
        ),
        ResultPair("Abigail <abigail(fo\\(o)@example.com>", True),
        ResultPair("Abigail <abigail(fo\\)o)@example.com> ", True),
        ResultPair("(foo) abigail@example.com", True),
        ResultPair("abigail@example.com (foo)", True),
        ResultPair('"Abi\\"gail" <abigail@example.com>', True),
        ResultPair("abigail@[example.com]", True),
        ResultPair("abigail@[exa\\[ple.com]", True),
        ResultPair("abigail@[exa\\]ple.com]", True),
        ResultPair('":sysmail"@  Some-Group. Some-Org', True),
        ResultPair("Muhammed.(I am  the greatest) Ali @(the)Vegas.WBA", True),
        ResultPair("mailbox.sub1.sub2@this-domain", True),
        ResultPair("sub-net.mailbox@sub-domain.domain", True),
        ResultPair("name:;", True),
        ResultPair("':;", True),
        ResultPair("name:   ;", True),
        ResultPair("Alfred Neuman <Neuman@BBN-TENEXA>", True),
        ResultPair("Neuman@BBN-TENEXA", True),
        ResultPair('"George, Ted" <Shared@Group.Arpanet>', True),
        ResultPair("Wilt . (the  Stilt) Chamberlain@NBA.US", True),
        ResultPair("Cruisers:  Port@Portugal, Jones@SEA;", True),
        ResultPair("$@[]", True),
        ResultPair("*()@[]", True),
        ResultPair('"quoted ( brackets" ( a comment )@example.com', True),
        ResultPair('"Joe & J. Harvey"\\x0D\\x0A     <ddd\\@ Org>', True),
        ResultPair('"Joe &\\x0D\\x0A J. Harvey" <ddd \\@ Org>', True),
        ResultPair(
            "Gourmets:  Pompous Person <WhoZiWhatZit\\@Cordon-Bleu>,\\x0D\\x0A"
            + '        Childs\\@WGBH.Boston, "Galloping Gourmet"\\@\\x0D\\x0A'
            + "        ANT.Down-Under (Australian National Television),\\x0D\\x0A"
            + "        Cheapie\\@Discount-Liquors;",
            True,
        ),
        ResultPair("   Just a string", False),
        ResultPair("string", False),
        ResultPair("(comment)", False),
        ResultPair("()@example.com", False),
        ResultPair("fred(&)barny@example.com", False),
        ResultPair("fred\\ barny@example.com", False),
        ResultPair("Abigail <abi gail @ example.com>", False),
        ResultPair("Abigail <abigail(fo(o)@example.com>", False),
        ResultPair("Abigail <abigail(fo)o)@example.com>", False),
        ResultPair('"Abi"gail" <abigail@example.com>', False),
        ResultPair("abigail@[exa]ple.com]", False),
        ResultPair("abigail@[exa[ple.com]", False),
        ResultPair("abigail@[exaple].com]", False),
        ResultPair("abigail@", False),
        ResultPair("@example.com", False),
        ResultPair("phrase: abigail@example.com abigail@example.com ;", False),
        ResultPair("invalid�char@example.com", False),
    ]
    __validator: EmailValidator = None

    def testValidator473_4_test3_decomposed(self) -> None:
        # Assert that the initial validator does not validate "test.local"
        self.assertFalse(self.validator._isValidDomain("test.local"))

        # Create a list of DomainValidator.Item objects
        items = [
            DomainValidator.Item(DomainValidator.ArrayType.GENERIC_PLUS, ["local"])
        ]

        # Create a new EmailValidator instance with custom DomainValidator
        val = EmailValidator(
            constructorId=0,
            allowLocal=True,
            allowTld=False,
            domainValidator=DomainValidator.getInstance2(True, items),
        )

        # Assert that the new validator validates "test.local"
        self.assertTrue(val._isValidDomain("test.local"))

    def testValidator473_4_test2_decomposed(self) -> None:
        self.assertFalse(self.validator._isValidDomain("test.local"))

        items: List[DomainValidator.Item] = []
        items.append(
            DomainValidator.Item(DomainValidator.ArrayType.GENERIC_PLUS, ["local"])
        )

        val = EmailValidator(
            constructorId=0,
            allowLocal=True,
            allowTld=False,
            domainValidator=DomainValidator.getInstance2(True, items),
        )

    def testValidator473_4_test1_decomposed(self) -> None:
        self.assertFalse(self.validator._isValidDomain("test.local"))
        items: List[Item] = []
        items.append(Item(ArrayType.GENERIC_PLUS, ["local"]))

    def testValidator473_4_test0_decomposed(self) -> None:
        self.assertFalse(
            self.validator._isValidDomain("test.local"),
            "Domain 'test.local' should be invalid",
        )

    def testValidator473_3_test0_decomposed(self) -> None:
        items: List[DomainValidator.Item] = []
        with self.assertRaises(ValueError):  # Equivalent to ValueError in Java
            EmailValidator(0, True, False, DomainValidator.getInstance2(False, items))

    def testValidator473_2_test0_decomposed(self) -> None:
        items: List[DomainValidator.Item] = []
        with self.assertRaises(ValueError):  # Equivalent to ValueError in Java
            EmailValidator(0, False, False, DomainValidator.getInstance2(True, items))

    def testValidator473_1_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            EmailValidator(0, False, False, None)

    def testValidator374_test0_decomposed(self) -> None:
        self.assertTrue(self.validator.isValid("abc@school.school"))

    def testValidator359_test1_decomposed(self) -> None:
        val = EmailValidator.getInstance1(False, True)
        self.assertFalse(val.isValid("test@.com"))

    def testValidator359_test0_decomposed(self) -> None:
        val = EmailValidator.getInstance1(False, True)

    def testEmailAtTLD_test1_decomposed(self) -> None:
        val = EmailValidator.getInstance1(False, True)
        self.assertTrue(val.isValid("test@com"))

    def testEmailAtTLD_test0_decomposed(self) -> None:
        val = EmailValidator.getInstance1(False, True)

    def testValidator365_test0_decomposed(self) -> None:
        self.assertFalse(
            self.validator.isValid(
                "Loremipsumdolorsitametconsecteturadipiscingelit.Nullavitaeligulamattisrhoncusnuncegestasmattisleo."
                + "Donecnonsapieninmagnatristiquedictumaacturpis.Fusceorciduifacilisisutsapieneuconsequatpharetralectus."
                + "Quisqueenimestpulvinarutquamvitaeportamattisex.Nullamquismaurisplaceratconvallisjustoquisportamauris."
                + "Innullalacusconvalliseufringillautvenenatissitametdiam.Maecenasluctusligulascelerisquepulvinarfeugiat."
                + "Sedmolestienullaaliquetorciluctusidpharetranislfinibus.Suspendissemalesuadatinciduntduisitametportaarcusollicitudinnec."
                + "Donecetmassamagna.Curabitururnadiampretiumveldignissimporttitorfringillaeuneque."
                + "Duisantetelluspharetraidtinciduntinterdummolestiesitametfelis.Utquisquamsitametantesagittisdapibusacnonodio."
                + "Namrutrummolestiediamidmattis.Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus."
                + "Morbiposueresedmetusacconsectetur.Etiamquisipsumvitaejustotempusmaximus.Sedultriciesplaceratvolutpat."
                + "Integerlacuslectusmaximusacornarequissagittissitametjusto."
                + "Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus.Maecenasindictumpurussedrutrumex.Nullafacilisi."
                + "Integerfinibusfinibusmietpharetranislfaucibusvel.Maecenasegetdolorlacinialobortisjustovelullamcorpersem."
                + "Vivamusaliquetpurusidvariusornaresapienrisusrutrumnisitinciduntmollissemnequeidmetus."
                + "Etiamquiseleifendpurus.Nuncfelisnuncscelerisqueiddignissimnecfinibusalibero."
                + "Nuncsemperenimnequesitamethendreritpurusfacilisisac.Maurisdapibussemperfelisdignissimgravida."
                + "Aeneanultricesblanditnequealiquamfinibusodioscelerisqueac.Aliquamnecmassaeumaurisfaucibusfringilla."
                + "Etiamconsequatligulanisisitametaliquamnibhtemporquis.Nuncinterdumdignissimnullaatsodalesarcusagittiseu."
                + "Proinpharetrametusneclacuspulvinarsedvolutpatliberoornare.Sedligulanislpulvinarnonlectuseublanditfacilisisante."
                + "Sedmollisnislalacusauctorsuscipit.Inhachabitasseplateadictumst.Phasellussitametvelittemporvenenatisfeliseuegestasrisus."
                + "Aliquameteratsitametnibhcommodofinibus.Morbiefficiturodiovelpulvinariaculis."
                + "Aeneantemporipsummassaaconsecteturturpisfaucibusultrices.Praesentsodalesmaurisquisportafermentum."
                + "Etiamnisinislvenenatisvelauctorutullamcorperinjusto.Proinvelligulaerat.Phasellusvestibulumgravidamassanonfeugiat."
                + "Maecenaspharetraeuismodmetusegetefficitur.Suspendisseamet@gmail.com"
            ),
            "The email should be invalid due to excessive length and invalid format.",
        )

    def testValidator293_test0_decomposed(self) -> None:
        self.assertTrue(self.validator.isValid("abc-@abc.com"))
        self.assertTrue(self.validator.isValid("abc_@abc.com"))
        self.assertTrue(self.validator.isValid("abc-def@abc.com"))
        self.assertTrue(self.validator.isValid("abc_def@abc.com"))
        self.assertFalse(self.validator.isValid("abc@abc_def.com"))

    @pytest.mark.skip(reason="Ignore")
    def testEmailFromPerl_test0_decomposed(self) -> None:
        errors = 0
        for index, result_pair in enumerate(self.__testEmailFromPerl):
            item = result_pair.item
            exp = result_pair.valid
            act = self.validator.isValid(item)
            if act != exp:
                print(f"{item}: expected {exp} actual {act}")
                errors += 1
        self.assertEqual(0, errors, "Expected 0 errors")

    def testEmailUserName_test0_decomposed(self) -> None:
        self.assertTrue(self.validator.isValid("joe1blow@apache.org"))
        self.assertTrue(self.validator.isValid("joe$blow@apache.org"))
        self.assertTrue(self.validator.isValid("joe-@apache.org"))
        self.assertTrue(self.validator.isValid("joe_@apache.org"))
        self.assertTrue(self.validator.isValid("joe+@apache.org"))
        self.assertTrue(self.validator.isValid("joe!@apache.org"))
        self.assertTrue(self.validator.isValid("joe*@apache.org"))
        self.assertTrue(self.validator.isValid("joe'@apache.org"))
        self.assertTrue(self.validator.isValid("joe%45@apache.org"))
        self.assertTrue(self.validator.isValid("joe?@apache.org"))
        self.assertTrue(self.validator.isValid("joe&@apache.org"))
        self.assertTrue(self.validator.isValid("joe=@apache.org"))
        self.assertTrue(self.validator.isValid("+joe@apache.org"))
        self.assertTrue(self.validator.isValid("!joe@apache.org"))
        self.assertTrue(self.validator.isValid("*joe@apache.org"))
        self.assertTrue(self.validator.isValid("'joe@apache.org"))
        self.assertTrue(self.validator.isValid("%joe45@apache.org"))
        self.assertTrue(self.validator.isValid("?joe@apache.org"))
        self.assertTrue(self.validator.isValid("&joe@apache.org"))
        self.assertTrue(self.validator.isValid("=joe@apache.org"))
        self.assertTrue(self.validator.isValid("+@apache.org"))
        self.assertTrue(self.validator.isValid("!@apache.org"))
        self.assertTrue(self.validator.isValid("*@apache.org"))
        self.assertTrue(self.validator.isValid("'@apache.org"))
        self.assertTrue(self.validator.isValid("%@apache.org"))
        self.assertTrue(self.validator.isValid("?@apache.org"))
        self.assertTrue(self.validator.isValid("&@apache.org"))
        self.assertTrue(self.validator.isValid("=@apache.org"))
        self.assertFalse(self.validator.isValid("joe.@apache.org"))
        self.assertFalse(self.validator.isValid(".joe@apache.org"))
        self.assertFalse(self.validator.isValid(".@apache.org"))
        self.assertTrue(self.validator.isValid("joe.ok@apache.org"))
        self.assertFalse(self.validator.isValid("joe..ok@apache.org"))
        self.assertFalse(self.validator.isValid("..@apache.org"))
        self.assertFalse(self.validator.isValid("joe(@apache.org"))
        self.assertFalse(self.validator.isValid("joe)@apache.org"))
        self.assertFalse(self.validator.isValid("joe,@apache.org"))
        self.assertFalse(self.validator.isValid("joe;@apache.org"))
        self.assertTrue(self.validator.isValid('"joe."@apache.org'))
        self.assertTrue(self.validator.isValid('".joe"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe+"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe@"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe!"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe*"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe\'"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe("@apache.org'))
        self.assertTrue(self.validator.isValid('"joe)"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe,"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe%45"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe;"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe?"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe&"@apache.org'))
        self.assertTrue(self.validator.isValid('"joe="@apache.org'))
        self.assertTrue(self.validator.isValid('".."@apache.org'))
        self.assertTrue(self.validator.isValid('"john\\"doe"@apache.org'))
        self.assertTrue(
            self.validator.isValid(
                "john56789.john56789.john56789.john56789.john56789.john56789.john@example.com"
            )
        )
        self.assertFalse(
            self.validator.isValid(
                "john56789.john56789.john56789.john56789.john56789.john56789.john5@example.com"
            )
        )
        self.assertTrue(
            self.validator.isValid("\\>escape\\\\special\\^characters\\<@example.com")
        )
        self.assertTrue(self.validator.isValid("Abc\\@def@example.com"))
        self.assertFalse(self.validator.isValid("Abc@def@example.com"))
        self.assertTrue(self.validator.isValid("space\\ monkey@example.com"))

    def testEmailWithSlashes_test0_decomposed(self) -> None:
        self.assertTrue(
            self.validator.isValid("joe!/blow@apache.org"), "/ and ! valid in username"
        )
        self.assertFalse(
            self.validator.isValid("joe@ap/ache.org"), "/ not valid in domain"
        )
        self.assertFalse(
            self.validator.isValid("joe@apac!he.org"), "! not valid in domain"
        )

    def testEmailLocalhost_test2_decomposed(self) -> None:
        no_local = EmailValidator.getInstance2(False)
        allow_local = EmailValidator.getInstance2(True)

        self.assertEqual(self.validator, no_local)

        self.assertTrue(
            allow_local.isValid("joe@localhost.localdomain"),
            "@localhost.localdomain should be accepted but wasn't",
        )
        self.assertTrue(
            allow_local.isValid("joe@localhost"),
            "@localhost should be accepted but wasn't",
        )
        self.assertFalse(
            no_local.isValid("joe@localhost.localdomain"),
            "@localhost.localdomain should not be accepted but was",
        )
        self.assertFalse(
            no_local.isValid("joe@localhost"),
            "@localhost should not be accepted but was",
        )

    def testEmailLocalhost_test1_decomposed(self) -> None:
        no_local = EmailValidator.getInstance2(False)
        allow_local = EmailValidator.getInstance2(True)
        self.assertEqual(self.validator, no_local)
        self.assertTrue(
            allow_local.isValid("joe@localhost.localdomain"),
            "@localhost.localdomain should be accepted but wasn't",
        )

    def testEmailLocalhost_test0_decomposed(self) -> None:
        no_local = EmailValidator.getInstance2(False)
        allow_local = EmailValidator.getInstance2(True)

    def testEmailWithControlChars_test0_decomposed(self) -> None:
        for c in range(0, 32):
            self.assertFalse(
                self.validator.isValid(f"foo{chr(c)}bar@domain.com"),
                f"Test control char {c}",
            )
        self.assertFalse(
            self.validator.isValid(f"foo{chr(127)}bar@domain.com"),
            "Test control char 127",
        )

    def testEmailWithSpaces_test0_decomposed(self) -> None:
        self.assertFalse(self.validator.isValid("joeblow @apache.org"))
        self.assertFalse(self.validator.isValid("joeblow@ apache.org"))
        self.assertFalse(self.validator.isValid(" joeblow@apache.org"))
        self.assertFalse(self.validator.isValid("joeblow@apache.org "))
        self.assertFalse(self.validator.isValid("joe blow@apache.org "))
        self.assertFalse(self.validator.isValid("joeblow@apa che.org "))
        self.assertTrue(self.validator.isValid('"joeblow "@apache.org'))
        self.assertTrue(self.validator.isValid('" joeblow"@apache.org'))
        self.assertTrue(self.validator.isValid('" joe blow "@apache.org'))

    def testEmailWithCommas_test0_decomposed(self) -> None:
        self.assertFalse(
            self.validator.isValid("joeblow@apa,che.org"),
            "Email with comma in domain should be invalid",
        )
        self.assertFalse(
            self.validator.isValid("joeblow@apache.o,rg"),
            "Email with comma in domain should be invalid",
        )
        self.assertFalse(
            self.validator.isValid("joeblow@apache,org"),
            "Email with comma in domain should be invalid",
        )

    def testValidator235_test2_decomposed(self) -> None:
        version = os.getenv(
            "JAVA_VERSION", "1.6"
        )  # Simulating Java's System.getProperty("java.version")
        if version < "1.6":
            print("Cannot run Unicode IDN tests")
            return  # Cannot run the test

        self.assertTrue(
            self.validator.isValid("someone@xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
        )
        self.assertTrue(
            self.validator.isValid("someone@президент.рф"),
            "президент.рф should validate",
        )
        self.assertTrue(
            self.validator.isValid("someone@www.b\u00fccher.ch"),
            "www.bücher.ch should validate",
        )
        self.assertFalse(
            self.validator.isValid("someone@www.\ufffd.ch"),
            "www.\ufffd.ch FFFD should fail",
        )
        self.assertTrue(
            self.validator.isValid("someone@www.b\u00fccher.ch"),
            "www.bücher.ch should validate",
        )
        self.assertFalse(
            self.validator.isValid("someone@www.\ufffd.ch"),
            "www.\ufffd.ch FFFD should fail",
        )

    def testValidator235_test1_decomposed(self) -> None:
        version = os.getenv(
            "JAVA_VERSION", "1.6"
        )  # Simulating Java's System.getProperty("java.version")
        if version < "1.6":
            print("Cannot run Unicode IDN tests")
            return  # Cannot run the test

        self.assertTrue(
            self.validator.isValid("someone@xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
        )

    def testValidator235_test0_decomposed(self) -> None:
        version = os.getenv("JAVA_VERSION")

    def testVALIDATOR_278_test0_decomposed(self) -> None:
        self.assertFalse(
            self.validator.isValid("someone@-test.com"),
            "Email with domain starting with '-' should be invalid",
        )
        self.assertFalse(
            self.validator.isValid("someone@test-.com"),
            "Email with domain ending with '-' should be invalid",
        )

    def testVALIDATOR_315_test0_decomposed(self) -> None:
        self.assertFalse(self.validator.isValid("me@at&t.net"))
        self.assertTrue(self.validator.isValid("me@att.net"))

    def testEmailWithBogusCharacter_test0_decomposed(self) -> None:
        self.assertFalse(self.validator.isValid("andy.noble@\u008fdata-workshop.com"))
        self.assertTrue(self.validator.isValid("andy.o'reilly@data-workshop.com"))
        self.assertFalse(self.validator.isValid("andy@o'reilly.data-workshop.com"))
        self.assertTrue(self.validator.isValid("foo+bar@i.am.not.in.us.example.com"))
        self.assertFalse(self.validator.isValid("foo+bar@example+3.com"))
        self.assertFalse(self.validator.isValid("test@%*.com"))
        self.assertFalse(self.validator.isValid("test@^&#.com"))

    def testEmailWithDotEnd_test0_decomposed(self) -> None:
        self.assertFalse(
            self.validator.isValid("andy.noble@data-workshop.com."),
            "Email ending with a dot should be invalid",
        )

    def testEmailWithDash_test0_decomposed(self) -> None:
        self.assertTrue(self.validator.isValid("andy.noble@data-workshop.com"))
        self.assertFalse(self.validator.isValid("andy-noble@data-workshop.-com"))
        self.assertFalse(self.validator.isValid("andy-noble@data-workshop.c-om"))
        self.assertFalse(self.validator.isValid("andy-noble@data-workshop.co-m"))

    def testEmailExtension_test0_decomposed(self) -> None:
        self.assertTrue(self.validator.isValid("jsmith@apache.org"))
        self.assertTrue(self.validator.isValid("jsmith@apache.com"))
        self.assertTrue(self.validator.isValid("jsmith@apache.net"))
        self.assertTrue(self.validator.isValid("jsmith@apache.info"))
        self.assertFalse(self.validator.isValid("jsmith@apache."))
        self.assertFalse(self.validator.isValid("jsmith@apache.c"))
        self.assertTrue(self.validator.isValid("someone@yahoo.museum"))
        self.assertFalse(self.validator.isValid("someone@yahoo.mu-seum"))

    def testEmailWithNumericAddress_test0_decomposed(self) -> None:
        self.assertTrue(
            self.validator.isValid("someone@[216.109.118.76]"),
            "Expected valid email with numeric address",
        )
        self.assertTrue(
            self.validator.isValid("someone@yahoo.com"),
            "Expected valid email with standard domain",
        )

    def testEmail_test0_decomposed(self) -> None:
        self.assertTrue(self.validator.isValid("jsmith@apache.org"))

    def setUp(self) -> None:
        self.validator = EmailValidator.getInstance0()

    @staticmethod
    def main(args: typing.List[str]) -> None:
        validator = EmailValidator.getInstance0()
        for arg in args:
            print(f"{arg}: {validator.isValid(arg)}")
