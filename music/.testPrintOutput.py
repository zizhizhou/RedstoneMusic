import sys
sys.path.append("..")

from numpy import gcd

import mcpi.minecraft as mmc
import tools
import readMidiFile as rmf

mc = tools.start(0)

mc.postToChat("Test mode, please input a path.")

while True:
    posts = mc.events.pollChatPosts()
    if len(posts) > 0:
        pathWithHyphen = posts[0].message
        path = pathWithHyphen.lstrip("-")
        a = list(rmf.readAndProcessMidi(path))
        file = open(".test.txt", "w")
        print(gcd.reduce([hit[0] for hit in a]))
        print([hit for hit in a])
        file.write(str(list(hit for hit in a)))
        file.close()
        break
