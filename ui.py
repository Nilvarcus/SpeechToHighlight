import tkinter as tk
import threading
import keyboard
import speech_recognition as sr
import datetime
import pyautogui

F15_SCAN_CODE = 102

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Speech Recognition App")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.listen_label = tk.Label(self, text="Press F15 to start listening")
        self.listen_label.pack(pady=10)
        self.transcription_label = tk.Label(self, text="")
        self.transcription_label.pack(pady=10)

def write_to_file(text):
    # write text to file with timestamp
    with open('output.txt', 'a') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {text}\n")

def on_key_press(event, app):
    if event.scan_code == F15_SCAN_CODE:
        pyautogui.press('F15')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            app.listen_label.config(text="Listening...")
            audio = r.listen(source, phrase_time_limit=10)
            try:
                text = r.recognize_google(audio)
                write_to_file(text)
                app.transcription_label.config(text=f"Transcription: {text}")
            except sr.UnknownValueError:
                app.transcription_label.config(text="Speech recognition could not understand audio")
            except sr.RequestError as e:
                app.transcription_label.config(text=f"Could not request results from Google Speech Recognition service; {e}")
            app.listen_label.config(text="Press F15 to start listening")

# create GUI and start keyboard listener
root = tk.Tk()
app = App(master=root)
keyboard.on_press(lambda event: on_key_press(event, app))
app.mainloop()