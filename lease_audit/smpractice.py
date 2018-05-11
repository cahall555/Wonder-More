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
    print("Current state: ",currentState,"New state: ",newState)
    currentState = newState


setState("start")
apartmentCommunity = ""
furnitureFee = ""

for word in leaseText:
    if currentState == "start":
        if "Apartment" in word and apartmentCommunity=="":
            setState("looking for community")
        elif "Furniture" in word:
            setState("looking for furnfee")
    elif currentState == "looking for community":
        if word == "Community:":
            setState("reading A.C.")
        else:
            setState("start")
    elif currentState == "reading A.C.":
        if word == "situated":
            setState("start")
        else:
            apartmentCommunity += word +" "
    elif currentState == "looking for furnfee":
        if word == "Fee:":
            setState("reading furnfee")
        else:
            setState("start")
    elif currentState =="reading furnfee":
        if word == "Occupancy":
            setState("start")
        else:
            furnitureFee += word +" "

print apartmentCommunity, furnitureFee
