import re
import time
from test_cases.mp_form.test_form\
    import test_get_creation_forms
import pytest

class TestExport:

    formid=""
    starttime=""
    endtime=""
    # 请求头的token,由前端获取用户的fuid后经过加密获得,测试环境没有区分
    headers = {"token": "60cb234cd01ab85a56eed20219aa72623feefe74253569a1047f8083ca4b0f15"}

    def test_export_excel(self,user1):
        """导出Excel数据
        selectColumns:隐藏列
        sortField:排序方式
        """
        form_res=test_get_creation_forms(user1)
        TestExport.formid = re.search('"formId":"(.*?)"', form_res.text)[1]
        TestExport.starttime=re.search('"actBeginTime":"(.*?)",', form_res.text)[1]
        TestExport.endtime=re.search('"actEndTime":"(.*?)",', form_res.text)[1]
        data={"startTime":TestExport.starttime,"endTime":TestExport.endtime,"dateType":"BY_MINUTE","cids":[0],"sortField":"TIME","sortType":"ASC","selectColumns":[]}
        res=user1.v1_export_formid_excel(TestExport.formid,TestExport.headers,data,method='post')
        assert res.status_code == 200
        assert res.data.get('message')=='操作成功'

    def test_export_image_archive(self,user1):
        """导出富媒体文件
        archiveType:汇总方式
        """
        data={"startTime":TestExport.starttime,"endTime":TestExport.endtime,"dateType":"BY_MINUTE",\
              "archiveType":1,"cids":["1"],"formId":TestExport.formid,"customList":[{"index":0,"value":-1}],"selectColumns":[]}
        res=user1.v1_export_formid_image_archive(TestExport.formid,TestExport.headers,data,method='post')
        assert res.status_code==200
        assert res.data.get('message') == '操作成功'

    def test_export_excel_image(self,user1):
        """导出excel带图文件"""
        data={"startTime":TestExport.starttime,"endTime":TestExport.endtime,"dateType":"BY_MINUTE",\
              "cids":[0],"sortField":"TIME","sortType":"ASC","selectColumns":[]}
        res=user1.v1_export_formid_excel_image(TestExport.formid,TestExport.headers,data,method='post')
        assert res.status_code == 200
        assert res.data.get('message') == '操作成功'

    def test_export_excel_url(self,user1):
        '''获取导出文件的url'''
        params={"pageSize":10,
                "pageOffset":0}
        time.sleep(3)
        res=user1.v1_formid_export_tasks(TestExport.formid,TestExport.headers,params,method='get')
        assert res.status_code == 200
        assert res.data.get('message') == '操作成功'


if __name__=="__main__":
    pytest.main()
