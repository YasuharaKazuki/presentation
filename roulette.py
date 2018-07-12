#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ウィンドウを作成するためにインポート
from tkinter import *

# スレッドを作成するためにインポート
import threading

# sleep関数を使うためにインポート
from time import sleep

# ランダムな値を決定するためにrandomをインポート
import random

# 人名リスト
list = []

class Window:
    def __init__(self):
        self.flg = False
        self.root = Tk()
        
        # 画面サイズを設定
        self.root.geometry("1000x500")
        
        # 表示する文字を宣言
        self.txt = StringVar()

        # 発表者の宣言
        self.speaker = StringVar()
        
        # アニメーションを実現
        t = threading.Thread(target=timeshift, args=(self,))
        t.start()

        # 表示する文字のフォントなどを調整
        Label(self.root, textvariable=self.txt,font = ("", 60)).pack()

        # 表示する発表者のフォントなどを調整
        Label(self.root, textvariable=self.speaker,font = ("", 120)).pack()

        # ボタンを入力すると再帰的に発生
        Button(self.root, text="もう一度", command=self.changeLabel, font = ("", 30)).place(x=400, y=400)

    def changeLabel(self):
        # 発表者の初期化
        self.speaker.set("")

        # アニメーションを実現
        t = threading.Thread(target=timeshift, args=(self,))
        t.start()

# アニメーションで文字を表示する関数
def timeshift(w):
    w.txt.set("発表者は\n")
    sleep(1)
    w.txt.set("発表者は・\n")
    sleep(1)
    w.txt.set("発表者は・・\n")
    sleep(1)
    w.txt.set("発表者は・・・\n")
    sleep(2)
    w.speaker.set(str(list[random.randint(0, len(list) - 1)]) + "!\n")


if __name__ == '__main__':
    w = Window()
    w.root.mainloop()