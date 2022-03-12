print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low + high)/2
numGuesses = 0
response = ''
numGuesses += 1
while response != 'c':
    print('Is your secret number ' + str(int(ans)) + '?')
    response = input('Enter h to indicate the guess is too high. Enter l to '
                     'indicate the guess is too low. Enter c to indicate I guessed correctly.')
    if response == 'h':
        high = ans
    elif response == 'l':
        low = ans
    else:
        print('')
    ans = (low + high)/2
print('Game over. Your secret number was: ' + str(int(ans)))
 