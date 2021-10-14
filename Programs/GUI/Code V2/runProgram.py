from threading import Thread
import os

def runGUI():
    import GUI

def runConv():
    import convertOutput


Thread(target=runGUI).start()
Thread(target=runConv).start()


