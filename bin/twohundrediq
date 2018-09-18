#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageEnhance, ImageGrab
from prettytable import PrettyTable
import pytesseract, argparse, os, cv2, sys, psutil, win32gui, win32ui, win32com.client, time, win32api, win32con, nltk, cv2, crayons, wikipedia

nltk.download("stopwords")

class warning:
    banner = """
----------------------------------------------------------------
[!] BE EXTRA SURE YOU ARE CONNECTED, IN FULLSCREEN, AND THAT [!]
[!] THERE ARE NO WINDOWS IN FRONT OF THE QUESTIONS/ANSWERS!! [!]
[!] -------------------------------------------------------- [!]
[!]                      INSTRUCTIONS:                       [!]
[!] WAIT ON THIS SCREEN UNTIL THE FIRST QUESTION POPS UP! AT [!]
[!] THAT TIME PRESS ENTER ON THE SCREEN! DON'T TOUCH A THING![!]
[!] LET THE PROGRAM WORK ITS MAGIC AND WHEN IT'S DONE YOU    [!]
[!] WILL SEE THE QUESTION AND RESULTS DISPLAYED ON SCREEN.   [!]
[!] THE BEST CHOICE WILL BE DISPLAYED IN AT THE BOTTOM!      [!]
----------------------------------------------------------------
»»»  Good Luck and If You Haven't Already Please Read Above  «««

    """

def checkLonelyScreen():
    check = True
    os.system("cls")
    try:
        print("[!] Running Check To See If LonelyScreen is Open [!]")
        processName = "LonelyScreen.exe"
        pids = psutil.pids()
        running = False
        for i in psutil.process_iter():
            process = psutil.Process(i.pid)
            pname = process.name()
            if pname == processName:
                os.system("cls")
                print("[!] Success: Found LonelyScreen Running! [!]")
                print("[*] Continuing... [*]")
                clearmenu()
                running = True
                return running
            else:
                pass
        if running == True:
            pass
        else:
            os.system("cls")
            print("[!] Error: LonelyScreen couldn't be found running! [!]")
    except KeyboardInterrupt:
        exit()

def windowEmumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def bringwindowtofront():
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEmumerationHandler, top_windows)
    for i in top_windows:
        if "lonelyscreen" in i[1].lower():
            print("[!] Opening LonelyScreen [!]")
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            time.sleep(0.5)
            screenshot()

def screenshot():
    win32api.keybd_event(win32con.VK_SNAPSHOT, 0)
    im = ImageGrab.grab()
    im.save("screenshot.jpg", "JPEG")
    print("[!] Screen Grabbed! [!]")
    time.sleep(0.2)
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEmumerationHandler, top_windows)
    for i in top_windows:
        if "command prompt" in i[1].lower():
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
    read()
    clearmenu()


def clearmenu():
    wait = True
    while wait == True:
        print("{}".format(crayons.green(warning.banner)))
        start = input("Press Enter To Start »» ")
        if start == "":
            bringwindowtofront()
        else:
            bringwindowtofront()


SCREEN_DIR = "screenshot.jpg"

def process_image(img):
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1)

    img = img.convert("L")

    # Crop for question
    w, h = img.size
    img = img.crop((600, 200, w-600, h-200))

    # Check work with...
    # img.show()

    return img

def read():
    stop = set(nltk.corpus.stopwords.words("english"))
    screen = process_image(Image.open(SCREEN_DIR))
    screen.save("screenshotprocessed.png")
    NEW_SCREEN_DIR = "screenshotprocessed.png"
    image = cv2.imread(NEW_SCREEN_DIR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    result = pytesseract.image_to_string(Image.open(filename), config="load_system_dawg=0 load_freq_dawg=0 tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz -psm 6")
    parts = result.split("\n\n")

    question = parts.pop(0).replace("\n", " ")
    q_terms = question.split(" ")
    q_terms = list(filter(lambda t: t not in stop, q_terms))
    q_terms = set(q_terms)

    parts = "\n".join(parts)
    parts = parts.split("\n")

    answers = list(filter(lambda p: len(p) > 0, parts))

    for i, a in enumerate(answers):
        answers[i] = a.replace("fi", "t")

    print("\n\n{}\n\n{}\n\n".format(
        crayons.blue(question),
        crayons.blue(", ".join(answers))
        ))

    answer_results = {}

    for answer in answers:
        records = wikipedia.search(answer)
        r = records[0] if len(records) else None

        if r is not None:
            p = wikipedia.page(r)
            answer_results[answer] = {
                "content": p.content,
                "words": p.content.split(" ")
            }

    for a in answer_results:
        term_count = 0

        for t in q_terms:
            term_count += answer_results[a]["words"].count(t)

        tc = term_count / len(answer_results[a]["words"])
        tcp = round(tc * 10000, 2)

        answer_results[a]["score"] = tcp

    max_a = 0
    max_a_key = None

    # Maximize
    for a in answer_results:
        if answer_results[a]["score"] > max_a:
            max_a_key = a
            max_a = max(answer_results[a]["score"], max_a)

    print(crayons.green(max_a_key))
    os.remove(filename)

def startmenu():
    print("""
200IQ HQ Trivia Bot by Macs
An Easy Way To Get A Few Bucks

Currently Supported Devices:

- iPhone

Currently Supported Systems:

- Windows

Required Programs:

- LonelyScreen
- HQ Trivia

[!] WARNING: NO ANSWERS ARE 100% POSITIVE TO BE TRUE! [!]
    """)
    options = {}
    options['help'] = 'Help Menu'
    options['start'] = 'Start Bot'
    options['exit'] = 'Exit'
    ans = True
    while ans == True:
        print("""

For Help Type help
To Start The Bot Type start
If You Would Like To Exit Type exit""")
        inp = input("\n»» ")
        if inp == "plshelpme":
            okie = True
            while okie == True:
                os.system("cls")
                print("""
                    Help Menu

Getting Started:

To start using The 200IQ Bot You Will Need A Few Things...

First, if you haven't already make sure all your modules
match up with the modules included in requirements.txt
in the root of this programs directory. You can run
`pip install -r requirements.txt` to install all req.
python modules automagically.

You will also need a program known as LonelyScreen. If you
don't already have it feel free to download it for free from
the original site (Google It). Install that and then you
should pretty much be all done!

This program basically guides you through what to do and
does most of the stuff for you! If you can't figure out what
is going on you probably shouldn't be using this. Then Again
you can't answer things on your own so I don't blame you...

Anyways enjoy your time. I did this as a project to work with
python's OCR capabailities. Have Fun! And go win some big bucks!
                """)
                print("[!] Type Exit To Go Back To The Main Screen! [!]")
                scndinp = input("\n»» ")
                options2 = {}
                options2['exit'] = "Exit"
                options2['Exit'] = "Exit"
                options2['EXIT'] = "Exit"
                options2['eXIT'] = "Exit"
                if scndinp == "exit":
                    startmenu()
                elif scndinp == "Exit":
                    startmenu()
                elif scndinp == "EXIT":
                    startmenu()
                elif scndinp == "eXIT":
                    startmenu()
                else:
                    print("[!] Try Again! [!]")
            ans = False
        elif inp == "start":
            checkLonelyScreen()
            ans = False
        elif inp == "exit":
            os.system("cls")
            print("Goodbye!")
            exit()
            ans = False
        else:
            print("[!] Error Unknown Selection Made!")

if __name__ == "__main__":
    startmenu()
