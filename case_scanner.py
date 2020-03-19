#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : case_scanner.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/2/14 9:47
import json
import os
import re
import sys
import time
import traceback
import unittest
from importlib.machinery import SourceFileLoader

import pymysql


log = lambda msg: print('[{}]   INFO: {}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), msg))


class ParserModuleCases:
    """
    解析unittest的测试用例信息
    """

    def __init__(self, file_path: str):
        self.module = self._import_module_from_file(file_path)

    @property
    def module_info(self):
        module_doc = self.module.__doc__

        def is_new_vesion(_doc):
            return re.compile('^(author|description|api_path|api_doc).+$', re.I | re.M).search(_doc)

        if module_doc:
            if is_new_vesion(module_doc):
                lines = module_doc.splitlines()
                info = {}
                for line in lines:
                    split_line = line.split(':', maxsplit=1)
                    if len(split_line) == 2:
                        info[split_line[0]] = split_line[1].strip()
                return info
            else:
                return {'description': module_doc.strip()}

        else:
            return {}

    @property
    def author(self):
        return getattr(self.module, 'AUTHOR', None) or getattr(self.module, 'author', None) or self.module_info.get(
            'author', 'unknown')

    @property
    def cases_name_info(self):
        """[{'method': 'method_name', 'case_doc': 'case_doc'}, ...]"""
        cases = []
        cases_name = self._get_cases_name()
        for module_name, class_name, method_name in cases_name:
            case_doc = getattr(getattr(self.module, class_name), method_name).__doc__
            cases.append({'method': method_name, 'case_doc': case_doc})
        return cases

    def _suite(self):
        return unittest.defaultTestLoader.loadTestsFromModule(self.module)

    def _get_cases_name(self):
        """
        <test_h5_open_api.OpenApiTest testMethod=test_v2_data>
        :return: [('test_h5_open_api', 'OpenApiTest', 'test_accountOriginalDataV1')
        """
        return re.findall('<(test.+?)\\.(.+?) testMethod=(.+?)>', str(self._suite()))

    @staticmethod
    def _import_module_from_file(module_file_path: str):
        if not module_file_path.endswith('.py'):
            raise Exception('Invalid module file! %s' % module_file_path)
        module_name = os.path.basename(module_file_path).replace('.py', '')
        return SourceFileLoader(module_name, module_file_path).load_module()


def get_test_case_name_info(file_path: str):
    """根据文件类型，返回用例文件的描述信息和用例信息"""
    parser = ParserModuleCases if file_path.endswith('.py') else ParserHrunCases
    test_case = parser(file_path)
    return test_case.module_info, test_case.cases_name_info, test_case.author


def gen_cases_data(product, project_name, startpath):
    """生成用例数据"""
    # 获取解释器路径和项目顶层路径
    sys_path = json.dumps([sys.executable, os.path.dirname(os.path.abspath(__file__))], ensure_ascii=False)
    startpath = os.path.abspath(startpath)
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S')
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                business_name = os.path.relpath(root, startpath)
                file_path = os.path.join(root, file)
                log(file_path)
                module_info, cases_name_info, author = get_test_case_name_info(file_path)
                yield {'product': product, 'sys_path': sys_path, 'project_name': project_name,
                       'project_path': startpath, 'business_name': business_name, 'file_name': file,
                       'file_description': module_info.get('description', ''),
                       'module_info': json.dumps({**module_info, 'case_count': len(cases_name_info)},  # 含用例头和用例数
                                                 ensure_ascii=False),
                       'case_name': json.dumps(cases_name_info, ensure_ascii=False),
                       'author': author, 'case_count': len(cases_name_info), 'create_time': cur_time,
                       'update_time': cur_time}


class DB:
    def __init__(self):
        self.conn = pymysql.connect(host='172.22.145.101', port=3306, user='DSJ_test_supper',
                                    passwd='c5f3cHH8fe_76c20c8d6#Hc030,f', db='test_bench_test',
                                    use_unicode=True, charset='utf8')
        self.cursor = self.conn.cursor()

    def execute(self, query, args: list):
        try:
            self.cursor.executemany(query, args=args)
        except Exception:
            self.conn.rollback()
            traceback.print_exc()
            raise Exception
        else:
            self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


db = DB()


def update_to_db(product, project_name, cases_data: list):
    """用例信息上传至数据库"""
    delete_cases_sql = """delete from tbl_file_case where product = %s and project_name=%s"""
    insert_cases_sql = """insert into tbl_file_case (product,project_name,project_path,business_name,file_name,
                                               file_description,module_info,case_name,author,sys_path,create_time,update_time) 
                    values (%(product)s,%(project_name)s,%(project_path)s,%(business_name)s,%(file_name)s,
                    %(file_description)s,%(module_info)s,%(case_name)s,%(author)s,%(sys_path)s,%(create_time)s,%(update_time)s)"""
    db.execute(delete_cases_sql, [(product, project_name)])
    db.execute(insert_cases_sql, cases_data)

    insert_cases_count_sql = """insert into tbl_case_count (product,project_name,`number`,create_time) 
                                values (%(product)s,%(project_name)s,%(number)s,%(create_time)s)"""
    cases_count = sum([case_data['case_count'] for case_data in cases_data])
    create_time = time.strftime('%Y-%m-%d %H:%M:%S')
    db.execute(insert_cases_count_sql,
               [{'product': product, 'project_name': project_name, 'number': cases_count, 'create_time': create_time}])


def _local_debug(cases_data):
    import subprocess
    from concurrent.futures import ThreadPoolExecutor

    def run_test(file):
        if file.endswith('.py'):
            subprocess.run(['python', '-m', 'unittest', file])
        else:
            subprocess.run(['hrun', file])

    cases_path = [os.path.join(case['project_path'], case['business_name'], case['file_name']) for case in cases_data]
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(run_test, cases_path)


def scan_run(projects, local_debug=False):
    """主运行函数"""
    log('开始搜索用例文件信息...')
    for project in projects:
        cases_data = list(gen_cases_data(project['product'], project['name'], project['case_path']))
        if cases_data:
            if os.getenv('runEnv'):
                update_to_db(project['product'], project['name'], cases_data)
                log('{} 用例数据上传成功！'.format(project['name']))
            elif local_debug:
                log('开始本地调试执行用例...')
                _local_debug(cases_data)
        else:
            log('路径无用例文件：{}'.format(project['case_path']))
    product = projects[0].get('product', 'NULL') if projects else None
    project_name_list = [item.get('name', '') for item in projects]
    projects_str = "', '".join(project_name_list)
    # 删除已经不存在的项目
    delete_projects_sql = f"""delete from tbl_file_case WHERE product = %s and project_name not in ('{projects_str}');"""
    db.execute(delete_projects_sql, [product])
    db.close()


if __name__ == '__main__':
    # case_scanning.py 应放在你pycharm项目的根目录下
    # name: 项目名称，一个projects可以加入多个项目，e.g. 接口测试项目、变量测试项目
    # case_path: 项目用例的顶层目录路径，相对的或绝对的都可
    # product: 产品线名称， 只能有一个产品线
    # 扫描的文件包含unittest中以 test_  Test_ TEST_ 开头的用例文件，每次扫描后都会全量更新
    # test_xxx.py 用例__doc__可包含用例描述信息，具体参考用例规范文档'
    # 上传用例前请先在本地调试好，可将local_debug=True取消注释'
    projects = [
        {'name': 'SuiBusiness',
         'case_path': 'SuiBusiness/test_cases',
         'product': '随手生意场景'},
    ]
    scan_run(projects,
             local_debug=True,
             )
