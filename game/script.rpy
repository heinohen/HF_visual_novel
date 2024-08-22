# Set a flag.
init python:
    from random import randint




define p = Character("Mr. Farmer", color="00ff44")
define v = Character("Vendor", color="5c5c5e")
define n = Character("Narrator", color="ffffff")
define b = Character("Boss", color="770699")

transform plot:
    xalign 0.16 yalign 0.60

transform vendor_pos:
    xalign 0.36 yalign 0.30 zoom 0.2

transform vendor_perus_pos:
    zoom 0.8

transform pelaaja_perus_pos:
    zoom 0.8

transform boss_exit1:
    xalign 0.70 yalign 0.30 zoom 0.5

transform boss_exit2:
    xalign 0.80 yalign 0.20 zoom 0.3

transform boss_exit3:
    xalign 0.90 yalign 0.10 zoom 0.1

transform endscene_pelaaja:
    xalign 0.40 yalign 0.45 zoom 0.2

transform endscene_vendori:
    xalign 0.60 yalign 0.45 zoom 0.15


# FARM LEVEL

label start:

    $ tutorial_done = False
    $ level1_done = False
    $ first = False
    $ second = False
    $ third = False

    # Initialize a variable.
    $ health_points = 5

    scene bg farm

    n "HELLO"
    n "WELCOME TO YOUR FARM!"

    show pelaaja oikea

    n "THIS IS YOU!"
    p "This is me!"
    p "So this is where i live"

    show vendori vasen at right,vendor_perus_pos
    show pelaaja oikea at left

    v "Hello im the vendor!"
    v "There is evil lurking in the forests"
    v "It is threatning the whole existence!"
    p "Wow... i better not go in to the forest then!"
    p "Im only here to farm"
    v "Be that as it may, but if you want seeds to plant..."
    v "YOU HAVE TO GO!"
    v "So i have one question for you..."
    p "OK tell me!"


label choices:

    v "Do you want to starve to death with no seeds?"
    v "OR..."
    v "Embark on a journey through time and space and fight monsters"
    p "I'm not worthy hero!"
    v "Maybe you are... maybe you aren't. That remains to be seen..."
    v "If you succeed collecting some seeds, i can provide help to defeat the great BOSS"
    v "How is it gonna be?"
menu:
    "Stay at the farm, please":
        jump farming
    "Embark on a great journey":
        #jump choices1_b
        jump straight_line
    # This ends the game.

label choices1_a:
    v "You made your choice!"
    v "Enjoy farming life"
    v "Are you sure ?"
menu:
    "Yes":
        hide vendori vasen
        jump farming
    "No":
        jump choices

label choices1_b:
    v "...."
    v "Why did you make it so hard"
    v "Anyways.. let's go"
    if not tutorial_done:
        jump not_farming
    else:
        jump level1melee

label not_farming:
    hide pelaaja oikea
    n "HE LEFT TO GO ON HIS CHOSEN PATH..."
    jump straight_line


label farming:
    show bg farm
    hide vendori vasen
    show pelaaja plant at plot
    p "Hmm, i don't seem to have any seeds to plant"
    p "Where did that vendor go..."
    show vendori vasen at right,vendor_perus_pos
    v "Thats what i told you..."
    hide pelaaja plant
    show pelaaja perus at left
    v "The seeds are in the forest!"
    v "So will you go and get some?"
    if tutorial_done and level1_done:
        menu:
            "Go farm!":
                jump farming
            "Go to the forest again":
                jump level1melee
            "Go fight THE BOSS (if you think you are ready)":
                jump bosslevel


menu:
    "Yes":
        jump choices1_b
    "No":
        jump choices1_a


label straight_line:
    scene bg road
    n "YOU SEE A STRAIGHT ROAD WITH A FOREST IN THE END..."
    n "DO YOU WANT TO ENTER THE FOREST"

menu:
    "Yes":
        $ tutorial_done = True
        jump tutorial
    "No":
        $ tutorial_done = False
        jump farmb
    

# TUTORIAL LEVEL

label tutorial:
    scene black
