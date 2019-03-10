# from datetime import datetime, timedelta, timezone
# now = datetime.now()

# print(now)
# print(type(now))

# dt = datetime(2015, 4, 19, 12, 20)

# print(dt)

# dt.timestamp()

# t = 1429417200.0

# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t)) 

# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
# print(now.strftime('%a, %b %d %H:%M'))

# print(now + timedelta(hours=10))

# tz_utc_8 = timezone(timedelta(hours=8))

# dt = now.replace(tzinfo=tz_utc_8)

# print(dt)

# # datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))

# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)

# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))

# print(bj_dt)

# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)

# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)


# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# print(dd['key2'])


# from collections import OrderedDict
# print(dict([('a', 1), ('c', 2), ('b', 3)]))
# print(OrderedDict([('a', 1), ('b', 2), ('b', 3)]))

# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1

# print(c)


# import base64
# print(base64.b64encode(b'binary\x00string'))
# print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

# print(base64.urlsafe_b64decode('abcd--__'))

# n = 10240099
# b1 = (n & 0xff000000) >> 24

# import struct

# print(struct.pack('>I', 10240099))

# struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# print(struct.unpack('<ccIIIIIIHH', s))


# import hashlib

# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())


# import hashlib

# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# import hashlib

# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

# import hmac
# message = b'Hello, world!'
# key = b'secret'
# h = hmac.new(key, message, digestmod='MD5')
# # 如果消息很长，可以多次调用h.update(msg)
# h.hexdigest()

import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# import itertools
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
#     print(c)


# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)


# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# list(ns)

# for c in itertools.chain('ABC', 'XYZ'):
#         print(c)

# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))


# class Query(object):

#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('Begin')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')

#     def query(self):
#         print('Query info about %s...' % self.name)

# # with Query('Bob') as q:
# #     q.query()

# from contextlib import contextmanager

# class Query(object):

#     def __init__(self, name):
#         self.name = name

#     def query(self):
#         print('Query info about %s...' % self.name)

# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')

# with create_query('Bob') as q:
#     q.query()

# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)

# with tag("h1"):
#     print("hello")
#     print("world")

# from contextlib import closing
# from urllib.request import urlopen


# # @contextmanager
# # def closing(thing):
# #     try:
# #         yield thing
# #     finally:
# #         thing.close()

# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)

# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# from urllib import request

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# from urllib import request, parse

# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass

# from xml.parsers.expat import ParserCreate

# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

#     def end_element(self, name):
#         print('sax:end_element: %s' % name)

#     def char_data(self, text):
#         print('sax:char_data: %s' % text)

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''

# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)


from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')