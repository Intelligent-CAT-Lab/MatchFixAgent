from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.MatchRatingApproachEncoder import *


class MatchRatingApproachEncoderTest(unittest.TestCase):

    def testCompare_Forenames_SEAN_PETE_NoMatchExpected_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Sean", "Pete"))

    def testCompare_Forenames_SEAN_PETE_NoMatchExpected_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_Forenames_SEAN_JOHN_MatchExpected_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Sean", "John"))

    def testCompare_Forenames_SEAN_JOHN_MatchExpected_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Murphy", "Lynch"))

    def testCompare_Surnames_MURPHY_LYNCH_NoMatchExpected_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_SurnameCornerCase_Nulls_NoMatch_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals(None, None))

    def testCompare_SurnameCornerCase_Nulls_NoMatch_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Murphy", ""))

    def testCompare_SurnamesCornerCase_MURPHY_NoSpace_NoMatch_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(
            encoder.isEncodeEquals("Murphy", " "),
            "Expected no match when comparing 'Murphy' with a space",
        )

    def testCompare_SurnamesCornerCase_MURPHY_Space_NoMatch_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("McGowan", "Mc Geoghegan"))

    def testCompare_MCGOWAN_MCGEOGHEGAN_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_PETERSON_PETERS_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Peterson", "Peters"))

    def testCompare_PETERSON_PETERS_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals(" P rz e m y s l", " P sh e m e sh i l"))

    def testCompare_Surname_PRZEMYSL_PSHEMESHIL_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(
            encoder.isEncodeEquals(
                "R o s o ch o w a c ie c", " R o s o k ho v a ts e ts"
            )
        )

    def testCompare_Surname_ROSOCHOWACIEC_ROSOKHOVATSETS_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("SZLAMAWICZ", "SHLAMOVITZ"))

    def testCompare_Surname_SZLAMAWICZ_SHLAMOVITZ_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("LEWINSKY", "LEVINSKI"))

    def testCompare_Surname_LEWINSKY_LEVINSKI_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("LIPSHITZ", "LIPPSZYC"))

    def testCompare_Surname_LIPSHITZ_LIPPSZYC_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Moskowitz", "Moskovitz"))

    def testCompare_Surname_MOSKOWITZ_MOSKOVITZ_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Auerbach", "Uhrbach"))

    def testCompare_Surname_AUERBACH_UHRBACH_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Hailey", "Halley"))

    def testCompare_Surname_HAILEY_HALLEY_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Cooper-Flynn", "Super-Lyn"))

    def testCompare_Surname_COOPERFLYNN_SUPERLYN_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("o'muireadhaigh", "Ó 'Muircheartaigh "))

    def testCompare_LongSurnames_OMUIRCHEARTAIGH_OMIREADHAIGH_SuccessfulMatch_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Moriarty", "OMuircheartaigh"))

    def testCompare_LongSurnames_MORIARTY_OMUIRCHEARTAIGH_DoesNotSuccessfulMatch_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("O'Sullivan", "Ó ' Súilleabháin"))

    def testCompare_Surname_OSULLIVAN_OSUILLEABHAIN_SuccessfulMatch_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Úna", "Oonagh"))

    def testCompare_Forenames_UNA_OONAGH_ShouldSuccessfullyMatchButDoesNot_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_KARL_ALESSANDRO_DoesNotMatch_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Karl", "Alessandro"))

    def testCompare_KARL_ALESSANDRO_DoesNotMatch_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Zach", "Zacharia"))

    def testCompare_ZACH_ZAKARIA_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Karl", "C"))

    def testCompareNameToSingleLetter_KARL_C_DoesNotMatch_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Kl", "Karl"))

    def testCompare_SmallInput_CARK_Kl_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_TOMASZ_TOM_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Tomasz", "tom"))

    def testCompare_TOMASZ_TOM_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Franciszek", "Frances"))

    def testCompare_FRANCISZEK_FRANCES_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Sophie", "Sofia"))

    def testCompare_SOPHIE_SOFIA_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_OONA_OONAGH_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Oona", "Oonagh"))

    def testCompare_OONA_OONAGH_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Micky", "Michael"))

    def testCompare_MICKY_MICHAEL_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_SAM_SAMUEL_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Sam", "Samuel"))

    def testCompare_SAM_SAMUEL_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Stephen", "Stefan"))

    def testCompare_STEPHEN_STEFAN_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Steven", "Stefan"))

    def testCompare_STEVEN_STEFAN_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Stephen", "Steven"))

    def testCompare_STEPHEN_STEVEN_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Cólm.   ", "C-olín"))

    def testCompare_COLM_COLIN_WithAccentsAndSymbolsAndSpaces_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_SEAN_SHAUN_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Séan", "Shaun"))

    def testCompare_SEAN_SHAUN_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Brian", "Bryan"))

    def testCompare_BRIAN_BRYAN_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Catherine", "Kathryn"))

    def testCompare_CATHERINE_KATHRYN_SuccessfullyMatched_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompare_ShortNames_AL_ED_WorksButNoMatch_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("Al", "Ed"))

    def testCompare_ShortNames_AL_ED_WorksButNoMatch_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_BURNS_BOURNE_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("Burns", "Bourne"))

    def testCompare_BURNS_BOURNE_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompare_SMITH_SMYTH_SuccessfullyMatched_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("smith", "smyth"))

    def testCompare_SMITH_SMYTH_SuccessfullyMatched_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testCompareNameSameNames_ReturnsFalseSuccessfully_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isEncodeEquals("John", "John"))

    def testCompareNameSameNames_ReturnsFalseSuccessfully_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testCompareNameNullSpace_ReturnsFalseSuccessfully_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals(None, " "))

    def testCompareNameNullSpace_ReturnsFalseSuccessfully_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testGetEncoding_One_Letter_to_Nothing_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("", encoder.encode1("E"))

    def testGetEncoding_One_Letter_to_Nothing_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetEncoding_Null_to_Nothing_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("", encoder.encode1(None))

    def testGetEncoding_Null_to_Nothing_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetEncoding_NoSpace_to_Nothing_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("", encoder.encode1(""))

    def testGetEncoding_NoSpace_to_Nothing_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetEncoding_Space_to_Nothing_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("", encoder.encode1(" "))

    def testGetEncoding_Space_to_Nothing_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetEncoding_SMYTH_to_SMYTH_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("SMYTH", encoder.encode1("Smyth"))

    def testGetEncoding_SMYTH_to_SMYTH_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetEncoding_SMITH_to_SMTH_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("SMTH", encoder.encode1("Smith"))

    def testGetEncoding_SMITH_to_SMTH_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetEncoding_HARPER_HRPR_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("HRPR", encoder.encode1("HARPER"))

    def testGetEncoding_HARPER_HRPR_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("test", "t"))

    def testisEncodeEqualsSecondNameJust1Letter_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("t", "test"))

    def testisEncodeEquals_CornerCase_FirstNameJust1Letter_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals(None, "test"))

    def testisEncodeEquals_CornerCase_FirstNameNull_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("test", None))

    def testisEncodeEquals_CornerCase_SecondNameNull_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals(" ", "test"))

    def testisEncodeEquals_CornerCase_FirstNameJustSpace_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("test", " "))

    def testisEncodeEquals_CornerCase_SecondNameJustSpace_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("", "test"))

    def testisEncodeEquals_CornerCase_FirstNameNothing_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isEncodeEquals("test", ""))

    def testisEncodeEquals_CornerCase_SecondNameNothing_ReturnsFalse_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testisVowel_SingleVowel_ReturnsTrue_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isVowel("I"))

    def testisVowel_SingleVowel_ReturnsTrue_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testcleanName_SuccessfullyClean_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("THISISATEST", encoder.cleanName("This-ís   a t.,es &t"))

    def testcleanName_SuccessfullyClean_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetMinRating_13_Returns_1_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(1, encoder.getMinRating(13))

    def testGetMinRating_13_Returns_1_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testgetMinRating_11_Returns_3_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(3, encoder.getMinRating(11))

    def testgetMinRating_11_Returns_3_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testgetMinRating_10_Returns3_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(3, encoder.getMinRating(10))

    def testgetMinRating_10_Returns3_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testgetMinRating_8_Returns3_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(3, encoder.getMinRating(8))

    def testgetMinRating_8_Returns3_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testgetMinRating_7_Returns4_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(4, encoder.getMinRating(7))

    def testgetMinRating_7_Returns4_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testgetMinRating_6_Returns4_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(4, encoder.getMinRating(6))

    def testgetMinRating_6_Returns4_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testgetMinRating_5_Returns4_Successfully2_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(4, encoder.getMinRating(5))

    def testgetMinRating_5_Returns4_Successfully2_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testgetMinRating_5_Returns4_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(4, encoder.getMinRating(5))

    def testgetMinRating_5_Returns4_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetMinRating_2_Returns5_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(5, encoder.getMinRating(2))

    def testGetMinRating_2_Returns5_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetMinRating_1_Returns5_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(5, encoder.getMinRating(1))

    def testGetMinRating_1_Returns5_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetMinRating_7_Return4_Successfully_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(4, encoder.getMinRating(7))

    def testGetMinRating_7_Return4_Successfully_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        result = encoder.leftToRightThenRightToLeftProcessing("EINSTEIN", "MICHAELA")
        self.assertEqual(0, result)

    def testleftTorightThenRightToLeft_EINSTEIN_MICHAELA_Returns0_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        result = encoder.leftToRightThenRightToLeftProcessing("ALEXANDER", "ALEXANDRA")
        self.assertEqual(4, result)

    def testleftTorightThenRightToLeft_ALEXANDER_ALEXANDRA_Returns4_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testGetFirstLast3_PETE_Returns_PETE_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("PETE", encoder.getFirst3Last3("PETE"))

    def testGetFirstLast3_PETE_Returns_PETE_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testGetFirstLast3__ALEXANDER_Returns_Aleder_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        result = encoder.getFirst3Last3("Alexzander")
        self.assertEqual("Aleder", result)

    def testGetFirstLast3__ALEXANDER_Returns_Aleder_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testRemoveVowel__DECLAN_Returns_DCLN_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("DCLN", encoder.removeVowels("DECLAN"))

    def testRemoveVowel__DECLAN_Returns_DCLN_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testRemoveVowel__AIDAN_Returns_ADN_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("ADN", encoder.removeVowels("AIDAN"))

    def testRemoveVowel__AIDAN_Returns_ADN_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("ALSSNDR", encoder.removeVowels("ALESSANDRA"))

    def testRemoveVowel_ALESSANDRA_Returns_ALSSNDR_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testIsVowel_SmallD_ReturnsFalse_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertFalse(encoder.isVowel("d"))

    def testIsVowel_SmallD_ReturnsFalse_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testIsVowel_CapitalA_ReturnsTrue_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertTrue(encoder.isVowel("A"))

    def testIsVowel_CapitalA_ReturnsTrue_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("BEETLE", encoder.removeDoubleConsonants("BEETLE"))

    def testRemoveDoubleDoubleVowel_BEETLE_NotRemoved_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("MISISIPI", encoder.removeDoubleConsonants("MISSISSIPPI"))

    def testRemoveDoubleConsonants_MISSISSIPPI_RemovedSuccessfully_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("BUBLE", encoder.removeDoubleConsonants("BUBBLE"))

    def testRemoveSingleDoubleConsonants_BUBLE_RemovedSuccessfully_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testAccentRemoval_NullValue_ReturnNullSuccessfully_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertIsNone(encoder.removeAccents(None))

    def testAccentRemoval_NullValue_ReturnNullSuccessfully_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testAccentRemoval_NINO_NoChange_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("", encoder.removeAccents(""))

    def testAccentRemoval_NINO_NoChange_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testAccentRemovalNormalString_NoChange_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(
            "Colorless green ideas sleep furiously",
            encoder.removeAccents("Colorless green ideas sleep furiously"),
        )

    def testAccentRemovalNormalString_NoChange_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual(
            "E,E,E,E,U,U,I,I,A,A,O,e,e,e,e,u,u,i,i,a,a,o,c",
            encoder.removeAccents("È,É,Ê,Ë,Û,Ù,Ï,Î,À,Â,Ô,è,é,ê,ë,û,ù,ï,î,à,â,ô,ç"),
        )

    def testAccentRemoval_ComprehensiveAccentMix_AllSuccessfullyRemoved_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("aeoußAEOUnNa", encoder.removeAccents("äëöüßÄËÖÜñÑà"))

    def testAccentRemoval_GerSpanFrenMix_SuccessfullyRemoved_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("A-e'i.,o&u", encoder.removeAccents("Á-e'í.,ó&ú"))

    def testAccentRemoval_MixedWithUnusualChars_SuccessfullyRemovedAndUnusualcharactersInvariant_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("AeiOuu", encoder.removeAccents("ÁeíÓuu"))

    def testAccentRemoval_UpperandLower_SuccessfullyRemovedAndCaseInvariant_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant_test1_decomposed(
        self,
    ) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("ae io  u", encoder.removeAccents("áé íó  ú"))

    def testAccentRemoval_WithSpaces_SuccessfullyRemovedAndSpacesInvariant_test0_decomposed(
        self,
    ) -> None:
        self.getStringEncoder()

    def testAccentRemoval_AllLower_SuccessfullyRemoved_test1_decomposed(self) -> None:
        encoder = MatchRatingApproachEncoder()
        self.assertEqual("aeiou", encoder.removeAccents("áéíóú"))

    def testAccentRemoval_AllLower_SuccessfullyRemoved_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def _createStringEncoder(self) -> MatchRatingApproachEncoder:
        return MatchRatingApproachEncoder()
