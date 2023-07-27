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

    stop music fadeout 1.0
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

    show katie
    with dissolve

    "???" "OMG OMG OMG, Sadie, look!"

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


    hide chris
    with dissolve

    "All 23 campers lined up on the dock, most teens arguing about who'd stand beside you."
    "Of course Chris put you in the direct center to stand out the most."
    "The people who ended up standing beside you were a tanned boy with a dark green shirt, on the other side a blonde with a mini skirt and in front of you crouching, a brunette boy with a light yellow shirt."

    show chris
    with dissolve

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
    
    
        #end of first scene, we're coming up to the campfire site where Chris introduces the game

    hide chris

    "You huff in annoyance, dragging yourself out of the water, scrunching up your shirt to get as much water out as possible."
    "You can feel other peoples' stares, but you're already used to this."
    "You are a celebrity after all."

    "???" "Hi, [name]. I got your luggage from the water so you don't lose it."
    "You look up. The blonde from the dock is handing you your suitcase."

    show lindsay

    us "Oh, hey. Thanks for that."
    "???" "Yeah, no problem. Us models need to look our for each other after all."
    "You smile at that and shake your head."
    linds "I'm Lindsay, want to walk to the fire pit together?"
    us "Sure thing, Lindsay."

    "It was a short walk, instead of talking to the blonde, you used the remaining minute walking looking around."
    "It looks worse than what you were promised."
    "But it will do for the pay."

    linds "So, [name]. I've seen you on so many shows, I've admired you since I little."
    us "Aww, that's nice to hear, Lindsay. I am a role model for many children after all..."


    scene campfire

    "You remember when the last show you were at wasn't a big success, but that wasn't your fault."
    "That's why as your punishment, your next gig was a rundown camp."
    "But the manager talked about Chris being a star in his own way as well. That he has some special charm."
    "Whatever that means..."


    show lindsay

    linds "Want to sit next to me, [name]?"
    us "Uh, sure."

    hide lindsay

    "You sit down on a stump, seeing many different kinds of people around you."

    show duncan
    "You accidentally make eye contact with a guy in a green mohawk and he winks at you."
    "You look away as fast as you looked at him and hear Chris cough to get all of your attention."
    hide duncan

    "When everyone quieted down, he continued speaking."
    show chris

    chris "This… is camp Wawanakwa."
    chris "Your home for the next eight weeks."
    chris "The campers sitting around you will be your cabinmates, your competition, and maybe even your friends. "
    chris "The camper who manages to stay on Total Drama Island the longest without getting voted off will win $100,000!"

    show chris at left
    show duncan at right

    duncan "‘Scuse me. What will the sleeping arrangements be?"
    show heather at center
    duncan "Because I’d like to request a bunk under her."
    heather "They’re not co-ed, are they?"

    chris "No. Girls get one side of each cabin and dudes, get the other."

    hide duncan
    hide heather

    show katie at right
    katie "I have to live with Sadie or I'll die!"

    show sadie at center
    sadie "And I’ll break out in hives. It’s true."

    hide chris
    hide sadie
    hide katie

    show gwen at right
    gwen "This cannot be happening..."

    show owen at center
    owen "Aww, c’mon guys! It’ll be fun! It’s like a big sleepover!"

    show tyler at left
    tyler "At least you don’t have to sleep next to him."


    hide owen
    hide gwen
    hide tyler


    show chris
    chris "Here’s the deal. We’re gonna split you into two teams. If I call your name out, go stand over there."
    show gwen at right
    chris "Gwen."
    show trent at left
    chris "Trent." 
    hide gwen
    show heather at right
    chris "Heather."
    hide trent
    show cody at left
    chris "Cody."
    hide heather
    show lindsay at right
    chris "Lindsay."
    hide cody
    show beth at left
    chris "Beth." 
    hide lindsay
    show katie at right
    chris "Katie." 
    hide beth
    show owen at left
    chris "Owen." 
    hide katie
    show leshawna at right
    chris "Leshawna."
    hide owen
    show justin at left
    chris "Justin."
    hide leshawna
    show noah at right
    chris "And… Noah."
    
    chris "From this moment on, you are officially known as… The Screaming Gophers!"

    hide chris
    hide noah
    hide justin
    show owen

    owen "Yeah! I'm a Gopher! Woohoo!"
    show katie at right

    katie "Wait. What about Sadie?"

    hide katie
    hide owen
    show chris

    chris "The rest of you over here."
    show geoff at left
    chris "Geoff."
    show bridgette at right
    chris "Bridgette."
    hide geoff
    show dj at left
    chris "DJ."
    hide bridgette
    show tyler at right
    chris "Tyler."
    hide dj
    show sadie at left
    chris "Sadie."
    hide tyler
    show izzy at right
    chris "Izzy."
    hide sadie
    show courtney at left
    chris "Courtney."
    hide izzy
    show ezekiel at right
    chris "Ezekiel."
    hide courtney
    show duncan at left
    chris "Duncan."
    hide ezekiel
    show eva at right
    chris "Eva"
    hide duncan
    show harold at left 
    chris "And... Harold!"
    hide eva
    hide harold
    chris "Move, move, move, move!"

    hide chris

    show sadie
    sadie "But Katie’s a Gopher! I have to be a Gopher!"
    show courtney at left 
    court "Sadie, is it? Come on. It’ll be okay."
    sadie "This is so unfair! I miss you, Katie!"
    show katie at right
    katie "I miss you too!"

    hide courtney 
    hide sadie
    hide katie

    show chris
    chris "You guys will officially be known as… The Killer Bass!"

    show harold at right 
    harold "It’s awesome. It’s like… Amazing."

    hide harold
    chris "All right, campers."
    chris "You and your team will be on camera in all public areas during this competition."
    

    "You interrupt Chris with waving your arm back and forth."
    us "Didn't you forget something?"
    chris "Aww, I didn't want to tell them later until the challenges began."
    
    "You look at Chris annoyed."
    "You don't even know on which team you're on right now!"

    chris "Well, since [name] is our special guest, they arrived here last minute."
    chris "They weren't originally a part of this game, but their manager wanted us to include them!"
    chris "So, after some thinking, we've decided upon ourselves that [name] will be part of the losing team."
    chris "But since we haven't began the challenge yet, you can decide on which team you want to be."

    chris "Will it be the Screaming Gophers... or the Killer Bass?"

    show heather at left
    heather "What?!"
    heather "You can't just do that!"
    heather "That's unfair!"

    chris "Rules are rules."
    hide heather
    chris "So. Choose who you want to help in today's challenge."



    menu:
        "The Screaming Gophers":
            jump choice1_SG

        "The Killer Bass":
            jump choice1_KB


    label choice1_SG:
        $ team = 'g'
        chris "[name] is now a Gopher!"

        jump choice1_done

    label choice1_KB:
        $ team = "b"
        chris "[name] is now a Bass!"

        jump choice1_done

    label choice1_done:
        chris "Anyway, let's continue on."



    # This ends the game.

    return
