from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

# ---------------- MAIN WINDOW ---------------- #

root = Tk()
root.title("Language Translation Tool")
root.geometry("1000x650")
root.config(bg="#f5f5f5")

# ---------------- LANGUAGES ---------------- #

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Korean": "ko",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt"
}

language_names = list(languages.keys())

# ---------------- FUNCTIONS ---------------- #

def translate_text():
    try:
        text = source_text.get(1.0, END).strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "Please enter text"
            )
            return

        source_lang = source_combo.get()
        target_lang = target_combo.get()

        source_code = languages[source_lang]
        target_code = languages[target_lang]

        translated = GoogleTranslator(
            source=source_code,
            target=target_code
        ).translate(text)

        target_text.delete(1.0, END)
        target_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_text():
    source_text.delete(1.0, END)
    target_text.delete(1.0, END)


def copy_text():
    text = target_text.get(1.0, END)

    root.clipboard_clear()
    root.clipboard_append(text)

    messagebox.showinfo(
        "Copied",
        "Translated text copied!"
    )


def speak_text():
    try:
        text = target_text.get(1.0, END).strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "No translated text"
            )
            return

        target_lang = target_combo.get()
        lang_code = languages[target_lang]

        tts = gTTS(text=text, lang=lang_code)

        filename = "voice.mp3"

        tts.save(filename)

        playsound(filename)

        os.remove(filename)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- TITLE ---------------- #

title = Label(
    root,
    text="🌍 Language Translation Tool",
    font=("Arial", 28, "bold"),
    bg="#f5f5f5",
    fg="#333"
)

title.pack(pady=20)

# ---------------- TEXT AREA ---------------- #

text_frame = Frame(root, bg="#f5f5f5")
text_frame.pack()

# Source Text
source_label = Label(
    text_frame,
    text="Enter Text",
    font=("Arial", 16, "bold"),
    bg="#f5f5f5"
)

source_label.grid(row=0, column=0, pady=10)

source_text = Text(
    text_frame,
    width=45,
    height=15,
    font=("Arial", 12)
)

source_text.grid(row=1, column=0, padx=20)

# Target Text
target_label = Label(
    text_frame,
    text="Translated Text",
    font=("Arial", 16, "bold"),
    bg="#f5f5f5"
)

target_label.grid(row=0, column=1, pady=10)

target_text = Text(
    text_frame,
    width=45,
    height=15,
    font=("Arial", 12)
)

target_text.grid(row=1, column=1, padx=20)

# ---------------- LANGUAGE FRAME ---------------- #

lang_frame = Frame(root, bg="#f5f5f5")
lang_frame.pack(pady=20)

# Source Language
source_combo = ttk.Combobox(
    lang_frame,
    values=language_names,
    width=25,
    state="readonly",
    font=("Arial", 12)
)

source_combo.grid(row=0, column=0, padx=20)
source_combo.set("English")

# Target Language
target_combo = ttk.Combobox(
    lang_frame,
    values=language_names,
    width=25,
    state="readonly",
    font=("Arial", 12)
)

target_combo.grid(row=0, column=1, padx=20)
target_combo.set("Telugu")

# ---------------- BUTTONS ---------------- #

button_frame = Frame(root, bg="#f5f5f5")
button_frame.pack(pady=20)

translate_btn = Button(
    button_frame,
    text="Translate",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8,
    command=translate_text
)

translate_btn.grid(row=0, column=0, padx=10)

clear_btn = Button(
    button_frame,
    text="Clear",
    bg="#f44336",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8,
    command=clear_text
)

clear_btn.grid(row=0, column=1, padx=10)

copy_btn = Button(
    button_frame,
    text="Copy",
    bg="#2196F3",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8,
    command=copy_text
)

copy_btn.grid(row=0, column=2, padx=10)

speak_btn = Button(
    button_frame,
    text="Speak",
    bg="#9C27B0",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8,
    command=speak_text
)

speak_btn.grid(row=0, column=3, padx=10)

# ---------------- RUN APP ---------------- #

root.mainloop()