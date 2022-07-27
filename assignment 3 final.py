from graphics import*
import math
from random import *



def drawButton(gwin,pt1, pt2, label):
    
    button1=Rectangle(pt1,pt2)
    button1.setFill("blue3")
    button1.draw(gwin)
    
    
   #Put Label on button at the midpoint
    midX = (pt1.getX()+pt2.getX())/2
    midY = (pt1.getY()+pt2.getY())/2

    button1Label = Text(Point(midX,midY), label)
    button1Label.setFill("white")
    button1Label.draw(gwin)


def encoder(string,key):
    etext=" "
    for ch in string:
        key = int(key)
        if 63 <= ord(ch) <= 90:
            code = ord(ch) + key
            if code > 90:
               code = code - 26
        elif 97 <= ord(ch) <= 122:
            code = cord(ch) + key
            if code> 122:
                code = code-26

        etext = etext + chr(code)
    return etext

def decoder(string,key):
    etext=" "
    for ch in string:
        if 97 <= ord(ch) <= 122:
            code1 = ord(ch) - key
            code2 = code1 % 26
            code3 = code2 + 97
            newchar = chr(code3)
            etext = etext + newchar

        elif 65 <= ord(ch) <= 90:
            code4 = ord(ch) - 65
            code5 = code4 - int(key)
            code6 = code5 % 26
            newcharm = chr(code6)
            message = message + newchar

        else:
            etext = etext + chr(ord(i))

    return etext
        

def main():
    #win.setCoords(0,0,100,100)
    win=GraphWin("assignment 3",600,600)                   
    win.setBackground("red")

    #this is for a prompt page 
    win1 = Text(Point(300,15), "Ceasar Cipher") 
    win1.setSize(36) #changes font size
    win1.setTextColor("blue")
    win1.draw(win)

#prompt1 just saying what the module does 
    prompt1 = Text(Point(300,75), "This program encodes and decodes words based on\
 the cipher key entered")
    prompt1.setTextColor(color_rgb(randrange(0,255),randrange(0,255),randrange(0,255)))
    prompt1.setSize(20)
    prompt1.draw(win)

    prompt2 = Text(Point(300,115), "Click anywhere to continue")
    prompt2.setSize(15)
    prompt2.draw(win)

    pt = win.getMouse()
    for i in range(65):
        prompt1.move(0, -5)
        prompt2.move(-5,0)
    prompt1.undraw()
    prompt2.undraw()
    
    #Text for Entry box of phrase 
    textMess = Text(Point(300,220), "Enter Phrase Here: ")
    textMess.draw(win)
    
    #Text for Entry box of key value  
    text2 = Text(Point(300, 320), "Enter the cipher key value here: ")
    text2.draw(win)



    #cipher entry box
    inputBoxNum = Entry(Point(300,300,),50)
    inputBoxNum.draw(win)

    #phrase entry box
    inputBox = Entry(Point(300,200,),50)
    inputBox.draw(win)
    #Buttons encoder and decoder
    drawButton(win, Point(100,400), Point(200,350), "Encoder")
    drawButton(win, Point(250,400), Point(330,350),"Decoder")

    #exit button
    drawButton(win, Point(375,400), Point(450, 350), "Exit")
    
#print ascii code
    newStr = Text(Point(100,100),"")
    newStr.draw(win)

    
#gets what user inputs into the text box and the key value
    userString = inputBox.getText()
    keyVal = inputBoxNum.getText()

    pt = win.getMouse()
    output = " "
    while not(pt.getX() <= 350 and pt.getX() >= 275 and pt.getY() >=220 and pt.getY() <=290): 
        
        keyVal= inputBoxNum.getText()
        #newStr.setText(output)
        userString = inputBox.getText()
    if (pt.getX() >= 100 and pt.getX() <= 200 and pt.getY() <= 400 and pt.getY() >= 350):
        
        output = encoder(userString, keyVal)
        newStr.setText(output)
        
    elif (pt.getX()>=250 and pt.getX()<=330) and (pt.getY()<=400 and pt.getY()>=350):
        output = decoder(userString, keyVal)
        newStr.setText(output)

        output.setText(decoder(userString.lower(),inputBoxNum.getText()))
        output.draw(win)
    

    #win.getMouse()
    #win.close()
main() 
                  
                  
                  
                
                
