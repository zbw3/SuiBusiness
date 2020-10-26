#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/8/13 12:29
import json
import typing
from mitmproxy import proxy, options, flowfilter, ctx
from mitmproxy.http import HTTPFlow
from base64 import b64decode
from mitmdump import DumpMaster, Options
from ilogger import logger
from tabulate import tabulate
from collections import OrderedDict
from mitmproxy.addonmanager import Loader

import sys
sys.path.append(r'E:\随手记-客户端\自动化项目\SuiBusiness')

class ShowBuriedPoint:
    BUSINESS_ID = 'behaviour'
    DEPARTMENT_ID = 'minip'
    EVENTS = OrderedDict(
        etype=True,
        action=True,
        minip_name='群报数小程序',
        channelid='微信',
        platform=True,
        uid=None,
        open_id=None,
        union_id=None,
        event_time=True,
        system_name=True,
        system_version=True,
        network_type=True,
        brand=True,
        model=True,
        pixel_ratio=True,
        screen_width=True,
        screen_height=True,
        window_width=True,
        window_height=True,
        statusbar_height=True,
        language=True,
        wxversion=True,
        fontsize_setting=True,
        sdk_version=True,
        url=None,
        custom1=True
    )
    CUSTOM_1 = OrderedDict(
        form_id=None,
        form_type=None,
        dfrom=None,
        title=None,
        card_type=None,
    )

    def __init__(self):
        self.filter = '~m GET & ~u /logCollect/events'
        self.number = 0

    def load(self, loader: Loader):
        ctx.options.dumper_filter = self.filter

    def assert_field(self, fields: OrderedDict, data: dict):
        for key, value in fields.items():
            if value is True:
                assert data.get(key) is not None
            if value and value is not True:
                assert data.get(key) == value

    def request(self, flow: HTTPFlow):
        if flowfilter.match(self.filter, flow):
            self.number += 1
            logger.info('%0.3d %s', self.number, flow.request.url)
            content = flow.request.query.get('content')
            if content:
                content_decoded = b64decode(content).decode('utf-8')
                print(content_decoded, '\n')

                content_dict = json.loads(content_decoded)
                assert content_dict['commons']['businessID'] == self.BUSINESS_ID
                assert content_dict['commons']['departmentID'] == self.DEPARTMENT_ID
                events = content_dict['events']
                for event in events:
                    self.assert_field(self.EVENTS, event)
                    print(tabulate(
                        [[event.get(key, '<未上报>') for key in self.EVENTS.keys()]],
                        headers=self.EVENTS.keys(),
                        tablefmt="grid",
                        stralign='center',
                        numalign='center'
                    ))
                    print('=' * 200)
                    print('custom1:', event['custom1'])


addons = [
    ShowBuriedPoint()
]

if __name__ == '__main__':
    opts = Options(listen_host='0.0.0.0', listen_port=8889, termlog_verbosity='info', flow_detail=0, scripts=__file__)
    m = DumpMaster(opts)
    m.run()
