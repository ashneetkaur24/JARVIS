import pyttsx3
import psutil
import pyautogui
from twilio.rest import Client
import speech_recognition as sr
import datetime
import os
import cv2
import random
from pyfirmata import Arduino, SERVO
from time import sleep
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
from pynput.keyboard import Key, Controller
import pyjokes
import speedtest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',170)



#Defining speak fuction here
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




#Defining takecommand fuction here
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 10
        audio = r.listen(source,timeout=10,phrase_time_limit=10)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        file = open('exitmsg.txt', 'r')
        f = file.readlines()
        rd = random.choice(f)
        speak(rd)
        return "none"
    return query






        
#Defining wish function here
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning maam")
    elif hour>12 and hour<18:
        speak("Good afternoon maam")
    else:
        speak("Good evening maam")
    speak("I am jarvis, your personal assistant, please tell me how may i help you maam")





#Defining sendEmail fuction here
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.login('akshayyadavindia31@gmail.com','9b8476ec7eb22b7e31269ce68a19775f')
    server.sendmail('akshayyadavindia31@gmail.com', content)
    server.close()

#Servo code here
port = 'COM3'
pin=10
board = Arduino(port)

board.digital[pin].mode=SERVO

def rotateservo(pin, angle):
        board.digital[pin].write(angle)
        sleep(0.015)


if __name__ == "__main__":
    wish()

    while True:
        
        query = takecommand().lower()
        

       
         #Assigning tasks here
        if "jarvis open notepad" and "open notepad"in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)

        elif "jarvis open command prompt" and "open command prompt"in query:
            os.system("start cmd")

        elif "jarvis i love you" and "i love you"  in query:
            speak("maam i love you too, but as a friend ")

        elif "jarvis open camera" and "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "jarvis play music" and "play music" in query:
            music_dir = "C:\\Users\\aksha\\OneDrive\\Desktop\\JARVIS-v1.0\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "jarvis what is my ip" and "what is my ip" in query:
            ip = get('https://api.ipify.org').text

            speak(f"maam, your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "jarvis turn on flashlight" and "turn on flashlight" in query:
            for i in range(0,90):
                rotateservo(pin, i)

        elif "jarvis turn off flashlight" and "turn off flashlight" in query:
            for i in range(0,1):
                rotateservo(pin, i)

        elif "jarvis open youtube" and "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "jarvis open facebook" and "open facebook" in query:
            webbrowser.open("https://www.facebook.com")

        elif "jarvis open instagram" and "open instagram" in query:
            webbrowser.open("https://www.instagram.com")

        elif "jarvis open twitter" and "open twitter" in query:
            webbrowser.open("https://www.twitter.com")

        elif "jarvis open google" and "open google" in query:
            speak("maam what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "jarvis send whatsapp message" and "send message" in query:
            speak("maam what should i send in message")
            cm = takecommand().lower()
            kit.sendwhatmsg("+919793577149",f"{cm}",15,16)

        elif "jarvis play a video on youtube" and "play video on youtube" in query:
            speak("maam which video i should i play")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

        elif "jarvis send email" and "send email" in query:
            try:
                
                to = ("teamakshayyadav@gmail.com")
                speak("maam what should i send")
                content = takecommand().lower()
                sendEmail(to,content)
                speak("email has been send successfully")

            except Exception as e:
                print(e)
                speak("sorry maam, i am not able to send it")

        elif "jarvis close it" and "close it" in query:
            time.sleep(3)
            keyboard = Controller()
            keyboard.press(Key.alt)
            keyboard.press(Key.f4)
            keyboard.release(Key.alt)
            keyboard.release(Key.f4)

        elif "jarvis tell me a joke" and "tell me a joke" in query:
            joke = pyjokes.get_joke('en')
            speak(joke)

        elif "jarvis shutdow the system" and "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "jarvis restart the system" and "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "jarvis put system on sleep mode" and "turn on sleepmode" in query:
            os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "jarvis where is my phone" and "where is my phone" in query:
            speak("ok maam i am making a call on it")
            account_sid = 'ACfa94d4df40ff12beba5112208cd4d80c'
            auth_token = '03bb647dc2aad07aa57d00d1ba402a00'
            client = Client(account_sid, auth_token)

            message = client.calls \
            .create(
                twiml='<Response><Say>hello</Say></Response>',
                from_='+19783078169',
                to='+916387051016'
                 )

        elif "jarvis where i am" and "what is my location" in query:
            speak("wait maam, let me check")

            try:
                ipAdd = get('https://api.ipify.org').txt
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"maam i am not sure, but i think we are in {city} city of {country}")

            except Exception as e:
                speak("sorry maam, due to network error i am not able to find out")
            pass

        elif "jarvis take screenshot" and "take screenshot" in query:
            speak("maam, please tell me the name for this screenshot image") 
            name = takecommand().lower()
            speak("please hold the screen for few seconds")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("done maam you can move your cursor now")

        elif "jarvis turn up the volume" and "volume up" in query:
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)
            pyautogui.press("volumeup")
            sleep(0.50)

        elif "jarvis turn down the volume" and "volume down" in query:
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            pyautogui.press("volumedown")
            sleep(0.50)
            
        elif "jarvis mute" and "mute" in query:
            pyautogui.press("volumemute")


        elif "my internet speed" and "my speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"maam we have {dl} bit per second downloading speed and {up} bit per second uploading speed")


        #elif "jarvis what is my battery percentage" and "check battery health":
            #battery = psutil.sensors_battery()
            #percentage = battery.percent
            #speak("maam our system have {percentage} percent battery")




        #jarvis exit code here

        elif "no jarvis" and "no thanks" in query:
            speak("thanks for using me maam, have a good day, i will miss you")
            sys.exit()

 

       


