import spacy
import textacy.extract

import nltk
from nltk import word_tokenize

def __init__(text):
    nlp = spacy.load('en_core_web_lg')
    # """
    # # I find women with children. I don't love it.
    # # I really love pony, and, maybe, cinema.
    # # """
    # text = """
    # London is the capital of Great Britain, the city great and ancient, large industrial and cultural centre. London stands on the river Thames. One of the eldest buildings is the Tower. Its old is for nearly a thousand years. In its long history the Tower has been a palace, a fortress and a prison. William the Conqueror built it. Now it is a museum.
    # One of the different bridges across the Thames is the Tower Bridge built in 1894.
    # The City of London is the centre of British business and commerce. It’s also famous for its greatest monument St. Paul’s Cathedral. It was built in 1708.
    # Westminster is to the west of the City of London. The House of Parliament (or the Palace of Westminster) stands on the bank of the Thames. The national flag over the Victoria Tower indicates that the Parliament is sitting. The Clock Tower of the House of Parliament contains the hour-bell called “Big Ben”.
    # Buckingham Palace is used now as an official London residence of the Queen. It is also in the part of London known as Westminster.
    # Piccadilly Circus is the London theatre-land. Piccadilly Circus is the symbol of London wealth.
    # London has many other famous places such as Westminster Abbey, Trafalgar square and others. """

    text_split = text.split()
    l = len(text_split)

    doc = nlp(text)
    # nltk.download('averaged_perceptron_tagger')
    key_word = []
    if l == 0:
        key_word = None

    elif l<= 50:
        # sentence = text.split('.')
        # new_text = ''
        # this_sens = ''
        #for i in sentence[0:-1]:
        sens = word_tokenize(text) #'I love pony, want women and cat')
        massiv = nltk.pos_tag(sens)
        #print(type(massiv))
    #print(massiv)
        for j in massiv:
            j = str(j)
            j = j.split("'")
        #print(j)
            if j[3] == 'NN':
                key_word.append(j[1])
            # for k in range(len(j)):
            #     if k == 'NN':
            #         key_word.append(j[k-1])

        #print(key_word)
            # this_sens = ''
            # doc = nlp(i)
            # #i.replace('.', '')   
            # key_word = [] 
            # for token in doc:
            #     #print(token.text, token.dep_, token.head)
            #     #if token.dep_ == 'nsubj' and (str(token.text)).lower() in ('i', 'me', 'you') :
            #     #     this_sens = this_sens+str(token.text)+' '+str(token.head)
            #     if token.dep_ == 'neg':
            #         count = 1
            #        # this_sens = 'Negative: '+this_sens
            #         break
            #     if token.dep_ == 'dobj':
            #         key_word.append(str(token.text))
            #         this_sens = this_sens+' '+str(token.text)
            #     if token.dep_ == 'prep':
            #         this_sens = this_sens+' '+str(token.text)
            #     if token.dep_ == 'pobj':
            #         this_sens = this_sens+' '+str(token.text)
            #     if token.dep_ =='npadvmod':
            #         this_sens = this_sens+', '+str(token.text)
            # print(this_sens)
            #print(this_sens)
            # if this_sens != '':
            #     new_text = new_text+this_sens+'. '
        # print(new_text)

    else:
        # for entity in doc.ents:
        #    print(f"{entity.text} ({entity.label_})")
        # statements = textacy.extract.semistructured_statements(doc, "london")
        #print("Facts about London:")
        #print(statements)
        key_word = list(textacy.extract.entities(doc, drop_determiners=True))
        #print(a)
    return key_word
    #подаем список слов  получаем предложения

    # print(doc)

    # for entity in doc.ents:
    #     print(f"{entity.text} ({entity.label_})")

    # statements = textacy.extract.semistructured_statements(doc, "pony")

    # print("Facts about London:")

    # print(statements)

    # a = list(textacy.extract.entities(doc, drop_determiners=True))
    # print(a)

    # for statement in statements:
    #     subject, verb, fact = statement
    #     print(f" - {fact}")

