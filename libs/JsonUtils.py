#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : JsonUtils.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/7/27 17:10
from typing import Union
from jsonpath import jsonpath


def json_diff(left: Union[list, dict], right: Union[list, dict]) -> list:
    """
    json 对象比较，以 left 对象为基准
    :param left: dict or list
    :param right:  dict or list
    :return: list
    """
    json_paths = jsonpath(left, '$..*', result_type='PATH')
    result = []
    if json_paths is False:  # left equal {} or []
        if left != right:
            return [{'path': '$', 'left_value': left, 'right_value': right}]
        return result

    for path in json_paths:
        left_value = jsonpath(left, path, result_type='VALUE')[0]
        if isinstance(left_value, (list, dict)):
            continue
        right_values = jsonpath(right, path, result_type='VALUE')  # 可能出现左边值有右边没有值的情况
        if isinstance(right_values, list):
            right_value = right_values[0]
            if left_value != right_value:
                result.append({'path': path, 'left_value': left_value, 'right_value': right_value})
        else:
            result.append({'path': path, 'left_value': left_value, 'right_value': '<JsonPathNotFound>'})
    return result
