#portscan
nmap -sC -sV 10.10.11.196 -o nmap.out
nmap -sC -sV 10.10.11.196 -p- -o nmap-all-ports.out

#stocker.htb
feroxbuster --url http://stocker.htb/img/webp/ -A -C 404 -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-files.txt -X /usr/share/wordlists/seclists/Discovery/Web-content/raft-medium-extensions.txt
feroxbuster --url http://stocker.htb/img/webp/ -A -C 404 -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-files.txt -x /usr/share/wordlists/seclists/Discovery/Web-content/raft-medium-extensions.txt
gospider -s http://stocker.htb/ -u web--sitemap --robots  -o CTFs/HackTheBox/Stocker/gospider.txt
ffuf -H "Host: FUZZ.stocker.htb" -c -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u http://10.10.11.196 -fs 178


#dev.stocker.htb
## cookiemonster

## (no)SQLi
### manual checks
	ffuf -request dev-login.req -w /usr/share/wordlists/seclists/Fuzzing/special-chars.txt -v -debug-log ffuf-login.log #connection failed. apperently ffuf uses https by default
	ffuf -request dev-login.req -w /usr/share/wordlists/seclists/Fuzzing/special-chars.txt -v -debug-log ffuf-login.log -request-proto http #tried with other wordlists like big-list-of-naughty-strings.txt, Generic-SQLi.txt, NoSQL.txt

### scripts
python3 nosqli-json.py #nothing fancy
python3 nosqli-url.py > nosqli-json-output.txt # errors!!