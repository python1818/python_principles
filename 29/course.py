from bs4 import BeautifulSoup
import requests
# base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
# r = requests.get(base_url).content
# soup = BeautifulSoup(r,"html.parser")
# all_p = soup.find_all("p")
# print(all_p)
# for paragraph in all_p:
#     # print(paragraph.string)
#     if paragraph.string != None:
#         print(paragraph.string)
# base_url = "https://www.nytimes.com/section/politics"
# r = requests.get(base_url).content
# soup = BeautifulSoup(r,"html.parser")
# r = requests.get(base_url).content
# soup = BeautifulSoup(r,"html.parser")

# section  = soup.find("section",{"id":"stream-panel"})
# print(secrione)

# articleList = section.find_all("li",{"class":"css-ye6x8s"})
# print(articleList)
# for i in articleList:
#     print(i)
# for  i in articleList:
#     print(i.h2.text)
# for i in articleList:
#     if i.h2:
#         print(i.h2.)


base_url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

r = requests.get(base_url).text
soup = BeautifulSoup(r,"html.parser")

movie_list = soup.find("tbody",{"class":"lister-list"}).find_all