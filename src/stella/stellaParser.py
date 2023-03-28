# Generated from stella/stellaParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,68,522,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,
        2,1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,3,5,3,52,8,3,10,3,12,3,55,
        9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,66,8,5,10,5,12,5,69,
        9,5,1,5,1,5,1,6,5,6,74,8,6,10,6,12,6,77,9,6,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,85,8,6,10,6,12,6,88,9,6,3,6,90,8,6,1,6,1,6,1,6,3,6,95,8,
        6,1,6,1,6,3,6,99,8,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,119,8,6,1,7,1,7,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,5,9,205,8,9,10,9,12,9,208,9,9,3,9,210,8,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,5,9,223,8,9,10,9,12,9,226,9,9,3,9,228,8,
        9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,236,8,9,10,9,12,9,239,9,9,3,9,241,
        8,9,1,9,1,9,1,9,1,9,1,9,3,9,248,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        5,9,257,8,9,10,9,12,9,260,9,9,3,9,262,8,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,271,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,292,8,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,5,9,335,8,9,10,9,12,9,338,9,9,3,9,340,8,9,1,9,1,9,
        1,9,1,9,5,9,346,8,9,10,9,12,9,349,9,9,1,10,1,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,363,8,12,1,12,1,12,1,12,1,
        12,1,12,5,12,370,8,12,10,12,12,12,373,9,12,3,12,375,8,12,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,383,8,12,10,12,12,12,386,9,12,3,12,388,
        8,12,1,12,1,12,1,12,1,12,1,12,5,12,395,8,12,10,12,12,12,398,9,12,
        3,12,400,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,423,
        8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        5,14,437,8,14,10,14,12,14,440,9,14,3,14,442,8,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,456,8,14,1,14,
        1,14,1,14,1,14,1,14,1,14,5,14,464,8,14,10,14,12,14,467,9,14,3,14,
        469,8,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,477,8,14,10,14,12,14,
        480,9,14,3,14,482,8,14,1,14,1,14,1,14,1,14,1,14,5,14,489,8,14,10,
        14,12,14,492,9,14,3,14,494,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,3,14,503,8,14,1,14,1,14,1,14,5,14,508,8,14,10,14,12,14,511,9,
        14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,3,16,520,8,16,1,16,0,2,18,
        28,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,0,602,0,34,
        1,0,0,0,2,37,1,0,0,0,4,40,1,0,0,0,6,43,1,0,0,0,8,56,1,0,0,0,10,60,
        1,0,0,0,12,118,1,0,0,0,14,120,1,0,0,0,16,122,1,0,0,0,18,291,1,0,
        0,0,20,350,1,0,0,0,22,354,1,0,0,0,24,422,1,0,0,0,26,424,1,0,0,0,
        28,502,1,0,0,0,30,512,1,0,0,0,32,516,1,0,0,0,34,35,3,6,3,0,35,36,
        5,0,0,1,36,1,1,0,0,0,37,38,3,18,9,0,38,39,5,0,0,1,39,3,1,0,0,0,40,
        41,3,28,14,0,41,42,5,0,0,1,42,5,1,0,0,0,43,47,3,8,4,0,44,46,3,10,
        5,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,53,
        1,0,0,0,49,47,1,0,0,0,50,52,3,12,6,0,51,50,1,0,0,0,52,55,1,0,0,0,
        53,51,1,0,0,0,53,54,1,0,0,0,54,7,1,0,0,0,55,53,1,0,0,0,56,57,5,46,
        0,0,57,58,5,36,0,0,58,59,5,2,0,0,59,9,1,0,0,0,60,61,5,38,0,0,61,
        62,5,60,0,0,62,67,5,65,0,0,63,64,5,1,0,0,64,66,5,65,0,0,65,63,1,
        0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,
        67,1,0,0,0,70,71,5,2,0,0,71,11,1,0,0,0,72,74,3,14,7,0,73,72,1,0,
        0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,
        1,0,0,0,78,79,5,41,0,0,79,80,5,64,0,0,80,89,5,3,0,0,81,86,3,16,8,
        0,82,83,5,1,0,0,83,85,3,16,8,0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,
        1,0,0,0,86,87,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,89,81,1,0,0,0,
        89,90,1,0,0,0,90,91,1,0,0,0,91,94,5,4,0,0,92,93,5,9,0,0,93,95,3,
        28,14,0,94,92,1,0,0,0,94,95,1,0,0,0,95,98,1,0,0,0,96,97,5,55,0,0,
        97,99,3,28,14,0,98,96,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,104,
        5,5,0,0,101,103,3,12,6,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,
        1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,108,
        5,52,0,0,108,109,3,18,9,0,109,110,5,2,0,0,110,111,5,6,0,0,111,119,
        1,0,0,0,112,113,5,57,0,0,113,114,5,64,0,0,114,115,5,7,0,0,115,116,
        3,28,14,0,116,117,5,2,0,0,117,119,1,0,0,0,118,75,1,0,0,0,118,112,
        1,0,0,0,119,13,1,0,0,0,120,121,5,45,0,0,121,15,1,0,0,0,122,123,5,
        64,0,0,123,124,5,8,0,0,124,125,3,28,14,0,125,17,1,0,0,0,126,127,
        6,9,-1,0,127,292,5,56,0,0,128,292,5,39,0,0,129,292,5,66,0,0,130,
        292,5,64,0,0,131,132,5,35,0,0,132,133,5,3,0,0,133,134,3,18,9,0,134,
        135,5,1,0,0,135,136,3,18,9,0,136,137,5,4,0,0,137,292,1,0,0,0,138,
        139,5,23,0,0,139,140,5,3,0,0,140,141,3,18,9,0,141,142,5,4,0,0,142,
        292,1,0,0,0,143,144,5,24,0,0,144,145,5,3,0,0,145,146,3,18,9,0,146,
        147,5,4,0,0,147,292,1,0,0,0,148,149,5,25,0,0,149,150,5,3,0,0,150,
        151,3,18,9,0,151,152,5,4,0,0,152,292,1,0,0,0,153,154,5,53,0,0,154,
        155,5,3,0,0,155,156,3,18,9,0,156,157,5,4,0,0,157,292,1,0,0,0,158,
        159,5,49,0,0,159,160,5,3,0,0,160,161,3,18,9,0,161,162,5,4,0,0,162,
        292,1,0,0,0,163,164,5,26,0,0,164,165,5,3,0,0,165,166,3,18,9,0,166,
        167,5,4,0,0,167,292,1,0,0,0,168,169,5,27,0,0,169,170,5,3,0,0,170,
        171,3,18,9,0,171,172,5,4,0,0,172,292,1,0,0,0,173,174,5,40,0,0,174,
        175,5,3,0,0,175,176,3,18,9,0,176,177,5,4,0,0,177,292,1,0,0,0,178,
        179,5,28,0,0,179,180,5,3,0,0,180,181,3,18,9,0,181,182,5,1,0,0,182,
        183,3,18,9,0,183,184,5,1,0,0,184,185,3,18,9,0,185,186,5,4,0,0,186,
        292,1,0,0,0,187,188,5,42,0,0,188,189,5,13,0,0,189,190,3,28,14,0,
        190,191,5,14,0,0,191,192,3,18,9,23,192,292,1,0,0,0,193,194,5,58,
        0,0,194,195,5,13,0,0,195,196,3,28,14,0,196,197,5,14,0,0,197,198,
        3,18,9,22,198,292,1,0,0,0,199,200,5,41,0,0,200,209,5,3,0,0,201,206,
        3,16,8,0,202,203,5,1,0,0,203,205,3,16,8,0,204,202,1,0,0,0,205,208,
        1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,210,1,0,0,0,208,206,
        1,0,0,0,209,201,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,
        5,4,0,0,212,213,5,5,0,0,213,214,5,52,0,0,214,215,3,18,9,0,215,216,
        5,2,0,0,216,217,5,6,0,0,217,292,1,0,0,0,218,227,5,5,0,0,219,224,
        3,18,9,0,220,221,5,1,0,0,221,223,3,18,9,0,222,220,1,0,0,0,223,226,
        1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,228,1,0,0,0,226,224,
        1,0,0,0,227,219,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,292,
        5,6,0,0,230,231,5,51,0,0,231,240,5,5,0,0,232,237,3,20,10,0,233,234,
        5,1,0,0,234,236,3,20,10,0,235,233,1,0,0,0,236,239,1,0,0,0,237,235,
        1,0,0,0,237,238,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,240,232,
        1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,292,5,6,0,0,243,244,
        5,11,0,0,244,247,5,64,0,0,245,246,5,7,0,0,246,248,3,18,9,0,247,245,
        1,0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,292,5,12,0,0,250,251,
        5,48,0,0,251,252,3,18,9,0,252,261,5,5,0,0,253,258,3,22,11,0,254,
        255,5,2,0,0,255,257,3,22,11,0,256,254,1,0,0,0,257,260,1,0,0,0,258,
        256,1,0,0,0,258,259,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,261,
        253,1,0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,263,264,5,6,0,0,264,
        292,1,0,0,0,265,270,5,13,0,0,266,267,3,18,9,0,267,268,5,1,0,0,268,
        269,3,18,9,0,269,271,1,0,0,0,270,266,1,0,0,0,270,271,1,0,0,0,271,
        272,1,0,0,0,272,292,5,14,0,0,273,274,5,43,0,0,274,275,3,18,9,0,275,
        276,5,54,0,0,276,277,3,18,9,0,277,278,5,37,0,0,278,279,3,18,9,3,
        279,292,1,0,0,0,280,281,5,47,0,0,281,282,5,64,0,0,282,283,5,7,0,
        0,283,284,3,18,9,0,284,285,5,44,0,0,285,286,3,18,9,2,286,292,1,0,
        0,0,287,288,5,3,0,0,288,289,3,18,9,0,289,290,5,4,0,0,290,292,1,0,
        0,0,291,126,1,0,0,0,291,128,1,0,0,0,291,129,1,0,0,0,291,130,1,0,
        0,0,291,131,1,0,0,0,291,138,1,0,0,0,291,143,1,0,0,0,291,148,1,0,
        0,0,291,153,1,0,0,0,291,158,1,0,0,0,291,163,1,0,0,0,291,168,1,0,
        0,0,291,173,1,0,0,0,291,178,1,0,0,0,291,187,1,0,0,0,291,193,1,0,
        0,0,291,199,1,0,0,0,291,218,1,0,0,0,291,230,1,0,0,0,291,243,1,0,
        0,0,291,250,1,0,0,0,291,265,1,0,0,0,291,273,1,0,0,0,291,280,1,0,
        0,0,291,287,1,0,0,0,292,347,1,0,0,0,293,294,10,20,0,0,294,295,5,
        22,0,0,295,346,3,18,9,21,296,297,10,19,0,0,297,298,5,33,0,0,298,
        346,3,18,9,20,299,300,10,18,0,0,300,301,5,21,0,0,301,346,3,18,9,
        19,302,303,10,17,0,0,303,304,5,50,0,0,304,346,3,18,9,18,305,306,
        10,9,0,0,306,307,5,15,0,0,307,346,3,18,9,10,308,309,10,8,0,0,309,
        310,5,16,0,0,310,346,3,18,9,9,311,312,10,7,0,0,312,313,5,17,0,0,
        313,346,3,18,9,8,314,315,10,6,0,0,315,316,5,18,0,0,316,346,3,18,
        9,7,317,318,10,5,0,0,318,319,5,19,0,0,319,346,3,18,9,6,320,321,10,
        4,0,0,321,322,5,20,0,0,322,346,3,18,9,5,323,324,10,39,0,0,324,325,
        5,29,0,0,325,346,5,64,0,0,326,327,10,38,0,0,327,328,5,29,0,0,328,
        346,5,66,0,0,329,330,10,21,0,0,330,339,5,3,0,0,331,336,3,18,9,0,
        332,333,5,1,0,0,333,335,3,18,9,0,334,332,1,0,0,0,335,338,1,0,0,0,
        336,334,1,0,0,0,336,337,1,0,0,0,337,340,1,0,0,0,338,336,1,0,0,0,
        339,331,1,0,0,0,339,340,1,0,0,0,340,341,1,0,0,0,341,346,5,4,0,0,
        342,343,10,16,0,0,343,344,5,34,0,0,344,346,3,28,14,0,345,293,1,0,
        0,0,345,296,1,0,0,0,345,299,1,0,0,0,345,302,1,0,0,0,345,305,1,0,
        0,0,345,308,1,0,0,0,345,311,1,0,0,0,345,314,1,0,0,0,345,317,1,0,
        0,0,345,320,1,0,0,0,345,323,1,0,0,0,345,326,1,0,0,0,345,329,1,0,
        0,0,345,342,1,0,0,0,346,349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,
        0,0,348,19,1,0,0,0,349,347,1,0,0,0,350,351,5,64,0,0,351,352,5,7,
        0,0,352,353,3,18,9,0,353,21,1,0,0,0,354,355,3,24,12,0,355,356,5,
        10,0,0,356,357,3,18,9,0,357,23,1,0,0,0,358,359,5,11,0,0,359,362,
        5,64,0,0,360,361,5,7,0,0,361,363,3,24,12,0,362,360,1,0,0,0,362,363,
        1,0,0,0,363,364,1,0,0,0,364,423,5,12,0,0,365,374,5,5,0,0,366,371,
        3,24,12,0,367,368,5,1,0,0,368,370,3,24,12,0,369,367,1,0,0,0,370,
        373,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,375,1,0,0,0,373,
        371,1,0,0,0,374,366,1,0,0,0,374,375,1,0,0,0,375,376,1,0,0,0,376,
        423,5,6,0,0,377,378,5,51,0,0,378,387,5,5,0,0,379,384,3,26,13,0,380,
        381,5,1,0,0,381,383,3,26,13,0,382,380,1,0,0,0,383,386,1,0,0,0,384,
        382,1,0,0,0,384,385,1,0,0,0,385,388,1,0,0,0,386,384,1,0,0,0,387,
        379,1,0,0,0,387,388,1,0,0,0,388,389,1,0,0,0,389,423,5,6,0,0,390,
        399,5,13,0,0,391,396,3,24,12,0,392,393,5,1,0,0,393,395,3,24,12,0,
        394,392,1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,1,0,0,0,
        397,400,1,0,0,0,398,396,1,0,0,0,399,391,1,0,0,0,399,400,1,0,0,0,
        400,401,1,0,0,0,401,423,5,14,0,0,402,403,5,35,0,0,403,404,5,3,0,
        0,404,405,3,24,12,0,405,406,5,1,0,0,406,407,3,24,12,0,407,408,5,
        4,0,0,408,423,1,0,0,0,409,423,5,39,0,0,410,423,5,56,0,0,411,423,
        5,66,0,0,412,413,5,53,0,0,413,414,5,3,0,0,414,415,3,24,12,0,415,
        416,5,4,0,0,416,423,1,0,0,0,417,423,5,64,0,0,418,419,5,3,0,0,419,
        420,3,24,12,0,420,421,5,4,0,0,421,423,1,0,0,0,422,358,1,0,0,0,422,
        365,1,0,0,0,422,377,1,0,0,0,422,390,1,0,0,0,422,402,1,0,0,0,422,
        409,1,0,0,0,422,410,1,0,0,0,422,411,1,0,0,0,422,412,1,0,0,0,422,
        417,1,0,0,0,422,418,1,0,0,0,423,25,1,0,0,0,424,425,5,64,0,0,425,
        426,5,7,0,0,426,427,3,24,12,0,427,27,1,0,0,0,428,429,6,14,-1,0,429,
        503,5,30,0,0,430,503,5,31,0,0,431,432,5,41,0,0,432,441,5,3,0,0,433,
        438,3,28,14,0,434,435,5,1,0,0,435,437,3,28,14,0,436,434,1,0,0,0,
        437,440,1,0,0,0,438,436,1,0,0,0,438,439,1,0,0,0,439,442,1,0,0,0,
        440,438,1,0,0,0,441,433,1,0,0,0,441,442,1,0,0,0,442,443,1,0,0,0,
        443,444,5,4,0,0,444,445,5,9,0,0,445,503,3,28,14,10,446,447,5,61,
        0,0,447,448,5,64,0,0,448,449,5,29,0,0,449,503,3,28,14,9,450,455,
        5,5,0,0,451,452,3,28,14,0,452,453,5,1,0,0,453,454,3,28,14,0,454,
        456,1,0,0,0,455,451,1,0,0,0,455,456,1,0,0,0,456,457,1,0,0,0,457,
        503,5,6,0,0,458,459,5,51,0,0,459,468,5,5,0,0,460,465,3,30,15,0,461,
        462,5,1,0,0,462,464,3,30,15,0,463,461,1,0,0,0,464,467,1,0,0,0,465,
        463,1,0,0,0,465,466,1,0,0,0,466,469,1,0,0,0,467,465,1,0,0,0,468,
        460,1,0,0,0,468,469,1,0,0,0,469,470,1,0,0,0,470,503,5,6,0,0,471,
        472,5,59,0,0,472,481,5,5,0,0,473,478,3,32,16,0,474,475,5,1,0,0,475,
        477,3,32,16,0,476,474,1,0,0,0,477,480,1,0,0,0,478,476,1,0,0,0,478,
        479,1,0,0,0,479,482,1,0,0,0,480,478,1,0,0,0,481,473,1,0,0,0,481,
        482,1,0,0,0,482,483,1,0,0,0,483,503,5,6,0,0,484,493,5,13,0,0,485,
        490,3,28,14,0,486,487,5,1,0,0,487,489,3,28,14,0,488,486,1,0,0,0,
        489,492,1,0,0,0,490,488,1,0,0,0,490,491,1,0,0,0,491,494,1,0,0,0,
        492,490,1,0,0,0,493,485,1,0,0,0,493,494,1,0,0,0,494,495,1,0,0,0,
        495,503,5,14,0,0,496,503,5,32,0,0,497,503,5,64,0,0,498,499,5,3,0,
        0,499,500,3,28,14,0,500,501,5,4,0,0,501,503,1,0,0,0,502,428,1,0,
        0,0,502,430,1,0,0,0,502,431,1,0,0,0,502,446,1,0,0,0,502,450,1,0,
        0,0,502,458,1,0,0,0,502,471,1,0,0,0,502,484,1,0,0,0,502,496,1,0,
        0,0,502,497,1,0,0,0,502,498,1,0,0,0,503,509,1,0,0,0,504,505,10,8,
        0,0,505,506,5,21,0,0,506,508,3,28,14,9,507,504,1,0,0,0,508,511,1,
        0,0,0,509,507,1,0,0,0,509,510,1,0,0,0,510,29,1,0,0,0,511,509,1,0,
        0,0,512,513,5,64,0,0,513,514,5,8,0,0,514,515,3,28,14,0,515,31,1,
        0,0,0,516,519,5,64,0,0,517,518,5,8,0,0,518,520,3,28,14,0,519,517,
        1,0,0,0,519,520,1,0,0,0,520,33,1,0,0,0,45,47,53,67,75,86,89,94,98,
        104,118,206,209,224,227,237,240,247,258,261,270,291,336,339,345,
        347,362,371,374,384,387,396,399,422,438,441,455,465,468,478,481,
        490,493,502,509,519
    ]

