from random import choice
import time
import os

word_list = word_list = ['knee', 'knife', 'knock', 'adapt', 'know', 'affect', 'land', 'afford', 'lap', 'large', 'last', 
        'borrow', 'map', 'margin', 'budget', 'mark', 'market', 'campus', 'nerve', 'civil', 'oppose', 'deal', 'porch', 'port', 'pose', 'quit', 'elite', 
        'quote', 'recipe', 'email', 'emerge', 'refuse', 'regard', 'scope', 'score', 'fiber', 'scream', 'screen', 'field', 'script', 'tactic', 'forest', 
        'tail', 'forget', 'form', 'talent', 'formal', 'uncle', 'gear', 'gender', 
        'gene', 'video', 'view', 'viewer', 'holy', 'weapon', 'home', 'wear', 'image', 'week', 'impact', 'year', 'income', 'yell', 'yellow', 'joy', 
        'judge', 'equal', 'lord', 'king', 'france', 'cousin', 'will', 'move', 'speedy', 'friend', 'seem', 'make', 'denial', 'love', 'wisdom', 
        'answer', 'mean', 'freely', 'leave', 'stand', 'part', 'well', 'serve', 'gentry', 'sick', 'enter', 'count', 'good', 'young', 'youth',
          'bear', 'father', 'face', 'frank', 'nature', 'haste', 'moral', 'paris', 'duty', 'look', 'time', 'long', 'steal', 'talk', 'return', 
          'hide', 'honour', 'like', 'pride', 'clock', 'true', 'minute', 'speak', 'tongue', 'obey', 'hand', 'place', 'proud', 'poor', 'praise', 
          'copy', 'follow', 'rich', 'royal', 'speech', 'always', 'say', 'hear', 'word', 'ear', 'grow', 'live', 'begin', 'heel', 'flame', 'lack',
            'snuff', 'sense', 'expire', 'wish', 'honey', 'bring', 'home', 'hive', 'give', 'room', 'lend', 'fill', 'know', 'month', 'rest', 'debate',
              'stock', 'exchange', 'note', 'sell', 'equity', 'large', 'liquid', 'attractive', 'guarantor', 'settlement', 'counter', 'dealer', 'different',
                'attract', 'cover', 'interest', 'frequently', 'likely', 'trade', 'transfer', 'money', 'security', 'seller', 'buyer', 'agree', 'price',
                  'ownership', 'particular', 'company', 'market', 'range', 'small', 'individual', 'larger', 'world', 'include', 'insurance', 'pension', 
                  'hedge', 'trader', 'physical', 'floor', 'method', 'known', 'open', 'offer', 'type', 'network', 'example', 'potential', 'specific',
                    'accept', 'match', 'sale', 'place', 'multiple', 'purpose', 'facilitate', 'provide', 'real', 'discovery', 'hybrid', 'location', 
                    'flow', 'broker', 'order', 'post', 'maintain', 'spread', 'case', 'close', 'difference', 'tape', 'brokerage', 'firm', 'investor', 
                    'play', 'important', 'role', 'program', 'electronic', 'computer', 'similar', 'purchase', 'drive', 'late', 'system']

def get_word(word):
  result = choice(word)
  return result

def clear_terminal():
    if os.getenv("TERM") is None:
        return
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                 
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
               
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
       
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
           
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    tries = 6
    display = ""

    print("Lets play in hangman!".upper())
    print("-" * 40)
    print(display_hangman(6))
    print("-" * 40)
    word_completion = '_' * len(word)
    print(f"THE WORD YOU NEED TO QUESS: {word_completion}")
    guessed_letters = []
    all_used_letters = []
    
    while tries > 0:
        clear_terminal()
        print("USED LETTERS:")
        print()
        print(",".join(all_used_letters).upper())
        print()
        print("PLEASE ENTER THE LETTER..")

        s = input().lower()
        print("...")
        
        time.sleep(2)
        print("-" * 40)

        if s.isalpha() == False:
            print("YOUR WORD IS:")
            print(display)
            print("OOps this is not a letter! Try again..")
            print(f"You have {tries} left!")
            tries -= 1
            print(display_hangman(tries))
            continue
    
        if s in guessed_letters or s in all_used_letters:
            print("YOUR WORD IS:")
            print(display)
            print("YOU HAD THIS LETTER BEFORE!")
            tries -= 1
            print(f"You have {tries} left!")
            print(display_hangman(tries))
            continue
    
        if s in word:
            guessed_letters.append(s)
            all_used_letters.append(s)
            display = ""

            for char in word:
            
                if char in guessed_letters:
                    display += char
                else:
                    display += "_"
            print("YOUR WORD IS:")           
            print(display)
            print(display_hangman(tries))
            print(f"You have {tries} left!")
        else:
            print("OOPS THIS WORD DONT HAVE THIS LETTER!")
            print("YOUR WORD IS:")
            print(display)
            all_used_letters.append(s)
            tries -= 1
            print(display_hangman(tries))
            print(f"You have {tries} left!")
        
        if tries == 0 and display != word:
          print("THE WORD WAS:")
          print(word)
          return "YOU LOSE!!!"
        if display == word:
          return "YOU WOOOOOOOOON !!!!"
        
        clear_terminal()

print(play(get_word(word_list)))

def play_again():

  answer = ""

  while answer != "n".lower():
    print("-" * 40)
    print("YOU WANT TO PLAY AGAIN?  y/n")
    a = input()
    if a == "y".lower():
      play(get_word(word_list))
    else:
      print("-" * 40)
      return "OK,SEE YOU LATER!"

print(play_again())