import re

def checkio(in_string):
    return in_string.replace("À", "A").replace("Á", "A").replace("Â", "A").replace("Ã", "A")\
        .replace("Ä", "A").replace("Å", "A").replace("È", "E").replace("É", "E")\
        .replace("Ê", "E").replace("Ë", "E").replace("à", "a").replace("á", "a").replace("â", "a").replace("ã", "a")\
        .replace("ä", "a").replace("å", "a").replace("ă", "a").replace("à", "a")\
        .replace("è", "e").replace("é", "e").replace("ê", "e").replace("ë", "e")\
        .replace("ò", "o").replace("ó", "o").replace("ô", "o").replace("õ", "o")\
        .replace("ö", "o").replace("ơ", "o").replace("ó", "o").replace("ì", "i")\
        .replace("ǹ", "n").replace("ù", "u").replace("ẁ", "w").replace("ỳ", "y")\
        .replace("Ì", "I").replace("Ǹ", "N").replace("Ò", "O").replace("Ù", "U")\
        .replace("Ẁ", "W").replace("Ỳ", "Y").replace("ằ", "a").replace("Ằ", "A")\
        .replace("ầ", "a").replace("Ầ", "A").replace("ề", "e").replace("Ề", "E")\
        .replace("ồ", "o").replace("Ồ", "O").replace("ừ", "u").replace("Ừ", "U")\
        .replace("ờ", "o").replace("Ờ", "O")
    in_string = re.sub("[ÀÁÂÃÄÅ]", "A", in_string)
    in_string = re.sub("Ç", "C", in_string)
    in_string = re.sub("[ÈÉÊË]", "E", in_string)
    in_string = re.sub("[ÌÍÎÏ]", "I", in_string)
    in_string = re.sub("Ð", "D", in_string)
    in_string = re.sub("Ñ", "N", in_string)
    in_string = re.sub("[ÒÓÔÕÖ]", "O", in_string)
    in_string = re.sub("[ÙÚÛÜ]", "U", in_string)
    in_string = re.sub("Ý", "Y", in_string)
    in_string = re.sub("[àáâãæăà]", "a", in_string)
    in_string = re.sub("ç", "c", in_string)
    in_string = re.sub("[èéêë]", "e", in_string)
    in_string = re.sub("[ìíîï]", "i", in_string)
    in_string = re.sub("ñ", "n", in_string)
    in_string = re.sub("[]", "o", in_string)
    in_string = re.sub("[ùúûü]", "u", in_string)
    in_string = re.sub("[ýÿ]", "y", in_string)
    return in_string