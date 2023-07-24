print('welcome to rock paper scissor')
import random
AI = random.randint(0,2)        #choosing random integer from 0-2
rock = 0                        #assigning integer value
paper = 1
scissor = 2
def Game(AI, Human):               #defining variable
    if Human == 0 and AI == 0:      #cross checking values for human and AI
        print('Human = Rock')
        print('AI = ROCK')
        print('Draw')
    elif Human == 0 and AI == 1:
        print('Human = Rock')
        print('AI = Paper')
        print('AI wins')
    elif Human == 0 and AI == 2:
        print('Human = Rock')
        print('AI = Scissor')
        print('Human wins')
    elif Human == 1 and AI == 0:
        print('Human = paper')
        print('AI = ROCK')
        print('Human wins')
    elif Human == 1 and AI == 1:
        print('Human = paper')
        print('AI = paper')
        print('draw')
    elif Human == 1 and AI == 2:
        print('Human = paper')
        print('AI = scissor')
        print('AI wins')
    elif Human == 2 and AI == 0:
        print('Human = scissor')
        print('AI = rock')
        print('AI wins')
    elif Human == 2 and AI == 1:
        print('Human = scissor')
        print('AI = paper')
        print('Human wins')
    else:                                #using else as its the only last option
        print('Human = scissor')
        print('AI = scissor')

        print('draw')
Game(AI, Human = int(input('Given that rock=0,paper=1,scissors=2 ,choose rock or paper or scissor?')))