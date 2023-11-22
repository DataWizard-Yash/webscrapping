import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.imdb.com/list/ls523102783/?ref_=watch_wchgd_1_1_m_wtw_netflix_nov23_i&sort=moviemeter,asc&st_dt=&mode=detail&page=1")


data = BeautifulSoup(req.content, "html.parser")

print(data.prettify)
# print(data.get_text)
