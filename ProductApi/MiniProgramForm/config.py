#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/3/23 14:56
"""
http://swagger.sui.work/pass/apidoc/share/show.htm?shareKey=8895efc612db2b171b1b78234060c562
"""
from settings.BaseConfig import Env

from settings.HostName import MiniProgramForm


class _Fuid:
    def __init__(self, test, uat, prodution=None):
        self._test = test
        self._uat = uat
        self._prodution = prodution or uat

    @property
    def fuid(self):
        env = Env()
        if env.is_test:
            return self._test
        elif env.is_uat:
            return self._uat
        else:
            return self._prodution


class UserFuid:
    user1 = _Fuid(test='1072705609905737732', uat='1032048209218088973').fuid  # ksw    1072705609905737732,uat:1074099735163650048    summer  1072705375733551112，uat:1032048209218088973
    user2 = _Fuid(test='1072705609905737732', uat='1028083468632055816').fuid  # moco
    user3 = _Fuid(test='1072705609905737732', uat='').fuid  # ksw
    kong_si_wen = _Fuid(test='1072705375733551112', uat='').fuid  # ksw    1072705609905737732    summer  1072705375733551112
    jiang_duan = _Fuid(test='1056011177739419657', uat='').fuid  # 蒋端
    zhou_ying = _Fuid(test='1027314905029545986', uat='').fuid  # 周莹
    hu_fei = _Fuid(test='1021591029641383937', uat='').fuid  # 胡斐
    hu_fei2 = _Fuid(test='1022245797535678549', uat='').fuid  # 胡斐2
    liu_peng_zhong = _Fuid(test='1021591279563182081', uat='').fuid  # 刘鹏忠
    chen_qi_lin = _Fuid(test='1040792416132530202', uat='').fuid  # 陈琦琳
    # user1 = _Fuid(test='1053828831317590037', uat='').fuid  # 已废弃的 UAT 用户
    # user2 = _Fuid(test='1059901948376911929', uat='').fuid  # 已废弃的 UAT 用户


