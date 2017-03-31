import codecs
import json
import re
import collections
dictionary = dict()
def convert():
    types = ["adj", "QuBie", "Connector", "adverb",
             "TanCi", "direction", "idiom", "phrase",
             "number", "number2", "noun", "sound",
             "preposition", "measureWord", "pronoun", "placeLocation",
             "time", "assist", "verb", "punctuation",
             "nonWord", "YuQi", "status", "name",
             "placeProperNoun", "Orgnization", "foreignSymbol", "otherNoun",
             "prefix", "suffix", "unkown", "unkown",
             "surname", "questionWord", "title", "poem"]
    f_in = codecs.open("DictOut.txt", 'r', "utf-8")
    f_out = open("ChineseSegmentorDictionary.txt", "w")
    codeSequence = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    count = len(codeSequence) - 1
    for line in f_in:
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        group = line.split(" ")
        if len(group[1]) == 0:
            continue
        word = group[0]
        word = word.replace(u'\ufeff', "")
        chars = list(word)
        count += 1
        if count % 10000 == 0:
            print(count, len(dictionary.keys()))
        charCount = 1
        typeCode = codeSequence[types.index(group[1])]
        wordCode = typeCode + getCode(codeSequence, count)
        totalLen = str(len(chars))
        for char in chars:
            if char not in dictionary.keys():
                dictionary[char] = wordCode + "1" + totalLen + ","
            else:
                dictionary[char] += wordCode + str(charCount) + totalLen + ","
            charCount += 1
    orderedDictionary = collections.OrderedDict(sorted(dictionary.items()))
    f_out.write("dictionary = {")
    for key in dictionary.keys():
        f_out.write('"' + key + '": "' + re.sub(",$", "", str(dictionary[key])) + '",\n')
    f_out.write("}")
def getCode(code, count):
    result = ""
    while count>=len(code):
        result = code[count%len(code)] + result
        count = int(count / len(code))
    result = code[count%len(code)] + result
    return result
convert()
