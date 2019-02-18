from lxml import etree
import urllib
url="https://www.3sgif.com/47840.html"
text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
"""
表达式	描述
nodename	选取此节点的所有子节点
/	从当前节点选取直接子节点
//	从当前节点选取子孙节点
.	选取当前节点
..	选取当前节点的父节点
@	选取属性
*	通配符，选择所有元素节点与元素名
@*	选取所有属性
[@attrib]	选取具有给定属性的所有元素
[@attrib='value']	选取给定属性具有给定值的所有元素
[tag]	选取所有具有指定元素的直接子节点
[tag='text']	选取所有具有指定元素并且文本内容是text节点

"""
def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    s=str(html,encoding="UTF-8")
    return s

def down_gif():
    print("downloading with xpath")
    s=gethtml(url)
    html=etree.HTML(s)
    #res=etree.tostring(html,encoding="UTF-8")
    #res=html.xpath('//body/section[@class="container"]/div[@class="content"]/article[@class="article-content"]/p')
    #res=html.xpath('//body//section[@class="container"]//div[@class="content"]//article[@class="article-content"]//p//img//@src')
    res=html.xpath('//article[@class="article-content"]//p//img//@src')
    print(res)
    #res=html.xpath()

if __name__=="__main__":
    down_gif()
"""
    html=etree.HTML(text) #初始化生成一个XPath解析对象
    result=etree.tostring(html,encoding='utf-8')   #解析对象输出代码
    print(type(html))
    print(type(result))
    print(result)

"""
