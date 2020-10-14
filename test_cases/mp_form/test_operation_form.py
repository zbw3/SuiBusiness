import pytest
from ProductApi.MiniProgramForm.form.enum import OperationFormType, TemplatesTabId


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
    api_map = {
        OperationFormType.OPERATION: user1.v1_form_operation_operation_operation_form_id,
        OperationFormType.NORMAL: user1.v1_form_operation_form_operation_form_id,
        OperationFormType.TEMPLATE: user1.v1_form_operation_template_operation_form_id
    }
    for item in forms:
        res = api_map[OperationFormType(item['formType'])](item['operationFormId'])
        assert res.status_code == 200, item


def test_templates_list(user1):
    """获取模板表单列表"""
    for tab_id in TemplatesTabId:
        res = user1.v1_templates_lit(tab_id.value, method=user1.GET)
        assert res.status_code == 200


if __name__ == '__main__':
    pytest.main()
