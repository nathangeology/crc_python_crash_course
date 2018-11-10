# Lesson 6 writing .py files instead of jupyter notebooks

# IF RUNNING IN SPYDER SET BREAKPOINTS USING F12

if __name__ == '__main__': # this line ensures we are in the main application
    # Start your game here, replace enter some text with a question you want to ask the player
    game_over = False
    tries = 0
    while not game_over:
        tries += 1
        some_text = input('Enter some text: ') # allows player to enter some text or a number
        print('You entered {}'.format(some_text))
        # Check the input with an if statement
        if some_text == '':
            print('do something')
        else:
            print('do something else')

        if tries == 5:
            game_over = True
            print('You took too long, game over')

        # Your task: make a 2-3 step text game with the starting code up above and have your neighbor try playing it