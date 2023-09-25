import pickle 
import time
import os
import random
import tkinter as tk
from tkinter import filedialog












#default dictionary
defdict = {"A": 1,
           "B": 2,
           "C": 3,
           "D": 4,
           "E": 5,
           "F": 6,
           "G": 7,
           "H": 8,
           "I": 9,
           "J": 10,
           "K": 11,
           "L": 12,
           "M": 13,
           "N": 14,
           "O": 15,
           "P": 16,
           "Q": 17,
           "R": 18,
           "S": 19,
           "T": 20,
           "U": 21,
           "W": 22,
           "X": 23,
           "Y": 24,
           "Z": 25,
           " ": 26
            }
#main functions
def Defaultdictsave():
    fp = open('D:\codw\python\crypt\Crypt\Dictionaries\defDictionary.pkl', 'wb')
    pickle.dump(defdict, fp)
def Load_dict():
    fp = open('Dictionaries/person_data.pkl', 'rb')
    print(pickle.load(fp)["A","B","C"," "])
def encrypt():
    print("What dictonary do you wanna use?")
    #root = tk.Tk()
    #root.withdraw()
    #fp = open(filedialog.askopenfilename(), 'rb')
 
    msg = input("what do you want to encrypt: ")

    
    print(len(msg))
    #print(pickle.load(fp)[msg])

def Genr():
    print(defdict["A"])
    
#start loop
def Start():

    while True:
        #commands are implimented with: if firstin == "command": ect
        print("Type 'help' if needed")
        firstin = input("Crypt>>: ")
        if firstin == "help":
            print("""
                  Dict-e   :   For encrypting mesages
                  Dict-d   :   For decrypting mesages
                  Gen-r    :   Generates a random dictionary

                  """)
            Start()
        if firstin == "Dict-e":
            encrypt()
            Start()
        if firstin =="Gen-r":
            
            Genr()
            Start()
        


        print("please re enter")
        Start()
#encrypt()
Defaultdictsave()
time.sleep(3)
#Start()