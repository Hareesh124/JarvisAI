#from fbs_runtime.application_context.PyQt5 import ApplicationContext
import random
import wikipedia
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import pywhatkit
import pyautogui
import PyPDF2
from speech_recognition import Recognizer




flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init()
engine.setProperty('rate',190)


def DS():
    link = 'https://meet139.webex.com/meet/pr1582596053'
    return link
def OOP():
    link = 'http://meet.google.com/sbd-efmy-whw'
    return link
def Maths():
    link = 'https://meet.google.com/nks-fduy-rqw'
    return link
def DPSD():
    link = 'https://meetingsapac14.webex.com/meet/sreekannan1114'
    return link
def CE():
    link = 'https://meet139.webex.com/meet/pr1582596053'
    return link


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning sir")
    elif hour > 12 and hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak('I am Jarvis your personal voice assistant')
    speak('How can i help you ')



class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()

    def run(self):
        self.JARVIS()

    @property
    def STT(self):

        R: Recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...........")
            audio = R.listen(source)

        try:
            print("Recog......")
            text = R.recognize_google(audio)

        except Exception:
            return "None"
        text = text.lower()
        print(text)
        return text

    def JARVIS(self):
        global time
        wish()
        while True:

            self.query = self.STT

            if 'good bye' in self.query:
                sys.exit()
            elif 'google' in self.query:
                search_term = self.query.replace('google', '')
                url = "https://google.com/search?q=" + search_term
                webbrowser.get().open(url)
                speak('here is what i found in the web')

            elif 'time' in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                speak('The time is' + time)
            elif 'who is' in self.query:
                person = self.query.replace('who is', '')
                info = wikipedia.summary(person, 2)
                print(info)
                speak(info)
            elif 'define' in self.query:
                definition = self.query.replace('define', '')
                info = wikipedia.summary(definition, 2)
                print(info)
                speak(info)
            elif 'youtube' in self.query:
                song = self.query.replace('play', '')
                print('playing' + song)
                speak('playing' + song)
                pywhatkit.playonyt(song)
            elif 'who are you' in self.query:
                speak('i am jarvis')
            elif 'what can you do' in self.query:
                speak('i can play videos on youtube , search about people , define things , tell you the time etcetera')
            elif "open instagram" in self.query:
                url = "https://www.instagram.com/"
                webbrowser.get().open(url)
                speak("opening instagram")
            elif "open twitter" in self.query:
                url = "https://twitter.com/"
                webbrowser.get().open(url)
                speak("opening twitter")
            elif 'screenshot' in self.query:
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'D:\Hareesh\desktop\screenshots py\ss.png')
            elif 'read' in self.query:
                book = open('oop.pdf', 'rb')
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.numPages
                for num in range(1,pages):
                    page = pdfReader.getPage(1)
                    text = page.extractText()
                    speak(text)
            elif 'join digital' in self.query:
                url = DPSD()
                webbrowser.get().open(url)
                speak('joining DPSD class')
                pyautogui.press('enter', interval=0.5)
                time.sleep(10)
                pyautogui.click(x=1144, y=1031)
            elif 'join data' in self.query:
                url = DS()
                webbrowser.get().open(url)
                speak("joining Data Structures class")
                pyautogui.press('enter', interval=0.5)
                time.sleep(10)
                pyautogui.click(x=1144, y=1031)
            elif 'join communication' in self.query:
                url = CE()
                webbrowser.get().open(url)
                speak("joining Coomunication Engineering class")
                pyautogui.press('enter', interval=0.5)
                time.sleep(10)
                pyautogui.click(x=1144, y=1031)
            elif 'join object' in self.query:
                url = OOP()
                webbrowser.get().open(url)
                speak("joining Object Oriented Programming class")
                pyautogui.press('enter', interval=0.5)
                time.sleep(10)
                pyautogui.click(x=622 , y=815)
                time.sleep(10)
                pyautogui.click(x=719 , y=804)
                time.sleep(10)
                pyautogui.click(x=1348 , y=636)
            elif 'join mathematics' in self.query:
                url = Maths()
                webbrowser.get().open(url)
                speak('joining discrete mathematics class')
                pyautogui.press('enter', interval=0.5)
                time.sleep(10)
                pyautogui.click(x=622, y=815)
                time.sleep(10)
                pyautogui.click(x=719, y=804)
                time.sleep(10)
                pyautogui.click(x=1348, y=636)
            elif 'open brave' in self.query:
                speak('Opening brave browser')
                pyautogui.press('win', interval=0.5)
                time.sleep(1)
                pyautogui.write('brave', interval=0.5)
                time.sleep(1)
                pyautogui.press('enter', interval=0.5)
                time.sleep(1)
                pyautogui.keyDown('ctrl')
                pyautogui.press('T')
                pyautogui.keyUp('ctrl')
            elif 'open spotify' in self.query:
                speak('Opening Spotify')
                pyautogui.press('win', interval=0.5)
                time.sleep(1)
                pyautogui.write('spotify', interval=0.5)
                time.sleep(1)
                pyautogui.press('enter', interval=0.5)
                time.sleep(1)
            elif 'open amazon prime' in self.query:
                speak('Opening amazon prime video')
                pyautogui.press('win', interval=0.5)
                time.sleep(1)
                pyautogui.write('amazon prime', interval=0.5)
                time.sleep(1)
                pyautogui.press('enter', interval=0.5)
                time.sleep(1)
            elif 'note' in self.query:
                url = "https://keep.google.com/#home"
                webbrowser.get().open(url)
                speak("You can take notes here")
            elif 'game' in self.query:
                speak("choose among rock paper or scissor")
                voice_data = self.STT
                moves = ["rock", "paper", "scissor"]

                cmove = random.choice(moves)
                pmove = voice_data

                speak("The computer chose " + cmove)
                speak("You chose " + pmove)
                # engine_speak("hi")
                if pmove == cmove:
                    speak("the match is draw")
                elif pmove == "rock" and cmove == "scissor":
                    speak("Player wins")
                elif pmove == "rock" and cmove == "paper":
                    speak("Computer wins")
                elif pmove == "paper" and cmove == "rock":
                    speak("Player wins")
                elif pmove == "paper" and cmove == "scissor":
                    speak("Computer wins")
                elif pmove == "scissor" and cmove == "paper":
                    speak("Player wins")
                elif pmove == "scissor" and cmove == "rock":
                    speak("Computer wins")
            elif "calculate" or "plus" or "by" or "into" or "raised" or "minus" or "multiply" or "divide" or "power" or "+" or "-" or "*" or "/" in self.query:
                opr = self.query.split()[2]

                if opr == '+':
                    speak(int(self.query.split()[1]) + int(self.query.split()[3]))
                elif opr == '-':
                    engine_speak(int(self.query.split()[1]) - int(self.query.split()[3]))
                elif opr == 'multiply' or opr == 'into':
                    speak(int(self.query.split()[1]) * int(self.query.split()[3]))
                elif opr == 'divide' or opr == 'by':
                    speak(int(self.query.split()[1]) / int(self.query.split()[3]))
                elif opr == 'power' or opr == 'raise to':
                    speak(int(self.query.split()[1]) ** int(self.query.split()[3]))
                # else:
                #     speak("Sorry i didnt get that")
                #     speak("Try again")
            elif 'weather' in self.query:
                url = "https://www.google.com/search?q=weather&oq=wea&aqs=chrome.0.69i59j69i57j69i60l4j5l2.1396j0j1&sourceid=chrome&ie=UTF-8"
                webbrowser.get().open(url)
            elif 'are you there' in self.query:
                speak('yes sir i am listening')


FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./scifi.ui"))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920, 1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                 "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 8)))





#if __name__ == '__main__':
 #   appctxt = ApplicationContext()
  #  screen = Main()
   # screen.show()
    #exit_code = appctxt.app.exec_()
   # sys.exit(exit_code)





app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())

