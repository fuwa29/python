#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 名前を返すcgi
import cgi

html_body = '''
<html>
<head><meta charset=utf-8></head>
<body>
</body>
<p>
あなたのお名前は<span style="font-size:48px"> %s </span>さんです！
</p>
</html>
'''

form = cgi.FieldStorage()

print('Content-type: text/html')
print(html_body % form['name'].value)
