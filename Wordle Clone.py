import random
import csv
from difflib import SequenceMatcher

with open("5_letter_word.csv","r") as csv_File:
            reader = csv.reader(csv_File)
            data = []
            for row in reader:
                if len(row) !=0:
                    data += [row]

class Wordle:

    def __init__(self, comp_list, user_guess_list, comparison_dict, data):
        self.comp_list = []
        self.user_guess_list = []
        self.comparison_dict = {1:'',
        2:'',
        3:'',
        4:'',
        5:'',}
        self.data = data

    def CreateWord(self):
        
        self.comp_list = random.choice(self.data)
        for i in range(len(self.comp_list)):
            self.comp_list[i] = self.comp_list[i].upper()     

    def UserGuess(self):
        run = True
        
        while run:
            user_input = input('Enter your 5 letter word: ')
            self.user_guess_list = list(user_input.upper())
            if self.user_guess_list in self.data:
                print('Your guess is', self.user_guess_list)
                print()
                run = False
            else:
                print('That is not a valid word. Try again!')
                print()

    def Comparison(self):
        #trying to fix issue with wp repetition

        for i in range(len(self.user_guess_list)):
            if self.user_guess_list[i] == self.comp_list[i]:
                self.comparison_dict.update({(i+1):'cp'})
            
            elif self.user_guess_list[i] in self.comp_list:
                self.comparison_dict.update({(i+1):'wp'})
    
            elif self.user_guess_list[i] not in self.comp_list:
                self.comparison_dict.update({(i+1):'w'})

    def StartUp(self):
        print()
        print('----------------------------------------------------------------------------------------------------------------')
        print('Welcome to Dexter\'s Wordle Clone')
        print('Similarly to the game mastermind, the aim of the game is to get your guess to equal the randomly generated word.')
        print('You will be told whether your guessed word is close to the generated word by these keys:')
        print('\'cp\': correct place, \'wp\': wrong place, \'w\': wrong')
        print('Good luck!')
        print('----------------------------------------------------------------------------------------------------------------')
        print()

    def Winner(self):
        print()
        print('Congrats you got the word!!!') 


def main():
    run = True
    play_again = True
    while play_again:
        print()
        attempts = 1

        user = Wordle(comp_list=[], user_guess_list=[], comparison_dict={}, data = data)
        user.StartUp()
        user.CreateWord()
        #print(user.comp_list)
        user.UserGuess()
            
        while user.comp_list != user.user_guess_list:
            user.Comparison()
            print(user.comparison_dict)
            attempts += 1
            user.user_guess_list = []
            user.UserGuess()
            
        if user.comp_list == user.user_guess_list:
            user.Winner()
            print('It took you',attempts,'attempts.')
            print()

        play_again = input('Do you want to play again (Yes/No): ').lower()
        if SequenceMatcher(a=play_again.lower(), b='yes').ratio() > 0.7 or SequenceMatcher(a=play_again.lower(), b='y').ratio() > 0.7:
            play_again = True
        else:
            play_again = False

if __name__ == '__main__':
    main()

