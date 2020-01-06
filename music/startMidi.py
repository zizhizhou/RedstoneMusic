# --------------------
# (main) startMidi.py
# v0.1.9 - 2019/7/30
# Double-click this to launch the program!
# --------------------

import sys
sys.path.append("..")

import mcpi.minecraft as mmc
import tools
import setSystem as ss
import constructSystem as cs

mc = tools.start(0)

# --------------------
# retry
# --------------------

def retry():

    mc.events.clearAll()

    while True:
        
        userChoicePost = mc.events.pollChatPosts()
        
        if len(userChoicePost) > 0:
            userChoice = userChoicePost[0].message
            
            try:
                a = int(userChoice)

            except ValueError:      # userChoice is not an integer
                mc.postToChat("")
                mc.postToChat("Process aborted.")
                mc.postToChat("")
                sys.exit(0)
                
            else:
                if a == 1:
                    mc.events.clearAll()
                    mc.postToChat("")
                    mc.postToChat("Process restarted.")
                    mc.postToChat("Please input (in-game) the path of the midi file you want to realize, beginning with an additional hyphen: (i.e. -C:\\Raspy\\test.mid or -/Users/<your-name>/Documents/test.mid)")
                    mc.postToChat("")
                    break
                else:
                    mc.events.clearAll()
                    mc.postToChat("")
                    mc.postToChat("Process aborted.")
                    mc.postToChat("")
                    sys.exit(0)

# --------------------
# main
# --------------------

if __name__ == "__main__":
    
    mc.postToChat("")
    mc.postToChat("Music Lab v0.1.9 initiated!")
    mc.postToChat("")
    mc.postToChat("Please input (in-game) the path of the midi file you want to realize, beginning with an additional hyphen: (i.e. -C:\\Raspy\\test.mid or -/Users/<your-name>/Documents/test.mid)")
    mc.postToChat("")

    while True:
        
        posts = mc.events.pollChatPosts()

        if len(posts) > 0:
            pathWithHyphen = posts[0].message
            path = pathWithHyphen.lstrip("-")

            try:
                configurationList = ss.setRedstoneSystem(path, mc)
            
            except FileNotFoundError:
                mc.postToChat("")
                mc.postToChat("Cannot find a file at your path, maybe used a false grammar?")
                mc.postToChat("Input 1 to try again, or input anything besides 1 to abort the process.")
                mc.postToChat("")
                retry()
                continue

            except PermissionError:
                mc.postToChat("")
                mc.postToChat("Uh-oh, seems like the program doesn't have the permission to visit that path. Try putting the file in a different folder.")
                mc.postToChat("Input 1 to try again, or input anything besides 1 to abort the process.")
                mc.postToChat("")
                retry()
                continue

            except IndexError:
                mc.postToChat("")
                mc.postToChat("The file you requested isn't midi file, or your midi file cannot be processed at the moment. Sorry!")
                mc.postToChat("Input 1 to try again, or input anything besides 1 to abort the process.")
                mc.postToChat("")
                retry()
                continue

            except ValueError as ve:
                mc.postToChat("")
                if ve == "Nothing":
                    mc.postToChat("There's literally nothing in your midi file. Therefore we cannot proceed.")
                if ve == "Too many voices":
                    mc.postToChat("Sorry, but we currently do not process midi files with moments of more than 15 notes playing. Try another file, or simplify the current file?")
                mc.postToChat("Input 1 to try again, or input anything besides 1 to abort the process.")
                mc.postToChat("")
                retry()
                continue

            else:
                break

    mc.events.clearAll()

    cs.constructRedstoneSystem(configurationList, mc)