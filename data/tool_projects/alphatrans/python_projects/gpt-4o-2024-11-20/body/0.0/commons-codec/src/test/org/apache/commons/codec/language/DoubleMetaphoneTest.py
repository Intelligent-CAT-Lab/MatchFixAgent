from __future__ import annotations
import time
import re
import enum
import numbers
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *


class DoubleMetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    __MATCHES: typing.List[typing.List[str]] = [
        ["Accosinly", "Occasionally"],
        ["Maddness", "Madness"],
        ["Occusionaly", "Occasionally"],
        ["Steffen", "Stephen"],
        ["Thw", "The"],
        ["Unformanlly", "Unfortunately"],
        ["Unfortally", "Unfortunately"],
        ["abilitey", "ability"],
        ["absorbtion", "absorption"],
        ["accidently", "accidentally"],
        ["accomodate", "accommodate"],
        ["acommadate", "accommodate"],
        ["acord", "accord"],
        ["adultry", "adultery"],
        ["aggresive", "aggressive"],
        ["alchohol", "alcohol"],
        ["alchoholic", "alcoholic"],
        ["allieve", "alive"],
        ["alot", "a lot"],
        ["alright", "all right"],
        ["amature", "amateur"],
        ["ambivilant", "ambivalent"],
        ["amourfous", "amorphous"],
        ["annoint", "anoint"],
        ["annonsment", "announcement"],
        ["annoyting", "anting"],
        ["annuncio", "announce"],
        ["anotomy", "anatomy"],
        ["antidesestablishmentarianism", "antidisestablishmentarianism"],
        ["antidisestablishmentarism", "antidisestablishmentarianism"],
        ["anynomous", "anonymous"],
        ["appelet", "applet"],
        ["appreceiated", "appreciated"],
        ["appresteate", "appreciate"],
        ["aquantance", "acquaintance"],
        ["aricticure", "architecture"],
        ["asterick", "asterisk"],
        ["asymetric", "asymmetric"],
        ["atentively", "attentively"],
        ["bankrot", "bankrupt"],
        ["basicly", "basically"],
        ["batallion", "battalion"],
        ["bbrose", "browse"],
        ["beauro", "bureau"],
        ["beaurocracy", "bureaucracy"],
        ["beggining", "beginning"],
        ["behaviour", "behavior"],
        ["beleive", "believe"],
        ["belive", "believe"],
        ["blait", "bleat"],
        ["bouyant", "buoyant"],
        ["boygot", "boycott"],
        ["brocolli", "broccoli"],
        ["buder", "butter"],
        ["budr", "butter"],
        ["budter", "butter"],
        ["buracracy", "bureaucracy"],
        ["burracracy", "bureaucracy"],
        ["buton", "button"],
        ["byby", "by by"],
        ["cauler", "caller"],
        ["ceasar", "caesar"],
        ["cemetary", "cemetery"],
        ["changeing", "changing"],
        ["cheet", "cheat"],
        ["cimplicity", "simplicity"],
        ["circumstaces", "circumstances"],
        ["clob", "club"],
        ["coaln", "colon"],
        ["colleaque", "colleague"],
        ["colloquilism", "colloquialism"],
        ["columne", "column"],
        ["comitmment", "commitment"],
        ["comitte", "committee"],
        ["comittmen", "commitment"],
        ["comittmend", "commitment"],
        ["commerciasl", "commercials"],
        ["commited", "committed"],
        ["commitee", "committee"],
        ["companys", "companies"],
        ["comupter", "computer"],
        ["concensus", "consensus"],
        ["confusionism", "confucianism"],
        ["congradulations", "congratulations"],
        ["contunie", "continue"],
        ["cooly", "coolly"],
        ["copping", "coping"],
        ["cosmoplyton", "cosmopolitan"],
        ["crasy", "crazy"],
        ["croke", "croak"],
        ["crucifiction", "crucifixion"],
        ["crusifed", "crucified"],
        ["cumba", "combo"],
        ["custamisation", "customization"],
        ["dag", "dog"],
        ["daly", "daily"],
        ["defence", "defense"],
        ["definate", "definite"],
        ["definately", "definitely"],
        ["dependeble", "dependable"],
        ["descrption", "description"],
        ["descrptn", "description"],
        ["desparate", "desperate"],
        ["dessicate", "desiccate"],
        ["destint", "distant"],
        ["develepment", "developments"],
        ["developement", "development"],
        ["develpond", "development"],
        ["devulge", "divulge"],
        ["dieties", "deities"],
        ["dinasaur", "dinosaur"],
        ["dinasour", "dinosaur"],
        ["discuess", "discuss"],
        ["disect", "dissect"],
        ["disippate", "dissipate"],
        ["disition", "decision"],
        ["dispair", "despair"],
        ["distarct", "distract"],
        ["distart", "distort"],
        ["distroy", "destroy"],
        ["doenload", "download"],
        ["dongle", "dangle"],
        ["doog", "dog"],
        ["dramaticly", "dramatically"],
        ["drunkeness", "drunkenness"],
        ["ductioneery", "dictionary"],
        ["ecstacy", "ecstasy"],
        ["egsistence", "existence"],
        ["eitiology", "etiology"],
        ["elagent", "elegant"],
        ["embarass", "embarrass"],
        ["embarassment", "embarrassment"],
        ["embaress", "embarrass"],
        ["encapsualtion", "encapsulation"],
        ["encyclapidia", "encyclopedia"],
        ["encyclopia", "encyclopedia"],
        ["engins", "engine"],
        ["enhence", "enhance"],
        ["ennuui", "ennui"],
        ["enventions", "inventions"],
        ["envireminakl", "environmental"],
        ["enviroment", "environment"],
        ["epitomy", "epitome"],
        ["equire", "acquire"],
        ["errara", "error"],
        ["evaualtion", "evaluation"],
        ["excede", "exceed"],
        ["excercise", "exercise"],
        ["excpt", "except"],
        ["exhileration", "exhilaration"],
        ["existance", "existence"],
        ["expleyly", "explicitly"],
        ["explity", "explicitly"],
        ["failer", "failure"],
        ["faver", "favor"],
        ["faxe", "fax"],
        ["firey", "fiery"],
        ["fistival", "festival"],
        ["flatterring", "flattering"],
        ["flukse", "flux"],
        ["fone", "phone"],
        ["forsee", "foresee"],
        ["frustartaion", "frustrating"],
        ["funetik", "phonetic"],
        ["gaurd", "guard"],
        ["generly", "generally"],
        ["ghandi", "gandhi"],
        ["gotton", "gotten"],
        ["gracefull", "graceful"],
        ["gradualy", "gradually"],
        ["grammer", "grammar"],
        ["hallo", "hello"],
        ["hapily", "happily"],
        ["harrass", "harass"],
        ["heellp", "help"],
        ["heighth", "height"],
        ["hellp", "help"],
        ["helo", "hello"],
        ["hifin", "hyphen"],
        ["hifine", "hyphen"],
        ["hiphine", "hyphen"],
        ["hippie", "hippy"],
        ["hippopotamous", "hippopotamus"],
        ["hourse", "horse"],
        ["houssing", "housing"],
        ["howaver", "however"],
        ["howver", "however"],
        ["humaniti", "humanity"],
        ["hyfin", "hyphen"],
        ["hystrical", "hysterical"],
        ["illegitament", "illegitimate"],
        ["imbed", "embed"],
        ["imediaetly", "immediately"],
        ["immenant", "immanent"],
        ["implemtes", "implements"],
        ["inadvertant", "inadvertent"],
        ["incase", "in case"],
        ["incedious", "insidious"],
        ["incompleet", "incomplete"],
        ["incomplot", "incomplete"],
        ["inconvenant", "inconvenient"],
        ["inconvience", "inconvenience"],
        ["independant", "independent"],
        ["independenent", "independent"],
        ["indepnends", "independent"],
        ["indepth", "in depth"],
        ["indispensible", "indispensable"],
        ["inefficite", "inefficient"],
        ["infact", "in fact"],
        ["influencial", "influential"],
        ["innoculate", "inoculate"],
        ["insistant", "insistent"],
        ["insistenet", "insistent"],
        ["instulation", "installation"],
        ["intealignt", "intelligent"],
        ["intelegent", "intelligent"],
        ["intelegnent", "intelligent"],
        ["intelejent", "intelligent"],
        ["inteligent", "intelligent"],
        ["intelignt", "intelligent"],
        ["intellagant", "intelligent"],
        ["intellegent", "intelligent"],
        ["intellegint", "intelligent"],
        ["intellgnt", "intelligent"],
        ["intensionality", "intensionally"],
        ["internation", "international"],
        ["interpretate", "interpret"],
        ["interpretter", "interpreter"],
        ["intertes", "interested"],
        ["intertesd", "interested"],
        ["invermeantial", "environmental"],
        ["irresistable", "irresistible"],
        ["irritible", "irritable"],
        ["isreal", "israel"],
        ["johhn", "john"],
        ["kippur", "kipper"],
        ["knawing", "knowing"],
        ["lesure", "leisure"],
        ["liasion", "lesion"],
        ["liason", "liaison"],
        ["likly", "likely"],
        ["liquify", "liquefy"],
        ["lloyer", "layer"],
        ["lossing", "losing"],
        ["luser", "laser"],
        ["maintanence", "maintenance"],
        ["mandelbrot", "Mandelbrot"],
        ["marshall", "marshal"],
        ["maxium", "maximum"],
        ["mic", "mike"],
        ["midia", "media"],
        ["millenium", "millennium"],
        ["miniscule", "minuscule"],
        ["minkay", "monkey"],
        ["mischievious", "mischievous"],
        ["momento", "memento"],
        ["monkay", "monkey"],
        ["mosaik", "mosaic"],
        ["mostlikely", "most likely"],
        ["mousr", "mouser"],
        ["mroe", "more"],
        ["necesary", "necessary"],
        ["necesser", "necessary"],
        ["neice", "niece"],
        ["neighbour", "neighbor"],
        ["nemonic", "pneumonic"],
        ["nevade", "Nevada"],
        ["nickleodeon", "nickelodeon"],
        ["nieve", "naive"],
        ["noone", "no one"],
        ["notin", "not in"],
        ["nozled", "nuzzled"],
        ["objectsion", "objects"],
        ["ocassion", "occasion"],
        ["occuppied", "occupied"],
        ["occurence", "occurrence"],
        ["octagenarian", "octogenarian"],
        ["opposim", "opossum"],
        ["organise", "organize"],
        ["organiz", "organize"],
        ["orientate", "orient"],
        ["oscilascope", "oscilloscope"],
        ["parametic", "parameter"],
        ["permissable", "permissible"],
        ["permmasivie", "permissive"],
        ["persue", "pursue"],
        ["phantasia", "fantasia"],
        ["phenominal", "phenomenal"],
        ["playwrite", "playwright"],
        ["poeses", "poesies"],
        ["poligamy", "polygamy"],
        ["politict", "politic"],
        ["pollice", "police"],
        ["polypropalene", "polypropylene"],
        ["possable", "possible"],
        ["practicle", "practical"],
        ["pragmaticism", "pragmatism"],
        ["preceeding", "preceding"],
        ["precios", "precision"],
        ["preemptory", "peremptory"],
        ["prefixt", "prefixed"],
        ["presbyterian", "Presbyterian"],
        ["presue", "pursue"],
        ["presued", "pursued"],
        ["privielage", "privilege"],
        ["priviledge", "privilege"],
        ["proceedures", "procedures"],
        ["pronensiation", "pronunciation"],
        ["pronounciation", "pronunciation"],
        ["properally", "properly"],
        ["proplematic", "problematic"],
        ["protray", "portray"],
        ["pscolgst", "psychologist"],
        ["psicolagest", "psychologist"],
        ["psycolagest", "psychologist"],
        ["quoz", "quiz"],
        ["radious", "radius"],
        ["reccomend", "recommend"],
        ["reccona", "raccoon"],
        ["recieve", "receive"],
        ["reconise", "recognize"],
        ["rectangeles", "rectangle"],
        ["reoccurring", "recurring"],
        ["repitition", "repetition"],
        ["replasments", "replacement"],
        ["respct", "respect"],
        ["respecally", "respectfully"],
        ["rsx", "RSX"],
        ["runnung", "running"],
        ["sacreligious", "sacrilegious"],
        ["salut", "salute"],
        ["searcheable", "searchable"],
        ["seferal", "several"],
        ["segements", "segments"],
        ["sence", "sense"],
        ["seperate", "separate"],
        ["sicolagest", "psychologist"],
        ["sieze", "seize"],
        ["simplye", "simply"],
        ["sitte", "site"],
        ["slyph", "sylph"],
        ["smil", "smile"],
        ["sometmes", "sometimes"],
        ["soonec", "sonic"],
        ["specificialy", "specifically"],
        ["spel", "spell"],
        ["spoak", "spoke"],
        ["sponsered", "sponsored"],
        ["stering", "steering"],
        ["straightjacket", "straitjacket"],
        ["stumach", "stomach"],
        ["stutent", "student"],
        ["styleguide", "style guide"],
        ["subpena", "subpoena"],
        ["substations", "substitutions"],
        ["supercede", "supersede"],
        ["superfulous", "superfluous"],
        ["susan", "Susan"],
        ["swimwear", "swim wear"],
        ["syncorization", "synchronization"],
        ["taff", "tough"],
        ["taht", "that"],
        ["tattos", "tattoos"],
        ["techniquely", "technically"],
        ["teh", "the"],
        ["tem", "team"],
        ["teo", "two"],
        ["teridical", "theoretical"],
        ["tesst", "test"],
        ["theridically", "theoretical"],
        ["thredically", "theoretically"],
        ["thruout", "throughout"],
        ["ths", "this"],
        ["titalate", "titillate"],
        ["tobagan", "tobaggon"],
        ["tommorrow", "tomorrow"],
        ["tomorow", "tomorrow"],
        ["trubbel", "trouble"],
        ["ttest", "test"],
        ["tyrrany", "tyranny"],
        ["unatourral", "unnatural"],
        ["unaturral", "unnatural"],
        ["unconisitional", "unconstitutional"],
        ["unconscience", "unconscious"],
        ["underladder", "under ladder"],
        ["unentelegible", "unintelligible"],
        ["unfortunently", "unfortunately"],
        ["unnaturral", "unnatural"],
        ["upcast", "up cast"],
        ["verison", "version"],
        ["vinagarette", "vinaigrette"],
        ["volunteerism", "voluntarism"],
        ["volye", "volley"],
        ["waite", "wait"],
        ["wan't", "won't"],
        ["warloord", "warlord"],
        ["whaaat", "what"],
        ["whard", "ward"],
        ["whimp", "wimp"],
        ["wicken", "weaken"],
        ["wierd", "weird"],
        ["wrank", "rank"],
        ["writeen", "righten"],
        ["writting", "writing"],
        ["wundeews", "windows"],
        ["yeild", "yield"],
    ]
    __FIXTURE: typing.List[typing.List[str]] = [
        ["Accosinly", "Occasionally"],
        ["Ciculer", "Circler"],
        ["Circue", "Circle"],
        ["Maddness", "Madness"],
        ["Occusionaly", "Occasionally"],
        ["Steffen", "Stephen"],
        ["Thw", "The"],
        ["Unformanlly", "Unfortunately"],
        ["Unfortally", "Unfortunately"],
        ["abilitey", "ability"],
        ["abouy", "about"],
        ["absorbtion", "absorption"],
        ["accidently", "accidentally"],
        ["accomodate", "accommodate"],
        ["acommadate", "accommodate"],
        ["acord", "accord"],
        ["adultry", "adultery"],
        ["aggresive", "aggressive"],
        ["alchohol", "alcohol"],
        ["alchoholic", "alcoholic"],
        ["allieve", "alive"],
        ["alot", "a lot"],
        ["alright", "all right"],
        ["amature", "amateur"],
        ["ambivilant", "ambivalent"],
        ["amification", "amplification"],
        ["amourfous", "amorphous"],
        ["annoint", "anoint"],
        ["annonsment", "announcement"],
        ["annoyting", "anting"],
        ["annuncio", "announce"],
        ["anonomy", "anatomy"],
        ["anotomy", "anatomy"],
        ["antidesestablishmentarianism", "antidisestablishmentarianism"],
        ["antidisestablishmentarism", "antidisestablishmentarianism"],
        ["anynomous", "anonymous"],
        ["appelet", "applet"],
        ["appreceiated", "appreciated"],
        ["appresteate", "appreciate"],
        ["aquantance", "acquaintance"],
        ["aratictature", "architecture"],
        ["archeype", "archetype"],
        ["aricticure", "architecture"],
        ["artic", "arctic"],
        ["asentote", "asymptote"],
        ["ast", "at"],
        ["asterick", "asterisk"],
        ["asymetric", "asymmetric"],
        ["atentively", "attentively"],
        ["autoamlly", "automatically"],
        ["bankrot", "bankrupt"],
        ["basicly", "basically"],
        ["batallion", "battalion"],
        ["bbrose", "browse"],
        ["beauro", "bureau"],
        ["beaurocracy", "bureaucracy"],
        ["beggining", "beginning"],
        ["beging", "beginning"],
        ["behaviour", "behavior"],
        ["beleive", "believe"],
        ["belive", "believe"],
        ["benidifs", "benefits"],
        ["bigginging", "beginning"],
        ["blait", "bleat"],
        ["bouyant", "buoyant"],
        ["boygot", "boycott"],
        ["brocolli", "broccoli"],
        ["buch", "bush"],
        ["buder", "butter"],
        ["budr", "butter"],
        ["budter", "butter"],
        ["buracracy", "bureaucracy"],
        ["burracracy", "bureaucracy"],
        ["buton", "button"],
        ["byby", "by by"],
        ["cauler", "caller"],
        ["ceasar", "caesar"],
        ["cemetary", "cemetery"],
        ["changeing", "changing"],
        ["cheet", "cheat"],
        ["cicle", "circle"],
        ["cimplicity", "simplicity"],
        ["circumstaces", "circumstances"],
        ["clob", "club"],
        ["coaln", "colon"],
        ["cocamena", "cockamamie"],
        ["colleaque", "colleague"],
        ["colloquilism", "colloquialism"],
        ["columne", "column"],
        ["comiler", "compiler"],
        ["comitmment", "commitment"],
        ["comitte", "committee"],
        ["comittmen", "commitment"],
        ["comittmend", "commitment"],
        ["commerciasl", "commercials"],
        ["commited", "committed"],
        ["commitee", "committee"],
        ["companys", "companies"],
        ["compicated", "complicated"],
        ["comupter", "computer"],
        ["concensus", "consensus"],
        ["confusionism", "confucianism"],
        ["congradulations", "congratulations"],
        ["conibation", "contribution"],
        ["consident", "consistent"],
        ["consident", "consonant"],
        ["contast", "constant"],
        ["contastant", "constant"],
        ["contunie", "continue"],
        ["cooly", "coolly"],
        ["copping", "coping"],
        ["cosmoplyton", "cosmopolitan"],
        ["courst", "court"],
        ["crasy", "crazy"],
        ["cravets", "caveats"],
        ["credetability", "credibility"],
        ["criqitue", "critique"],
        ["croke", "croak"],
        ["crucifiction", "crucifixion"],
        ["crusifed", "crucified"],
        ["ctitique", "critique"],
        ["cumba", "combo"],
        ["custamisation", "customization"],
        ["dag", "dog"],
        ["daly", "daily"],
        ["danguages", "dangerous"],
        ["deaft", "draft"],
        ["defence", "defense"],
        ["defenly", "defiantly"],
        ["definate", "definite"],
        ["definately", "definitely"],
        ["dependeble", "dependable"],
        ["descrption", "description"],
        ["descrptn", "description"],
        ["desparate", "desperate"],
        ["dessicate", "desiccate"],
        ["destint", "distant"],
        ["develepment", "developments"],
        ["developement", "development"],
        ["develpond", "development"],
        ["devulge", "divulge"],
        ["diagree", "disagree"],
        ["dieties", "deities"],
        ["dinasaur", "dinosaur"],
        ["dinasour", "dinosaur"],
        ["direcyly", "directly"],
        ["discuess", "discuss"],
        ["disect", "dissect"],
        ["disippate", "dissipate"],
        ["disition", "decision"],
        ["dispair", "despair"],
        ["disssicion", "discussion"],
        ["distarct", "distract"],
        ["distart", "distort"],
        ["distroy", "destroy"],
        ["documtations", "documentation"],
        ["doenload", "download"],
        ["dongle", "dangle"],
        ["doog", "dog"],
        ["dramaticly", "dramatically"],
        ["drunkeness", "drunkenness"],
        ["ductioneery", "dictionary"],
        ["dur", "due"],
        ["duren", "during"],
        ["dymatic", "dynamic"],
        ["dynaic", "dynamic"],
        ["ecstacy", "ecstasy"],
        ["efficat", "efficient"],
        ["efficity", "efficacy"],
        ["effots", "efforts"],
        ["egsistence", "existence"],
        ["eitiology", "etiology"],
        ["elagent", "elegant"],
        ["elligit", "elegant"],
        ["embarass", "embarrass"],
        ["embarassment", "embarrassment"],
        ["embaress", "embarrass"],
        ["encapsualtion", "encapsulation"],
        ["encyclapidia", "encyclopedia"],
        ["encyclopia", "encyclopedia"],
        ["engins", "engine"],
        ["enhence", "enhance"],
        ["enligtment", "Enlightenment"],
        ["ennuui", "ennui"],
        ["enought", "enough"],
        ["enventions", "inventions"],
        ["envireminakl", "environmental"],
        ["enviroment", "environment"],
        ["epitomy", "epitome"],
        ["equire", "acquire"],
        ["errara", "error"],
        ["erro", "error"],
        ["evaualtion", "evaluation"],
        ["evething", "everything"],
        ["evtually", "eventually"],
        ["excede", "exceed"],
        ["excercise", "exercise"],
        ["excpt", "except"],
        ["excution", "execution"],
        ["exhileration", "exhilaration"],
        ["existance", "existence"],
        ["expleyly", "explicitly"],
        ["explity", "explicitly"],
        ["expresso", "espresso"],
        ["exspidient", "expedient"],
        ["extions", "extensions"],
        ["factontion", "factorization"],
        ["failer", "failure"],
        ["famdasy", "fantasy"],
        ["faver", "favor"],
        ["faxe", "fax"],
        ["febuary", "february"],
        ["firey", "fiery"],
        ["fistival", "festival"],
        ["flatterring", "flattering"],
        ["fluk", "flux"],
        ["flukse", "flux"],
        ["fone", "phone"],
        ["forsee", "foresee"],
        ["frustartaion", "frustrating"],
        ["fuction", "function"],
        ["funetik", "phonetic"],
        ["futs", "guts"],
        ["gamne", "came"],
        ["gaurd", "guard"],
        ["generly", "generally"],
        ["ghandi", "gandhi"],
        ["goberment", "government"],
        ["gobernement", "government"],
        ["gobernment", "government"],
        ["gotton", "gotten"],
        ["gracefull", "graceful"],
        ["gradualy", "gradually"],
        ["grammer", "grammar"],
        ["hallo", "hello"],
        ["hapily", "happily"],
        ["harrass", "harass"],
        ["havne", "have"],
        ["heellp", "help"],
        ["heighth", "height"],
        ["hellp", "help"],
        ["helo", "hello"],
        ["herlo", "hello"],
        ["hifin", "hyphen"],
        ["hifine", "hyphen"],
        ["higer", "higher"],
        ["hiphine", "hyphen"],
        ["hippie", "hippy"],
        ["hippopotamous", "hippopotamus"],
        ["hlp", "help"],
        ["hourse", "horse"],
        ["houssing", "housing"],
        ["howaver", "however"],
        ["howver", "however"],
        ["humaniti", "humanity"],
        ["hyfin", "hyphen"],
        ["hypotathes", "hypothesis"],
        ["hypotathese", "hypothesis"],
        ["hystrical", "hysterical"],
        ["ident", "indent"],
        ["illegitament", "illegitimate"],
        ["imbed", "embed"],
        ["imediaetly", "immediately"],
        ["imfamy", "infamy"],
        ["immenant", "immanent"],
        ["implemtes", "implements"],
        ["inadvertant", "inadvertent"],
        ["incase", "in case"],
        ["incedious", "insidious"],
        ["incompleet", "incomplete"],
        ["incomplot", "incomplete"],
        ["inconvenant", "inconvenient"],
        ["inconvience", "inconvenience"],
        ["independant", "independent"],
        ["independenent", "independent"],
        ["indepnends", "independent"],
        ["indepth", "in depth"],
        ["indispensible", "indispensable"],
        ["inefficite", "inefficient"],
        ["inerface", "interface"],
        ["infact", "in fact"],
        ["influencial", "influential"],
        ["inital", "initial"],
        ["initinized", "initialized"],
        ["initized", "initialized"],
        ["innoculate", "inoculate"],
        ["insistant", "insistent"],
        ["insistenet", "insistent"],
        ["instulation", "installation"],
        ["intealignt", "intelligent"],
        ["intejilent", "intelligent"],
        ["intelegent", "intelligent"],
        ["intelegnent", "intelligent"],
        ["intelejent", "intelligent"],
        ["inteligent", "intelligent"],
        ["intelignt", "intelligent"],
        ["intellagant", "intelligent"],
        ["intellegent", "intelligent"],
        ["intellegint", "intelligent"],
        ["intellgnt", "intelligent"],
        ["intensionality", "intensionally"],
        ["interate", "iterate"],
        ["internation", "international"],
        ["interpretate", "interpret"],
        ["interpretter", "interpreter"],
        ["intertes", "interested"],
        ["intertesd", "interested"],
        ["invermeantial", "environmental"],
        ["irregardless", "regardless"],
        ["irresistable", "irresistible"],
        ["irritible", "irritable"],
        ["islams", "muslims"],
        ["isotrop", "isotope"],
        ["isreal", "israel"],
        ["johhn", "john"],
        ["judgement", "judgment"],
        ["kippur", "kipper"],
        ["knawing", "knowing"],
        ["latext", "latest"],
        ["leasve", "leave"],
        ["lesure", "leisure"],
        ["liasion", "lesion"],
        ["liason", "liaison"],
        ["libary", "library"],
        ["likly", "likely"],
        ["lilometer", "kilometer"],
        ["liquify", "liquefy"],
        ["lloyer", "layer"],
        ["lossing", "losing"],
        ["luser", "laser"],
        ["maintanence", "maintenance"],
        ["majaerly", "majority"],
        ["majoraly", "majority"],
        ["maks", "masks"],
        ["mandelbrot", "Mandelbrot"],
        ["mant", "want"],
        ["marshall", "marshal"],
        ["maxium", "maximum"],
        ["meory", "memory"],
        ["metter", "better"],
        ["mic", "mike"],
        ["midia", "media"],
        ["millenium", "millennium"],
        ["miniscule", "minuscule"],
        ["minkay", "monkey"],
        ["minum", "minimum"],
        ["mischievious", "mischievous"],
        ["misilous", "miscellaneous"],
        ["momento", "memento"],
        ["monkay", "monkey"],
        ["mosaik", "mosaic"],
        ["mostlikely", "most likely"],
        ["mousr", "mouser"],
        ["mroe", "more"],
        ["neccessary", "necessary"],
        ["necesary", "necessary"],
        ["necesser", "necessary"],
        ["neice", "niece"],
        ["neighbour", "neighbor"],
        ["nemonic", "pneumonic"],
        ["nevade", "Nevada"],
        ["nickleodeon", "nickelodeon"],
        ["nieve", "naive"],
        ["noone", "no one"],
        ["noticably", "noticeably"],
        ["notin", "not in"],
        ["nozled", "nuzzled"],
        ["objectsion", "objects"],
        ["obsfuscate", "obfuscate"],
        ["ocassion", "occasion"],
        ["occuppied", "occupied"],
        ["occurence", "occurrence"],
        ["octagenarian", "octogenarian"],
        ["olf", "old"],
        ["opposim", "opossum"],
        ["organise", "organize"],
        ["organiz", "organize"],
        ["orientate", "orient"],
        ["oscilascope", "oscilloscope"],
        ["oving", "moving"],
        ["paramers", "parameters"],
        ["parametic", "parameter"],
        ["paranets", "parameters"],
        ["partrucal", "particular"],
        ["pataphysical", "metaphysical"],
        ["patten", "pattern"],
        ["permissable", "permissible"],
        ["permition", "permission"],
        ["permmasivie", "permissive"],
        ["perogative", "prerogative"],
        ["persue", "pursue"],
        ["phantasia", "fantasia"],
        ["phenominal", "phenomenal"],
        ["picaresque", "picturesque"],
        ["playwrite", "playwright"],
        ["poeses", "poesies"],
        ["polation", "politician"],
        ["poligamy", "polygamy"],
        ["politict", "politic"],
        ["pollice", "police"],
        ["polypropalene", "polypropylene"],
        ["pompom", "pompon"],
        ["possable", "possible"],
        ["practicle", "practical"],
        ["pragmaticism", "pragmatism"],
        ["preceeding", "preceding"],
        ["precion", "precision"],
        ["precios", "precision"],
        ["preemptory", "peremptory"],
        ["prefices", "prefixes"],
        ["prefixt", "prefixed"],
        ["presbyterian", "Presbyterian"],
        ["presue", "pursue"],
        ["presued", "pursued"],
        ["privielage", "privilege"],
        ["priviledge", "privilege"],
        ["proceedures", "procedures"],
        ["pronensiation", "pronunciation"],
        ["pronisation", "pronunciation"],
        ["pronounciation", "pronunciation"],
        ["properally", "properly"],
        ["proplematic", "problematic"],
        ["protray", "portray"],
        ["pscolgst", "psychologist"],
        ["psicolagest", "psychologist"],
        ["psycolagest", "psychologist"],
        ["quoz", "quiz"],
        ["radious", "radius"],
        ["ramplily", "rampantly"],
        ["reccomend", "recommend"],
        ["reccona", "raccoon"],
        ["recieve", "receive"],
        ["reconise", "recognize"],
        ["rectangeles", "rectangle"],
        ["redign", "redesign"],
        ["reoccurring", "recurring"],
        ["repitition", "repetition"],
        ["replasments", "replacement"],
        ["reposable", "responsible"],
        ["reseblence", "resemblance"],
        ["respct", "respect"],
        ["respecally", "respectfully"],
        ["roon", "room"],
        ["rought", "roughly"],
        ["rsx", "RSX"],
        ["rudemtry", "rudimentary"],
        ["runnung", "running"],
        ["sacreligious", "sacrilegious"],
        ["saftly", "safely"],
        ["salut", "salute"],
        ["satifly", "satisfy"],
        ["scrabdle", "scrabble"],
        ["searcheable", "searchable"],
        ["secion", "section"],
        ["seferal", "several"],
        ["segements", "segments"],
        ["sence", "sense"],
        ["seperate", "separate"],
        ["sherbert", "sherbet"],
        ["sicolagest", "psychologist"],
        ["sieze", "seize"],
        ["simpfilty", "simplicity"],
        ["simplye", "simply"],
        ["singal", "signal"],
        ["sitte", "site"],
        ["situration", "situation"],
        ["slyph", "sylph"],
        ["smil", "smile"],
        ["snuck", "sneaked"],
        ["sometmes", "sometimes"],
        ["soonec", "sonic"],
        ["specificialy", "specifically"],
        ["spel", "spell"],
        ["spoak", "spoke"],
        ["sponsered", "sponsored"],
        ["stering", "steering"],
        ["straightjacket", "straitjacket"],
        ["stumach", "stomach"],
        ["stutent", "student"],
        ["styleguide", "style guide"],
        ["subisitions", "substitutions"],
        ["subjecribed", "subscribed"],
        ["subpena", "subpoena"],
        ["substations", "substitutions"],
        ["suger", "sugar"],
        ["supercede", "supersede"],
        ["superfulous", "superfluous"],
        ["susan", "Susan"],
        ["swimwear", "swim wear"],
        ["syncorization", "synchronization"],
        ["taff", "tough"],
        ["taht", "that"],
        ["tattos", "tattoos"],
        ["techniquely", "technically"],
        ["teh", "the"],
        ["tem", "team"],
        ["teo", "two"],
        ["teridical", "theoretical"],
        ["tesst", "test"],
        ["tets", "tests"],
        ["thanot", "than or"],
        ["theirselves", "themselves"],
        ["theridically", "theoretical"],
        ["thredically", "theoretically"],
        ["thruout", "throughout"],
        ["ths", "this"],
        ["titalate", "titillate"],
        ["tobagan", "tobaggon"],
        ["tommorrow", "tomorrow"],
        ["tomorow", "tomorrow"],
        ["tradegy", "tragedy"],
        ["trubbel", "trouble"],
        ["ttest", "test"],
        ["tunnellike", "tunnel like"],
        ["tured", "turned"],
        ["tyrrany", "tyranny"],
        ["unatourral", "unnatural"],
        ["unaturral", "unnatural"],
        ["unconisitional", "unconstitutional"],
        ["unconscience", "unconscious"],
        ["underladder", "under ladder"],
        ["unentelegible", "unintelligible"],
        ["unfortunently", "unfortunately"],
        ["unnaturral", "unnatural"],
        ["upcast", "up cast"],
        ["upmost", "utmost"],
        ["uranisium", "uranium"],
        ["verison", "version"],
        ["vinagarette", "vinaigrette"],
        ["volumptuous", "voluptuous"],
        ["volunteerism", "voluntarism"],
        ["volye", "volley"],
        ["wadting", "wasting"],
        ["waite", "wait"],
        ["wan't", "won't"],
        ["warloord", "warlord"],
        ["whaaat", "what"],
        ["whard", "ward"],
        ["whimp", "wimp"],
        ["wicken", "weaken"],
        ["wierd", "weird"],
        ["wrank", "rank"],
        ["writeen", "righten"],
        ["writting", "writing"],
        ["wundeews", "windows"],
        ["yeild", "yield"],
        ["youe", "your"],
    ]

    def testSetMaxCodeLength_test5_decomposed(self) -> None:
        value = "jumped"
        doubleMetaphone = DoubleMetaphone()

        self.assertEqual(4, doubleMetaphone.getMaxCodeLen(), "Default Max Code Length")
        self.assertEqual(
            "JMPT", doubleMetaphone.doubleMetaphone1(value, False), "Default Primary"
        )
        self.assertEqual(
            "AMPT", doubleMetaphone.doubleMetaphone1(value, True), "Default Alternate"
        )

        doubleMetaphone.setMaxCodeLen(3)

        self.assertEqual(3, doubleMetaphone.getMaxCodeLen(), "Set Max Code Length")
        self.assertEqual(
            "JMP", doubleMetaphone.doubleMetaphone1(value, False), "Max=3 Primary"
        )
        self.assertEqual(
            "AMP", doubleMetaphone.doubleMetaphone1(value, True), "Max=3 Alternate"
        )

    def testSetMaxCodeLength_test4_decomposed(self) -> None:
        value = "jumped"
        doubleMetaphone = DoubleMetaphone()

        self.assertEqual(4, doubleMetaphone.getMaxCodeLen(), "Default Max Code Length")
        self.assertEqual(
            "JMPT", doubleMetaphone.doubleMetaphone1(value, False), "Default Primary"
        )
        self.assertEqual(
            "AMPT", doubleMetaphone.doubleMetaphone1(value, True), "Default Alternate"
        )

        doubleMetaphone.setMaxCodeLen(3)
        self.assertEqual(3, doubleMetaphone.getMaxCodeLen(), "Set Max Code Length")

    def testSetMaxCodeLength_test3_decomposed(self) -> None:
        value = "jumped"
        doubleMetaphone = DoubleMetaphone()
        self.assertEqual(4, doubleMetaphone.getMaxCodeLen(), "Default Max Code Length")
        self.assertEqual(
            "JMPT", doubleMetaphone.doubleMetaphone1(value, False), "Default Primary"
        )
        self.assertEqual(
            "AMPT", doubleMetaphone.doubleMetaphone1(value, True), "Default Alternate"
        )
        doubleMetaphone.setMaxCodeLen(3)

    def testSetMaxCodeLength_test2_decomposed(self) -> None:
        value = "jumped"
        double_metaphone = DoubleMetaphone()
        self.assertEqual(4, double_metaphone.getMaxCodeLen(), "Default Max Code Length")
        self.assertEqual(
            "JMPT", double_metaphone.doubleMetaphone1(value, False), "Default Primary"
        )
        self.assertEqual(
            "AMPT", double_metaphone.doubleMetaphone1(value, True), "Default Alternate"
        )

    def testSetMaxCodeLength_test1_decomposed(self) -> None:
        value = "jumped"
        doubleMetaphone = DoubleMetaphone()
        self.assertEqual(4, doubleMetaphone.getMaxCodeLen(), "Default Max Code Length")

    def testSetMaxCodeLength_test0_decomposed(self) -> None:
        value: str = "jumped"
        doubleMetaphone = DoubleMetaphone()

    def testNTilde_test1_decomposed(self) -> None:
        encoder = DoubleMetaphone()
        self.assertTrue(
            encoder.isDoubleMetaphoneEqual0("\u00f1", "N"),
            "Expected '\u00f1' to be considered equal to 'N'",
        )

    def testNTilde_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testIsDoubleMetaphoneNotEqual_test0_decomposed(self) -> None:
        self.doubleMetaphoneNotEqualTest(False)
        self.doubleMetaphoneNotEqualTest(True)

    def testIsDoubleMetaphoneEqualWithMATCHES_test1_decomposed(self) -> None:
        self.validateFixture(self.__MATCHES)
        for i, pair in enumerate(self.__MATCHES):
            name0, name1 = pair
            match1 = self.getStringEncoder().isDoubleMetaphoneEqual1(
                name0, name1, False
            )
            match2 = self.getStringEncoder().isDoubleMetaphoneEqual1(name0, name1, True)
            if not match1 and not match2:
                pytest.fail(f"Expected match [{i}] {name0} and {name1}")

    def testIsDoubleMetaphoneEqualWithMATCHES_test0_decomposed(self) -> None:
        self.validateFixture(self.__MATCHES)

    def testIsDoubleMetaphoneEqualExtended3_test4_decomposed(self) -> None:
        self.validateFixture(self.__FIXTURE)
        failures = io.StringIO()
        matches = io.StringIO()
        cr = os.linesep
        matches.write(f"private static final String[][] MATCHES = {{{cr}")
        fail_count = 0

        for i, pair in enumerate(self.__FIXTURE):
            name0, name1 = pair
            match1 = self.getStringEncoder().isDoubleMetaphoneEqual1(
                name0, name1, False
            )
            match2 = self.getStringEncoder().isDoubleMetaphoneEqual1(name0, name1, True)

            if not match1 and not match2:
                fail_msg = f"[{i}] {name0} and {name1}{cr}"
                failures.write(fail_msg)
                fail_count += 1
            else:
                matches.write(f'{{"{name0}", "{name1}"}},{cr}')

        matches.write("};")
        if fail_count > 0:
            pytest.fail(f"Failures encountered: {fail_count}{cr}{failures.getvalue()}")

    def testIsDoubleMetaphoneEqualExtended3_test3_decomposed(self) -> None:
        self.validateFixture(self.__FIXTURE)
        failures = io.StringIO()
        matches = io.StringIO()
        cr = os.linesep
        matches.write(f"private static final String[][] MATCHES = {{{cr}")
        fail_count = 0

        for i, pair in enumerate(self.__FIXTURE):
            name0, name1 = pair
            match1 = self.getStringEncoder().isDoubleMetaphoneEqual1(
                name0, name1, False
            )
            match2 = self.getStringEncoder().isDoubleMetaphoneEqual1(name0, name1, True)

            if not match1 and not match2:
                fail_msg = f"[{i}] {name0} and {name1}{cr}"
                failures.write(fail_msg)
                fail_count += 1
            else:
                matches.write(f'{{"{name0}", "{name1}"}},{cr}')

        matches.write("};")

    def testIsDoubleMetaphoneEqualExtended3_test2_decomposed(self) -> None:
        self.validateFixture(self.__FIXTURE)
        failures = io.StringIO()
        matches = io.StringIO()
        cr = os.linesep
        matches.write(f"private static final String[][] MATCHES = {{{cr}")
        fail_count = 0

        for i, pair in enumerate(self.__FIXTURE):
            name0, name1 = pair
            match1 = self.getStringEncoder().isDoubleMetaphoneEqual1(
                name0, name1, False
            )
            match2 = self.getStringEncoder().isDoubleMetaphoneEqual1(name0, name1, True)

            if not match1 and not match2:
                fail_msg = f"[{i}] {name0} and {name1}{cr}"
                failures.write(fail_msg)
                fail_count += 1
            else:
                matches.write(f'{{"{name0}", "{name1}"}},{cr}')

        # Optionally, you can handle the output of failures and matches here
        # For example, you could print them or write them to a file
        if fail_count > 0:
            pytest.fail(f"Number of failures: {fail_count}{cr}{failures.getvalue()}")

    def testIsDoubleMetaphoneEqualExtended3_test1_decomposed(self) -> None:
        self.validateFixture(self.__FIXTURE)
        failures = io.StringIO()
        matches = io.StringIO()
        cr = os.linesep
        matches.write(f"private static final String[][] MATCHES = {{{cr}")

    def testIsDoubleMetaphoneEqualExtended3_test0_decomposed(self) -> None:
        self.validateFixture(self.__FIXTURE)

    def testIsDoubleMetaphoneEqualExtended2_test0_decomposed(self) -> None:
        test_fixture = [["Jablonski", "Yablonsky"]]
        self.doubleMetaphoneEqualTest(test_fixture, True)

    def testIsDoubleMetaphoneEqualBasic_test1_decomposed(self) -> None:
        test_fixture = [
            ["", ""],
            ["Case", "case"],
            ["CASE", "Case"],
            ["caSe", "cAsE"],
            ["cookie", "quick"],
            ["quick", "cookie"],
            ["Brian", "Bryan"],
            ["Auto", "Otto"],
            ["Steven", "Stefan"],
            ["Philipowitz", "Filipowicz"],
        ]
        self.doubleMetaphoneEqualTest(test_fixture, False)
        self.doubleMetaphoneEqualTest(test_fixture, True)

    def testIsDoubleMetaphoneEqualBasic_test0_decomposed(self) -> None:
        test_fixture = [
            ["", ""],
            ["Case", "case"],
            ["CASE", "Case"],
            ["caSe", "cAsE"],
            ["cookie", "quick"],
            ["quick", "cookie"],
            ["Brian", "Bryan"],
            ["Auto", "Otto"],
            ["Steven", "Stefan"],
            ["Philipowitz", "Filipowicz"],
        ]
        self.doubleMetaphoneEqualTest(test_fixture, False)

    def testEmpty_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(None))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(""))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(" "))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0("\t\n\r "))

    def testEmpty_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(None))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(""))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(" "))
        self.getStringEncoder()

    def testEmpty_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(None))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(""))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(" "))

    def testEmpty_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(None))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(""))
        self.getStringEncoder()

    def testEmpty_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(None))
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(""))

    def testEmpty_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertIsNone(self.getStringEncoder().doubleMetaphone0(None))
        self.getStringEncoder()

    def testEmpty_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertIsNotNone(encoder, "getStringEncoder() returned None")
        self.assertIsNone(
            encoder.doubleMetaphone0(None), "doubleMetaphone0(None) did not return None"
        )

    def testEmpty_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testDoubleMetaphone_test1_decomposed(self) -> None:
        self.__assertDoubleMetaphone("TSTN", "testing")
        self.__assertDoubleMetaphone("0", "The")
        self.__assertDoubleMetaphone("KK", "quick")
        self.__assertDoubleMetaphone("PRN", "brown")
        self.__assertDoubleMetaphone("FKS", "fox")
        self.__assertDoubleMetaphone("JMPT", "jumped")
        self.__assertDoubleMetaphone("AFR", "over")
        self.__assertDoubleMetaphone("0", "the")
        self.__assertDoubleMetaphone("LS", "lazy")
        self.__assertDoubleMetaphone("TKS", "dogs")
        self.__assertDoubleMetaphone("MKFR", "MacCafferey")
        self.__assertDoubleMetaphone("STFN", "Stephan")
        self.__assertDoubleMetaphone("KSSK", "Kuczewski")
        self.__assertDoubleMetaphone("MKLL", "McClelland")
        self.__assertDoubleMetaphone("SNHS", "san jose")
        self.__assertDoubleMetaphone("SNFP", "xenophobia")
        self.assertDoubleMetaphoneAlt("TSTN", "testing")
        self.assertDoubleMetaphoneAlt("T", "The")
        self.assertDoubleMetaphoneAlt("KK", "quick")
        self.assertDoubleMetaphoneAlt("PRN", "brown")
        self.assertDoubleMetaphoneAlt("FKS", "fox")
        self.assertDoubleMetaphoneAlt("AMPT", "jumped")
        self.assertDoubleMetaphoneAlt("AFR", "over")
        self.assertDoubleMetaphoneAlt("T", "the")
        self.assertDoubleMetaphoneAlt("LS", "lazy")
        self.assertDoubleMetaphoneAlt("TKS", "dogs")
        self.assertDoubleMetaphoneAlt("MKFR", "MacCafferey")
        self.assertDoubleMetaphoneAlt("STFN", "Stephan")
        self.assertDoubleMetaphoneAlt("KXFS", "Kutchefski")
        self.assertDoubleMetaphoneAlt("MKLL", "McClelland")
        self.assertDoubleMetaphoneAlt("SNHS", "san jose")
        self.assertDoubleMetaphoneAlt("SNFP", "xenophobia")
        self.assertDoubleMetaphoneAlt("FKR", "Fokker")
        self.assertDoubleMetaphoneAlt("AK", "Joqqi")
        self.assertDoubleMetaphoneAlt("HF", "Hovvi")
        self.assertDoubleMetaphoneAlt("XRN", "Czerny")

    def testDoubleMetaphone_test0_decomposed(self) -> None:
        self.__assertDoubleMetaphone("TSTN", "testing")
        self.__assertDoubleMetaphone("0", "The")
        self.__assertDoubleMetaphone("KK", "quick")
        self.__assertDoubleMetaphone("PRN", "brown")
        self.__assertDoubleMetaphone("FKS", "fox")
        self.__assertDoubleMetaphone("JMPT", "jumped")
        self.__assertDoubleMetaphone("AFR", "over")
        self.__assertDoubleMetaphone("0", "the")
        self.__assertDoubleMetaphone("LS", "lazy")
        self.__assertDoubleMetaphone("TKS", "dogs")
        self.__assertDoubleMetaphone("MKFR", "MacCafferey")
        self.__assertDoubleMetaphone("STFN", "Stephan")
        self.__assertDoubleMetaphone("KSSK", "Kuczewski")
        self.__assertDoubleMetaphone("MKLL", "McClelland")
        self.__assertDoubleMetaphone("SNHS", "san jose")
        self.__assertDoubleMetaphone("SNFP", "xenophobia")

    def testCodec184_test5_decomposed(self) -> None:
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", False))
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", True))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", False))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", True))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("", "aa", False))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("", "aa", True))

    def testCodec184_test4_decomposed(self) -> None:
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", False))
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", True))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", False))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", True))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("", "aa", False))

    def testCodec184_test3_decomposed(self) -> None:
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", False))
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", True))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", False))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", True))

    def testCodec184_test2_decomposed(self) -> None:
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", False))
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", True))
        self.assertFalse(DoubleMetaphone().isDoubleMetaphoneEqual1("aa", "", False))

    def testCodec184_test1_decomposed(self) -> None:
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", False))
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", True))

    def testCodec184_test0_decomposed(self) -> None:
        self.assertTrue(DoubleMetaphone().isDoubleMetaphoneEqual1("", "", False))

    def testCCedilla_test1_decomposed(self) -> None:
        encoder = DoubleMetaphone()
        self.assertTrue(encoder.isDoubleMetaphoneEqual0("\u00e7", "S"))

    def testCCedilla_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def _createStringEncoder(self) -> DoubleMetaphone:
        return DoubleMetaphone()

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        if len(pairs) == 0:
            self.fail("Test fixture is empty")
        for i, pair in enumerate(pairs):
            if len(pair) != 2:
                self.fail(f"Error in test fixture in the data array at index {i}")

    def doubleMetaphoneNotEqualTest(self, alternate: bool) -> None:
        encoder = self.getStringEncoder()
        self.assertFalse(encoder.isDoubleMetaphoneEqual1("Brain", "Band", alternate))
        self.assertFalse(encoder.isDoubleMetaphoneEqual1("Band", "Brain", alternate))

        if not alternate:
            self.assertFalse(encoder.isDoubleMetaphoneEqual0("Brain", "Band"))
            self.assertFalse(encoder.isDoubleMetaphoneEqual0("Band", "Brain"))

    def doubleMetaphoneEqualTest(
        self, pairs: typing.List[typing.List[str]], useAlternate: bool
    ) -> None:
        self.validateFixture(pairs)
        for pair in pairs:
            name0 = pair[0]
            name1 = pair[1]
            fail_msg = f"Expected match between {name0} and {name1} (use alternate: {useAlternate})"
            self.assertTrue(
                self.getStringEncoder().isDoubleMetaphoneEqual1(
                    name0, name1, useAlternate
                ),
                fail_msg,
            )
            self.assertTrue(
                self.getStringEncoder().isDoubleMetaphoneEqual1(
                    name1, name0, useAlternate
                ),
                fail_msg,
            )
            if not useAlternate:
                self.assertTrue(
                    self.getStringEncoder().isDoubleMetaphoneEqual0(name0, name1),
                    fail_msg,
                )
                self.assertTrue(
                    self.getStringEncoder().isDoubleMetaphoneEqual0(name1, name0),
                    fail_msg,
                )

    def assertDoubleMetaphoneAlt(self, expected: str, source: str) -> None:
        self.assertEqual(
            expected, self.getStringEncoder().doubleMetaphone1(source, True)
        )

    def __assertDoubleMetaphone(self, expected: str, source: str) -> None:
        self.assertEqual(expected, self.getStringEncoder().encode1(source))
        try:
            self.assertEqual(expected, self.getStringEncoder().encode0(source))
        except EncoderException as e:
            self.fail(f"Unexpected exception: {e}")
        self.assertEqual(expected, self.getStringEncoder().doubleMetaphone0(source))
        self.assertEqual(
            expected, self.getStringEncoder().doubleMetaphone1(source, False)
        )
