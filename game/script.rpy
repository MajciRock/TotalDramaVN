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

    # We still need to create our own character user, but for that we need to add our name as well.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "MajciRock edited some code"

    # This ends the game.

    return
