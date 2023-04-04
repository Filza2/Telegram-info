from rich.console import Console
from requests import get
import re,os

console=Console()

def header():
    os.system('cls' if os.name=='nt' else 'clear');console.print("""
████████╗███████╗██╗     ███████╗              ██╗███╗   ██╗███████╗ ██████╗ 
╚══██╔══╝██╔════╝██║     ██╔════╝              ██║████╗  ██║██╔════╝██╔═══██╗
   ██║   █████╗  ██║     █████╗      █████╗    ██║██╔██╗ ██║█████╗  ██║   ██║
   ██║   ██╔══╝  ██║     ██╔══╝      ╚════╝    ██║██║╚██╗██║██╔══╝  ██║   ██║
   ██║   ███████╗███████╗███████╗              ██║██║ ╚████║██║     ╚██████╔╝
   ╚═╝   ╚══════╝╚══════╝╚══════╝              ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                                                                                        
                             By  @TweakPY - @vv1ck
""")
header()
    
user=input("- Enter The username : ").strip();header()
try:
    r=get(f"https://t.me/{user}")
    if r.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:console.print("- [bold red]Error[/bold red], user Not Found !");exit()
    else:
        try:
            username=re.findall(f'<title>Telegram: Contact (.*?)</title>',r.text)[0]
            name=re.findall(f'<meta property="og:title" content="(.*?)">',r.text)[0];name=str(name).replace('\t', '')
            description=re.findall(f'<meta property="og:description" content="(.*?)">',r.text)[0];description=str(description).replace('\t', '')
            try:
                subscribers_count=re.findall(f'<div class="tgme_page_extra">(.*?)</div>',r.text)[0]
                console.print(f"""- username : [bold red]{username}[/bold red]
- Name : [bold red]{name}[/bold red]
- Description : [bold red]{description}[/bold red]
- Subscribers Count : [bold red]{subscribers_count}[/bold red]
- Type : [bold red]Channel[/bold red]""")
            except Exception as e:
                console.print(f"""- username : [bold red]{username}[/bold red]
- Name : [bold red]{name}[/bold red]
- Description : [bold red]{description}[/bold red]
- Type : [bold red]user[/bold red]""")
        except Exception as e:console.print("- [bold red]Error[/bold red], user Not Valid !");exit()
		
		
except Exception as e:console.print('- [bold red]Error ![/bold red]');exit()
