from random import randint

import pygame  # For everything

pygame.init()

window = pygame.display.set_mode([1000, 1000]) # Window
fly = pygame.Rect(randint(0, 950), randint(0, 950), 20, 20) # Fly
enemy = pygame.Rect(randint(0, 950), randint(0, 950), 20, 20) # The dark matter fly
player = pygame.Rect(500, 500, 50, 50) # Player Rect
x = 0 # Used as speed variables
y = 0
flyx = 0
flyy = 0
enemyx = 0
enemyy = 0

gameloop = True # For the game loop
brakes = False # If the person is going into standby

day_length = 5000 # Day length

input("Welcome to the fly catching simulator! Your objective is to catch flies. [ENTER FOR THE HOW TO PLAY MANUAL]")
input("""
HOW TO PLAY
-----------
Use the arrow keys to accelerate
Collect flies (brown)
Avoid dark matter flies
Collect as many flies as you can in one day [PRESS ENTER TO START THE GAME]
""") # Explanation on how to play

tax_amt = randint(1, 20) # Tax (collected at the end of the game

money = 0 # How much the person made (1 fly = 1 money)

fly_counter = 0 
while gameloop: # Game Loop
    flyx = randint(-5, 5)
    flyy = randint(-5, 5)
    enemyx = randint(-10, 10)
    enemyy = randint(-10, 10)
    window.fill((10, 230, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # All of the events
            gameloop = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]:
                y += 1
            elif key[pygame.K_UP]:
                y -= 1
            elif key[pygame.K_RIGHT]:
                x += 1
            elif key[pygame.K_LEFT]:
                x -= 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not brakes:
                brakes = True
            elif brakes:
                brakes = False
    if not brakes: # Moves if brakes are not active
        player.x += x
        player.y += y

    if player.x < -40: # Prevents the player from going out of bounds (in a cool way)
        player.x = 1000
    if player.y < -40:
        player.y = 1000
    if player.x > 1000:
        player.x = -40
    if player.y > 1000:
        player.y = -40

    if fly.x < -40: # Prevents the fly from going out of bounds (in a cool way)
        fly.x = 1000
    if fly.y < -40:
        fly.y = 1000
    if fly.x > 1000:
        fly.x = -40
    if fly.y > 1000:
        fly.y = -40

    if enemy.x < -40: # Prevents the fly from going out of bounds (in a cool way)
        enemy.x = 1000
    if enemy.y < -40:
        enemy.y = 1000
    if enemy.x > 1000:
        enemy.x = -40
    if enemy.y > 1000:
        enemy.y = -40

    fly.x += flyx
    fly.y += flyy

    enemy.x += enemyx
    enemy.y += enemyy

    if fly.x > (player.x - 25) and fly.x < (player.x + 25):
        if fly.y > (player.y - 25) and fly.y < (player.y + 25):
            if x > 2 or x < -2 or y > 2 or y < -2:
                print("You got one fly!")
                fly_counter += 1
                print("Total fly count: " + str(fly_counter))
                fly.x = randint(0, 950)
                fly.y = randint(0, 950)

    if enemy.x > (player.x - 25) and enemy.x < (player.x + 25):
        if enemy.y > (player.y - 25) and enemy.y < (player.y + 25):
            print("Oh noes! A dark matter fly has rescued its friend!")
            fly_counter -= 1
            print("Total fly count: " + str(fly_counter))
            enemy.x = randint(0, 950)
            enemy.y = randint(0, 950)

    pygame.draw.rect(window, (88, 57, 39), fly)
    pygame.draw.rect(window, (255, 0, 0), player)
    pygame.draw.rect(window, (81, 31, 102), enemy)
    pygame.display.flip()

    day_length -= 1
    if day_length == 0:
        gameloop = False

    pygame.time.delay(10)

money = fly_counter
money -= tax_amt
input("""
DAY SUMMARY:
------------
Flies caught:
""" + str(fly_counter) + """
-------------
Money made (subtotal):
""" + str(money + tax_amt) + """
----------------------
Tax:
""" + str(tax_amt) + """
----
TOTAL:
""" + str(money) + """
---------
PRESS ENTER WHEN DONE READING THE SUMMARY (or boasting about how many flies you caught)
""")
if money > 0:
    input("Congrats! You made profit. That means you won! You can try again and see if you can make more profit!")
else:
    input("Whoops. You lost. Try again and see if you can make profit!")

