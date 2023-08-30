
#Bad choice.
bad_choice = 'Youd made a bad choice sorry '




choice = input('You are admittted to Howgwarts School of Witchcraft &  Wizardry and the sorting hat asked you whether You choose SLYTHERIN or GRYFFINDOR ')
#this is the first option that has harry potter and ron weasley.
if choice.lower() == 'gryffindor':
    harry_ron = input('You chose gryffindor Who do you prefer between HARRY or RON ')
    if harry_ron.lower() == 'harry':
        riddle_voldemort_spell = input('Do you want to find TOM RIDDLE , fight VOLDEMORT or learn a cool SPELL')
        if riddle_voldemort_spell.lower() == 'tom riddle':
            print('Trust me you dont want to find this kid hes evil ')
        elif riddle_voldemort_spell.lower() == 'voldemort':
            print('Congrats you kicked voldemort right in the nose ')
        elif riddle_voldemort_spell.lower() == 'spell':
            print('Congrats you learned the patronam spell ')
        else:
            print(bad_choice)
    elif harry_ron.lower() == 'ron':
        chess_hermione_car = input('What do you like the most between HERMIONE GRANGER , your dads BLUE CAR or WIZARD CHESS ')
        if chess_hermione_car.lower() == 'HERMIONE GRANGER':
            print('Congrats mate you get to take your crush on a sweet date')
        elif chess_hermione_car.lower == 'chess':
            print('Congrats mate you get to take part in an important wizard chess game to save the world ')
        elif chess_hermione_car.lower() == 'blue car':
            print('You put a 2.0 turbo on the blue car now Elon Musk want to hire you')
        else:
            print(bad_choice)
# this is the second option that has Draco Malfoy and professor snape
elif choice.lower() == 'slytherin':
     snape_malfoy = input('Congrats you picked Slytherin Who do you prefer between PROFESSOR SNAPE and DRACO MALFOY ')
    if snape_malfoy.lower() == 'snape':
            creepy_noble = input('Do you prefer to be known as the CREEPY professor or you want people to know your true NOBLE mission')
            if creepy_noble.lower() == 'creepy':
                print('Youre one creepy old man smile a little dude! ')
            elif creepy_noble.lower() == 'noble':
                print('Thanks for being on Harrys side the whole time.')
            else:
                print(bad_choice)
elif snape_malfoy.lower == 'Draco Malfoy':
            quidditch_advice = ('Do you want to win at QUIDDITCH or do you want some LIFE ADVICE')
            if quidditch_advice.lower == 'quidditch':
                print('You need to get the firebolt')
            elif quidditch_advice == ('advice'):
                print('Leave Voldemort he will use you and leave you for dead ')
            else: 
                print(bad_choice)
            