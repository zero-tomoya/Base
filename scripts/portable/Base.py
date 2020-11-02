
import tkinter
import copy
import sys,pickle
from tkinter import messagebox
from tkinter import ttk
import os
import time
import webbrowser
import traceback
import threading
import tkinter.font as tkFont
import configparser
# this Softwere Defalut browser is keyword search 

s=0
print('')
print(' simple Base browser　Ver 1.5')
# 文字色の指定

cor="Black"
back="grey"
if os.path.isfile("resource/config/default.conf")==True:
    config = configparser.ConfigParser()
    config.read('resource/config/default.conf')
    conf=config['SECTION1'].get('enable')
    if conf=="True" or conf==True:
        cor=config['SECTION1'].get('color')
        back=config['SECTION1'].get('backcolor')
    
try:

    def resourcePath(filename):
      if hasattr(sys, "_MEIPASS"):
          return os.path.join(sys._MEIPASS, filename)
      return os.path.join(filename)

    def exitf(event):
        global s
        ret=messagebox.askyesno("Simple Base browser", "このプログラムを終了しますか?")
        if ret==True:
            root.destroy()
            sys.exit(1)
        else:
            return "break"

    def vf(event):
        global txt
        global combo
        with open("resource/dat/url.DAT", 'rb') as f:
            url = pickle.load(f)
        if txt.get()=="":
            return "break"
        if combo.get()=="キーワード検索":
            web=url+txt.get()
        else:
            if "https://" in txt.get() or "http://" in txt.get():
                web=copy.copy(txt.get())
            else:
                web="https://"+txt.get()
        webbrowser.open_new(web)
        txt.delete(0,tkinter.END)
        return "break"
    
    def dcall(event):
        time.sleep(0.1)
        thread1 = threading.Thread(target=vf,args=(event,))
        thread1.start()
        return "break"
        
    root = tkinter.Tk()
    root.resizable(False, False)
    root['bg'] = 'grey'
    root.iconbitmap(default="resource/icon/ifs.ico")
    Static1 = tkinter.Label(text=u' ', background='grey')
    Static4 = tkinter.Label(text=u' ', background='grey')

    root.title(u"Simple Base browser (portable)")
    root.geometry("400x350")

    fontStyle = tkFont.Font(family="Meiryo", size=20)

    Static1.pack()
    Static1.pack()

    lbl1 = tkinter.Label(text='Simple Base browser',foreground=cor, font=fontStyle,background=back)
    lbl1.pack()

    Static2 = tkinter.Label(text=u' ',background='grey')
    Static2.pack()

# ラベルの生成
    lbl = tkinter.Label(text='検索キーワード',foreground=cor,background=back)
    lbl.pack()
    txt = tkinter.Entry(width=20)
    txt.pack()
    Static4 = tkinter.Label(text=u' ', background=back)
    Static4.pack()

# 検索ボタンの生成
    Button5 = tkinter.Button(text=u'検索',font=("",10))
    Button5.bind("<Button-1>",dcall)
    Button5.pack()

    Static5 = tkinter.Label(text=u' ', background=back)
    Static5.pack()
#background

#foreground
    Static6 = tkinter.Label(text=u'モード切替',foreground=cor,background=back)
    Static6.pack()

# コンボボックスの生成
    combo = ttk.Combobox(root, state='readonly')
    combo["values"] = ("キーワード検索","指定のURLへ移動")
    combo.current(0)
    combo.pack()

    Static7 = tkinter.Label(text=u' ', background=back)
    Static7.pack()

    Button3 = tkinter.Button(text=u'閉じる',font=("",10))
    Button3.bind("<Button-1>",exitf)
    Button3.pack()
    root.mainloop()

except SystemExit:
    pass

except:
    with open('error.log', 'a') as fs:
        traceback.print_exc(file=fs)