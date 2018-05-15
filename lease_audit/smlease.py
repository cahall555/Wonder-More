#!/usr/bin/python
import PyPDF2
import pandas as pd
import numpy as np
import re

file = open('step1','rb')
reader = PyPDF2.PdfFileReader(file)
page = reader.getPage(0)
leaseText = page.extractText()
leaseText = leaseText.split(" ")
#print(leaseText)

currentState = ""

def setState(newState):
    global currentState
    #print("Current state: ",currentState,"New state: ",newState)
    currentState = newState

setState("start")

apartmentCommunity = ""
furnitureFee = ""

dict1 = {"Apartment":["looking for community"],"Community:":"Reading","Fee:":"looking for furniture fee"}

transition = {
    "state1": {
        "next_states": ["looking for community","looking for furnfee"],
        "accumulator": True,
        "invalid_state": "state1"
    },
    "state2": {
        "next_states": ["situated","Occupancy"],
        "accumulator": False,
        "invalid_state": "state1"
    }
}


for word in leaseText:
    for key in dict1:
        if key in word:
            setState(dict1.get(key))
        elif currentState == "Reading":
            if word == "situated":
                currentState = ""
            else:
                apartmentCommunity += word +" "
print(apartmentCommunity)

             
    