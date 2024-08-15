# Set a flag.
init python:
    from random import randint




define p = Character("Mr. Farmer", color="00ff44")
define v = Character("Vendor", color="5c5c5e")
define n = Character("Narrator", color="ffffff")
define b = Character("Boss", color="770699")


# FARM LEVEL

label start:

    $ tutorial_done = False
    $ first = False
    $ second = False
    $ third = False

    # Initialize a variable.
    $ health_points = 3

    scene bg farm

    n "hello"
    n "welcome to your farm!"

    show pelaaja oikea

    n "this is you!"
    p "i'm created in a new Ren'Py game."
    p "This is me speaking to me"

    show vendori vasen at right
    show pelaaja oikea at left

    v "Hello im the vendor!"
    v "I have one question for you"

    p "OK tell me!"


label choices:

    v "Do you want to continue farming?"
    v "OR..."
    v "Embark on a journey through time and space and fight monsters"
    p "I'm not worthy hero!"
    v "Maybe you are... maybe you aren't. That remains to be seen..."
    v "If you succeed collecting some seeds, i can provide help to defeat the great BOSS"
    v "How is it gonna be?"
menu:
    "Continue farming, please":
        jump choices1_a
    "Embark on a great journey":
        #jump choices1_b
        jump bosslevel
    # This ends the game.

label choices1_a:
    v "You made your choice!"
    v "Enjoy farming life"
    v "Are you sure ?"
menu:
    "Yes":
        jump farming
    "No":
        jump choices

label choices1_b:
    v "...."
    v "Why did you make it so hard"
    v "Anyways.. let's go"
    v "I almost forgot"
    v "Here take this hoe with you"
    jump not_farming

label not_farming:
    hide pelaaja oikea
    n "He left to go on his chosen path..."
    jump straight_line


label farming:
    show pelaaja vasen at left
    p "LETS FARM"
    show vendori vasen at right
    v "Isn't there something else you would want to do?"

menu:
    "Yes":
        jump choices1_b
    "No":
        jump choices1_a


label straight_line:
    scene bg road
    n "You see a straight road with a forest in the end..."
    n "Do you want to enter the forest"

menu:
    "Yes (Starts tutorial level)":
        jump tutorial
    "No (Goes back to farm)":
        jump farming
    

# TUTORIAL LEVEL

label tutorial:
    scene black
# https://unsplash.com/photos/photo-of-pathway-between-trees-Xepovj4Dwd8?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash
    n "Well here you are.."
    show pelaaja perus at left
    p "Well here i truly am..."
    p "A bit frightened to be frank"
    n "As the vendor said if you complete the journey you gain seeds to farm!"
    n "We'll start slow, here is the most basic things that you must overcome"
    show hamis melee at right
    n "If you see a dark coloured spider, it is melee, and can only bite you!"
    show hamis melee at center
    n "Hit it with your hoe!"
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
    n "Good job!"
    show pelaaja perus at left
    n "If you see a green coloured spider, it is ranged ... so beware of the web attack!"
    show hamis ranged at right
    n "You can also gain ranged attack through harvested crops"
    n "Try to throw it with mud!"
    ### ATTACK BLOCK
    $ enemy_name = "RANGED SPIDER"
    $ hamis_ranged = 2
    while hamis_ranged > 0:
        $ rand = randint(0,5)
        "Your hitpoints [health_points], [enemy_name]'s [hamis_ranged]"
        menu: 
            "Try to hit":
                if rand % 2 == 0:
                    $ hamis_ranged -= 1
                    "HIT"
                else:
                    "MISS!!!"
    hide hamis melee
    ###
    n "This completes the tutorial... you gain your first seed"
    n "Do you want to play the tutorial again?"
menu:
    "Yes":
        jump tutorial
    "No":
        jump farmb

# FARM AFTER TUTORIAL

label farmb:
    scene bg farm
    show pelaaja perus at left
    show vendori vasen at right
    v "Well you made it back..."
    v "Now the real challenge awaits..."
    v "But first go and plant the seed"
menu:
    "Go plant":
        jump farmc
    "I don't want to":
        return

label farmc:
    scene bg farm
    show pelaaja perus at left
    show vendori vasen at right
    v "Very good..."
    jump level1melee

label farmd:
    scene bg farm
    show pelaaja perus at left
    show vendori vasen at right
    v "Very good..."
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
    n "Welldone!, do you wish to continue?"
    menu:
        "Yes":
            if first and not second:
                jump level1ranged
            elif first and second:
                jump level1melee
            else:
                $ first, second, third = False, False, False
                jump farmd
        "No":
            $ first, second, third = False, False, False
            jump farm

    jump farmd

label bosslevel:
    scene blue
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
    jump endscene
    

label ripscene:
    scene bg farm
    n "Now one of the plots is your own grave..."
    n "Better luck next time"
    return


label endscene:
    scene bg farm
    n "You saved your farm and the whole planet"
    n "... you indeed are the Hero Farmer!"
    return

