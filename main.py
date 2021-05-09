# Importing Required Libraries
import pyautogui
import schedule
import time
import os

# Hashes to be used later
hashes = "#" * 99


# Selecton of Class
print(hashes)
print('Hi Dhairya!I will start your classes as per schedule you will enter')
print(hashes)
print("\n")
print("1. BEE")
print("2. MCP")
print("3. CSA")
print("4. OOPS")
print("5. AWD")
print("6. CSA-Doubt")
print("7.MCP-Thursday")
print(hashes+"\n\n\n")


#Input Desired Details
class_id=int(input("Plz enter your Desired Class Number="))
meet_time = input("Enter the start Time")
duration=int(input("Plz enter the duration of the class(In Minutes)"))
print(hashes)

meet_id=''
password=''
link=''   

if (class_id==1):
    meet_id+='91751069426'
    password+='394592'
elif(class_id==2):
    meet_id='975 6189 5331'
    password='154156'    
elif(class_id==3):
    meet_id+='96489596135'
    print(meet_id)
    password='378175'
elif(class_id==4):
    link='https://teams.microsoft.com/_#/school/conversations/Group%2014%20Class?threadId=19:676331dadf2e4128b90eb545670797ee@thread.tacv2&ctx=channel'
elif(class_id==5):
    link='https://teams.microsoft.com/_#/school/conversations/General?threadId=19:fd696d1dfbc143b89cbe8abbe929660e@thread.tacv2&ctx=channel'
elif(class_id==6):
    meet_id+='96489596135'
    print(meet_id)
    password='378175'    

print(meet_id+" "+link)    






#Funcions for classes to be started
def zoomClass():

#It will give you error if you have looged in in your zoom desktop.So logout before using
    
    #Opening Zoom
    time.sleep(0.2)
    pyautogui.press('esc', interval=0.1)
    time.sleep(0.3)
    pyautogui.press('win', interval=0.5)
    pyautogui.write('zoom')
    time.sleep(1)
    pyautogui.press('enter', interval=0.5)
    time.sleep(2)

    #Clicking On Join Meeting.
    x=pyautogui.center((pyautogui.locateOnScreen('./joinIMG.png')))[0]
    y=pyautogui.center((pyautogui.locateOnScreen('./joinIMG.png')))[1]
    print(x)
    print(y)
    pyautogui.click(x, y)
    time.sleep(.5)

    #Entering My details
    pyautogui.press('enter',interval=2)
    pyautogui.write(meet_id)
    time.sleep(6)
    pyautogui.press('enter', interval=2)
    pyautogui.write(password)
    pyautogui.press('enter', interval=2)
    pyautogui.write("dhairya0192.be20@chitkara.edu.in")
    pyautogui.press('enter', interval=2)

    #Joining Message
    print("I have started session for you Dhairya.Come Fast")


    #Waiting for class to end
    time.sleep(duration * 60)

    #Closing Zoom Class
    os.system("TASKKILL /F /IM zoom.exe")
    time.sleep(0.5)


def teamsClass():
    #Closing Edge if already opened
    os.system("TASKKILL /F /IM msedge.exe")

    #Opening Edge
    time.sleep(1)
    pyautogui.press("win",interval=0.5)
    time.sleep(1)
    pyautogui.write("Edge",interval=0.05)
    pyautogui.press("enter")
    time.sleep(5)

    #Switching to new Tab
    x1=pyautogui.center((pyautogui.locateOnScreen('./newTab.PNG')))[0]
    y1=pyautogui.center((pyautogui.locateOnScreen('./newTab.PNG')))[1]
    print(x1)
    print(y1)
    pyautogui.click(x1, y1)

    #Entering Teams Class link
    pyautogui.write(link)
    pyautogui.press("enter")

    #Finding Join Button
    flag=pyautogui.locateOnScreen('./join.png')
    time.sleep(10)
    pyautogui.scroll(-50)
    

    #Checking if the class has started
    flag=None
    while(flag==None):
        flag=pyautogui.locateOnScreen('./join.PNG')
        print(flag)
        print("Sorry Dhairya!The class is yet not started.I will check again in Minute")
        time.sleep(5)

    #Clicking Join Button    
    x=pyautogui.center(flag)[0]
    y=pyautogui.center(flag)[1]
    print(x)
    print(y)
    pyautogui.click(x, y)
    time.sleep(5)
    
    #Joining Class    
    x2=pyautogui.center((pyautogui.locateOnScreen('./a')))[0]
    y2=pyautogui.center((pyautogui.locateOnScreen('./a')))[1]
    print(x2)
    print(y2)

    pyautogui.click(x2,y2)

    #Joining Message
    print("I have started session for you Dhairya.Come Fast")

    #Waiting for class to end
    time.sleep(duration*60)

    #Closing Browser and Leaving Class
    os.system("TASKKILL /F /IM msedge.exe")
    


# Scheduling Class
if (class_id==1 or class_id==2 or class_id==3):
    schedule.every().day.at(meet_time).do(zoomClass)
else:
    schedule.every().day.at(meet_time).do(teamsClass)

#Checking if Task is pending
while True:
    schedule.run_pending()
    time.sleep(1)

