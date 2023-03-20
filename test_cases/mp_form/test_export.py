import re
import time
from test_cases.mp_form.test_form \
    import test_get_creation_forms
import pytest


class TestExport:
    formid = ""
    starttime = ""
    endtime = ""
    fuid = ""
    taskid = ""
    # 请求头的token,由前端获取用户的fuid后经过加密获得,测试环境没有区分
    headers = {"token": "60cb234cd01ab85a56eed20219aa72623feefe74253569a1047f8083ca4b0f15"}

    def test_getDownloadVersion(self, user1):
        """获取下载版本"""
        form_res = test_get_creation_forms(user1)
        TestExport.formid = re.search('"formId":"(.*?)"', form_res.text)[1]
        TestExport.starttime = re.search('"actBeginTime":"(.*?)",', form_res.text)[1]
        TestExport.endtime = re.search('"actEndTime":"(.*?)",', form_res.text)[1]
        TestExport.fuid = re.search('"fuid":"(.*?)"', form_res.text)[1]
        params = {"fuid": TestExport.fuid}
        res = user1.v1_pre_download_getDownloadVersion(params, method='get')
        assert res.status_code == 200

    def test_privilege_hasExportTimes(self, user1):
        """查看用户是否有下载次数
        exportType:导出类型"""
        params = {"exportType": 1, "formId": TestExport.formid, "userId": TestExport.fuid}
        res = user1.user_privilege_hasExportTimes(params, method='get')
        assert res.status_code == 200
        assert res.data.get("data") == 1

    def test_export_excel(self, user1):
        """导出Excel数据
        selectColumns:隐藏列
        sortField:排序方式
        """

        data = {"startTime": TestExport.starttime, "endTime": TestExport.endtime, "dateType": "BY_MINUTE", "cids": [0],
                "sortField": "TIME", "sortType": "ASC", "selectColumns": []}
        res = user1.v1_export_form_excel(TestExport.formid, TestExport.headers, data, method='post')
        TestExport.taskid = re.search('{"taskId":"(.*?)"}', res.text)[1]
        assert res.status_code == 200

    def test_form_cancel_export_task(self, user1):
        """取消导出任务"""
        res = user1.v1_form_cancel_export_task(TestExport.formid, TestExport.taskid, TestExport.headers, method='put')
        assert res.status_code == 200

    def test_export_image_archive(self, user1):
        """导出富媒体文件
        archiveType:汇总方式
        """
        data = {"startTime": TestExport.starttime, "endTime": TestExport.endtime, "dateType": "BY_MINUTE", \
                "archiveType": 1, "cids": ["1"], "formId": TestExport.formid, "customList": [{"index": 0, "value": -1}],
                "selectColumns": []}
        res = user1.v1_export_form_image_archive(TestExport.formid, TestExport.headers, data, method='post')
        assert res.status_code == 200

    def test_export_excel_image(self, user1):
        """导出excel带图文件"""
        data = {"startTime": TestExport.starttime, "endTime": TestExport.endtime, "dateType": "BY_MINUTE", \
                "cids": [0], "sortField": "TIME", "sortType": "ASC", "selectColumns": []}
        res = user1.v1_export_form_excel_image(TestExport.formid, TestExport.headers, data, method='post')
        assert res.status_code == 200

    def test_export_excel_url(self, user1):
        '''获取导出文件的url'''
        params = {"pageSize": 10, "pageOffset": 0}
        time.sleep(3)
        res = user1.v1_form_export_tasks(TestExport.formid, TestExport.headers, params, method='get')
        assert res.status_code == 200
        assert res.data.get('message') == '操作成功'

    def test_getExportTimes(self, user1):
        """获取导出次数"""
        params = {"formId": TestExport.formid}
        res = user1.user_privilege_getExportTimes(params, method='get')
        assert res.status_code == 200

    def test_check_form_change(self, user1):
        """检查表单更改"""
        res = user1.v1_check_form_change(TestExport.formid, TestExport.headers, method='get')
        assert res.status_code == 200
        assert res.data.get("message") == "操作成功"


if __name__ == "__main__":
    pytest.main()
