import configparser
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import telethon
import sys
import csv
import traceback
import time
import random
import os, sys
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def Name_banner():
   os.system('clear')
   print(f"""
    {gr}" Welcome to IIT DEVELOPER 
       	{re}╦ ╦ ╔╦╗{cy}╔═╗ ┌─┐ ┬ ┬ ╔═╗ ║  ╔═╗ ┌─┐┌─┐┬─┐
        {re}║ ║  ║ {cy}║ ║ ├┤  │ │ ├┤  ║  ║ ║ ├─┘├┤ ├┬┘
        {re}╩ ╩  ╩ {cy}╚═╝ └─┘  ─  ╚═╝ ╚═ ╚═╝ ┴  └─┘┴└─
        version : 2.0
        {re} Created By {cy} IIT DEVELOPER {gr}Team 
        """)
def setup_banner():
      Name_banner()
      print(f"""
	    {re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	    {re}╚═╗{cy}├┤  │ │ │├─┘
	    {re}╚═╝{cy}└─┘ ┴ └─┘┴
	    """)
def Help():
     print(gr+"[1] First Install Your Appliaction using Menu button 1 ")
     print(gr+"[2] second Step set Your with This Applictin like Give your API IS, Hash Id, And your No and you can reset any time  ")
     print(gr+"[3] Scrap data From any Group using Menu C button and it's work when your Setup Process already complated  ")
     print(gr+"[4]  ")
     menu()
  
  
  
def installapp():
     setup_banner()
     print(gr+"[+] Installing requierments ...")
     os.system('python -m pip install telethon')
     os.system('pip install telethon')
     os.system('clear')	
     print(gr+"[+] installation  Complate  !")
     menu()
      
def setupForScrape():
   setup_banner()
   os.system("touch configScrap.data")
   cpass = configparser.RawConfigParser()
   cpass.add_section('cred')
   xid = input(gr+"[+] enter api ID : "+re)
   cpass.set('cred', 'id', xid)
   xhash = input(gr+"[+] enter hash ID : "+re)
   cpass.set('cred', 'hash', xhash)
   xphone = input(gr+"[+] enter phone number : "+re)
   cpass.set('cred', 'phone', xphone)
   setup = open('configScrap.data', 'w')
   cpass.write(setup)
   setup.close()
   print(gr+"[+] setup complete !")
	
   menu()	
      
	
def setupForAddData():
   setup_banner()
   os.system("touch configAddData.data")
   cpass = configparser.RawConfigParser()
   cpass.add_section('cred')
   xid = input(gr+"[+] enter api ID : "+re)
   cpass.set('cred', 'id', xid)
   xhash = input(gr+"[+] enter hash ID : "+re)
   cpass.set('cred', 'hash', xhash)
   xphone = input(gr+"[+] enter phone number : "+re)
   cpass.set('cred', 'phone', xphone)
   setup = open('configAddData.data', 'w')
   cpass.write(setup)
   setup.close()
   print(gr+"[+] setup complete !")
   menu()	
             
                 
        
def scraper ():
 Name_banner()
 cpass = configparser.RawConfigParser()
 cpass.read('configScrap.data')
 try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
 except KeyError:
    Name_banner
    print(re+"[!] Go to menu and install application  !!\n")	
    sys.exit(1)
 client.connect()
 if not client.is_user_authorized():
    client.send_code_request(phone)
   
    Name_banner
    client.sign_in(phone, input(gr+'[+] Enter the code: '+re))
 
 os.system('clear')
 Name_banner
 chats = []
 last_date = None
 chunk_size = 500
 groups=[]
 
 result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
 chats.extend(result.chats)
 
 for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
 print(gr+'[+] Choose a group to scrape members :'+re)
 i=0
 for g in groups:
    print(gr+'['+cy+str(i)+']' + ' - ' + g.title)
    i+=1
 
 print('')
 g_index = input(gr+"[+] Enter a Number : "+re)
 target_group=groups[int(g_index)]
 
 print(gr+'[+] Fetching Members...')
 time.sleep(1)
 all_participants = []
 all_participants = client.get_participants(target_group, aggressive=True)
 
 print(gr+'[+] Saving In file...')
 time.sleep(1)
 with open("members.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])  
 os.system('clear')	
 print(gr+'[+] Members scraped successfully.  ')
 print(gr+'[+] Wait 5 second....  menu is Opening ')
 menu()
  
def AddMemberInGroup():	
 Name_banner()
 cpass = configparser.RawConfigParser()
 cpass.read('configAddData.data')

 try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
    async def main():
    # Now you can use all client methods listed below, like for example...
       await client.send_message('me', 'Hello !!!!!')
 
 except KeyError:
    os.system('clear')
    Name_banner()
    print(re+"[!] Goto Menu and first setup your Account for adding dara  !!\n")
    sys.exit(1)

 SLEEP_TIME_1 = 100
 SLEEP_TIME_2 = 100
 with client:
    client.loop.run_until_complete(main())
 client.connect()
 if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('40779'))

 users = []
 with open(r"members.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

 chats = []
 last_date = None
 chunk_size = 1000
 groups = []

 result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
 ))
 chats.extend(result.chats)

 for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

 print('Choose a group to add members:')
 i = 0
 for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

 g_index = input("Enter a Number: ")
 target_group = groups[int(g_index)]

 target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
 mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
 n = 0
 for user in users:
    n += 1
    if n % 80 == 0:
        time.sleep(60)
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Waiting for 60-180 Seconds...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("Some Technical Issu Found.Please Wait Second ..... Solving...")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
        print("Waiting for 5 Seconds...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue
	
 menu()
def menu():
    print("Main Menu Select any one ")
    time.sleep(1)
    print()
    choice = input("""
    A: Install Application 
    B: Setup Your Acount for scrapping Data
    C: Scrape Data From Group
    D: Setup Acount for Add Data in Group
    E: Add Member Into Group 
    H: How to Work this  
    Q: Quit/Log Out
    
    Please enter your choice: """)                  
    if choice == "A" or choice =="a":
         installapp () 
    elif choice == "B" or choice =="b":
         setupForScrape()        
    elif choice == "C" or choice =="c":
         scraper()
    elif choice=="D" or choice=="d":
         setupForAddData()
    elif choice == "E" or choice =="b":
         AddMemberInGroup()
    elif choice == "H" or choice =="c":
         Help() 
    elif choice=="Q" or choice=="q":
         sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()

	
	
def main():
     menu()   
main()


  
