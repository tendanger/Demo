# -*- coding:utf-8 -*-

import urllib.request

url = "http://www.renren.com/335099917/profile"

headers = {
    "Host" : "www.renren.com",
    "Connection" : "keep-alive",
    #"Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer" : "http://www.renren.com/SysHome.do",
    #"Accept-Encoding" : "gzip, deflate, sdch",
    "Cookie" : "anonymid=jdx9pfnd-nxt0sb; depovince=GW; jebecookies=8b36c7ae-a1dc-41e7-a2fc-bff2e970696d|||||; _r01_=1; JSESSIONID=abc8defwFmiPQaeENg5gw; ick_login=e6e34601-19df-4d01-ab3e-a767f520dc3c; _de=C6E53E292CEC75087D49636C5D3D4B7E696BF75400CE19CC; p=02673a8d3d88ff39614390c98e5899997; ap=335099917; first_login_flag=1; ln_uact=809967956@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20130619/0025/h_main_eGDF_ed370000038a113e.jpg; t=f263dff1a059afe4c3e99ec2458af5787; societyguester=f263dff1a059afe4c3e99ec2458af5787; id=335099917; xnsid=46e4dbd6; loginfrom=syshome",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
}

request = urllib.request.Request(url, headers = headers)

response = urllib.request.urlopen(request)

html = response.read()
html = html.decode("utf-8")
print(html)
