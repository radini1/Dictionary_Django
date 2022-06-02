from django.shortcuts import render
from PyDictionary import PyDictionary
from wordhoard import Synonyms, Antonyms


def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = Synonyms(search_string=search).find_synonyms()
    antonyms = Antonyms(search_string=search).find_antonyms()
    context = {'synonyms': synonyms,
               'meaning': meaning,
               'antonyms': antonyms
               }
    return render(request, 'word.html', context)

    