class Test:
    HOSTNAME = MiniProgramForm.TEST
    APP_ID = 'wx1e766c9a00355017'
    DUFAULT_FUID = '1026957780256297009'

    # APP_ID = 'wxc67f6d90678e1fe4'  # 已废弃的 UAT
    # DUFAULT_FUID = '1053828831317590037'  # 已废弃的 UAT 用户

    class Url:
        """
        如果不是默认的域名 HOSTNAME， 可以传一个元组或列表，如:
        v1_login2 = ('https://hostname', '/v1/login2')
        """
        v1_login_test = '/v1/login_test'

        v1_operation_position = '/v1/operation_position'
        # v1_config = '/v1/config'
        v1_config = 'https://qun-oss1.feidee.cn/TCNF/config.json'
        wx_mp_link = "/wx_mp_link"

        v1_creation_forms = '/v1/creation_forms'
        v1_participation_forms = '/v1/participation_forms'
        # v1_examples = '/v1/examples'   已废弃
        v1_image = '/v1/image'
        v1_form = '/v1/form'
        v1_form_form_id = '/v1/form/{formId}'  # 已弃用
        v3_form_form_id = '/v1/form/{formId}'
        v2_form_id_form_data = '/v2/{formId}/form_data'
        v3_form_id_form_datas = '/v3/{formId}/form_datas'
        v1_form_id_status = '/v1/form/{formId}/status'
        v1_order_list_form_id = '/v1/order/list/{formId}'
        v1_order_form_id_order_id = '/v1/order/{formId}/{orderId}'
        v1_order_query_form_id_fuid = '/v1/order/query/{formId}/{fuid}'
        v1_order_form_id_order_id_remarks = '/v1/order/{formId}/{orderId}/remarks'
        v1_statistic_analysis_form_id = '/v1/statistic/analysis/{formId}'
        v1_statistic_detail_form_id = '/v1/statistic/detail/{formId}'
        v1_form_id_cycle_form_datas = '/v1/{formId}/cycle/form_datas'
        v2_form_id_cycle_participant = '/v2/{formId}/cycle/participant'
        v2_form_id_cycle_ranking = '/v2/{formId}/cycle/ranking'
        v1_form_id_participant_fuid = '/v1/{formId}/participant/{fuid}'

        v1_operation_forms = '/v1/operation_forms'
        v1_form_operation_operation_operation_form_id = '/v1/form_operation/operation/{operationFormId}'
        v1_form_operation_form_operation_form_id = '/v1/form_operation/form/{operationFormId}'
        v1_form_operation_template_operation_form_id = '/v1/form_operation/template/{operationFormId}'
        v1_templates_lit = '/v1/templates/list'
        v1_form_manager_invitation_code = '/v1/form/manager/invitation_code'
        v1_form_manager = '/v1/form/manager'
        v1_form_manager_form_id = '/v1/form/manager/{formId}'
        v1_form_managers_form_id = '/v1/form/managers/{formId}'
        v1_form_manager_poster = '/v1/form/manager/poster'
        v1_form_operation_official_account_form_id = '/v1/form_operation/official_account/{operationFormId}'
        v1_complaint = '/v1/complaint'
        v1_comlpaint_reason = '/v1/complaint/reason'
        v1_map_location_info = 'v1/map/location_info'
        v1_name_list = '/v1/name_list'  #废弃
        v1_namelist = '/v1/name_list/{nlid}' #废弃
        v1_export_url_name_list_nlid = '/v1/export_url/name_list/{nlid}'
        v1_export_name_list_nlid_ticket = '/v1/export/name_list/{nlid}'
        v1_form_id_sign_up = '/v1/{formId}/sign_up'
        v1_form_id_sign_up_form_data_id = '/v1/{formId}/sign_up/{formDataId}'
        v1_form_profile = '/v1/form/{formId}/profile'
        v1_form_catalog = 'v1/form/{formId}/catalog'
        v1_manager_forms = '/v1/manager_forms'
        v1_from_inform = '/v1/{formId}/inform'
        v1_form_id_remind = '/v1/remind/{formId}'
        v1_form_data_last = '/v1/{formId}/form_data/last'
        v1_form_data_owener = '/v1/{formId}/form_data/owner'

        v3_form_id_patch_status = '/v3/form/{formId}/patch/status'
        v3_form_id_patched_times = '/v3/form/{formId}/patched/times'
        v1_finish_page_banner = '/v1/finish_page_banner'
        v1_end_forms = '/v1/delete/forms/end'
        v1_end_forms_delete = '/v1/delete/forms/end'
        v1_delete_forms = '/v1/delete/forms'
        v1_form_id_participant_check = '/v1/form/{formId}/participation/check'
        v1_form_id_vote_cid = '/v1/form/{formId}/vote/{cid}'
        v1_form_id_page_style = '/v1/{formId}/pageStyle'
        v1_form_id_sign_up_delete = '/v1/{formId}/sign_up/{formDataId}'
        v2_export_excel_url = '/v2/export_excel_url/form/{formId}'
        v2_export_form_ticket = '/v2/export/form/{formId}'
        v1_export_attachment_url = '/v1/export_attachment_url/form/{formId}'
        v1_export_attachment_ticket = '/v1/export/attachment/form/{formId}'
        v1_export_excel = '/v1/export/{form_id}/excel'

        user_export_times = '/user/privilege/hasExportTimes'
        user_add_export_times = '/user/privilege/addExportTimes'
        user_get_export_times = '/user/privilege/getExportTimes'
        v1_form_like = '/v1/form/{formId}/like/{formDataId}'
        v1_form_comment_post = '/v1/form/{formId}/comment/{formDataId}'
        v1_form_comment_delete = '/v1/form/{formId}/comment/{formDataId}'
        v1_form_last_comment = '/v1/form/{formId}/userLastComment'
        v1_form_comment_page_get = '/v1/form/{formId}/comment/{formDataId}'
        v3_like_comment_rate_remark = '/v3/form/{formId}/likeCommentRateRemark'
        v1_form_rate_config = '/v1/form/{formId}/rateConfig'
        v1_form_rate = '/v1/form/{formId}/rate/{formDataId}'
        v1_overt_form_list = '/v1/overt_form/list'

        v1_name_used = '/v1/{formId}/name_list/used'
        v1_name_order_used = '/v1/{formId}/name_list/ordered_used'
        v1_name_form_data_list = 'v1/form/{formId}/nameListFormDataList'
        v1_form_name_list_template = '/v1/form/nameListTemplate'
        v1_name_list_form_datas = '/v1/{formId}/name_list/form_datas'
        v1_name_list_not_filled = '/v1/{formId}/name_list/not_filled'
        v1_name_list_filled_notify = '/v1/{formId}/name_list/filled_notify'
        v1_storage_space_regular_tips_ack = '/v1/storage_space/regular_tips_ack'  # 已废弃
        v1_storage_space_status = '/v1/storage_space/status'  #已废弃

        v1_form_data_delete = '/v1/delete/{formId}/form_data'
        v1_recycle_forms = '/v1/recycle/forms'
        v1_recycle_form = '/v1/recycle/form'
        v1_recycle_form_all = '/v1/recycle/form/all'
        v1_delete_form_data_dete = '/v1/delete/{formId}/form_data/date'
        v1_date_count = '/v1/delete/{formId}/form_data/date_count'
        v1_open_api_sign_up_developer = '/openapi/v1/signupDeveloper'
        v1_developer = '/openapi/v1/developer'

        #群组相关
        v1_group_member = '/v1/group_member/{groupId}'   # get/delete
        v1_group = '/v1/group'
        v1_group_operate = '/v1/group/{groupId}'  #/put/delete
        v1_group_admin = '/v1/group_member/super_admin/{groupId}' #post/delete
        v1_group_list ='/v1/group/group_list'
        v1_group_forms = '/v1/group/forms/{groupId}'
        v1_group_invite = '/v1/group/invite_token/{groupId}'
        v1_join_group = '/v1/group/join/{groupId}'
        v1_quit_group = '/v1/group/quit/{groupId}'





class Uat:
    APP_ID = 'wx3f32186d2340171c'
    HOSTNAME = MiniProgramForm.UAT
    DUFAULT_FUID = '1025186602202501154'

    class Url(Test.Url):
        pass


class Production(Uat):
    HOSTNAME = MiniProgramForm.PROD

    class Url:
        v1_config = 'https://qunoss1.qun100.con/PCNF/config.json'


# 上传图片接口是否使用缓存的 URL
USE_LOCAL_CACHE_URL = True
