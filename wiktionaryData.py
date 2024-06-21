# import requests
# from bs4 import BeautifulSoup
import json
import re


# def fetch_webpage_data(url):
#     try:
#         response = requests.get(url)
#         # Check if the response is successful
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')
#             return soup
#         else:
#             print(f"Failed to fetch URL. Status code: {response.status_code}")
#             return None
#     except requests.RequestException as e:
#         print(f"Error occurred: {e}")
#         return None
    
# from urllib.parse import quote
# word = 'غضب'
# wiki_url = 'https://en.wiktionary.org/wiki/{}#Arabic'.format(word)
# # wiki_url_quoted = quote(wiki_url, safe=':/')
# data = fetch_webpage_data(wiki_url) 

# if data:
#     # Now you can start parsing the data using BeautifulSoup
#     # For example, let's extract the content of the "<page>" tag:
#     print(data)
# else:
#     print("Failed to fetch the data.")

def matchWord(word1,word2):
    normalize = lambda x : re.sub(u'[\\u064e\\u064f\\u0650\\u0651\\u0652\\u064c\\u064b\\u064d\\u0640\\ufc62]', '', x)
    
    return normalize(word1) == normalize(word2)

def searchWikt(word):
    with open("wikiData/kaikki.org-dictionary-Arabic.json", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if matchWord(data['word'], word):
                print(data)
                break

# searchWikt('تَكْلِيم')
            