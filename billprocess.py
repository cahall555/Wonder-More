from datascience import*
import numpy as np
import pandas as pd
import re

def cleanDescription(array):
    return re.search('-AppID [0-9]{0,6}:[\Wa-zA-Z]{0,40} [\Wa-zA-Z]{0,40}-',array).group()
    

#load csv file, select relevent tables and select appropriate date range. 
#$0 bills do not need to be processed.    
bills= pd.read_csv('RealPageAccounting.csv')
bill = Table.read_table('RealPageAccounting.csv')
bill = bill.select('BILL_NO','POSTING_DATE','CREATED_DATE','DUE_DATE','DESCRIPTION','MEMO','AMOUNT')
bill = bill.where('CREATED_DATE',are.equal_to('4/18/2018')).where('AMOUNT',are.above(0))

#Remove unique information from description to create a group-able/sum-able table. 
description = bill.column('DESCRIPTION')
print(len(description))
newdescription = []
for i, val in enumerate(description):
    takeout = cleanDescription(val)
    start, end = val.split(takeout)
    keep = start +" "+ end
    newdescription.append(keep)
    #newdescription = newdescription.with_column('Description',newdescription)
newdescription = make_array(newdescription)
print(newdescription)
print(bill)
d = bill.append_column('New Description',newdescription)
print(d)
#Group by bill number and description to create a bill that is summarized and not detailed during upload.
calc = bill.select('BILL_NO','DESCRIPTION','AMOUNT')
calc = calc.groups(['BILL_NO','DESCRIPTION'],sum)
