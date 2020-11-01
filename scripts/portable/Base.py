
import tkinter
import copy
import sys,pickle
from tkinter import messagebox
from tkinter import ttk
import os
import webbrowser
import traceback
import tkinter.font as tkFont
import configparser
# this Softwere Defalut browser is keyword search 

print('')
print(' simple Base browser　Ver 1.5')
# 文字色の指定
cor="Black"
if os.path.isfile("./default.conf")==True:
    config = configparser.ConfigParser()
    config.read('./default.conf')
    cor=config['SECTION1'].get('color')
try:

    def resourcePath(filename):
      if hasattr(sys, "_MEIPASS"):
          return os.path.join(sys._MEIPASS, filename)
      return os.path.join(filename)

    def exitf(event):
        ret=messagebox.askyesno("Simple Base browser", "このプログラムを終了しますか?")
        if ret==True:
            root.destroy()
            sys.exit(1)
        else:
            return "break"

    def vf(event):
        global txt
        global combo
        with open("./url.DAT", 'rb') as f:
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
        txt.delete(0,tlkinter.END)
        return "break"

    root = tkinter.Tk()
    root.resizable(False, False)
    root['bg'] = 'grey'
    root.iconbitmap(default="./ifs.ico")
    Static1 = tkinter.Label(text=u' ', background='grey')
    Static4 = tkinter.Label(text=u' ', background='grey')

    root.title(u"Simple Base browser")
    root.geometry("400x350")

    fontStyle = tkFont.Font(family="Meiryo", size=20)

    Static1.pack()
    Static1.pack()

    lbl1 = tkinter.Label(text='Simple Base browser',foreground=cor, font=fontStyle,background="grey")
    lbl1.pack()

    Static2 = tkinter.Label(text=u' ',background='grey')
    Static2.pack()

# ラベルの生成
    lbl = tkinter.Label(text='検索キーワード',foreground=cor,background="grey")
    lbl.pack()
    txt = tkinter.Entry(width=20)
    txt.pack()
    Static4 = tkinter.Label(text=u' ', background='grey')
    Static4.pack()

# 検索ボタンの生成
    Button5 = tkinter.Button(text=u'検索',font=("",10))
    Button5.bind("<Button-1>",vf)
    Button5.pack()

    Static5 = tkinter.Label(text=u' ', background='grey')
    Static5.pack()
#background

#foreground
    Static6 = tkinter.Label(text=u'モード切替',foreground=cor,background="grey")
    Static6.pack()

# コンボボックスの生成
    combo = ttk.Combobox(root, state='readonly')
    combo["values"] = ("キーワード検索","指定のURLへ移動")
    combo.current(0)
    combo.pack()

    Static7 = tkinter.Label(text=u' ', background='grey')
    Static7.pack()

    Button3 = tkinter.Button(text=u'閉じる',font=("",10))
    Button3.bind("<Button-1>",exitf)
    Button3.pack()
    root.mainloop()

except:
    with open('error.log', 'a') as fs:
        traceback.print_exc(file=fs)