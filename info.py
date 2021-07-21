import os
import requests
import string
stream = os.popen('curl --silent http://127.0.0.1:4040/api/tunnels | jq .tunnels[0].public_url')
output = stream.read()

import string
sample_str = "{}".format(output)
last_chars = sample_str[7:]

p = last_chars[:26]

r= p[:-2]


url1= 'https://api.telegram.org/bot1718187783:AAGLVyeXsl0xWFhMM4fjYrV3ij7pE04HSt4/sendMessage?chat_id=-418475197&text=MAC-VNC'

url2= 'https://api.telegram.org/bot1718187783:AAGLVyeXsl0xWFhMM4fjYrV3ij7pE04HSt4/sendMessage?chat_id=-418475197&text={}'.format(r)
requests.get(url1)
requests.get(url2)
