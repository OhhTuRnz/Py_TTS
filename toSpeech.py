# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:53:04 2022

@author: turnz
"""
# Import the required module for text 
# to speech conversion
from gtts import gTTS as gT
from pygame import mixer
import time

# This module is imported so that we can 
# play the converted audio
#import os
"*os.system calls cmd (windows in this case)*"
    
lang_dict = {1 : 'en', 2 : 'es'}

language = ' '

def main():
    global language
    print("Choose a language: ")
    print(*lang_dict.items(), sep = ', ')
    inp = int(input())
    while(inp not in lang_dict):
        print('Cant find that language')
        inp = input()
    change_lang(lang_dict.get(inp))


def foo():
    mixer.init()
    a = language
    try:
        obj = gT(text = "Tonto" if a == 'es' else 'dumbie', lang = a, slow = False)
        obj.save("Tontazo.mp3")
        mixer.music.load("Tontazo.mp3")
        mixer.music.play()
        while(mixer.music.get_busy()):
            time.sleep(1)
        mixer.quit()
    except Exception as e:
        print(str(e))
    
def change_lang(lang):
    if not lang in lang_dict.values():
        raise AssertionError('Language not found')
    global language
    language = lang