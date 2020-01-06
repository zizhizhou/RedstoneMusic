from mido import MidiFile, tick2second, tempo2bpm, second2tick
from time import time, sleep

t = time()
bwv = r"C:/Users/lenovo/Desktop/BWV 934 - cut.mid"

# for msg in MidiFile(r"C:/Users/lenovo/Desktop/BWV 934.mid").play():
#    if t != time():
#        t = time()
#        print("Time: ", t)
#    print(msg)

mid = MidiFile(bwv)
print(f"Type={mid.type}")
# tempo = 500000
print("ticks_per_beat = {}".format(mid.ticks_per_beat))
track = mid.tracks[0]
for track in mid.tracks:
    print(f"\nTrack {track.name}\n")
    for msg in track:
        print(msg)
    # if msg.type == 'set_tempo':
    #     tempo = msg.tempo
    #     print("TEMPO RESET:", tempo)
    # else:
    #     print(msg)
#         print("Note:", msg.note - 60, "\tBeat:",
#             second2tick(msg.time, mid.ticks_per_beat, tempo) / tempo)
#             # tick2second(msg.time, mid.ticks_per_beat, tempo))
# else:
#     print("Type:", msg.type, "Note:", msg.note - 60, "\tTime:", msg.time)