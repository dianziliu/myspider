import requests
import os
import urllib
import re
os.chdir("downpic")
path="urls.txt"
"""

<span class="article-nav-prev">上一篇<br><a href="https://www.3sgif.com/47814.html" rel="prev">GIF出处：美女gif出处不看后悔 口技很好！</a></span>
			<span class="article-nav-next">下一篇<br><a href="https://www.3sgif.com/47839.html" rel="next">GIF出处：经典gif动态出处 这腿你能玩多久？</a></span>

	<div class="article-paging"> <a href="https://www.3sgif.com/47838.html"><span>1</span></a> <a href="https://www.3sgif.com/47838.html/2/"><span>2</span></a> <span>3</span> <a href="https://www.3sgif.com/47838.html/4/"><span>4</span></a> <a href="https://www.3sgif.com/47838.html/5/"><span>5</span></a> <a href="https://www.3sgif.com/47838.html/6/"><span>6</span></a> <a href="https://www.3sgif.com/47838.html/7/"><span>7</span></a></div>  

    https://www.gifwu.net/wp-content/uploads/2018/06/IPZ-809.gif
"""


"""
print("downloading with requests")
url = "https://ac.qq.com/ComicView/index/id/512063/cid/143"
r = requests.get(url) 
with open("pic.png", "wb") as code:
    code.write(r.content)
"""

def gethtml(url):
    """
    获取网页的源代码，并转为string格式
    """
    page = urllib.request.urlopen(url)
    html = page.read()
    s=str(html,encoding="UTF-8")
    return s

def get_urls():
    """
    从一个url开始获取urls
    """
    print("****down fig****")
    with open(path,"w") as us:
        urls=["https://www.3sgif.com/47839.html"]
        print(urls)
        for i in range(49):
            try:
                s=get_prev_url(urls[i])
                urls.append(s)
                us.write(s+"\n")
            except:
                continue
        
        print("end")


def get_prev_url(url):
    """
    特定的前向访问
    """
    prev_prt=re.compile("上一篇<br><a href=\"https://www.3sgif.com/\d+\.html\" rel=\"prev\">")
    #start
    html=gethtml(url)
    #print(html)
    res=re.findall(prev_prt,html)
    return res[0][16:-13]

def get_gif_url(url):
    """
    通过正则找出gif图的url
    """

    gif_ptr=re.compile("<img src=.+\.gif\"")
    html=gethtml(url)
    res=re.findall(gif_ptr,html)
    return res[0][10:]
def down_gif():
    """
    下载gif的主要函数
    """
    i=25
    with open(path,"r") as us:
        for j in us.readlines():
            url=j[:-1]
            num=get_gif_numbers(url)
            print(num)
            for k in range(num):
                try:
                    gif_url=get_gif_url(url+"/"+str(k+1))
                    print(gif_url)
                    down(gif_url,str(i))
                except:
                    continue
                i=i+1

def get_gif_numbers(url):
    """
    获取一个网页中gif的数量
    """
    url_ptr=re.compile("<span>\d+</span>")
    html=gethtml(url)
    res=re.findall(url_ptr,html)
    return len(res)            
def down(url,i):
    """
    下载文件的函数
    """
    r = requests.get(url) 
    with open(i+".gif", "wb") as code:
        code.write(r.content)
if __name__=="__main__":
    down_gif()
