print("Welcome to my game")

playing = input('Would you like to play? ')

if playing.lower() != 'yes':
    quit()

print('Lets play!')
score = 0

answer = input('Who killed PAUL? ')
if answer.lower() == 'micheal':
    print('Got it!')
    score +=1
else: 
    print('Incorrect')

answer = input("Would you like to continue? :)")
if answer.lower() == 'yes':
    print('We move now ')
else:
    print('Oky Next Time')
    quit()

answer = input('Who sold Jesus? ')
if answer.lower() == 'juda':
    print('Got it!')
    score +=1
else: 
    print('Incorrect')

answer = input('Who denied Jesus? ')
if answer.lower() == 'peter':
    print('Got it!')
    score +=1
else: 
    print('Incorrect') 

print('You got ' + str(score /3 * 100) + '%')
