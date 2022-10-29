import requests, re, json, random, os, time, sys

#----------- MODULE RICH -------------
from rich import print as prints
from rich.panel import Panel
#----------- MODULE IMPORT -------------
#from insta.dump import cok_ig
from dump import cok_ig

reed = "[bold red]"
blue = "[bold blue]"
class Mulai:

    def __init__(self):
        self.ses = requests.Session()
        self.yayanxd()

    def hapus_coki(self):
        try:os.remove("coki_ig.txt")
        except:pass

    def ua_ig(self):
        an = random.randint(4,12)
        tg = random.randint(111,999)
        xx = (f'Mozilla/5.0 (Linux; Android {an}; MYA-L22 Build/HUAWEIMYA-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36 Instagram 98.0.0.15.{tg} Android (23/{an}; 320dpi; 720x1192; HUAWEI; MYA-L22; HWMYA-L6737; mt6735; ru_KZ; 159526784')
        return xx

    def logo(self):
        if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
        elif "win" in sys.platform.lower():
            try:os.system("cls")
            except:pass
        else:
            try:os.system("clear")
            except:pass
        prints(f"""{blue}  ____             _         ______                  {reed} _____ _____ 
{blue} |  _ \           | |       |  ____|                 {reed}|_   _/ ____|
{blue} | |_) |_ __ _   _| |_ ___  | |__ ___  _ __ ___ ___  {reed}  | || |  __ 
{blue} |  _ <| '__| | | | __/ _ \ |  __/ _ \| '__/ __/ _ \ {reed}  | || | |_ |
{blue} | |_) | |  | |_| | ||  __/ | | | (_) | | | (_|  __/ {reed} _| || |__| |
{blue} |____/|_|   \__,_|\__\___| |_|  \___/|_|  \___\___| {reed}|_____\_____|
                        {reed}BY Yayan XD. @2022""")

    def login(self):
        self.logo()
        prints(Panel(" [!] masukan cookie insta akun tumbal anda", style="bold white"))
        coki = input("masukan cookie insta: ")
        try:
            id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
            po = self.ses.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":self.ua_ig()},cookies={"cookie":coki})
            xx = json.loads(po.text)
            if "full_name" in str(xx):
                nama = xx["user"]["full_name"]
                open("coki_ig.txt", "w").write(coki)
                prints(Panel(f"selamat [bold green]{nama}[/] cookie kamu valid", style="bold white", padding=(0,5)));time.sleep(3);self.yayanxd()
            elif "challenge_required" in str(xx):
                exit("[!] akun checkpoint")
            else:
                exit("[!] cookie invalid")
        except KeyError:
            exit("cookie invalid")
        except requests.ConnectionError:
            exit("\n[!] gagal menghubungkan ke internet")

    def yayanxd(self):
        self.logo()
        try:
            coki = open("coki_ig.txt", "r").read()
        except FileNotFoundError:
            self.login()
        try:
            id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
            po = self.ses.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":self.ua_ig()},cookies={"cookie":coki})
            xx = json.loads(po.text)
            if "full_name" in str(xx):
                nama = xx["user"]["full_name"]
            elif "challenge_required" in str(xx):
                print("[!] akun checkpoint");self.hapus_coki();time.sleep(3);self.login()
        except KeyError:
            print("\n[!] akun checkpoint");self.hapus_coki();time.sleep(3);self.login()
        except requests.ConnectionError:
            exit("\n[!] gagal menghubungkan ke internet")
        ip = self.ses.get("https://api.ipify.org/?format=json").json()["ip"]
        prints(Panel(f"     welcome [bold green]{nama}[/] in Brute Force Instagram",style="bold white", padding=(0,5)))
        prints(Panel.fit("""    [[bold cyan]01[/]] dump pengikut          [[bold cyan]04[/]] cek hasil crack
    [[bold cyan]02[/]] dump mengikuti         [[bold cyan]05[/]] bot auto followers
    [[bold cyan]03[/]] dump pencarian         [[bold red]00[/]] keluar ([bold red]logout[/])""", style="bold white", padding=(0,5)))
        cok = input("[?] pilih: ")
        if cok in ["", " "]:
            prints(Panel(" [!] jangan kosong", style="bold white", padding=(0,5)));time.sleep(2);self.yayanxd()
        elif cok in ["1", "01"]:
            cok_ig.Xnxx().pengikut()
        elif cok in ["2", "02"]:
            cok_ig.Xnxx().mengikut()
        elif cok in ["3", "03"]:
            cok_ig.Xnxx().pencarii()
        elif cok in ["4", "04"]:
            cok_ig.Xnxx().hsl_crac()
        elif cok in ["5", "05"]:
            exit("belum selesai")
        elif cok in ["0", "00"]:
            cok_ig.Xnxx().Keluaarr()
        else:
            prints(Panel(" [!] input yang bener", style="bold white", padding=(0,5)));time.sleep(2);self.yayanxd()

Mulai()