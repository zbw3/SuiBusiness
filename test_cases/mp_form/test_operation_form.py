import pytest

def test_get_operation_forms(user1):
    """验证首页瀑布流表单展示"""
    tables = ['TUTORIAL_HELP', 'CASE_TEMPLATE']
    for table in tables:
        res = user1.v1_operation_forms(table, method=user1.GET)
        assert res.status_code == 200



def test_get_operation_form_content(user1):
    """验证运营贴详情（OPERATION、NORMAL、TEMPLATE）"""
    res1 = user1.v1_operation_forms("TUTORIAL_HELP", method=user1.GET)
    forms = res1.data.get('data').get('examples')
    print(len(forms))
    for i in range(len(forms)):
        if forms[i]['formType'] == 'OPERATION':
            res = user1.v1_form_operation_operation_operation_form_id(forms[i]['operationFormId'])
            assert res.status_code == 200
        elif forms[i]['formType'] == 'NORMAL':
            res = user1.v1_form_operation_form_operation_form_id(forms[i]['operationFormId'])
            assert res.status_code == 200
        else:
            res = user1.v1_form_operation_template_operation_form_id(forms[i]['operationFormId'])
            assert res.status_code == 200

def test_templates_list(user1):
    """获取模板表单列表"""
    tables = ['STATISTIC', 'INFORMATION', 'SHOPPING', 'SIGN_UP', 'QUESTIONNAIRE']
    for table in tables:
        res = user1.v1_templates_lit(table, method=user1.GET)
        assert res.status_code == 200

if __name__ == '__main__':
    pytest.main()










