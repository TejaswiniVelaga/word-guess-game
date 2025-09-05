import random
word_bank = ['university', 'bangalore', 'andhrapradesh','tamilnadu','karnataka']
word = random.choice(word_bank)
guessedWord = ['_']*len(word)
attempts = 10
while attempts >0:
    print('\nCurrent word: '+' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print ('Great! Correct guess!!')
    else:
        attempts-=1
        print("ohh no! wrong guess")
        print('\n Attempts left: '+ str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations! YOU DID IT!! and the word is: ' + word)
        break
if attempts == 0 and '_' in guessedWord:
        print('\nYou\'ve run out of attempts! The word was: ' + word)
        
