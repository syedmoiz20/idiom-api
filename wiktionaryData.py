import json
import re

def matchWord(word1,word2):
    normalize = lambda x : re.sub(u'[\\u064e\\u064f\\u0650\\u0651\\u0652\\u064c\\u064b\\u064d\\u0640\\ufc62]', '', x)
    
    return normalize(word1) == normalize(word2)

def searchWikt(word):
    with open("wikiData/arabic-dict.json", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if matchWord(data['word'], word):
                print(data)
                break

# searchWikt('تَكْلِيم')
            