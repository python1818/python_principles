from bs4 import BeautifulSoup
html_code="""  
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Eren</title>
</head>
<body>
    <h1>blue akadami<h1>
    <div class="group1">    
        <h2>python gencler kodlama basliyor kursu</h2>    
        <ul>
            <li>random modulu</li>
            <li>math modulu</li>
            <li>datatime modulu</li>
        </ul>
    </div>
    <div class="group2">    
        <h2>windows kursu</h2>    
        <ul>
            <li>exel kursu</li>
            <li>word kursu</li>
            <li>powerpoint modulu</li>
        </ul>
    </div>
    <p>merhaba python kullanıcıları</p>
    <img src="image.jpg" alt="">
    
</body>
</html>
"""
soup =BeautifulSoup(html_code, 'html.parser')
# print(soup.title.string)
# result= soup.find_all("h2")
# print(result[1])
# print(result[0])
# print(result[0].string)
# print(result[1].string)
# for i in result:
#     print(i.string)
# result1=soup.find("div",{"class":"group1"})
# result2=soup.find("div",{"class":"group2"}).find_all("li")
# print(result1)
# print (result2)
# for i in result2:
#     print(i.string)
import requests

r =requests.get("https://www.webtekno.com/").content
soup = BeautifulSoup(r,"html.parser")
print(soup)