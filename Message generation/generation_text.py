import random
def __init__(fact, Exist):

    Hello = ['Hello', 'Hi', 'Hey', 'Good day', "G'day", 'Hey, how are you?', 'Hey there', "Hi, what's up?", 'Yo', 'Greetings', 'Hail', 'Hallo', 'Howday' ]

    Question = ["How’s it going?", 'How are things?', 'How is your day going?', 'How do you spend your free time?', 'What does your name mean?', 'Tell me about yourself', 'Who had the biggest impact on you while you were growing up?', 'What are your hobbies?', 'What is your biggest goal?', 'What do you like to do on the weekend?', 'Have you ever had a nickname? And if so, what was the story behind it?', 'What was your favorite TV show while you were growing up?', 'What are your favorite TV shows now?', 'What are your favorite movies?', 'Do you like to cook?', 'Where do you want to live when we retire?', 'Do you see yourself as an optimist, pessimist or realist, and why?', 'What is your favorite family tradition?', 'What in your life do you feel most grateful for?' ]

    Compliment = ['Your smile is contagious.', 'I bet you make babies smile.', "If cartoon bluebirds were real, a couple of 'em would be sitting on your shoulders singing right now.", "You're like sunshine on a rainy day.", 'I bet you sweat glitter.', 'I like your style.', 'Is that your picture next to "charming" in the dictionary?', "You're a smart cookie.", 'You deserve a hug right now.', "Our community is better because you're in it.", 'The people you love are lucky to have you in their lives.', "You're a gift to those around you.", "You're gorgeous—and that's the least interesting thing about you.", 'You look great.', 'Your eyes are breathtaking.', 'How is it that you always look so great?', "You may dance like no one's watching, but everyone's watching because you're mesmerizing.", 'You have cute elbows. For real.', 'Your hair looks stunning.']

    # file = 'c:\\Users\\ALISA\\Desktop\\Вуз\\Проектная практика\\Hi.txt'
    # message =[]
    # Hello = file.readline()
    # a = random.randint(0, len(Hello)-1)
    # b = random.randint(0, len(Question)-1)
    # c = random.randint(0, len(Compliment)-1)
    
    if Exist == True:
        message = []
        for i in range(len(fact[0])):
            a = random.randint(0, len(Hello)-1)
            b = random.randint(0, len(Question)-1)
            c = random.randint(0, len(Compliment)-1)
            if fact[1][i] == 0:
                break
            #print(fact)
            fact[1][i] = fact[1][i][:-1]
            fact_text = str("I thought you were interested in "+fact[0][i]+". Did you know that "+fact[1][i]+'?')
            mes = []
            mes = [[Hello[a]], [Question[b]], [Compliment[c]], [fact_text]]
            message.append(mes)
            # message[i].append(Question[b])
            # message[i].append(Compliment[c])
            # message[i].append(fact_text)
    else:
        a = random.randint(0, len(Hello)-1)
        b = random.randint(0, len(Question)-1)
        c = random.randint(0, len(Compliment)-1)
        i = 0
        # message = [[0]*3]
        # for i in range(3):
        #     message.append([''])
        message = [[[Hello[a]], [Question[b]], [Compliment[c]]]]
        # message[0][0] = Hello[a]
        # message[0][1] = Question[b]
        # message[0][2] = Compliment[c]

    return(message)

# m = __init__(0, False)
# print(m)