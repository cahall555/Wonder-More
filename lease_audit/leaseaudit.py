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
print(leaseText)
class LeaseProcessing:
   
    def __init__(self, lease, prameters):
        self.parameters = prameters
        self.lease = lease 
        self.result = {}
    

    def findParameters(self):
        currentKeyword = None
        for index in range(len(self.lease)):
            val = self.lease[index]
            found = False
            for parameter in self.parameters:
                if parameter in val:
                    currentKeyword = parameter
                    found = True
            if found:
                print "Found keyword ", currentKeyword
                self.result [currentKeyword]=[]
            elif currentKeyword <> None:
                self.result [currentKeyword].append(val)


params = ["Community","Resident(s)","Apartment Unit Type","Unit Number","Lease Term","Base Rent","Pet Rent","Short Term Premium","Furniture Fee","Double Occupancy Premium","Base Rent","Payable for Lease Term","Equal Monthly installments","Application Fee","Administrative Fee","Security Deposit","Pet Deposit","Rent Concession","Rent Credit","Guarantor's Name"]

sm = LeaseProcessing(leaseText, params)
sm.findParameters()
print sm.result
