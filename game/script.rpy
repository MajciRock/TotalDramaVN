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

    chris "At the dramatic campfire ceremony, where each week, all but one camper will receive a marshmallow."

    show chris

    chris "In the end, only one will be left standing and will be rewarded with cheesy tabloid fame and a small fortune, which let’s face it, they’ll probably blow in a week."
    chris "To survive, they’ll have to battle… "
    chris "Black flies, grizzly bears…"
    chris "Disgusting camp food…"
    chris "And each other."
    chris "Every moment will be caught on one of the hundreds of cameras situated all over the camp. "

    scene dock
    with dissolve
    
    show chris happy
    
    chris "Who will crumble under the pressure?"
    chris "Find out here, right now, on Total. Drama. Island!"



        #end of introduction, the character gets introduced

    scene island

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

    chris "Before we continue, I want to introduce you all to a very special guest, you know them, you love them, this is probably the only chance you have in actually meeting them face to face!"
    chris "Famous teen star [name]!"

    us "Hello, Canada!"

    "You yell out while waving towards the camera."
    "You can notice a fat guy pushing all the people nearby to get to you."

    show owen

    "He shakes your hand with pure excitement, radiating so much joy."
    "???" "Oh my god! [name]!"
    "???" "It's an honour to have you here, dude-"
    "???" "I-i-i mean-"

    show owen at left
    show heather at right

    "???" "He means that he doesn't know how to talk to celebrities."
    heather "I'm Heather, by the way."

    


    



    # This ends the game.

    return
