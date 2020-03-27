# -*- coding: utf-8 -*-


import datetime
import json
import sys
import time
import requests


class DingTalkWarn(object):
    def __init__(self, config):
        self.start_time = config['start_time']
        self.end_time = config['end_time']
        self.interval = config['interval']
        self.token = config['token']
        self.atMobiles = config['atMobiles']
        self.base_content = config['base_content']
        self.isAtAll = config['isAtAll']
        self.n = 0
        self.pre_time = None

    def send_msg(self):
        try:
            msg = {
                'msgtype': 'text',
                'text': {
                    'content': self.content
                }, 'at': {
                    'atMobiles': self.atMobiles,
                    'isAtAll': self.isAtAll
                }
            }
            api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
            headers = {'Content-Type': 'application/json;charset=utf-8'}
            data = requests.post(api, data=json.dumps(msg), headers=headers).json()
            return json.dumps(data)
        except Exception as e:
            return str(e)

    def scheduler(self):

        """

        当前时间 <开始时间 等待 interval 分钟
        当前时间>=开始时间 <=结束时间 每interval 分钟发送一次消息
        当前时间 > 结束时间 等待23小时

        """

        while True:
            now = datetime.datetime.now()
            self.str_now = now.strftime('%Y%m%d %H:%M:%S')
            self.today = self.str_now[:8]
            if self.pre_time is not None:
                if int(self.str_now[:8]) - int(self.pre_time[:8]) >0:#跨天清零
                    self.n = 0
            start_crontab_hour, start_crontab_minute = self.start_time.split(':')
            start_crontab_time = start_crontab_hour +  start_crontab_minute
            end_crontab_hour, end_crontab_minute = self.end_time.split(':')
            end_crontab_time = end_crontab_hour + end_crontab_minute
            now_hour, now_minute = self.str_now[9::][:5].split(':')
            if now_hour + now_minute > end_crontab_time: #当前时间 超过结束时间
                print('当前时间超过结束时间')
                time.sleep(60)
            else:#当前时间 <= 结束时间
                print('当前时间 <= 结束时间')
                if now_hour + now_minute < start_crontab_time: #小于开始时间
                    print('当前时间小于开始时间 轮询等待60秒')
                    time.sleep(60)
                else:
                    print('当前时间>=开始时间 且小于等于结束时间')
                    self.n += 1
                    self.content = self.base_content.format(**locals())
                    self.pre_time = self.str_now
                    self.send_msg()
                    time.sleep(self.interval*60)



if __name__ == '__main__':
    args = sys.argv
    start_time = '18:30'
    end_time = '20:35'
    interval = 30
    if '--start_time' in args:
        index = args.index('--start_time') + 1
        start_time = args[index]
    if '--end_time' in args:
        index = args.index('--end_time') + 1
        end_time = args[index]
    if '--interval' in args:
        index = args.index('--interval') + 1
        interval = int(args[index])
    token = '916406e0dcfbd3083ba3392cd6ab06da5ffaf580cfe48258ab8db6456f54902e'
    base_content = """\
当前时间:【{self.str_now}】
上次发送时间:【{self.pre_time}】
自【{self.start_time}】时起至【{self.end_time}】时止
间隔{self.interval}分钟发送一次
此次为【{self.today}】第【{self.n}】次发送消息
记得考勤打卡-填写发送日报-填写禅道\
"""
    atMobiles = ['18811788263']
    isAtAll = False
    config = {
        'start_time': start_time,
        'end_time': end_time,
        'interval': interval,
        'token': token,
        'base_content': base_content,
        'atMobiles': atMobiles,
        'isAtAll': isAtAll

    }
    obj = DingTalkWarn(config=config)
    obj.scheduler()


