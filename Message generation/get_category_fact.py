import itertools
from datetime import datetime

import work_with_text as wwt
import fact as fact

def __init__(text):
    facts_all = []
    key_word = wwt.__init__(text) #слова из текста
    #print(key_word)
    
    #key_word_category = []
    #facts_category_all = []

    # for one_word in key_word:
    #     key_word_category.append(wwr.__init__(one_word)) #все категории к словам из текста
    # #key_word.append(wwr.__init__(one_word))
    # print(key_word_category)

    for one_word in key_word:
        facts = fact.get_fact(one_word) #факты по основным словам
        facts_all.append(facts)
    # for one_word in key_word_category:
    #     if type(one_word) == list:
    #         for word in one_word:
    #             print(key_word_category)
    #             facts_category = fact.get_fact(one_word, False) #факты по категориям
    #             facts_category_all.append(facts_category)
    #    else:
    #        print(key_word_category)
    #        facts_category = fact.get_fact(one_word, False) #факты по категориям
    #        facts_category_all.append(facts_category)
    facts = [key_word, facts_all]
    #facts_category = [key_word_category, facts_category_all]
    return (facts)
