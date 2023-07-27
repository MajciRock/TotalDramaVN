# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.






define chris = Character("Chris")
define chef = Character("Chef")
define ez = Character("Ezekiel")
define noah = Character("Noah")
define justin = Character("Justin")
define katie = Character("Katie")
define tyler = Character("Tyler")
define cody = Character("Cody")
define beth = Character("Beth")
define sadie = Character("Sadie")
define court = Character("Courtney")
define harold = Character("Harold")
define eva = Character("Eva")
define trent = Character("Trent")
define bridge = Character("Bridgette")
define linds = Character("Lindsay")
define dj = Character("DJ")
define izzy = Character("Izzy")
define geoff = Character("Geoff")
define leshawna = Character("Leshawna")
define duncan = Character("Duncan")
define heather = Character("Heather")
define gwen = Character("Gwen")
define owen = Character("Owen")

define us = Character("[name]")

    # We still need to create our own character user, but for that we need to add our name as well.



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

            
    scene dock

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

            
    show chris
    # These display lines of dialogue.

    chris "Yo! We’re comin’ at you live from Camp Wawanakwa, somewhere in Muskoka, Ontario!"
    chris "I’m your host, Chris McLean." 
    chris "Dropping season one of the hottest new reality show on television right now!"
    chris "Here's the deal."
    chris "Twenty-two campers have signed up to spend eight weeks right here at this crummy old summer camp."
    chris "They’ll compete in challenges against each other, then have to face the judgment of their fellow campers. "
    chris "Every three days, one team will either win a reward or watch one of their team members walk down the Dock of Shame, take a ride on the loser boat, and leave Total Drama Island for good."
    chris "Their fate will be decided here"

    scene campfire
    with dissolve

    show chris happy
    with dissolve

    chris "At the dramatic campfire ceremony, where each week, all but one camper will receive a marshmallow."

    show chris
    with dissolve

    chris "In the end, only one will be left standing and will be rewarded with cheesy tabloid fame and a small fortune, which let’s face it, they’ll probably blow in a week."
    chris "To survive, they’ll have to battle… "
    chris "Black flies, grizzly bears…"
    chris "Disgusting camp food…"
    chris "And each other."
    chris "Every moment will be caught on one of the hundreds of cameras situated all over the camp. "

    scene dock
    with dissolve
    
    show chris happy
    with dissolve
    
    chris "Who will crumble under the pressure?"
    chris "Find out here, right now, on Total. Drama. Island!"



        #end of introduction, the character gets introduced

    scene island
    with dissolve

    "You are a famous movie star who has been working in the film business since about seven."
    "Your first official role was when you played the main character of a Bisney film."
    "Even though it didn't go well, you've been acting in movies and TV shows alike since then."
    "Yesterday you got a call from your manager, something about a 'Chris McLean' hosting a tv show live."
    "At first you weren't interested until she told you how much the producers are paying just to get on the show."
    "Apart from the overbearing fans... surely it can't be that bad..."
    "Right?"

    
    python:
        name = renpy.input("What's the name of the movie star?")
        name = name.strip() or "Camper"
        

    scene dock
    show chris happy
    with dissolve

    chris "Before we continue, I want to introduce you all to a very special guest, you know them, you love them, this is probably the only chance you have in actually meeting them face to face!"
    chris "Famous teen star [name]!"

    us "Hello, Canada!"

    "You yell out while waving towards the camera."
    "You can notice a fat guy pushing all the people nearby to get to you."
    
    hide chris happy
    show owen
    with dissolve

    "He shakes your hand with pure excitement, radiating so much joy."
    "???" "Oh my god! [name]!"
    "???" "It's an honour to have you here, dude-"
    "???" "I-i-i mean-"
    
    show owen at right
    show heather at left
    with dissolve

    "???" "He means that he doesn't know how to talk to celebrities."
    heather "I'm Heather, by the way."

    "You could notice some people rolling their eyes at this."
    "But too much time hasn't passed until two new fans came running towards you, interrupting Heather."

    hide owen
    hide heather
    with dissolve

    "???" "OMG OMG OMG, Sadie, look!"

    show katie
    with dissolve
    sadie "OMG, Katie. I know!"

    show sadie at left
    show katie at right
    with dissolve

    "Katie & Sadie" "It's super duper nice to meet you, [name]!"

    "They squeal so loudly that you had to place your hands on top of your ears, in fear that your eardrums might bleed out."



    
    show chris at center
    with dissolve

    "Chris taps on his wrist, indicating we have to move along and dismisses both girls to stand beside you."
    
    hide sadie
    hide katie
    with dissolve

    chris "I know how impatient you all are, especially because you've met another special celebrity just now."
    chris "But we need a group photo for the promos."
    chris "Everyone at the end of the dock!"


    show dock 
    with dissolve

    "All 23 campers lined up on the dock, most teens arguing about who'd stand beside you."
    "Of course Chris put you in the direct center to stand out the most."
    "The people who ended up standing beside you were a tanned boy with a dark green shirt, on the other side a blonde with a mini skirt and in front of you crouching, a brunette boy with a light yellow shirt."

    chris "Okay!"
    chris "One, two, three."
    chris "Oops, forgot the lens cap!"
    chris "Okay, hold that pose!"
    chris "One! Tw- oh. No, wait. Card's full. Hang on."

    "???" "Come on man, my face is startin' to freeze!"

    chris "Got it. Okay, everyone say 'Wawanakwa!'"
    "Everyone"  "Wawanakwa!"

    "You could hear the dock giving up under you. All 23 of you fell into the icy cold water, swimming back to shore for dear life."
    "Chris was laughing at this, he was standing on a boat this whole time after all, not getting wet the slightest bit."

    chris "Okay guys. Dry off and meet me at the campfire pit in ten!"
    
    
    
    
    # This ends the game.

    return
