from selenium import webdriver
import base64
import time

message = "TmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA="
message2 ="TmV2ZXIgZ29ubmEgbGV0IHlvdSBkb3du"
message3 ="TmV2ZXIgZ29ubmEgcnVuIGFyb3VuZCBhbmQgZGVzZXJ0IHlvdQ=="
message4 = "TmV2ZXIgZ29ubmEgbWFrZSB5b3UgY3J5"
message5 = "TmV2ZXIgZ29ubmEgc2F5IGdvb2RieWU="
message6 = "TmV2ZXIgZ29ubmEgdGVsbCBhIGxpZSBhbmQgaHVydCB5b3U="

base64_bytes = message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')
print(message)

base64_bytes = message2.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message2 = message_bytes.decode('ascii')
print(message2)

base64_bytes = message3.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message3 = message_bytes.decode('ascii')
print(message3)

base64_bytes = message4.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message4 = message_bytes.decode('ascii')
print(message4)

base64_bytes = message5.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message5 = message_bytes.decode('ascii')
print(message5)

base64_bytes = message6.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message6 = message_bytes.decode('ascii')
print(message6)
time.sleep(2.5)
url = "https://bit.ly/3oBjY4L"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(2)

browser.find_element_by_xpath('//*[@id="movie_player"]/div[5]/button').click()
#browser.find_element_by_xpath('//*[@id="movie_player"]/div[32]/div[2]/div[1]/button').click()


