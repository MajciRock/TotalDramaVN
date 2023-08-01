# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.






transform slightleft:
    xalign 0.15
    yalign 1.0
 
transform slightright:
    xalign 0.85
    yalign 1.0  

define chris = Character("Chris")
define chef = Character("Chef")
define ez = Character("Ezekiel")
define noah = Character("Noah")
define just = Character("Justin")
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
define lesh = Character("Leshawna")
define duncan = Character("Duncan")
define heather = Character("Heather")
define gwen = Character("Gwen")
define owen = Character("Owen")

define us = Character("[name]")



#Beginning frienship level with all the characters from 0 to 10
#Every starting level if they're not a fan or don't know much about us starts with 3.
#The maximum starting level is 4.5 of a friendship.
#When the friend level reaches above 7.5 then relationships options can be possible.


default fri_ez = 3.0
if fri_ez > 7.5:
    default rel_ez = 0

default fri_noah = 3.6
if fri_noah > 7.5:
    default rel_noah = 0

default fri_just = 3.8
if fri_just > 7.5:
    default rel_just = 0

default fri_katie = 4.5
if fri_katie > 7.5:
    default rel_katie = 0

default fri_tyler = 3.3
if fri_tyler > 7.5:
    default rel_tyler = 0

default fri_cody = 4.5
if fri_cody > 7.5:
    default rel_cody = 0

default fri_beth = 4.0
if fri_beth > 7.5:
    default rel_beth = 0

default fri_sadie = 4.5
if fri_sadie > 7.5:
    default rel_sadie = 0

default fri_court = 3.5
if fri_court > 7.5:
    default rel_court = 0

default fri_harold = 4.0
if fri_harold > 7.5:
    default rel_harold = 0

default fri_eva = 3.5
if fri_eva > 7.5:
    default rel_eva = 0

default fri_trent = 4.2
if fri_trent > 7.5:
    default rel_trent = 0

default fri_bridge = 3.6
if fri_bridge > 7.5:
    default rel_bridge = 0

default fri_linds = 4.4
if fri_linds > 7.5:
    default rel_linds = 0

default fri_dj = 3.5
if fri_dj > 7.5:
    default rel_dj = 0

default fri_izzy = 3.1
if fri_izzy > 7.5:
    default rel_izzy = 0

default fri_geoff = 3.4
if fri_geoff > 7.5:
    default rel_geoff = 0

default fri_lesh = 3.7
if fri_lesh > 7.5:
    default rel_lesh = 0

default fri_duncan = 3.2
if fri_duncan > 7.5:
    default rel_duncan = 0

default fri_heather = 3.3
if fri_heather > 7.5:
    default rel_heather = 0

default fri_gwen = 4.2
if fri_gwen > 7.5:
    default rel_gwen = 0

default fri_owen = 4.5
if fri_owen > 7.5:
    default rel_owen = 0


#Checking who is still left in the game
default game_ez = True
default game_noah = True
default game_just = True
default game_katie = True
default game_tyler = True
default game_cody = True
default game_beth = True
default game_sadie = True
default game_court = True
default game_harold = True
default game_eva = True
default game_trent = True
default game_bridge = True
default game_linds = True
default game_dj = True
default game_izzy = True
default game_geoff = True
default game_lesh = True
default game_duncan = True
default game_heather = True
default game_gwen = True
default game_owen = True




# The game starts here.

