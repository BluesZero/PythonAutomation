#Hanged Man
import random
#hangman data
hangmanSequence = [
    {"drawing": [" ___ ", "|   |", "|   o ", "|", "|"]},
    {"drawing": [" ___ ", "|   |", "|   o ", "|   |", "|"]},
    {"drawing": [" ___ ", "|   |", "|   o ", "|  /|", "|"]},
    {"drawing": [" ___ ", "|   |", "|   o ", "|  /|\\", "|"]},
    {"drawing": [" ___ ", "|   |", "|   o ", "|  /|\\", "|  / "]},
    {"drawing": [" ___ ", "|   |", "|   o ", "|  /|\\", "|  / \\"]}
]

#Initialize variables
print("SAVE THE HANGED BROO!!, GUESS THE WOOOORDD!!!")
wordsList = ['AVOCADO', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY', 'FIG', 'GRAPE']
guessWord = random.choice(wordsList)
guessedWords = ['_' for _ in range(len(guessWord))]
lifes = 5

def main():
  #show remaining letters to guess and draw the hangman   
  while lifes >= 0 and '_' in guessedWords:
    stageDrawing = hangmanSequence[lifes]['drawing']
    print("\n".join(stageDrawing))
    print(' '.join(guessedWords))
    process()

    #if you have no remaining lifes break the bucle
    if lifes < 0 or '_' not in guessedWords:
      break
    
  if lifes < 0:
    print("\nTHE BRO WAS HANGED NOOO000")
  else:
    print("\nCONGRATULATIONS! You've saved the brO!")

    
def process():
  global lifes
  counter = 0
  inWord = input("Insert a letter: ").upper()
  
  for char in guessWord:
    if char == inWord:
      guessedWords[counter] = inWord
    counter += 1
    
  if inWord not in guessWord:
    lifes -= 1
  
main()

