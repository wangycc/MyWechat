#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import urllib2
import cookielib
import json
import re
def search():
    url = "http://www.miaopai.com/miaopai/index_api?cateid=2002&per=20&page=1"
    url2 = "http://www.meipai.com/medias/hot"
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0')]
    urllib2.install_opener(opener)
    html = urllib2.urlopen(url).read()
    html2 = urllib2.urlopen(url2).read()
    rex = r'http://mvvideo2.meitudata.com/.*?mp4'
    rexx = r'http://mvimg1.meitudata.com/.*?320'
    value = re.findall(rex, html2)
    value2 = re.findall(rexx, html2)
    jo = json.loads(html)
    f = open('/root/Desktop/sp.html','wb')
    text = jo["result"]
    f.write('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>24小时最热视频</title><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1">     <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->     <title>全网24小时最热视频</title>      <!-- Bootstrap -->     <link href="dist/css/bootstrap.min.css" rel="stylesheet">     <link href="css/css.css" rel="stylesheet">      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->     <!-- WARNING: Respond.js doesnt work if you view the page via file:// -->     <!--[if lt IE 9]>       <script src="//cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>       <script src="//cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script><![endif]--><style>body {font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;background:#F4F2ED none repeat scroll 0% 0%;}</style></head><body class = "home-tempate"><div class = "container">')
    f.write('<center><div class="gradient"><div class="header"><h2>路人甲的视频小站</h2><p>以下视频收集新浪、美拍、秒拍网24小时内最热视频，如有侵权必删</p><div class="clearfix"><a href="http://stchat.cn/zhihu.html" class="btn btn-success btn-lg">Try it now!</a></div></div></div><br><div class="container-fluid">')
    for i in text:
        f.write('<div class="row-fluid">')
        f.write('<video src="'+i["channel"]["stream"]["base"]+'" controls="controls" width="320" height="240"' + 'poster="' + i["channel"]["pic"]["base"] + '.jpg"></video></div>')
    for (i,j) in zip(value,value2):
        f.write('<div class="row-fluid">')
        f.write('<video src="'+i+'" controls="controls" width="320" height="240"' + 'poster="' + j+ '"></video></div>')
    f.write("</div><center></div></html>")
    f.flush()
    f.close()

if __name__=='__main__':
    search()