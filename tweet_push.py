#-*- coding:utf-8 -*-

import tweepy, time
from tweepy import OAuthHandler

C_KEY = "Jh5WdFZkgLKg1wv4m3FrQ"
C_SECRET = "Rb1a5aK33jyRJTvFRDkbnnL8rw2onUhffPNvueVKmBE"

oauth = tweepy.OAuthHandler(C_KEY, C_SECRET)
oauth_url = oauth.get_authorization_url()

now = time.localtime()
make_time = str(now.tm_year) + "년" + str(now.tm_mon) + "월" + str(now.tm_mday) + "일 " + str(now.tm_hour) + ":" + str(now.tm_min) + ":" + str(now.tm_sec)
#print('Open the URL : ' + oauth_url)

#input_pin = input('PIN : ')
#oauth.get_access_token(input_pin)
#print("AK = '%s'" % oauth.access_token.key)
#print("AS = '%s'" % oauth.access_token.secret)

#A_KEY = "2233063692-IU93TlRfbcSBExvqi0ouAphNAOQgwszBFSV8P6v"
#A_SECRET = "pEXyyELmrPsVw2F1oHRTD24PnkBNm9K4Zian5IQK6kRI"

A_KEY = '2233063692-Y1Pc9biy3kUQ9aHgd2iZMTb4xkJ51ub78HbkOpo'
A_SECRET = 'vew3UAxcP6uJg19PQ4dug1smu3Xazt7aTKy0SVx1dXm1X'

oauth.set_access_token(A_KEY, A_SECRET)
api = tweepy.API(auth_handler=oauth, api_root='/1.1', secure=True)

api.update_status(make_time + '\nPIR Sensor detect motion! Check your home!')
