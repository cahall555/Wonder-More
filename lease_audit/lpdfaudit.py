import PyPDF2
file = open('step1.pdf','rb')
reader = PyPDF2.PdfFileReader(file)
page = reader.getPage(0)
lease = page.extractText()
ll = lease.split()
print(ll[100])
audit = {"Property","Resident(s)","Apartment Unit Type","Unit Number","Lease Term","Base Rent","Pert Rent","Short Term Premium","Furniture Fee","Double Occupancy Premium","Base Rent","Payable for Lease Term","Equal Monthly installments","Application Fee","Administrative Fee","Security Deposit","Pet Deposit","Rent Concession","Rent Credit","Guarantor's Name"}
print(audit)
