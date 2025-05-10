import tkinter as tk
from tkinter import scrolledtext
import openai
from openai import OpenAI

# 🔑 Ganti dengan API key kamu
client = OpenAI(api_key="ISI_API_KEY_KAMU_DI_SINI") 

def get_bot_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Kamu adalah chatbot ramah untuk portofolio pengembang Python."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
    
def send_message():
    user_input = entry_box.get()
    if user_input.strip() == "":
        return
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"Kamu: {user_input}\n", "user")
    entry_box.delete(0, tk.END)
    
    bot_response = get_bot_response(user_input)
    chat_box.insert(tk.END, f"Bot: {bot_response}\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

# GUI
root = tk.Tk()
root.title("ChatGPT Chatbot - Portofolio")
root.geometry("500x550")
root.config(bg="#eef")

title_label = tk.Label(root, text="🤖 ChatGPT Portofolio", font=("Helvetica", 16, "bold"), bg="#eef")
title_label.pack(pady=10)

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Helvetica", 11))
chat_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
chat_box.tag_config("user", foreground="blue")
chat_box.tag_config("bot", foreground="dark green")

entry_box = tk.Entry(root, font=("Helvetica", 12))
entry_box.pack(padx=10, pady=10, fill=tk.X)
entry_box.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Kirim", command=send_message, bg="#4CAF50", fg="white", font=("Helvetica", 12))
send_button.pack(pady=5)

root.mainloop()
