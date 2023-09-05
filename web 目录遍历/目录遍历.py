# Time: 2023/5/24 15:18

import requests

url = "http://challenge-88fe15103038d8b0.sandbox.ctfhub.com:10080/flag_in_here"

for i in range(5):
    for j in range(5):
        url_final = url + "/" + str(i) + "/" + str(j)
        r = requests.get(url_final)
        r.encoding = "utf-8"
        get_file = r.text
        if "flag.txt" in get_file:
            print(url_final)

