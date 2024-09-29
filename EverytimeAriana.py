import sys
from threading import Thread, Lock
import time

lock = Lock()

def animate_text(text, char_delay):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()

def Ariana(lyric, start_delay, char_delay):
    time.sleep(start_delay)  
    animate_text(lyric, char_delay)

def Everytime():
    lyrics = [
        "You get high and call on the regular",
        "I get weak and fall like a teenager",
        "Why, oh, why does God keep bringing me (Mm) back to you?(Back to you, baby)",
        "I get drunk, pretend that I'm over it",
        "Self-destruct, show up like an idiot",
        "Why, oh, why does God keep bringing me back to you?",
        "I go back to you, back to you, back to you(I go back to you)",
        "Back to you, back to you, back to you(Back to you)",
        "I go back to you, back to you, back to you every time (I go)",
        "I go back to you, back to you, back to you (You)",
        "Back to you, back to you, back to you",
        "I go back to you, back to you, back to you every time",
    ]

    delays = [0.1, 4.0, 7.0, 13.0, 17.0, 20.0, 26.0, 29.0, 32.0, 39.0, 42.0, 45.0,]

    threads = []
    for i in range(len(lyrics)):
        lyric = lyrics[i]
        start_delay = delays[i]
        char_delay = 0.070

        t = Thread(target=Ariana, args=(lyric, start_delay, char_delay))
        threads.append(t)
        t.start()


Everytime()
