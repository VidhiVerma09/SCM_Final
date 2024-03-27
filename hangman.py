import pygame #module
import random #module
from sys import exit #module
pygame.init() #initialize
pygame.mixer.init() #initialize the music :o

clock = pygame.time.Clock() #FPS

screen = pygame.display.set_mode((800, 600)) #display window

pygame.display.set_caption("Hangman") #Title

Background_Image =  pygame.image.load('assets/images/base.jpg') #load background
Background_Image = pygame.transform.scale(Background_Image, (800, 600)) #change it's size
Hang = pygame.image.load('assets/images/hung.png')
Hang = pygame.transform.scale(Hang, (200, 200))
Stick_reaper =  pygame.image.load('assets/images/stick.png')
Stick_reaper = pygame.transform.scale(Stick_reaper, (180, 180))
Stick_hang =  pygame.image.load('assets/images/hanged.jpg')
Stick_hang = pygame.transform.scale(Stick_hang, (50, 50))
win = pygame.image.load('assets/images/cool.png')
win = pygame.transform.scale(win, (150, 150))
Lose = pygame.image.load('assets/images/sed.png')
Lose = pygame.transform.scale(Lose, (150, 150))
Cat = pygame.image.load('assets/images/cat.png')
Cat = pygame.transform.scale(Cat, (150, 150))
Music = pygame.mixer.Sound('assets/sound/an_amazing_and_beautiful_day_where_nothing_is_wrong.ogg')
Sound_channel = Music.play()
Lose_Sound = pygame.mixer.Sound('assets/sound/fart.mp3')
Winner = pygame.mixer.Sound('assets/sound/mony.mp3')
Sad = pygame.mixer.Sound('assets/sound/moye.mp3')
Winner1 = pygame.mixer.Sound('assets/sound/rizz.mp3')
Saddest = pygame.mixer.Sound('assets/sound/hamter.mp3')
Lives = pygame.image.load('assets/images/heart.png')
Lives = pygame.transform.scale(Lives, (50, 50))

words = {
    'easy': ['python', 'hangman', 'game', 'player', 'coding'],
    'medium': ['apple', 'banana', 'orange', 'grape', 'melon'],
    'hard': ['elephant', 'rhinoceros', 'crocodile', 'giraffe', 'hippopotamus']
    } #different types of words, based on difficulty
def diff(): #function for difficulty
    while True: #loop
        print('Select the difficulty: (1) Easy (Miscellaneous) (2) Medium (fruits) (3) Hard (animals)')
        diffchosen = input("Enter the number corresponding to the difficulty you want to choose :)") 
        if diffchosen == '1':
            return 'easy'
        elif diffchosen == '2':
            return 'medium'
        elif diffchosen == '3':
            return 'hard'
        else:
            print("Invalid, Try again :(")
difficulty = diff() #a variable with the function
word_pool = words[difficulty] #the words to be guessed based on chosen difficulty
word = random.choice(word_pool) #using random module to randomly select a word

guessed = set() #a set used to contain the letters which players has guessed

max_strikes = 6 #maximum number of wrong guesses

strikes = 0 #current strikes

game_over = False #currently the game is not over ;)

Wins = 0

Loses = 0

def draw(word, letters_guessed): #function to show words and stuff on interface  
    display_word = ' ' #empty string
    for letter in word: #for every letter in the word being guessed
        if letter in letters_guessed: #if the letter being guessed is correct
            display_word += letter + ' ' #add the letter to display with a space to make it look clean
        else:
            display_word += '_ '
    font = pygame.font.SysFont(None, 60) #font
    text = font.render(display_word, True, (0, 0, 0)) #render the font on screen
    screen.blit(text, (100, 400)) #display text on the screen 

    

def reset(): #restart the game
    global word, guessed, strikes, game_over
    word = random.choice(word_pool)
    guessed = set()
    strikes = 0 
    game_over = False
    Music.play()
    Saddest.stop()
    Winner.stop()

def heart(strikes): #shows the number of strikes or number of guesses left
    heart_rect = Lives.get_rect() #turn it into a rectangle
    x = 10
    y = 10
    for i in range(strikes):
        screen.blit(Lives, (x, y))
        x += heart_rect.width + 5

    





while True: #keeps the window open until closed by user
    
    for event in pygame.event.get(): #Used for user input
        if event.type == pygame.QUIT: #To quit the game
            pygame.quit()
            exit() #sys function
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
                letter = chr(event.key)
                if letter not in guessed: #check the set we created earlier
                    guessed.add(letter)
                    if letter not in word: #if letter does not match any letters of the word
                        strikes += 1 #wrong guess leads to this :(    
        elif event.type == pygame.KEYDOWN and game_over: #key for restarting
            if event.key == pygame.K_r:
                if strikes >= max_strikes:
                    Loses += 1
                    reset()
                if set(word) <= guessed:
                    Wins += 1 
                    reset()
                

    font_stats = pygame.font.Font(None, 20) #wins and loses
    text_wins = font_stats.render('Wins: ' + str(Wins), True, (0, 255, 0))
    text_loses = font_stats.render('Loses: ' + str(Loses), True, (255, 0, 0))   
           

    
    screen.blit(Background_Image, (0,0)) #display on screen
    screen.blit(Hang, (550, 110)) #display
    heart(max_strikes-strikes) #lives
    screen.blit(text_wins,(650, 20))   
    screen.blit(text_loses,(650, 60)) 
    if strikes>0 and not game_over: #when there is a strike 
        screen.blit(Stick_reaper, (5 + strikes * 50, 115)) #the reaper will appear and drag you to your death :>
    draw(word, guessed) #updating the display  to the current state

    if strikes >= max_strikes: #if you run out guesses, you lose :(
        game_over = True
        
    if set(word) <= guessed: #if you guess all the letters in word correctly, you win :)
        game_over = True


    
    
    if game_over:
        if set(word) <= guessed: #you guessed it :>
            screen.fill((0, 255, 0)) #gren color
            Winner.play()
            Sound_channel.stop()
            screen.blit(win, (250, 250))
            font = pygame.font.Font('assets/font/GravediggerPersonalUse-K7ayW.ttf', 20) #downloaded font
            text = font.render('Congratulations, You have won, PRESS R TO RESTART', True, (0, 0, 255)) #Winner
            screen.blit(text, (100, 100)) #text location on display
        if strikes >= max_strikes: #you lost
            Saddest.play()
            screen.blit(Stick_hang, (671, 160)) #you got hanged :(
            Sound_channel.stop()
            font = pygame.font.Font('assets/font/GravediggerPersonalUse-K7ayW.ttf', 20) #downloaded font
            text = font.render('You lose, The word was  ' + word, True, (255, 0, 0))#Loser :>
            text1 = font.render('Press R to restart', True, (255, 0, 0)) 
            screen.blit(text, (100, 100)) #text locations on display
            screen.blit(Lose, (50, 150))
            screen.blit(text1, (100, 550))
            screen.blit(Cat, (250, 150))
            

    pygame.display.update() #update the game in realtime, every second
    clock.tick(60) #frame rate, 60 fps ;)