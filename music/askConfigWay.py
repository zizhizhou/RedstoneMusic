# --------------------
# askConfigWay.py
# Let the user define their own way of configuration
# --------------------

import sys
sys.path.append("..")

# --------------------
# askConfigWay
# --------------------

def askConfigWay(gameName):
    gameName.postToChat("")
    gameName.postToChat("There are currently two ways of configuring the redstone system.")
    gameName.postToChat("Way 1 is to make all note blocks mono-timbre, which also means the pitch range will be reduced. You can choose the timbre later.")
    gameName.postToChat("Way 2 is to remain all notes in the same pitches. The program will choose double bass as the timbre of low range, harp as of medium range, glockenspiel as of high range.")
    gameName.postToChat("Input 1 or 2 to decide which way to configure.")
    gameName.postToChat("")

    while True:
        decideConfigPost = gameName.events.pollChatPosts()
        if len(decideConfigPost) > 0:
            decideConfig = decideConfigPost[0].message
            try:
                a = int(decideConfig)
            except ValueError:      # decideConfig is not an integer
                gameName.events.clearAll()
                gameName.postToChat("")
                gameName.postToChat("You didn't input an integer, please input again.")
                gameName.postToChat("")
                continue
            else:
                if a == 1 or a == 2:
                    gameName.events.clearAll()
                    b = askTimbre(a, gameName)
                    return [a, b]
                else:
                    gameName.events.clearAll()
                    gameName.postToChat("")
                    gameName.postToChat("Your input doesn't fall between 1 and 2, please input again.")
                    gameName.postToChat("")
                    continue

# --------------------
# askTimbre
# --------------------

def askTimbre(a, gameName):

    if a == 1:

        gameName.postToChat("")
        gameName.postToChat("There are currently seven timbres:")
        gameName.postToChat("Harp/piano (1), double bass (2), glockenspiel (3), flute (4), chime (5), guitar (6), xylophone (7).")
        gameName.postToChat("Input an integer between 1 and 7 to choose your timbre.")
        gameName.postToChat("")

        while True:
            decideTimbrePost = gameName.events.pollChatPosts()
            if len(decideTimbrePost) > 0:
                decideTimbre = decideTimbrePost[0].message
                try:
                    b = int(decideTimbre)
                except ValueError:      # decideTimbre is not an integer
                    gameName.events.clearAll()
                    gameName.postToChat("")
                    gameName.postToChat("You didn't input an integer, please input again.")
                    gameName.postToChat("")
                    continue
                else:
                    if 1 <= b <= 7:
                        gameName.events.clearAll()
                        return b
                    else:
                        gameName.events.clearAll()
                        gameName.postToChat("")
                        gameName.postToChat("Your input doesn't fall between 1 and 7, please input again.")
                        gameName.postToChat("")
                        continue

    if a == 2:
        return 0