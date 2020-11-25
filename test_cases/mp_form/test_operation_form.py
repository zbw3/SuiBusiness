import pytest
from ProductApi.MiniProgramForm.form.enum import OperationFormType, TemplatesTabId

@pytest.mark.skip(reason='1.14.0版本已弃用运营帖分类')
def test_get_operation_forms(user1):
    """验证首页瀑布流表单展示"""
    tables = ['TUTORIAL_HELP', 'CASE_TEMPLATE']
    for table in tables:
        res = user1.v1_operation_forms(table, method=user1.GET)
        assert res.status_code == 200

def test_get_operation_forms_all(user1):
    """验证获取首页瀑布流所有表单数据, 1.14.0版本去除了分类tab"""
    res = user1.v1_operation_forms(table_id='NO_TAB', method=user1.GET)
    assert res.status_code == 200
    data = res.data.get('data')
    assert data.get('banners') == [], res.text
    assert len(data.get('examples')) > 0, res.text


def test_get_operation_form_content(user1):
    """验证运营贴详情（OPERATION、NORMAL、TEMPLATE、OFFICIAL_ACCOUNT）"""
    res1 = user1.v1_operation_forms("NO_TAB", method=user1.GET)
    forms = res1.data.get('data').get('examples')
    api_map = {
        OperationFormType.OPERATION: user1.v1_form_operation_operation_operation_form_id,
        OperationFormType.NORMAL: user1.v1_form_operation_form_operation_form_id,
        OperationFormType.TEMPLATE: user1.v1_form_operation_template_operation_form_id,
        OperationFormType.OFFICIAL_ACCOUNT: user1.v1_form_operation_official_account_form_id
    }
    for item in forms:
        res = api_map[OperationFormType(item['formType'])](item['operationFormId'])
        assert res.status_code == 200, res.text
        assert res.data.get('data'), res.text


def test_templates_list(user1):
    """获取模板中心表单列表"""
    for tab_id in TemplatesTabId:
        res = user1.v1_templates_lit(tab_id.value, method=user1.GET)
        assert res.status_code == 200, res.text
        assert res.data.get('data'), res.text


if __name__ == '__main__':
    pytest.main()
