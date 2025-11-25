import time
import os
import sys

lyrics = [
    "🎵 Playing: Tere Bina🎧",
    "Besabar ho rahi hai 💞",
    "ye meri baahein...... 🤗",
    "Tu kahan hai ",
    "Benazar ho rahi hai ",
    "ye nigaahein👀....",
    "Tu kahan",
    "Apne dil, se mera, haq mitane lage ",
    "Mere har khwaab ko, Tum jalane lage🔥",
    "Dil mein bharne laga hai dhuaan.....  ",
    "tere bina, marz aadha aadhura hai ❤️‍🩹",
    "ek dhundh hai ",
    "shaam hai n savera hai ",
    "tanha hun main, phir bhi tanha nahi ",
    "dar ye hai ki fana ho na jaunnnn🥀..... "
]

durations = [1,1.1,1.5,0.5,0.7,1.2,0.3,0,0,0.7,0,0,0,0,0]


def typewriter(text, delay=1, hold=1.2):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.15)
    time.sleep(hold)
    print()  # New line


for i, line in enumerate(lyrics):
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen
    typewriter(line, delay=0.005, hold=durations[i])