# https://unsplash.com/photos/photo-of-pathway-between-trees-Xepovj4Dwd8?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash
    n "WELL HERE YOU ARE"
    n "IN THE DARK FOREST"
    show pelaaja perus at left
    p "Well here i truly am..."
    p "A bit frightened to be frank"
    n "AS THE VENDOR SAID, IF YOU COMPLETE THE JOURNEY YOU GAIN SEEDS TO FARM!"
    n "WE'LL START SLOW, HERE IS THE MOST BASIC THINGS THAT YOU MUST OVERCOME"
    show hamis melee at right
    n "IF YOU SEE A DARK COLOURED SPIDER, IT IS MELEE, AND CAN ONLY BITE YOU"
    show hamis melee at center
    n "HIT IT WITH YOUR HOE!"
    show pelaaja hyokki at center
    ### ATTACK BLOCK
    $ hamis_health = 1
    $ enemy_name = "MELEE SPIDER"
    while hamis_health > 0:
        $ rand = randint(0,5)
        $ enemy_rand = randint(0,10)
        "Your hitpoints [health_points], [enemy_name]'s [hamis_health]"
        menu: 
            "Try to hit":
                if rand % 2 == 0:
                    $ hamis_health -= 1
                    "HIT"
                    hide hamis melee
                else:
                    "MISS!!!"
    ###
    n "GOOD JOB!"
    show pelaaja perus at left
    n "IF YOU SEE A GREEN COLOURED SPIDER, IT IS RANGED MONSTER"
    n "SO BEWARE OF THE WEB ATTACK"
    show hamis ranged at right
    n "YOU CAN EVENTUALLY GAIN RANGED ATTACK YOURSELF THROUGH HARVESTED CROPS..."
    n "IF YOU MAKE IT THAT FAR..."
    ### ATTACK BLOCK
    $ enemy_name = "RANGED SPIDER"
    $ hamis_ranged = 2
    while hamis_ranged > 0:
        $ rand = randint(0,5)
        "Your hitpoints [health_points], [enemy_name]'s [hamis_ranged]"
        menu: 
            "Try to hit":
                show pelaaja hyokki at right
                if rand % 2 == 0:
                    $ hamis_ranged -= 1
                    "HIT"
                    show pelaaja perus at left
                else:
                    "MISS!!!"
                    show pelaaja perus at left

    hide hamis melee
    ###
    n "THIS COMPLETES THE TUTORIAL"
    n "YOU GAIN YOUR FIRST SEED!"
    n "DO YOU WANT TO RETURN TO THE FARM AND CONTINUE?"
menu:
    "Yes (goes to farm)":
        jump farmb
    "No (plays tutorial again)":
        jump tutorial

# FARM AFTER TUTORIAL

label farmb:
    scene bg farm
    show pelaaja perus at left

    if not tutorial_done:
        # TUTORIAL NOT YET COMPLETED
        p "Huh, that was scary road..."
        p "I cannot fanthom what that forest would be like..."
        show vendori vasen at right
        v "Why are you back?"
        p "I completed the road section"
        v "That was not the task..."
        v "Go back and come to when you get the seed!"
        jump straight_line
    else:
        show vendori vasen at right
        v "Well you made it back..."
        v "Go and plant the seed"
        jump farmc


label farmc:
    scene bg farm
    show pelaaja plant at plot
    show vendori vasen at vendor_pos
    $ health_points = 5
    v "Very good..."
    v "NOW the first real test awaits you in the forest"
    v "There you will find a path along the river"
    v "And definately more spiders"
    v "But if you make it through to the source of the river"
    v "You gain yet another seed!"
    v "Are you ready?"
menu:
    "Yes":
        jump level1melee
    "No":
        jump farming
        

label farmd:
    scene bg farm
    show pelaaja perus at left
    show vendori vasen at right,vendor_perus_pos
    v "Very good..."
    v "You made it back"
    v "What do you want to do next?"
menu:
    "Go farm!":
        jump farming
    "Go to the forest again":
        jump level1melee
    "Go fight THE BOSS (if you think you are ready)":
        jump bosslevel


# LEVEL 
#https://unsplash.com/photos/flowing-river-between-tall-trees-7BjhtdogU3A?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash



# REWORK THE LEVEL HEALTH
label level1melee:
    scene bg level
    p "Whats this"
    show pelaaja perus at left
    p "Where am i now..."
    p "Oh no...."
    show hamis melee at right
    ### ATTACK BLOCK
    $ hamis_health = 1
    $ enemy_name = "MELEE SPIDER"
    $ enemy_dead = False
    while hamis_health > 0:
        $ rand = randint(0,5)
        $ enemy_rand = randint(0,10)
        "Your hitpoints [health_points], [enemy_name]'s [hamis_health]"
        menu: 
            "Try to hit":
                show pelaaja hyokki at right
                if rand % 2 == 0:
                    $ hamis_health -= 1
                    "HIT"
                    if hamis_health == 0:
                        $ enemy_dead = True
                        if first:
                            $ third = True
                        $ first = True
                        hide hamis melee
                        jump level1b
                else:
                    "MISS!!!"
                show pelaaja perus at left
        "[enemy_name]'s TURN"
        if enemy_dead == False:
            show hamis melee at left
            if enemy_rand % 2 == 0:
                $ health_points -= 1
                "IT BIT YOU"
                if health_points == 0:
                    jump ripscene # YOU DIED
                    return
            else:
                "MISS"
        show hamis melee at right
    ###
