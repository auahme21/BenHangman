lives = 6
word = ""
letter = ""
updatedSpaces= []
global UpdateSpaces
global lives
global word
letter =["h"]
word = ['hamza']
def check(UpdateSpaces):
    lives = 6
    UpdateSpaces= ['-','-','-','-','-']
    if letter in word:
        word.find(letter,0,len(word)-1)
        UpdateSpaces[0]='h'
        word.find(letter,1,len(word)-1)
        UpdateSpaces[1]='a'
        word.find(letter,2,len(word)-1)
        UpdateSpaces[2]='m'
        word.find(letter,3,len(word)-1)
        UpdateSpaces[3]='z'
        word.find(letter,4,len(word)-1)
        UpdateSpaces[4]='a'
    else:
        lives = lives - 1
def initialize():
    global word
    global updatedSpaces
    word = "airport"
    print("_ " * len(word))
    updatedSpaces = ("_ " * len(word))
    print("Try to guess the word within 6 tries")
    print(updatedSpaces)
    
def getLetter():
    global letter
    print("What is your guess?")
    letter = raw_input()

#def check():
    
def won():
    global lives
    if updatedSpaces == word:
        print('Congratulations, you got the word!')
    else:
        '''lives = lives -1
        if lives == 0:
            print('You lost :(')'''
        getLetter()

def main():
    initialize()
    getLetter()
    #check()
    
