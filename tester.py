from exelreader import *
import requests
import json
table = ReadFromExel("test.xlsx", "FirstList")
realValue = []
predValue = []
#file = "Output.txt"
file = "BNZauto.txt"
for idx, row in table.iterrows():
    if idx > 0:
        reqValue = []
        for idx2, r in enumerate(row):
            if idx2 > 0:
                if(idx2 == len(table.columns)-1):
                    realValue.append(r)
                else:
                    reqValue.append(str(r).replace('.', ','))
        s =json.dumps(reqValue)
        re = requests.post(f"http://localhost:34976/FKB/GetConc?namefile={file}",
                          json=reqValue)
        predValue.append(re.text.replace(',','.').replace('"',''))
errAbs = 0
errCom = 0
for id3, val in enumerate(realValue):
    #print(f"{realValue[id3]} : {float(predValue[id3])} -- {abs(realValue[id3] - float(predValue[id3]))}")
    errAbs += abs(realValue[id3] - float(predValue[id3]))
    errCom += abs(realValue[id3] - float(predValue[id3]))/ max(realValue[id3],float(predValue[id3]))
print (f"Error abs: {errAbs/len(realValue)} /n Error Com: {errCom/len(realValue)}")


