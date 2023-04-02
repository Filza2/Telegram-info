from requests import get
import re
print("""
████████╗███████╗██╗     ███████╗    ███╗   ██╗███████╗
╚══██╔══╝██╔════╝██║     ██╔════╝    ████╗  ██║██╔════╝
   ██║   █████╗  ██║     █████╗      ██╔██╗ ██║█████╗  
   ██║   ██╔══╝  ██║     ██╔══╝      ██║╚██╗██║██╔══╝  
   ██║   ███████╗███████╗███████╗    ██║ ╚████║██║     
   ╚═╝   ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝╚═╝                                                            

             By  @TweakPY - @vv1ck
""")
user=input("[?] Enter the user : ")
r=get(f"https://t.me/{user}")
try:
	if r.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
		print("[!] user Not Found !")
	else:
		try:
			username=re.findall(f'<title>Telegram: Contact (.*?)</title>',r.text)[0]
			name=re.findall(f'<meta property="og:title" content="(.*?)">',r.text)[0]
			description=re.findall(f'<meta property="og:description" content="(.*?)">',r.text)[0]
			try:
				subscribers_count=re.findall(f'<div class="tgme_page_extra">(.*?)</div>',r.text)[0]
				print(str(f'[+] username: [{username}]\n[+] name: [{name}]\n[+] description: [{description}]\n[+] subscribers count: [{subscribers_count}]\n------------------------'))
			except:print(str(f'[+] username: [{username}]\n[+] name: [{name}]\n[+] description: [{description}]\n------------------------'))
		except:print('[!] user Not valid')
except:print("[!] Error ...")
