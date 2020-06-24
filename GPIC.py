from github import Github
import random
import time
import requests
import json

def send(data):
    Github("Himanshu-Cyber-Code", "Himanshu-Cyber-Code-GitHub-Pass").get_repo("Himanshu-Cyber-Code/QRlib").update_file(Github("Himanshu-Cyber-Code", "Himanshu-Cyber-Code-GitHub-Pass").get_repo("Himanshu-Cyber-Code/QRlib").get_contents("contact.json").path, "contact over IP", '{"data":"'+str(data)+'" , "check":"'+str(random.randint(0,99999999999999999999999999999999999999999999999999999999999999999999999999999999))+'"}', Github("Himanshu-Cyber-Code", "Himanshu-Cyber-Code-GitHub-Pass").get_repo("Himanshu-Cyber-Code/QRlib").get_contents("contact.json").sha)      

def recive():
    check = json.loads(requests.get("https://himanshu-cyber-code.github.io/QRlib/contact.json",headers={"Cache-Control": "no-cache","Pragma": "no-cache"}).text)
    check = check["check"]

    while(True):
        res = requests.get("https://himanshu-cyber-code.github.io/QRlib/contact.json",headers=headers).text
        res = json.loads(res)
        global check
        _check = res["check"]
        if(_check != check):
            print(res["data"])
            print("")
            check = _check
    
while(True):
    time.sleep(6)
    main()