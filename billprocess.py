from datascience import*
import numpy as np
import pandas as pd
import re

def cleanDescription(array):
    return re.search('-AppID [0-9]{0,6}:[\Wa-zA-Z]{0,80}-',array).group()
    

#load csv file, select relevent tables and select appropriate date range. 
#$0 bills do not need to be processed.    
bill = Table.read_table('RealPageAccounting.csv')
bill = bill.select('BILL_NO','POSTING_DATE','CREATED_DATE','DUE_DATE','DESCRIPTION','MEMO','AMOUNT')
bill = bill.where('CREATED_DATE',are.equal_to('4/18/2018')).where('AMOUNT',are.above(0))

#Remove unique information from description to create a group-able/sum-able table. 
description = bill.column('DESCRIPTION')
newdescription = make_array([])
for i, val in enumerate(description):
    takeout = cleanDescription(val)
    start, end = val.split(takeout)
    keep = start +" "+ end
    newdescription=np.append(newdescription, keep)
bill.append_column('NEW',newdescription)
#Group by bill number and description to create a bill that is summarized and not detailed during upload.
sumamount = bill.select('BILL_NO','POSTING_DATE','CREATED_DATE','DUE_DATE','NEW','AMOUNT','MEMO').groups(['BILL_NO',
'POSTING_DATE','CREATED_DATE','DUE_DATE','NEW','MEMO'],sum).relabel('AMOUNT sum','AMOUNT')
totaldue = sumamount.select('BILL_NO','AMOUNT').group('BILL_NO',sum).relabel('AMOUNT sum','TOTAL_DUE')
final = sumamount.join('BILL_NO',totaldue)
print(final)
#Create billing upload
#final.to_csv('realpage.csv')