label start:

    stop music fadeout 1.0


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

            
    scene dock

    play music "waterfall.mp3" fadein 1.0 loop

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
    
    show owen at slightright
    show heather at slightleft
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

    show sadie at slightleft
    show katie at slightright
    with dissolve

    "Katie & Sadie" "It's super duper nice to meet you, [name]!"

    "They squeal so loudly that you had to place your hands on top of your ears, in fear that your eardrums might bleed out."



    show sadie with moveinleft:
        xalign 0.07
        yalign 1.0
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
    with dissolve

    "You huff in annoyance, dragging yourself out of the water, scrunching up your shirt to get as much water out as possible."
    "You can feel other peoples' stares, but you're already used to this."
    "You are a celebrity after all."

    "???" "Hi, [name]. I got your luggage from the water so you don't lose it."
    "You look up. The blonde from the dock is handing you your suitcase."

    show lindsay
    with dissolve

    us "Oh, hey. Thanks for that."
    "???" "Yeah, no problem. Us models need to look our for each other after all."
    "You smile at that and shake your head."
    linds "I'm Lindsay, want to walk to the fire pit together?"
    us "Sure thing, Lindsay."

    "It was a short walk, instead of talking to the blonde, you used the remaining minute walking looking around."
    "It looks worse than what you were promised."
    "But it will do for the pay."

    linds "So, [name]. I've seen you on so many shows, I've admired you since I was little."
    us "Aww, that's nice to hear, Lindsay. I am a role model for many children after all..."


    scene campfire
    with dissolve

    "You remember when the last show you were at wasn't a big success, but that wasn't your fault."
    "That's why as your punishment, your next gig was a rundown camp."
    "But the manager talked about Chris being a star in his own way as well. That he has some special charm."
    "Whatever that means..."


    show lindsay
    with dissolve

    linds "Want to sit next to me, [name]?"
    us "Uh, sure."

    hide lindsay
    with dissolve

    "You sit down on a stump, seeing many different kinds of people around you."

    show duncan
    with dissolve
    "You accidentally make eye contact with a guy in a green mohawk and he winks at you."
    "You look away as fast as you looked at him and hear Chris cough to get all of your attention."
    hide duncan
    with dissolve

    "When everyone quieted down, he continued speaking."
    show chris
    with dissolve

    chris "This… is camp Wawanakwa."
    chris "Your home for the next eight weeks."
    chris "The campers sitting around you will be your cabinmates, your competition, and maybe even your friends. "
    chris "The camper who manages to stay on Total Drama Island the longest without getting voted off will win $100,000!"

    show chris at slightleft with moveinleft
    show duncan at slightright
    with dissolve

    "???" "‘Scuse me. What will the sleeping arrangements be?"
    show heather at center
    with dissolve
    "???" "Because I’d like to request a bunk under her."
    heather "They’re not co-ed, are they?"

    chris "No. Girls get one side of each cabin and dudes, get the other."

    hide duncan
    hide heather
    with dissolve

    show katie at slightright
    with dissolve
    katie "I have to live with Sadie or I'll die!"

    show sadie at center
    with dissolve
    sadie "And I’ll break out in hives. It’s true."

    hide chris
    hide sadie
    hide katie
    with dissolve

    show gwen at slightright
    with dissolve
    "???" "This cannot be happening..."

    show owen at center
    with dissolve
    "???" "Aww, c’mon guys! It’ll be fun! It’s like a big sleepover!"

    show tyler:
        xalign 0.07
        yalign 1.0
    with dissolve
    tyler "At least you don’t have to sleep next to him."


    hide owen
    hide gwen
    hide tyler
    with dissolve

    show chris
    with dissolve
    chris "Here’s the deal. We’re gonna split you into two teams. If I call your name out, go stand over there."
    show gwen at slightright
    with dissolve
    chris "Gwen."
    show trent at slightleft
    with dissolve
    chris "Trent." 
    hide gwen
    show heather at slightright
    with dissolve
    chris "Heather."
    hide trent
    show cody at slightleft
    with dissolve
    chris "Cody."
    hide heather
    show lindsay at slightright
    with dissolve
    chris "Lindsay."
    hide cody
    show beth at slightleft
    with dissolve
    chris "Beth." 
    hide lindsay
    show katie at slightright
    with dissolve
    chris "Katie." 
    hide beth
    show owen at left
    with dissolve
    chris "Owen." 
    hide katie
    show leshawna at slightright
    with dissolve
    chris "Leshawna."
    hide owen
    show justin at slightleft
    with dissolve
    chris "Justin."
    hide leshawna
    show noah at slightright
    with dissolve
    chris "And… Noah."

    chris "From this moment on, you are officially known as… The Screaming Gophers!"

    hide chris
    hide noah
    hide justin
    show owen
    with dissolve

    owen "Yeah! I'm a Gopher! Woohoo!"
    show katie at slightright
    with dissolve

    katie "Wait. What about Sadie?"

    hide katie
    hide owen
    show chris
    with dissolve

    chris "The rest of you over here."
    show geoff at slightleft
    with dissolve
    chris "Geoff."
    show bridgette at slightright
    with dissolve
    chris "Bridgette."
    hide geoff
    show dj:
        xalign 0.10
        yalign 1.0
    with dissolve
    chris "DJ."
    hide bridgette
    show tyler at slightright
    with dissolve
    chris "Tyler."
    hide dj
    show sadie:
        xalign 0.10
        yalign 1.0
    with dissolve
    chris "Sadie."
    hide tyler
    show izzy at slightright
    with dissolve
    chris "Izzy."
    hide sadie
    show courtney at slightleft
    with dissolve
    chris "Courtney."
    hide izzy
    show ezekiel at slightright
    with dissolve
    chris "Ezekiel."
    hide courtney
    show duncan at slightleft
    with dissolve
    chris "Duncan."
    hide ezekiel
    show eva at slightright
    with dissolve
    chris "Eva"
    hide duncan
    show harold at slightleft
    with dissolve
    chris "And... Harold!"
    hide eva
    hide harold
    with dissolve
    chris "Move, move, move, move!"

    hide chris
    with dissolve

    show sadie
    with dissolve
    sadie "But Katie’s a Gopher! I have to be a Gopher!"
    show courtney at slightleft 
    with dissolve
    court "Sadie, is it? Come on. It’ll be okay."
    sadie "This is so unfair! I miss you, Katie!"
    show katie at slightright
    with dissolve
    katie "I miss you too!"

    hide courtney 
    hide sadie
    hide katie
    with dissolve

    show chris
    with dissolve
    chris "You guys will officially be known as… The Killer Bass!"

    show harold at slightright
    with dissolve
    harold "It’s awesome. It’s like… Amazing."

    hide harold
    with dissolve
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

    show heather at slightleft
    with dissolve
    heather "What?!"
    heather "You can't just do that!"
    heather "That's unfair!"

    chris "Rules are rules."
    hide heather
    with dissolve
    chris "So. Choose who you want to help in today's challenge."



    menu:
        "The Screaming Gophers":
            jump choice1_SG

        "The Killer Bass":
            jump choice1_KB


    label choice1_SG:
        $ team = 'g'

        $ fri_gwen += 0.1
        $ fri_beth += 0.1
        $ fri_trent += 0.1
        $ fri_just += 0.1
        $ fri_lesh += 0.1
        $ fri_noah += 0.1
        $ fri_katie += 0.2
        $ fri_heather += 0.2
        $ fri_linds += 0.2
        $ fri_owen += 0.2
        $ fri_cody += 0.2
        
        $ fri_sadie -= 0.1

        
        chris "[name] is now a Gopher!"
        "You can hear your team cheering and the other one letting out many awws."
        "You look at your team."

        hide chris
        show gwen at slightleft
        with dissolve

        "The teal haired girl smiles at you,"
        show trent at slightright
        with dissolve
        "and so does the boy who had the guitar earlier on himself."

        hide gwen
        hide trent
        with dissolve

        show lindsay
        with dissolve
        "Lindsay's jumping out of joy and clapping her hands while squealing."
        show owen at right 
        with dissolve
        owen "Woohooo!"
        owen "[name] is on our team! The party can start now!"

        hide lindsay
        hide owen
        with dissolve

        jump choice1_done


    label choice1_KB:
        $ team = "b"

        $ fri_eva += 0.1
        $ fri_court += 0.1
        $ fri_duncan += 0.1
        $ fri_izzy += 0.1
        $ fri_bridge += 0.1
        $ fri_geoff += 0.1
        $ fri_ez += 0.1
        $ fri_tyler += 0.1
        $ fri_dj += 0.1
        $ fri_harold += 0.1
        $ fri_sadie += 0.2

        $ fri_owen -= 0.1
        $ fri_katie -= 0.1
        $ fri_linds -= 0.1
        $ fri_cody -= 0.1
        $ fri_heather -= 0.1



        chris "[name] is now a Bass!"
        "You can hear your team cheering and the other one letting out many awws."
        "You look at your team."

        hide chris
        show duncan at slightright
        with dissolve
        "The guy who winked at you earlier is smirking now."
        show courtney at slightleft
        with dissolve
        "A prepped up girl is smiling at you gently and proudly. Giving you a small wave."

        hide duncan
        hide courtney
        with dissolve

        show katie at slightright
        show sadie at slightleft
        with dissolve
        "Katie and Sadie act like enormous fangirls, they're holding their hands while squealing and jumping around in joy."

        show geoff
        with dissolve
        geoff "Rad, man. We got [name] on our team."

        hide katie
        hide sadie
        hide geoff
        with dissolve

        jump choice1_done



    label choice1_done:
        show chris
        with dissolve
        chris "Quiet down, campers."
        chris "[name] might change teams in the future either way, so don't be too sad about it."
        chris "The more you lose, the more time you can spend with them!"

        "Chris chuckles in delight and moves along towards the campsite."

        scene cabins 
        show chris
        with fade

        chris "All right, campers."
        chris "You and your team will be on camera in all public areas during this competition."
        chris "You will also be able to share your innermost thoughts on tape with video diaries anytime you want."
        chris "Except for [name]."
        chris "They have to share their thoughts at least once a day to update the whole world how your living environment is."
        us "But... why only me?"
        chris "Manager's orders."
        "You roll your eyes at this and sigh, but keep listening to Chris."
        chris "The confessional is for letting the audience at home know what you're really thinking."
        chris "Or it might just help to get something off your chest."

        scene confessional
        with fade
        "As you get inside the confessional you nearly puke."
        us "Oh my god, it stinks in here!"
        us "And I have to be in here EVERYDAY."
        us "At least I don't have to come here today anymore... except if I really wanted to say something to the world."

        scene cabins 
        show chris
        with fade

        chris "All right. Any questions?"
        chris "Cool. Let's find your cabins."

        "Chris gets closer to the cabins to show which one is whose."
        chris "Gophers, you’re in the east cabins."
        chris "Bass, you’re in the west."
        chris "But [name] is in neither!"
        chris "They'll be staying at the campsite where me and my buddy Chef will be enjoying gourmet cousine together, while everyone else will be enjoying the slob he cooks."

        "Most campers groan at this, but Heather of course doesn't stay silent."
        show heather at slightleft
        with dissolve
        heather "And where is joy in making them stay at a special place while everyone is here? Huh?"
        chris "They don't need to move cabins all the time during their stay on the island."
        heather "THAT... that actually makes sense."
        "She groans and crosses her arms."
        hide heather
        with dissolve

        chris "You can all get comfy inside of your cabins."
        chris "I'm just going to show [name] where they can leave all their stuff."
        hide chris
        with dissolve

        "Most campers were already hurrying towards their new cabins."
        "Some were looking back at you, maybe thinking of following you."
        "But Chris had already left and started walking in a different direction."
        "You hurry along, cathing up to him."
        
        scene dock
        show chris
        with fade 
        chris "Okay, [name]."
        chris "You'll be staying in a mini van next to the cabin me and Chef are sharing."
        chris "Since you arrived last minute I couldn't afford anything more special for you."
        chris "Anyway, I wanted to ask you something."
        chris "How much do you care about ratings? The ratings of the shows you star in?"

        menu:
            "I care a lot about the ratings.":
                jump choice2_Lots

            "I care a little bit.":
                jump choice2_Little

            "I don't think about them.":
                jump choice2_Nope

            us "Well..."


        label choice2_Lots:
            "They're the most important thing in shows."
            $ sabotage = True
            $ manipulation = True 

            chris "I totally agree!"
            chris "I'm glad we're on the same page here."

            us "Yeah... So why were you asking me this?"
            "Chris smirks at you."

            chris "I would like you to cause some chaos in the teams while you'll be participating."
            "You get intrigued by Chris."
            "Seems like he knows what he's talking about."

            us "Yes? Continue?"

            chris "Well, I think you can find some interesting ways to sabotage or manipulate people here."
            chris "While we're at OUR campsite, we can talk about these things."
            chris "Even now, the cameras are off. So no one would know that we're planning to cause chaos."

            us "I'm in. But how will I know what to do?"

            chris "You can simply come ask me for some 'dirt' on the other campers to use for your tasks."
            chris "Or do whatever you think is right at that moment."
            chris "We watch the footage every now and then regarding everything that's been going on around the island."
            chris "But the things we'll definitely rewatch? The confessionals. Where only me and the audience knows what's going on."
            chris "For those, I can just hint to you what's going on. Otherwise the audince will know you're not a fair player, but we can say you're observant instead."

            chris "What do you say?"


            menu:
                "You will sabotage and manipulate during the competition.":
                    jump choice2_1_both

                "You might sabotage or manipulate during the competition.":
                    jump choice2_1_maybe

                "You will play without sabotaging or manipulating. in the competition.":
                    jump choice2_1_none
                
                us "Hmm..."


            label choice2_1_both:
                us "It's a deal! The audience should have a show they won't forget!"
                "Chris chuckles."
                chris "That's what I hoped for."
                chris "I knew it was a good idea getting you on the show!"
                us "Technically, my manag-"
                chris "The deets aren't important! Let's check out your van."

                jump choice2_done


            label choice2_1_maybe:
                us "Maybe"

                jump choice2_done

            label choice2_1_none:
                us "No, thank you."
                
                jump choice2_done



        label choice2_Little:
            "I want them to be good but I won't go to drastic measures."
            $ sabotage = True
            $ manipulation = False






            jump choice2_done

        label choice2_Nope:
            "I don't care about those things at all."
            $ sabotage = False 
            $ manipulaton = False




            jump choice2_done



        label choice2_done:
            chris "I guess so."




    # This ends the game.

    return
