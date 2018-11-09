#!/usr/bin/python
#coding=utf-8
import json
import urllib
import requests
import bs4
import flaskTest.GongZongHaoWeb as gzh

class iciba:
    # 初始化
    def __init__(self, wechat_config):
        self.appid = wechat_config['appid']
        self.appsecret = wechat_config['appsecret']
        self.template_id = wechat_config['template_id']
        self.access_token = ''

    # 获取access_token
    def get_access_token(self, appid, appsecret):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid,appsecret)
        request = requests.post(url)
        data = json.loads(request.text)
        access_token = data['access_token']
        self.access_token = access_token
        return self.access_token

    # 发送消息
    def send_msg(self, openid, template_id):
        contents, title, newsURL=gzh.get_news()
        msg = {
            'touser': openid,
            'template_id': template_id,
            'url': "http://127.0.0.1:4501/ ",
            'data': {
                'content': {
                    'value': title,
                    'color': '#0000CD'
                    },
                'translation': {
                    'value': contents,
                }
            }
        }
        json_data = json.dumps(msg)
        if self.access_token == '':
            self.get_access_token(self.appid, self.appsecret)
        access_token = self.access_token
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % str(access_token)
        request = requests.post(url, data=json_data)
        return json.loads(request.text)

    # 为设置的用户列表发送消息
    def send_everyday_words(self, openids):
        for openid in openids:
            result = self.send_msg(openid, self.template_id)
            if result['errcode'] == 0:
                print(' [INFO] send to %s is success' % openid)
            else:
                print(' [ERROR] send to %s is error' % openid)

    # 执行
    def run(self, openids):
        self.send_everyday_words(openids)

if __name__ == '__main__':
    # 微信配置
    wechat_config = {
        'appid': 'wx82a11f2c86068d9e', #此处填写你的appid
        'appsecret': '7c2b206d19cc5b0f9e49d841acef672b', #此处填写你的appsecret
        'template_id': 'Pr8bzy5jN2d7-7K_cu8-3wypAVXk_81ImaeM9ZO5bYA' #此处填写你的模板消息ID
    }
    # 用户列表
    openids = [
        'oRh_C0tdUMPByJJsT0squ-C948WQ', #此处填写你的微信号
        #'xxxx', #如果有多个用户也可以
    #'xxxx',
    ]
    # 执行
    icb = iciba(wechat_config)
    icb.run(openids)