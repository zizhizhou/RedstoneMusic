'''
Test File
Please write your test code here
Note that this file could be modified by anyone
'''
from multiprocessing import Process, Pipe
from time import sleep
from tools import start


def f(conn):
    sleep(3)
    conn.send([42, None, 'hello'])
    conn.close()


class Runner():
    def __init__(self, conn):
        print("Runners on their way!")
        self.conn = conn
        sleep(2)
        conn.send("Got it!")
        self.z()

    def z(self):
        print("zing...")
        sleep(2)
        print("zed w")


if __name__ == '__main__':
    mc = start(0)
    while True:
        l = mc.events.pollDeaths()
        if l:
            print(l)
        l = mc.events.pollLogins()
        if l:
            print(l)
        l = mc.events.pollQuits()
        if l:
            print(l)
        l = mc.events.pollRespawns()
        if l:
            print(l)
        sleep(0.2)