label level1ranged:
    scene bg level
    p "Lets move on"
    show pelaaja perus at left
    p "Whats that sound..."
    p "Oh..."
    show hamis ranged at right
    ### ATTACK BLOCK
    $ ranged_health = 1
    $ enemy_name = "RANGED SPIDER"
    $ enemy_dead = False
    while ranged_health > 0:
        $ rand = randint(0,5)
        $ enemy_rand = randint(0,10)
        "Your hitpoints [health_points], [enemy_name]'s [ranged_health]"
        menu: 
            "Try to hit":
                show pelaaja hyokki at right
                if rand % 2 == 0:
                    $ ranged_health -= 1
                    "HIT"
                    if ranged_health == 0:
                        $ enemy_dead = True
                        hide hamis ranged
                        $ second = True
                        jump level1b
                else:
                    "MISS!!!"
                show pelaaja perus at left
        "[enemy_name]'s TURN"
        if enemy_dead == False:
            if enemy_rand % 2 == 0:
                "WEB ATTACK"
                $ health_points -= 1
                "HIT"
                if health_points == 0:
                    jump ripscene # YOU DIED
                    return
            else:
                "MISS"
        show hamis ranged at right
    ###

label level1b:
    scene black
    n "Well done!, do you wish to continue?"
    $ print(first, second, third)
    menu:
        "Yes":
            if first and not second:
                jump level1ranged
            elif first and second and not third:
                jump level1melee
            elif first and second and third:
                $ print('should jump to farm...')
                $ first, second, third = False, False, False
                $ level1_done = True
                jump farmd
        "No":
            $ first, second, third = False, False, False
            jump farming
            
label bosslevel:
    scene black
    show boss perus at right
    show pelaaja perus at left
    b "HELLO"
    p "um.... hi"
    p "who or what are you?"
    b "I AM THE RULER OF ALL THE WORLDS..."
    b "PREPARE TO DIE!"
    show boss attack at right
    $ count = 5
    
    while count > 0:

        "T-minus [count]."

        $ count -= 1

    "BYE!"
    $ health_points = 5
    $ enemy_health = 3
    $ enemy_name = "THE BOSS"
    $ enemy_dead = False
    while enemy_health > 0:
        $ rand = randint(0,5)
        $ enemy_rand = randint(0,10)
        "Your hitpoints [health_points], [enemy_name]'s [enemy_health]"
        menu: 
            "Try to hit":
                show pelaaja hyokki at right
                if rand % 2 == 0:
                    $ enemy_health -= 1
                    "HIT!!!"
                    if enemy_health == 0:
                        $ enemy_dead = True
                        hide boss attack
                        $ second = True
                        jump bossdialogue
                else:
                    "MISS!!!"
                show pelaaja perus at left
        "[enemy_name]'s TURN"
        if enemy_dead == False:
            show boss attack at left
            "BOSS ATTACK"
            if enemy_rand % 2 == 0:
                $ health_points -= 1
                "HIT"
                if health_points == 0:
                    jump ripscene # YOU DIED
                    return
            else:
                "MISS"
        show boss attack at right
    ###

label bossdialogue:
    show boss perus at right
    show pelaaja perus at left
    b "You've defeated me..."
    b "For now!"
    show boss perus at boss_exit1
    b "BUT I SHALL RETURN"
    show boss perus at boss_exit2
    b "You better be ready for it!"
    show boss perus at boss_exit3
    b "MUAHAHAHAHA"
    hide boss perus
    show pelaaja perus at center
    p "Well, now i can farm in peace i hope..."
    jump endscene


label ripscene:
    scene bg farm
    n "Now one of the plots is your own grave..."
    n "Better luck next time"
    return


label endscene:
    scene bg farm
    show pelaaja perus at endscene_pelaaja
    show vendori vasen at endscene_vendori
    n "The boss is defeated!"
    show pelaaja oikea at left, pelaaja_perus_pos
    show vendori vasen at right, vendor_perus_pos
    v "Well done, you truly are the HERO FARMER!"
    p "Thanks a lot, hopefully he doesn't come back like he told..."
    return

