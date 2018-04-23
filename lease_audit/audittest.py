#!/usr/bin/python
import re

import numpy as np
import pandas as pd
import PyPDF2


def extractDate(line):
    return re.search('[0-9]{2}/[0-9]{2}/[0-9]{4}',line).group(0) 
def extractDollar(line):
    return re.search('[\W0-9]{1,8}',line).group(0)
def extractApttype(line):
    return re.search('[0-5] Bed [0-5] Bath',line).group(0)
def extractProperty(line):
    return re.search('[a-zA-Z]{1,40}(?= situated)',line).group(0)

file = open('step1','rb')
reader = PyPDF2.PdfFileReader(file)
page = reader.getPage(0)
lease = page.extractText()
lease = lease.split(',')
for line in lease:
    if "Lease Term" in line:
        terms = line.split(':')
        for index in range(len(terms)):
            val = terms[index]
            if "Starting Date" in val:
                start = extractDate(terms[index+1])
            if "Ending Date" in val:
                end = extractDate(terms[index+1])
            if "Apartment Unit Type" in val:
                apttype = extractApttype(terms[index+1])
    if "Additional Monthly Rent (if applicable)" in line:
        monthly = line.split(':')
        for index in range(len(monthly)):
            mval = monthly[index]
            if "Pet Rent" in mval:
                petrent = extractDollar(monthly[index+1])
            if "Short Term Premium" in mval:
                shortterm = extractDollar(monthly[index+1])
            if "Furniture Fee" in mval:
                furniturefee = extractDollar(monthly[index+1])
            if "Double Occupancy Premium" in mval:
                doubleocc = extractDollar(monthly[index+1])
    if "Application Fee" in line:
        fee = line.split(':')
        for index in range(len(fee)):
            feeval = fee[index]
            if "Application Fee" in feeval:
                appfee = extractDollar(fee[index+1])
            if "Administrative Fee" in feeval:
                adminfee = extractDollar(fee[index+1])
            if "Security Deposit" in feeval:
                securitydeposit = extractDollar(fee[index+1])
            if "Pet Deposit" in feeval:
                petdeposit = extractDollar(fee[index+1])
            if "Special" in feeval:
                specialconcession = extractDollar(fee[index+1])
            if "Concession Amount" in feeval:
                recurringconcession = extractDollar(fee[index+1])
    if "BASIC TERMS" in line:
        basic = line.split(':')
        for index in range(len(basic)):
            basicval = basic[index]
            if "Apartment Community" in basicval:
                aptcommunity = extractProperty(basic[index+1])

print aptcommunity, start, end, apttype, petrent, shortterm, furniturefee, doubleocc, appfee
print adminfee, securitydeposit, petdeposit, specialconcession, recurringconcession
#print(lease)
