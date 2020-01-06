"""
Defines a few interfaces that should be used to communicate

The controlling program is called "Chase"
Level generators, defined below, are called "Level"
"""
import sys
from multiprocessing import SimpleQueue
from typing import List, Tuple, Iterable
import mcpi.minecraft as mmc
from abc import ABC, abstractmethod
from mcpi.vec3 import Vec3 as V3
from enum import Enum, IntEnum


class Dir(Enum):
    """North, South, East, West, Bottom, Top"""
    N, S, E, W, B, T = 'n', 's', 'e', 'w', 'b', 't'


class Cmd(IntEnum):
    """Commands for Chase & Level communication"""
    TERM, ENT, EXI = 0, 1, 2


class Window:
    """The beginning and the end window frame of a Level

    The area within an exit Window of a Level belongs to that Level.
    A Level MUST guarantee that players can only leave through
    its exit Window. A player may enter the next Level from
    anywhere within the previous exit Window.
    The exit Window is up to the previous Level, however the
    next one has to do something such as narrowing or widening
    the path to make sure the entrance eventually suits itself
    """

    def __init__(self, middle: V3, width: int, height: int, direction: Dir):
        """Middle for window bottom center (Vec3, int, int, Direction)"""
        self.middle = middle
        self.width = width
        self.height = height
        self.direction = direction

    def __dir__(self) -> Iterable[str]:
        return ["middle", "width", "height", "direction", "is_in"]

    def __repr__(self):
        return "<Window w={}, h={}, mid={}, d={}".format(
            self.width, self.height, self.middle, self.direction
        )

    def has_pos(self, pos: V3) -> bool:
        """Judge whether a position is on the window"""
        if self.direction == Dir.N or self.direction == Dir.S:
            return (-self.width // 2 <= pos.x - self.middle.x <= self.width // 2
                    and 0 <= pos.y - self.middle.y <= self.height
                    and int(pos.z) == self.middle.z)
        elif self.direction == Dir.E or self.direction == Dir.W:
            return (-self.width // 2 <= pos.z - self.middle.z <= self.width // 2
                    and 0 <= pos.y - self.middle.y <= self.height
                    and int(pos.x) == self.middle.x)


class Level(ABC):
    """Implement all the abstract methods to become a Level!"""
    players: List[int]  # Player id, read from here

    @staticmethod  # The exit window is universally calculated for all instances
    @abstractmethod
    def exitWin(entrance: Window):
        """Tell Chase your exit Window. Both Chase and Level can make use of it"""
        pass

    def __init__(self, queue: SimpleQueue, address: str, port: int, entWin: Window):
        """Initialize a level generator

        conn: Used to communicate with the Chase
        address: Connection address to start a new mcpi connection
        port: Connection port to start a new mcpi connection
        entrance: The entrance window to begin level with
        """
        self.queue = queue
        self.mc = mmc.Minecraft.create(address, port)
        self.entWin = entWin
        self._construct()
        self.players = []
        while True:
            while not queue.empty():
                rec: Tuple[Cmd, List] = queue.get()  # New msg
                if rec[0] == Cmd.TERM:
                    self._cleanup()
                    return
                elif rec[0] == Cmd.ENT:
                    self.players.extend(rec[1])
                elif rec[0] == Cmd.EXI:
                    for i in rec[1]:
                        try:
                            self.players.remove(i)
                        except ValueError:
                            sys.stderr.write(f"Player(id) {i} not found in {self}!")
            self._loop()

    @abstractmethod
    def _construct(self):
        """This will only be called once at the beginning. Window in "self.entWin\""""
        pass

    @abstractmethod
    def _loop(self):
        """Main loop to maintain your level. Player ids in "self.players\""""
        pass

    @abstractmethod
    def _cleanup(self):
        """Called when exit to do some clean up job if necessary"""
        pass
