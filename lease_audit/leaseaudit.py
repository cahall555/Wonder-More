import PyPDF2
import pandas as pd
import numpy as np
file = open('21step1.pdf','rb')
reader = PyPDF2.PdfFileReader(file)
page = reader.getPage(0)
lease = page.extractText()
leasel = lease.split()
leasel = pd.DataFrame(leasel)
