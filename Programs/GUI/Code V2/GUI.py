from textbox import *
#Output to EyeBraille
#from convertOutput import *
import subprocess
import threading

import pygame
import time
#File Dialog
import Tkinter
from Tkinter import *
from tkFileDialog import askopenfilename
#PDF
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
#import os
#import pdfminer

pygame.init()

display_width = 800
display_height = 600

#Defined Colours
white = (255,255,255)
grey = (200,200,200)
light_grey = (125,125,125)
gold = (255,223,20)


GUI_Display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Eye Braille')
clock = pygame.time.Clock()
exit_Condition = False



pygame.display.update()

##
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
##

##
def message_display(text, font, font_size, rect):
    Text_Font = pygame.font.Font(font,font_size)
    TextSurf, TextRect = text_objects(text, Text_Font)
    TextRect.center = (rect[0]+rect[2]/2,rect[1]+rect[3]/2)
    GUI_Display.blit(TextSurf, TextRect)

    #time.sleep(2) #Display for 2 second
##

##Button
def button(msg, font, font_size, rect, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Mouse Hover
    if rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1]:
        pygame.draw.rect(GUI_Display,ac,rect)
        if click[0] == 1 and action != None:
            action()
            action = None
    else:
        pygame.draw.rect(GUI_Display,ic,rect)

    message_display(msg,font,font_size,rect)
##

##Upload File
def upload_file():
    tk_root = Tk()
    tk_root.withdraw()

    result = askopenfilename(
        initialdir=tk_root,
        title="Select File",
        filetypes=[("PDF Documents", "*.pdf")],
    )

    if len(result)>0:
        print ("You chose %s" % result)
        #string = 'pdf2txt.py -o Text_File.txt -t tag %s' % result
        #os.system(string)
        text = convert(result,)
        textFile = open("Text_File.txt", "w") #make text file
        textFile.write(text) #write text to text file
##

##Convert PDF to Txt
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 
##

##Main Menu
def main_menu():
    
    global exit_Condition
    
    while not exit_Condition:
        pygame.display.update()
        clock.tick(15)
        GUI_Display.fill(gold)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_Condition = True

        #message_display("Eye Braille",'freesansbold.ttf',115,(0,0,display_width,display_height))
        logo = pygame.image.load('Eye_Braille.png')
        GUI_Display.blit(logo, (display_width/2-logo.get_width()/2,0))

        #Buttons/Menu Options
        button("Upload Content",'freesansbold.ttf',20,(display_width/2-85,400,170,50),grey,light_grey, upload_content)
        button("Enter Text",'freesansbold.ttf',20,(display_width/2-85,500,170,50),grey,light_grey, enter_text)
##

##Upload Content Menu
def upload_content():
    
    global exit_Condition
    
    while not exit_Condition:
        pygame.display.update()
        clock.tick(15)
        GUI_Display.fill(gold)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_Condition = True

        #Instruction
        message_display("Select and upload a PDF File:",'freesansbold.ttf',20,(0,0,display_width,display_height/8))

        button("Upload PDF",'freesansbold.ttf',20,(display_width/2-75,100,150,50),grey,light_grey, upload_file)
        button("Back",'freesansbold.ttf',20,(50,500,100,50),grey,light_grey, main_menu)
##

##Enter Text Menu
def enter_text():
    input_box = InputBox(GUI_Display, display_width/2-100, 100, 100, 32)
    input_boxes = [input_box]
    global exit_Condition
    
    
    
    while not exit_Condition:
        pygame.display.update()
        clock.tick(15)
        GUI_Display.fill(gold)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                exit_Condition = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()
        
        for box in input_boxes:
            box.draw()
            
        
        #os.system("python2 convertOutput.py &")
        #subprocess.Popen(['./convertOutput.py'])
        #Instruction
        message_display("Enter text to be displayed on EyeBraille",'freesansbold.ttf',20,(0,0,display_width,display_height/8))

        button("Back",'freesansbold.ttf',20,(50,500,100,50),grey,light_grey, main_menu)

        #NOTE: Exclude some special characters
##
   
main_menu()
pygame.quit()
quit()

        
