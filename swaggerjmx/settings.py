# -*- coding: utf-8 -*-

"""
Parameter initialization is a global variable by default. When calling the relevant API,
you need to inherit the setting class and set the corresponding parameters.

"""


class Settings(object):
    """
    # swagger_url
    ST.swagger_url = 'https://www.baidu.com/'
    # 报告生成路径
    ST.report_path = 'jmx'
    """
    report_path = 'jmx'  # 默认在当前路径生成jmx文件夹
    swagger_url = None
