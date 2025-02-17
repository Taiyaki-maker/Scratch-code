# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import time
count = 0
running = False
output = ""
time2 = 10

words = {"A": "・－","B": "－・・・","C": "－・－・","D": "－・・","E": "・","F": "・・－・",
              "G": "－－・","H": "・・・・","I": "・・","J": "・－－－","K": "－・－","L": "・－・・",
              "M": "－－","N": "－・","O": "－－－","P": "・－－・","Q": "－－・－","R": "・－・",
              "S": "・・・","T": "－","U": "・・－","V": "・・・－","W": "・－－","X": "－・・－","Y": "－・－－","Z": "－－・・"
}
 
def morse_code_encrypt(st):
    codes = [words[s] for s in st if s in words]
    return '  '.join(codes)

morses = {v:k for k,v in words.items()}
 
def morse_code_decrypt(code):
    codes = code.replace('  ',' ').split(' ')
    answers = [morses[c] for c in codes if c in morses]
    return '  '.join(answers)

def word(time):
    if time < 0.12:
        return "・"
    else:
        return "－"
        
def start_motor(event):
    global running,time1,time2,output
    running = True
    time1 = time.time()
    if time.time() - time2 > 0.3 and len(output) > 1:
        print(morse_code_decrypt(output))
        output = ""

def stop_motor(event):
    global running,time1,time2,output
    output += word(time.time() - time1)
    if len(output) > 3:
        print(morse_code_decrypt(output))
        output = ""
    running = False
    time2 = time.time()

    
def display(event):
    global output
    print(morse_code_decrypt(output))
    output = ""

# rootメインウィンドウの設定
root = tk.Tk()
root.title("tkinter application")
root.geometry("200x100")

# 各種ウィジェットの作成
button = tk.Button(root, text ="forward")
button.bind('<ButtonPress-1>',start_motor)
button.bind('<ButtonRelease-1>',stop_motor)
root.bind("<KeyPress>", display)
#root.bind("<KeyRelease>", stop_motor)

# 各種ウィジェットの設置
button.pack()

root.mainloop()