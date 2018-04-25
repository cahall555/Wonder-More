#!/usr/bin/python
import PyPDF2
import pandas as pd
import numpy as np

file = open('21step1.pdf','rb')
reader = PyPDF2.PdfFileReader(file)
page = reader.getPage(0)
lease = page.extractText()
leasel = lease.split()

class StateMachine (State):
    def__init__(self):
        print (string(self))
        
    def findParameters(self, parameters)
      """ search for lease parameters""""
     for parameter in parameters:
        """input search loop here"""
parameters = ["Property","Resident(s)","Apartment Unit Type","Unit Number","Lease Term","Base Rent","Pert Rent","Short Term Premium","Furniture Fee","Double Occupancy Premium","Base Rent","Payable for Lease Term","Equal Monthly installments","Application Fee","Administrative Fee","Security Deposit","Pet Deposit","Rent Concession","Rent Credit","Guarantor's Name"]

leasel = pd.DataFrame(leasel)
findParameters(parameters)


