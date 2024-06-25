#? 어딘가에 접속할 때 사용하는 라이브러리
import requests
#? 정규식!
import re

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(out_addr)