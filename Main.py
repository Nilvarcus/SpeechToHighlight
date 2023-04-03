import keyboard
import speech_recognition as sr
import datetime
import pyautogui

F15_SCAN_CODE = 102
F14_SCAN_CODE = 101

def write_to_file(text):
    # write text to file with timestamp
    with open('output.txt', 'a') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {text}\n")

def on_key_press(event):
    if event.scan_code == F15_SCAN_CODE:
        pyautogui.press('F15')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak now...')
            audio = r.listen(source, phrase_time_limit=10)
            try:
                text = r.recognize_google(audio)
                write_to_file(text)
                print(f"Transcription: {text}")
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

def on_key_press_highlight(event):
    if event.scan_code == F14_SCAN_CODE:
        pyautogui.press('F14')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak now...')
            audio = r.listen(source, phrase_time_limit=10)
            try:
                text = r.recognize_google(audio)
                write_to_file(text)
                print(f"HIGHLIGHT Transcription: {text}")
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
    

# listen for key press events
keyboard.on_press(on_key_press)
keyboard.on_press(on_key_press_highlight)

# keep the script running
keyboard.wait()