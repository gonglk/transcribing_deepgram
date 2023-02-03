import wikipediaapi
#import nltk
from nltk import word_tokenize, pos_tag
#nltk.download('brown')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')


def get_summary(word):
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    
    page = wiki_wiki.page(word)
    return page.summary[:1000]


def get_wiki_url(word):
    wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    page = wiki.page(word)
    if page.exists():
        return page.fullurl
    else:
        return None

def get_nouns(text):
    words = word_tokenize(text)
    tagged = pos_tag(words)
    nouns = [word for word, pos in tagged if pos in ["NN", "NNS", "NNP", "NNPS"]]
    return nouns

#transcript = "Machine learning is a technique."
#nouns = get_nouns(text)
def wiki_search(transcript):
    nouns = get_nouns(transcript)
    wiki_result = []
    for noun in nouns:
        summary = get_summary(noun)
        url = get_wiki_url(noun)
        wiki_result.append({noun:summary,
                            "url":url})
    return wiki_result

#print(wiki_search(transcript))
