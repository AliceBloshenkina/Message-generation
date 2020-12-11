


import work_with_text as wwt
import get_category_fact as gtf                             
import generation_text as gen_tx                              


text = input('Enter text: ')
# key_word = gcf.__init__(text)
#facts = fact.get_fact(key_word)

#print(key_word, facts)
facts = gtf.__init__(text)
message = gen_tx.__init__(facts, True)
           # message_cat = gen_tx.__init__(facts_cat, True)
            
if message == []:
    message = gen_tx.__init__('no', False)

if text == '':
    message = gen_tx.__init__('no', False)

for i in range(len(message)):
    print('Message: ')
    for j in range(len(message[i])):
        print(message[i][j][0])
    print('\n')