class stellaParser ( Parser ):

    grammarFileName = "stellaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'('", "')'", "'{'", "'}'", 
                     "'='", "':'", "'->'", "'=>'", "'<|'", "'|>'", "'['", 
                     "']'", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", 
                     "'+'", "'*'", "'List::head'", "'List::isempty'", "'List::tail'", 
                     "'Nat::pred'", "'Nat::iszero'", "'Nat::rec'", "'.'", 
                     "'Bool'", "'Nat'", "'Unit'", "'and'", "'as'", "'cons'", 
                     "'core'", "'else'", "'extend'", "'false'", "'fix'", 
                     "'fn'", "'fold'", "'if'", "'in'", "'inline'", "'language'", 
                     "'let'", "'match'", "'not'", "'or'", "'record'", "'return'", 
                     "'succ'", "'then'", "'throws'", "'true'", "'type'", 
                     "'unfold'", "'variant'", "'with'", "'\\u00B5'" ]

    symbolicNames = [ "<INVALID>", "Surrogate_id_SYMB_0", "Surrogate_id_SYMB_1", 
                      "Surrogate_id_SYMB_2", "Surrogate_id_SYMB_3", "Surrogate_id_SYMB_4", 
                      "Surrogate_id_SYMB_5", "Surrogate_id_SYMB_6", "Surrogate_id_SYMB_7", 
                      "Surrogate_id_SYMB_8", "Surrogate_id_SYMB_9", "Surrogate_id_SYMB_10", 
                      "Surrogate_id_SYMB_11", "Surrogate_id_SYMB_12", "Surrogate_id_SYMB_13", 
                      "Surrogate_id_SYMB_14", "Surrogate_id_SYMB_15", "Surrogate_id_SYMB_16", 
                      "Surrogate_id_SYMB_17", "Surrogate_id_SYMB_18", "Surrogate_id_SYMB_19", 
                      "Surrogate_id_SYMB_20", "Surrogate_id_SYMB_21", "Surrogate_id_SYMB_22", 
                      "Surrogate_id_SYMB_23", "Surrogate_id_SYMB_24", "Surrogate_id_SYMB_25", 
                      "Surrogate_id_SYMB_26", "Surrogate_id_SYMB_27", "Surrogate_id_SYMB_28", 
                      "Surrogate_id_SYMB_29", "Surrogate_id_SYMB_30", "Surrogate_id_SYMB_31", 
                      "Surrogate_id_SYMB_32", "Surrogate_id_SYMB_33", "Surrogate_id_SYMB_34", 
                      "Surrogate_id_SYMB_35", "Surrogate_id_SYMB_36", "Surrogate_id_SYMB_37", 
                      "Surrogate_id_SYMB_38", "Surrogate_id_SYMB_39", "Surrogate_id_SYMB_40", 
                      "Surrogate_id_SYMB_41", "Surrogate_id_SYMB_42", "Surrogate_id_SYMB_43", 
                      "Surrogate_id_SYMB_44", "Surrogate_id_SYMB_45", "Surrogate_id_SYMB_46", 
                      "Surrogate_id_SYMB_47", "Surrogate_id_SYMB_48", "Surrogate_id_SYMB_49", 
                      "Surrogate_id_SYMB_50", "Surrogate_id_SYMB_51", "Surrogate_id_SYMB_52", 
                      "Surrogate_id_SYMB_53", "Surrogate_id_SYMB_54", "Surrogate_id_SYMB_55", 
                      "Surrogate_id_SYMB_56", "Surrogate_id_SYMB_57", "Surrogate_id_SYMB_58", 
                      "Surrogate_id_SYMB_59", "Surrogate_id_SYMB_60", "COMMENT_antlr_builtin", 
                      "MULTICOMMENT_antlr_builtin", "StellaIdent", "ExtensionName", 
                      "INTEGER", "WS", "ErrorToken" ]

    RULE_start_Program = 0
    RULE_start_Expr = 1
    RULE_start_Type = 2
    RULE_program = 3
    RULE_languageDecl = 4
    RULE_extension = 5
    RULE_decl = 6
    RULE_annotation = 7
    RULE_paramDecl = 8
    RULE_expr = 9
    RULE_binding = 10
    RULE_match_case = 11
    RULE_pattern = 12
    RULE_labelledPattern = 13
    RULE_stellatype = 14
    RULE_recordFieldType = 15
    RULE_variantFieldType = 16

    ruleNames =  [ "start_Program", "start_Expr", "start_Type", "program", 
                   "languageDecl", "extension", "decl", "annotation", "paramDecl", 
                   "expr", "binding", "match_case", "pattern", "labelledPattern", 
                   "stellatype", "recordFieldType", "variantFieldType" ]

    EOF = Token.EOF
    Surrogate_id_SYMB_0=1
    Surrogate_id_SYMB_1=2
    Surrogate_id_SYMB_2=3
    Surrogate_id_SYMB_3=4
    Surrogate_id_SYMB_4=5
    Surrogate_id_SYMB_5=6
    Surrogate_id_SYMB_6=7
    Surrogate_id_SYMB_7=8
    Surrogate_id_SYMB_8=9
    Surrogate_id_SYMB_9=10
    Surrogate_id_SYMB_10=11
    Surrogate_id_SYMB_11=12
    Surrogate_id_SYMB_12=13
    Surrogate_id_SYMB_13=14
    Surrogate_id_SYMB_14=15
    Surrogate_id_SYMB_15=16
    Surrogate_id_SYMB_16=17
    Surrogate_id_SYMB_17=18
    Surrogate_id_SYMB_18=19
    Surrogate_id_SYMB_19=20
    Surrogate_id_SYMB_20=21
    Surrogate_id_SYMB_21=22
    Surrogate_id_SYMB_22=23
    Surrogate_id_SYMB_23=24
    Surrogate_id_SYMB_24=25
    Surrogate_id_SYMB_25=26
    Surrogate_id_SYMB_26=27
    Surrogate_id_SYMB_27=28
    Surrogate_id_SYMB_28=29
    Surrogate_id_SYMB_29=30
    Surrogate_id_SYMB_30=31
    Surrogate_id_SYMB_31=32
    Surrogate_id_SYMB_32=33
    Surrogate_id_SYMB_33=34
    Surrogate_id_SYMB_34=35
    Surrogate_id_SYMB_35=36
    Surrogate_id_SYMB_36=37
    Surrogate_id_SYMB_37=38
    Surrogate_id_SYMB_38=39
    Surrogate_id_SYMB_39=40
    Surrogate_id_SYMB_40=41
    Surrogate_id_SYMB_41=42
    Surrogate_id_SYMB_42=43
    Surrogate_id_SYMB_43=44
    Surrogate_id_SYMB_44=45
    Surrogate_id_SYMB_45=46
    Surrogate_id_SYMB_46=47
    Surrogate_id_SYMB_47=48
    Surrogate_id_SYMB_48=49
    Surrogate_id_SYMB_49=50
    Surrogate_id_SYMB_50=51
    Surrogate_id_SYMB_51=52
    Surrogate_id_SYMB_52=53
    Surrogate_id_SYMB_53=54
    Surrogate_id_SYMB_54=55
    Surrogate_id_SYMB_55=56
    Surrogate_id_SYMB_56=57
    Surrogate_id_SYMB_57=58
    Surrogate_id_SYMB_58=59
    Surrogate_id_SYMB_59=60
    Surrogate_id_SYMB_60=61
    COMMENT_antlr_builtin=62
    MULTICOMMENT_antlr_builtin=63
    StellaIdent=64
    ExtensionName=65
    INTEGER=66
    WS=67
    ErrorToken=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ProgramContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def program(self):
            return self.getTypedRuleContext(stellaParser.ProgramContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_Program" ):
                listener.enterStart_Program(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_Program" ):
                listener.exitStart_Program(self)




    def start_Program(self):

        localctx = stellaParser.Start_ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_Program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            localctx.x = self.program()
            self.state = 35
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ExprContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_Expr" ):
                listener.enterStart_Expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_Expr" ):
                listener.exitStart_Expr(self)




    def start_Expr(self):

        localctx = stellaParser.Start_ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start_Expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx.x = self.expr(0)
            self.state = 38
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # StellatypeContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_Type" ):
                listener.enterStart_Type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_Type" ):
                listener.exitStart_Type(self)




    def start_Type(self):

        localctx = stellaParser.Start_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start_Type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            localctx.x = self.stellatype(0)
            self.state = 41
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._extension = None # ExtensionContext
            self.extensions = list() # of ExtensionContexts
            self._decl = None # DeclContext
            self.decls = list() # of DeclContexts

        def languageDecl(self):
            return self.getTypedRuleContext(stellaParser.LanguageDeclContext,0)


        def extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExtensionContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExtensionContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)


        def getRuleIndex(self):
            return stellaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = stellaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.languageDecl()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 44
                localctx._extension = self.extension()
                localctx.extensions.append(localctx._extension)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144152571471200256) != 0):
                self.state = 50
                localctx._decl = self.decl()
                localctx.decls.append(localctx._decl)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LanguageDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_languageDecl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LanguageCoreContext(LanguageDeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.LanguageDeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_45(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_45, 0)
        def Surrogate_id_SYMB_35(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_35, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguageCore" ):
                listener.enterLanguageCore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguageCore" ):
                listener.exitLanguageCore(self)



    def languageDecl(self):

        localctx = stellaParser.LanguageDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_languageDecl)
        try:
            localctx = stellaParser.LanguageCoreContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(stellaParser.Surrogate_id_SYMB_45)
            self.state = 57
            self.match(stellaParser.Surrogate_id_SYMB_35)
            self.state = 58
            self.match(stellaParser.Surrogate_id_SYMB_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_extension

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnExtensionContext(ExtensionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExtensionContext
            super().__init__(parser)
            self._ExtensionName = None # Token
            self.extensionNames = list() # of Tokens
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_37(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_37, 0)
        def Surrogate_id_SYMB_59(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_59, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def ExtensionName(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.ExtensionName)
            else:
                return self.getToken(stellaParser.ExtensionName, i)
        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnExtension" ):
                listener.enterAnExtension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnExtension" ):
                listener.exitAnExtension(self)



    def extension(self):

        localctx = stellaParser.ExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_extension)
        self._la = 0 # Token type
        try:
            localctx = stellaParser.AnExtensionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(stellaParser.Surrogate_id_SYMB_37)
            self.state = 61
            self.match(stellaParser.Surrogate_id_SYMB_59)
            self.state = 62
            localctx._ExtensionName = self.match(stellaParser.ExtensionName)
            localctx.extensionNames.append(localctx._ExtensionName)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 63
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 64
                localctx._ExtensionName = self.match(stellaParser.ExtensionName)
                localctx.extensionNames.append(localctx._ExtensionName)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(stellaParser.Surrogate_id_SYMB_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclTypeAliasContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self.name = None # Token
            self.atype = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_56(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_56, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclTypeAlias" ):
                listener.enterDeclTypeAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclTypeAlias" ):
                listener.exitDeclTypeAlias(self)


    class DeclFunContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self._annotation = None # AnnotationContext
            self.annotations = list() # of AnnotationContexts
            self.name = None # Token
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnType = None # StellatypeContext
            self.throwType = None # StellatypeContext
            self._decl = None # DeclContext
            self.localDecls = list() # of DeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_40(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_40, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_51(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_51, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def Surrogate_id_SYMB_54(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_54, 0)
        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(stellaParser.AnnotationContext,i)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclFun" ):
                listener.enterDeclFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclFun" ):
                listener.exitDeclFun(self)



    def decl(self):

        localctx = stellaParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41, 45]:
                localctx = stellaParser.DeclFunContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 72
                    localctx._annotation = self.annotation()
                    localctx.annotations.append(localctx._annotation)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 78
                self.match(stellaParser.Surrogate_id_SYMB_40)
                self.state = 79
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 80
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 81
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 82
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 83
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 88
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 91
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 92
                    self.match(stellaParser.Surrogate_id_SYMB_8)
                    self.state = 93
                    localctx.returnType = self.stellatype(0)


                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 96
                    self.match(stellaParser.Surrogate_id_SYMB_54)
                    self.state = 97
                    localctx.throwType = self.stellatype(0)


                self.state = 100
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144152571471200256) != 0):
                    self.state = 101
                    localctx._decl = self.decl()
                    localctx.localDecls.append(localctx._decl)
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
                self.match(stellaParser.Surrogate_id_SYMB_51)
                self.state = 108
                localctx.returnExpr = self.expr(0)
                self.state = 109
                self.match(stellaParser.Surrogate_id_SYMB_1)
                self.state = 110
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [57]:
                localctx = stellaParser.DeclTypeAliasContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(stellaParser.Surrogate_id_SYMB_56)
                self.state = 113
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 114
                self.match(stellaParser.Surrogate_id_SYMB_6)
                self.state = 115
                localctx.atype = self.stellatype(0)
                self.state = 116
                self.match(stellaParser.Surrogate_id_SYMB_1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_annotation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InlineAnnotationContext(AnnotationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.AnnotationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_44(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_44, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineAnnotation" ):
                listener.enterInlineAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineAnnotation" ):
                listener.exitInlineAnnotation(self)



    def annotation(self):

        localctx = stellaParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_annotation)
        try:
            localctx = stellaParser.InlineAnnotationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(stellaParser.Surrogate_id_SYMB_44)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.paramType = None # StellatypeContext

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_paramDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamDecl" ):
                listener.enterParamDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamDecl" ):
                listener.exitParamDecl(self)




    def paramDecl(self):

        localctx = stellaParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            localctx.name = self.match(stellaParser.StellaIdent)
            self.state = 123
            self.match(stellaParser.Surrogate_id_SYMB_7)
            self.state = 124
            localctx.paramType = self.stellatype(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IsEmptyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_23(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_23, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsEmpty" ):
                listener.enterIsEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsEmpty" ):
                listener.exitIsEmpty(self)


    class FoldContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_41(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_41, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFold" ):
                listener.enterFold(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFold" ):
                listener.exitFold(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_20(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_20, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)


    class IsZeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_26(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_26, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsZero" ):
                listener.enterIsZero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsZero" ):
                listener.exitIsZero(self)


    class LessThanOrEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_15(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_15, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThanOrEqual" ):
                listener.enterLessThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThanOrEqual" ):
                listener.exitLessThanOrEqual(self)


    class SuccContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_52(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_52, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSucc" ):
                listener.enterSucc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSucc" ):
                listener.exitSucc(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)


    class GreaterThanOrEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_17(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_17, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanOrEqual" ):
                listener.enterGreaterThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanOrEqual" ):
                listener.exitGreaterThanOrEqual(self)


    class LessThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThan" ):
                listener.enterLessThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThan" ):
                listener.exitLessThan(self)


    class LogicNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_48(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_48, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicNot" ):
                listener.enterLogicNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicNot" ):
                listener.exitLogicNot(self)


    class DotRecordContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.label = None # Token
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_28(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_28, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotRecord" ):
                listener.enterDotRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotRecord" ):
                listener.exitDotRecord(self)


    class ParenthesisedExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisedExpr" ):
                listener.enterParenthesisedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisedExpr" ):
                listener.exitParenthesisedExpr(self)


    class GreaterThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_16(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_16, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThan" ):
                listener.enterGreaterThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThan" ):
                listener.exitGreaterThan(self)


    class EqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_18(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_18, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)


    class TailContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_24(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_24, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail" ):
                listener.enterTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail" ):
                listener.exitTail(self)


    class MultiplyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_21(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_21, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)


    class RecordContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._binding = None # BindingContext
            self.bindings = list() # of BindingContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_50(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_50, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def binding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.BindingContext)
            else:
                return self.getTypedRuleContext(stellaParser.BindingContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord" ):
                listener.enterRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord" ):
                listener.exitRecord(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.exprs = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)


    class LogicAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_32(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_32, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)


    class LogicOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_49(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_49, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)


    class HeadContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_22(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_22, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)


    class NotEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_19(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_19, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqual" ):
                listener.enterNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqual" ):
                listener.exitNotEqual(self)


    class PredContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)


    class MatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._match_case = None # Match_caseContext
            self.cases = list() # of Match_caseContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_47(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_47, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def match_case(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.Match_caseContext)
            else:
                return self.getTypedRuleContext(stellaParser.Match_caseContext,i)

        def Surrogate_id_SYMB_1(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_1)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_1, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatch" ):
                listener.enterMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatch" ):
                listener.exitMatch(self)


    class TypeAscContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_33(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_33, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAsc" ):
                listener.enterTypeAsc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAsc" ):
                listener.exitTypeAsc(self)


    class NatRecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.initial = None # ExprContext
            self.step = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_27(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_27, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNatRec" ):
                listener.enterNatRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNatRec" ):
                listener.exitNatRec(self)


    class ConstFalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_38(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_38, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstFalse" ):
                listener.enterConstFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstFalse" ):
                listener.exitConstFalse(self)


    class AbstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_40(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_40, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_51(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_51, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction" ):
                listener.enterAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction" ):
                listener.exitAbstraction(self)


    class ConstIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstInt" ):
                listener.enterConstInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstInt" ):
                listener.exitConstInt(self)


    class UnfoldContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_57(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_57, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnfold" ):
                listener.enterUnfold(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnfold" ):
                listener.exitUnfold(self)


    class VariantContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.label = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_10(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_10, 0)
        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariant" ):
                listener.enterVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariant" ):
                listener.exitVariant(self)


    class ConstTrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_55(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_55, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstTrue" ):
                listener.enterConstTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstTrue" ):
                listener.exitConstTrue(self)


    class DotTupleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.index = None # Token
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_28(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_28, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotTuple" ):
                listener.enterDotTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotTuple" ):
                listener.exitDotTuple(self)


    class FixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_39(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_39, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFix" ):
                listener.enterFix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFix" ):
                listener.exitFix(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.var = None # Token
            self.value = None # ExprContext
            self.body = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_46(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_46, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.condition = None # ExprContext
            self.thenExpr = None # ExprContext
            self.elseExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_42(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_42, 0)
        def Surrogate_id_SYMB_53(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_53, 0)
        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)


    class ApplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.fun = None # ExprContext
            self._expr = None # ExprContext
            self.args = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)


    class TupleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.exprs = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)


    class ConsListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.head = None # ExprContext
            self.tail = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_34(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_34, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsList" ):
                listener.enterConsList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsList" ):
                listener.exitConsList(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stellaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                localctx = stellaParser.ConstTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 127
                self.match(stellaParser.Surrogate_id_SYMB_55)
                pass
            elif token in [39]:
                localctx = stellaParser.ConstFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(stellaParser.Surrogate_id_SYMB_38)
                pass
            elif token in [66]:
                localctx = stellaParser.ConstIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                localctx.n = self.match(stellaParser.INTEGER)
                pass
            elif token in [64]:
                localctx = stellaParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                localctx.name = self.match(stellaParser.StellaIdent)
                pass
            elif token in [35]:
                localctx = stellaParser.ConsListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(stellaParser.Surrogate_id_SYMB_34)
                self.state = 132
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 133
                localctx.head = self.expr(0)
                self.state = 134
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 135
                localctx.tail = self.expr(0)
                self.state = 136
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [23]:
                localctx = stellaParser.HeadContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(stellaParser.Surrogate_id_SYMB_22)
                self.state = 139
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 140
                localctx.list_ = self.expr(0)
                self.state = 141
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [24]:
                localctx = stellaParser.IsEmptyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(stellaParser.Surrogate_id_SYMB_23)
                self.state = 144
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 145
                localctx.list_ = self.expr(0)
                self.state = 146
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [25]:
                localctx = stellaParser.TailContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(stellaParser.Surrogate_id_SYMB_24)
                self.state = 149
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 150
                localctx.list_ = self.expr(0)
                self.state = 151
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [53]:
                localctx = stellaParser.SuccContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(stellaParser.Surrogate_id_SYMB_52)
                self.state = 154
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 155
                localctx.n = self.expr(0)
                self.state = 156
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [49]:
                localctx = stellaParser.LogicNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(stellaParser.Surrogate_id_SYMB_48)
                self.state = 159
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 160
                localctx.expr_ = self.expr(0)
                self.state = 161
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [26]:
                localctx = stellaParser.PredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(stellaParser.Surrogate_id_SYMB_25)
                self.state = 164
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 165
                localctx.n = self.expr(0)
                self.state = 166
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [27]:
                localctx = stellaParser.IsZeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(stellaParser.Surrogate_id_SYMB_26)
                self.state = 169
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 170
                localctx.n = self.expr(0)
                self.state = 171
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [40]:
                localctx = stellaParser.FixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.match(stellaParser.Surrogate_id_SYMB_39)
                self.state = 174
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 175
                localctx.expr_ = self.expr(0)
                self.state = 176
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [28]:
                localctx = stellaParser.NatRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.match(stellaParser.Surrogate_id_SYMB_27)
                self.state = 179
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 180
                localctx.n = self.expr(0)
                self.state = 181
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 182
                localctx.initial = self.expr(0)
                self.state = 183
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 184
                localctx.step = self.expr(0)
                self.state = 185
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [42]:
                localctx = stellaParser.FoldContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.match(stellaParser.Surrogate_id_SYMB_41)
                self.state = 188
                self.match(stellaParser.Surrogate_id_SYMB_12)
                self.state = 189
                localctx.type_ = self.stellatype(0)
                self.state = 190
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 191
                localctx.expr_ = self.expr(23)
                pass
            elif token in [58]:
                localctx = stellaParser.UnfoldContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                self.match(stellaParser.Surrogate_id_SYMB_57)
                self.state = 194
                self.match(stellaParser.Surrogate_id_SYMB_12)
                self.state = 195
                localctx.type_ = self.stellatype(0)
                self.state = 196
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 197
                localctx.expr_ = self.expr(22)
                pass
            elif token in [41]:
                localctx = stellaParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 199
                self.match(stellaParser.Surrogate_id_SYMB_40)
                self.state = 200
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 201
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 202
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 203
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 208
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 211
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 212
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 213
                self.match(stellaParser.Surrogate_id_SYMB_51)
                self.state = 214
                localctx.returnExpr = self.expr(0)
                self.state = 215
                self.match(stellaParser.Surrogate_id_SYMB_1)
                self.state = 216
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [5]:
                localctx = stellaParser.TupleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & -6870960376516705019) != 0):
                    self.state = 219
                    localctx._expr = self.expr(0)
                    localctx.exprs.append(localctx._expr)
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 220
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 221
                        localctx._expr = self.expr(0)
                        localctx.exprs.append(localctx._expr)
                        self.state = 226
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 229
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [51]:
                localctx = stellaParser.RecordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 230
                self.match(stellaParser.Surrogate_id_SYMB_50)
                self.state = 231
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 232
                    localctx._binding = self.binding()
                    localctx.bindings.append(localctx._binding)
                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 233
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 234
                        localctx._binding = self.binding()
                        localctx.bindings.append(localctx._binding)
                        self.state = 239
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 242
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [11]:
                localctx = stellaParser.VariantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 243
                self.match(stellaParser.Surrogate_id_SYMB_10)
                self.state = 244
                localctx.label = self.match(stellaParser.StellaIdent)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 245
                    self.match(stellaParser.Surrogate_id_SYMB_6)
                    self.state = 246
                    localctx.rhs = self.expr(0)


                self.state = 249
                self.match(stellaParser.Surrogate_id_SYMB_11)
                pass
            elif token in [48]:
                localctx = stellaParser.MatchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 250
                self.match(stellaParser.Surrogate_id_SYMB_47)
                self.state = 251
                self.expr(0)
                self.state = 252
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & -6907114380488342267) != 0):
                    self.state = 253
                    localctx._match_case = self.match_case()
                    localctx.cases.append(localctx._match_case)
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 254
                        self.match(stellaParser.Surrogate_id_SYMB_1)
                        self.state = 255
                        localctx._match_case = self.match_case()
                        localctx.cases.append(localctx._match_case)
                        self.state = 260
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 263
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [13]:
                localctx = stellaParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 265
                self.match(stellaParser.Surrogate_id_SYMB_12)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & -6870960376516705019) != 0):
                    self.state = 266
                    localctx._expr = self.expr(0)
                    localctx.exprs.append(localctx._expr)

                    self.state = 267
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 268
                    localctx._expr = self.expr(0)
                    localctx.exprs.append(localctx._expr)


                self.state = 272
                self.match(stellaParser.Surrogate_id_SYMB_13)
                pass
            elif token in [43]:
                localctx = stellaParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 273
                self.match(stellaParser.Surrogate_id_SYMB_42)
                self.state = 274
                localctx.condition = self.expr(0)
                self.state = 275
                self.match(stellaParser.Surrogate_id_SYMB_53)
                self.state = 276
                localctx.thenExpr = self.expr(0)
                self.state = 277
                self.match(stellaParser.Surrogate_id_SYMB_36)
                self.state = 278
                localctx.elseExpr = self.expr(3)
                pass
            elif token in [47]:
                localctx = stellaParser.LetContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 280
                self.match(stellaParser.Surrogate_id_SYMB_46)
                self.state = 281
                localctx.var = self.match(stellaParser.StellaIdent)
                self.state = 282
                self.match(stellaParser.Surrogate_id_SYMB_6)
                self.state = 283
                localctx.value = self.expr(0)
                self.state = 284
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 285
                localctx.body = self.expr(2)
                pass
            elif token in [3]:
                localctx = stellaParser.ParenthesisedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 287
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 288
                self.expr(0)
                self.state = 289
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 345
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = stellaParser.MultiplyContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 293
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 294
                        self.match(stellaParser.Surrogate_id_SYMB_21)
                        self.state = 295
                        self.expr(21)
                        pass

                    elif la_ == 2:
                        localctx = stellaParser.LogicAndContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 296
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 297
                        self.match(stellaParser.Surrogate_id_SYMB_32)
                        self.state = 298
                        self.expr(20)
                        pass

                    elif la_ == 3:
                        localctx = stellaParser.AddContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 299
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 300
                        self.match(stellaParser.Surrogate_id_SYMB_20)
                        self.state = 301
                        self.expr(19)
                        pass

                    elif la_ == 4:
                        localctx = stellaParser.LogicOrContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 302
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 303
                        self.match(stellaParser.Surrogate_id_SYMB_49)
                        self.state = 304
                        self.expr(18)
                        pass

                    elif la_ == 5:
                        localctx = stellaParser.LessThanContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 305
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 306
                        self.match(stellaParser.Surrogate_id_SYMB_14)
                        self.state = 307
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = stellaParser.LessThanOrEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 308
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 309
                        self.match(stellaParser.Surrogate_id_SYMB_15)
                        self.state = 310
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = stellaParser.GreaterThanContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 311
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 312
                        self.match(stellaParser.Surrogate_id_SYMB_16)
                        self.state = 313
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 8:
                        localctx = stellaParser.GreaterThanOrEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 314
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 315
                        self.match(stellaParser.Surrogate_id_SYMB_17)
                        self.state = 316
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 9:
                        localctx = stellaParser.EqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 317
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 318
                        self.match(stellaParser.Surrogate_id_SYMB_18)
                        self.state = 319
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 10:
                        localctx = stellaParser.NotEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 320
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 321
                        self.match(stellaParser.Surrogate_id_SYMB_19)
                        self.state = 322
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 11:
                        localctx = stellaParser.DotRecordContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 323
                        if not self.precpred(self._ctx, 39):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 39)")
                        self.state = 324
                        self.match(stellaParser.Surrogate_id_SYMB_28)
                        self.state = 325
                        localctx.label = self.match(stellaParser.StellaIdent)
                        pass

                    elif la_ == 12:
                        localctx = stellaParser.DotTupleContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 326
                        if not self.precpred(self._ctx, 38):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 38)")
                        self.state = 327
                        self.match(stellaParser.Surrogate_id_SYMB_28)
                        self.state = 328
                        localctx.index = self.match(stellaParser.INTEGER)
                        pass

                    elif la_ == 13:
                        localctx = stellaParser.ApplicationContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.fun = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 329
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 330
                        self.match(stellaParser.Surrogate_id_SYMB_2)
                        self.state = 339
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & -6870960376516705019) != 0):
                            self.state = 331
                            localctx._expr = self.expr(0)
                            localctx.args.append(localctx._expr)
                            self.state = 336
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==1:
                                self.state = 332
                                self.match(stellaParser.Surrogate_id_SYMB_0)
                                self.state = 333
                                localctx._expr = self.expr(0)
                                localctx.args.append(localctx._expr)
                                self.state = 338
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 341
                        self.match(stellaParser.Surrogate_id_SYMB_3)
                        pass

                    elif la_ == 14:
                        localctx = stellaParser.TypeAscContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 342
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 343
                        self.match(stellaParser.Surrogate_id_SYMB_33)
                        self.state = 344
                        localctx.type_ = self.stellatype(0)
                        pass

             
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.rhs = None # ExprContext

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_binding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinding" ):
                listener.enterBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinding" ):
                listener.exitBinding(self)




    def binding(self):

        localctx = stellaParser.BindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            localctx.name = self.match(stellaParser.StellaIdent)
            self.state = 351
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 352
            localctx.rhs = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Match_caseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def Surrogate_id_SYMB_9(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_9, 0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_match_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatch_case" ):
                listener.enterMatch_case(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatch_case" ):
                listener.exitMatch_case(self)




    def match_case(self):

        localctx = stellaParser.Match_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_match_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.pattern()
            self.state = 355
            self.match(stellaParser.Surrogate_id_SYMB_9)
            self.state = 356
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_pattern

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PatternIntContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.n = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternInt" ):
                listener.enterPatternInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternInt" ):
                listener.exitPatternInt(self)


    class PatternConsContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.head = None # PatternContext
            self.tail = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_34(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_34, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternCons" ):
                listener.enterPatternCons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternCons" ):
                listener.exitPatternCons(self)


    class PatternTrueContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_55(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_55, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternTrue" ):
                listener.enterPatternTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternTrue" ):
                listener.exitPatternTrue(self)


    class PatternTupleContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._pattern = None # PatternContext
            self.patterns = list() # of PatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternTuple" ):
                listener.enterPatternTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternTuple" ):
                listener.exitPatternTuple(self)


    class PatternListContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._pattern = None # PatternContext
            self.patterns = list() # of PatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternList" ):
                listener.enterPatternList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternList" ):
                listener.exitPatternList(self)


    class PatternVarContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternVar" ):
                listener.enterPatternVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternVar" ):
                listener.exitPatternVar(self)


    class PatternRecordContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._labelledPattern = None # LabelledPatternContext
            self.patterns = list() # of LabelledPatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_50(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_50, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def labelledPattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.LabelledPatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.LabelledPatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternRecord" ):
                listener.enterPatternRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternRecord" ):
                listener.exitPatternRecord(self)


    class ParenthesisedPatternContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)

        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisedPattern" ):
                listener.enterParenthesisedPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisedPattern" ):
                listener.exitParenthesisedPattern(self)


    class PatternVariantContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.label = None # Token
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_10(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_10, 0)
        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternVariant" ):
                listener.enterPatternVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternVariant" ):
                listener.exitPatternVariant(self)


    class PatternSuccContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.n = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_52(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_52, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternSucc" ):
                listener.enterPatternSucc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternSucc" ):
                listener.exitPatternSucc(self)


    class PatternFalseContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_38(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_38, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatternFalse" ):
                listener.enterPatternFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatternFalse" ):
                listener.exitPatternFalse(self)



    def pattern(self):

        localctx = stellaParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = stellaParser.PatternVariantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(stellaParser.Surrogate_id_SYMB_10)
                self.state = 359
                localctx.label = self.match(stellaParser.StellaIdent)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 360
                    self.match(stellaParser.Surrogate_id_SYMB_6)
                    self.state = 361
                    self.pattern()


                self.state = 364
                self.match(stellaParser.Surrogate_id_SYMB_11)
                pass
            elif token in [5]:
                localctx = stellaParser.PatternTupleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & -6907114380488342267) != 0):
                    self.state = 366
                    localctx._pattern = self.pattern()
                    localctx.patterns.append(localctx._pattern)
                    self.state = 371
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 367
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 368
                        localctx._pattern = self.pattern()
                        localctx.patterns.append(localctx._pattern)
                        self.state = 373
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 376
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [51]:
                localctx = stellaParser.PatternRecordContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.match(stellaParser.Surrogate_id_SYMB_50)
                self.state = 378
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 387
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 379
                    localctx._labelledPattern = self.labelledPattern()
                    localctx.patterns.append(localctx._labelledPattern)
                    self.state = 384
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 380
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 381
                        localctx._labelledPattern = self.labelledPattern()
                        localctx.patterns.append(localctx._labelledPattern)
                        self.state = 386
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 389
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [13]:
                localctx = stellaParser.PatternListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 390
                self.match(stellaParser.Surrogate_id_SYMB_12)
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & -6907114380488342267) != 0):
                    self.state = 391
                    localctx._pattern = self.pattern()
                    localctx.patterns.append(localctx._pattern)
                    self.state = 396
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 392
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 393
                        localctx._pattern = self.pattern()
                        localctx.patterns.append(localctx._pattern)
                        self.state = 398
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 401
                self.match(stellaParser.Surrogate_id_SYMB_13)
                pass
            elif token in [35]:
                localctx = stellaParser.PatternConsContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 402
                self.match(stellaParser.Surrogate_id_SYMB_34)
                self.state = 403
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 404
                localctx.head = self.pattern()
                self.state = 405
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 406
                localctx.tail = self.pattern()
                self.state = 407
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [39]:
                localctx = stellaParser.PatternFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 409
                self.match(stellaParser.Surrogate_id_SYMB_38)
                pass
            elif token in [56]:
                localctx = stellaParser.PatternTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 410
                self.match(stellaParser.Surrogate_id_SYMB_55)
                pass
            elif token in [66]:
                localctx = stellaParser.PatternIntContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 411
                localctx.n = self.match(stellaParser.INTEGER)
                pass
            elif token in [53]:
                localctx = stellaParser.PatternSuccContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 412
                self.match(stellaParser.Surrogate_id_SYMB_52)
                self.state = 413
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 414
                localctx.n = self.pattern()
                self.state = 415
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            elif token in [64]:
                localctx = stellaParser.PatternVarContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 417
                localctx.name = self.match(stellaParser.StellaIdent)
                pass
            elif token in [3]:
                localctx = stellaParser.ParenthesisedPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 418
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 419
                self.pattern()
                self.state = 420
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelledPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def getRuleIndex(self):
            return stellaParser.RULE_labelledPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledPattern" ):
                listener.enterLabelledPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledPattern" ):
                listener.exitLabelledPattern(self)




    def labelledPattern(self):

        localctx = stellaParser.LabelledPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_labelledPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 425
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 426
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StellatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_stellatype

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TypeTupleContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.types = list() # of StellatypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeTuple" ):
                listener.enterTypeTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeTuple" ):
                listener.exitTypeTuple(self)


    class TypeVarContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVar" ):
                listener.enterTypeVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVar" ):
                listener.exitTypeVar(self)


    class TypeVariantContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._variantFieldType = None # VariantFieldTypeContext
            self.fieldTypes = list() # of VariantFieldTypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_58(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_58, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def variantFieldType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.VariantFieldTypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.VariantFieldTypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVariant" ):
                listener.enterTypeVariant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVariant" ):
                listener.exitTypeVariant(self)


    class TypeUnitContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_31(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_31, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeUnit" ):
                listener.enterTypeUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeUnit" ):
                listener.exitTypeUnit(self)


    class TypeBoolContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_29(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_29, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBool" ):
                listener.enterTypeBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBool" ):
                listener.exitTypeBool(self)


    class TypeNatContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_30(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_30, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeNat" ):
                listener.enterTypeNat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeNat" ):
                listener.exitTypeNat(self)


    class TypeRecContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.var = None # Token
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_60(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_60, 0)
        def Surrogate_id_SYMB_28(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_28, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeRec" ):
                listener.enterTypeRec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeRec" ):
                listener.exitTypeRec(self)


    class TypeParensContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParens" ):
                listener.enterTypeParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParens" ):
                listener.exitTypeParens(self)


    class TypeFunContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.paramTypes = list() # of StellatypeContexts
            self.returnType = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_40(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_40, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeFun" ):
                listener.enterTypeFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeFun" ):
                listener.exitTypeFun(self)


    class TypeRecordContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._recordFieldType = None # RecordFieldTypeContext
            self.fieldTypes = list() # of RecordFieldTypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_50(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_50, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def recordFieldType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.RecordFieldTypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.RecordFieldTypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeRecord" ):
                listener.enterTypeRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeRecord" ):
                listener.exitTypeRecord(self)


    class TypeListContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.types = list() # of StellatypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)


    class TypeSumContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.left = None # StellatypeContext
            self.right = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_20(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_20, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSum" ):
                listener.enterTypeSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSum" ):
                listener.exitTypeSum(self)



    def stellatype(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stellaParser.StellatypeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_stellatype, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                localctx = stellaParser.TypeBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 429
                self.match(stellaParser.Surrogate_id_SYMB_29)
                pass
            elif token in [31]:
                localctx = stellaParser.TypeNatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 430
                self.match(stellaParser.Surrogate_id_SYMB_30)
                pass
            elif token in [41]:
                localctx = stellaParser.TypeFunContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 431
                self.match(stellaParser.Surrogate_id_SYMB_40)
                self.state = 432
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & 2666412730197476357) != 0):
                    self.state = 433
                    localctx._stellatype = self.stellatype(0)
                    localctx.paramTypes.append(localctx._stellatype)
                    self.state = 438
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 434
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 435
                        localctx._stellatype = self.stellatype(0)
                        localctx.paramTypes.append(localctx._stellatype)
                        self.state = 440
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 443
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 444
                self.match(stellaParser.Surrogate_id_SYMB_8)
                self.state = 445
                localctx.returnType = self.stellatype(10)
                pass
            elif token in [61]:
                localctx = stellaParser.TypeRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 446
                self.match(stellaParser.Surrogate_id_SYMB_60)
                self.state = 447
                localctx.var = self.match(stellaParser.StellaIdent)
                self.state = 448
                self.match(stellaParser.Surrogate_id_SYMB_28)
                self.state = 449
                localctx.type_ = self.stellatype(9)
                pass
            elif token in [5]:
                localctx = stellaParser.TypeTupleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 450
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & 2666412730197476357) != 0):
                    self.state = 451
                    localctx._stellatype = self.stellatype(0)
                    localctx.types.append(localctx._stellatype)

                    self.state = 452
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 453
                    localctx._stellatype = self.stellatype(0)
                    localctx.types.append(localctx._stellatype)


                self.state = 457
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [51]:
                localctx = stellaParser.TypeRecordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 458
                self.match(stellaParser.Surrogate_id_SYMB_50)
                self.state = 459
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 460
                    localctx._recordFieldType = self.recordFieldType()
                    localctx.fieldTypes.append(localctx._recordFieldType)
                    self.state = 465
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 461
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 462
                        localctx._recordFieldType = self.recordFieldType()
                        localctx.fieldTypes.append(localctx._recordFieldType)
                        self.state = 467
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 470
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [59]:
                localctx = stellaParser.TypeVariantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 471
                self.match(stellaParser.Surrogate_id_SYMB_58)
                self.state = 472
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 473
                    localctx._variantFieldType = self.variantFieldType()
                    localctx.fieldTypes.append(localctx._variantFieldType)
                    self.state = 478
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 474
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 475
                        localctx._variantFieldType = self.variantFieldType()
                        localctx.fieldTypes.append(localctx._variantFieldType)
                        self.state = 480
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 483
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass
            elif token in [13]:
                localctx = stellaParser.TypeListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 484
                self.match(stellaParser.Surrogate_id_SYMB_12)
                self.state = 493
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & 2666412730197476357) != 0):
                    self.state = 485
                    localctx._stellatype = self.stellatype(0)
                    localctx.types.append(localctx._stellatype)
                    self.state = 490
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 486
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 487
                        localctx._stellatype = self.stellatype(0)
                        localctx.types.append(localctx._stellatype)
                        self.state = 492
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 495
                self.match(stellaParser.Surrogate_id_SYMB_13)
                pass
            elif token in [32]:
                localctx = stellaParser.TypeUnitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 496
                self.match(stellaParser.Surrogate_id_SYMB_31)
                pass
            elif token in [64]:
                localctx = stellaParser.TypeVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 497
                localctx.name = self.match(stellaParser.StellaIdent)
                pass
            elif token in [3]:
                localctx = stellaParser.TypeParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 498
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 499
                self.stellatype(0)
                self.state = 500
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 509
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = stellaParser.TypeSumContext(self, stellaParser.StellatypeContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stellatype)
                    self.state = 504
                    if not self.precpred(self._ctx, 8):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                    self.state = 505
                    self.match(stellaParser.Surrogate_id_SYMB_20)
                    self.state = 506
                    localctx.right = self.stellatype(9) 
                self.state = 511
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RecordFieldTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.type_ = None # StellatypeContext

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_recordFieldType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordFieldType" ):
                listener.enterRecordFieldType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordFieldType" ):
                listener.exitRecordFieldType(self)




    def recordFieldType(self):

        localctx = stellaParser.RecordFieldTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_recordFieldType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 513
            self.match(stellaParser.Surrogate_id_SYMB_7)
            self.state = 514
            localctx.type_ = self.stellatype(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariantFieldTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.type_ = None # StellatypeContext

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_variantFieldType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariantFieldType" ):
                listener.enterVariantFieldType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariantFieldType" ):
                listener.exitVariantFieldType(self)




    def variantFieldType(self):

        localctx = stellaParser.VariantFieldTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variantFieldType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 517
                self.match(stellaParser.Surrogate_id_SYMB_7)
                self.state = 518
                localctx.type_ = self.stellatype(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        self._predicates[14] = self.stellatype_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 39)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 38)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 16)
         

    def stellatype_sempred(self, localctx:StellatypeContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 8)
         




