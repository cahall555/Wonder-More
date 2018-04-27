#!/usr/bin/python
import PyPDF2
import pandas as pd
import numpy as np
import re

file = open('21step1.pdf','rb')
reader = PyPDF2.PdfFileReader(file)
page = reader.getPage(0)
lease = page.extractText()
lease = lease.split(" ")
print(lease)
class StateMachine:
    """State machine to use parameters as token. Token unlocks machine and searches document for
    parameters. Parameter results will be put in results when found. State machine starts in locked status"""
    state = "locked"

    def__init__(self, prameters, result):
        self.parameters = ["Community","Resident(s)","Apartment Unit Type","Unit Number","Lease Term","Base Rent","Pet Rent","Short Term Premium","Furniture Fee","Double Occupancy Premium","Base Rent","Payable for Lease Term","Equal Monthly installments","Application Fee","Administrative Fee","Security Deposit","Pet Deposit","Rent Concession","Rent Credit","Guarantor's Name"]
        self.result = []
        StateMachine.state = "locked"

    def start(self):

        
    def findParameters(self, parameters):
        for index in range(len(lease)):
            val = lease[index]
            for parameter in parameters:
                return.re.search()


