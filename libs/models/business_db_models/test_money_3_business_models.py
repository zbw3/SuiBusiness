from peewee import *
from playhouse.shortcuts import model_to_dict

database = MySQLDatabase('test_money_3_business',
                         **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True,
                            'host': 'ssj0.testfeideedba.com', 'port': 3232, 'user': 'SSJ_feidee',
                            'password': 'Hf#df_6c#b7,d8d#2ee6_fe85H3d'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class AcquiringAccount(BaseModel):
    account_no = CharField()
    channel_type = IntegerField()
    create_time = DateTimeField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField()
    property = IntegerField()
    status = IntegerField()
    type = IntegerField()

    class Meta:
        table_name = 'acquiring_account'


class AcquiringCardQrcode(BaseModel):
    count = CharField(constraints=[SQL("DEFAULT ''")])
    create_by = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField()
    description = CharField(constraints=[SQL("DEFAULT ''")])
    export_status = CharField(constraints=[SQL("DEFAULT '0'")])
    export_time = CharField(constraints=[SQL("DEFAULT ''")])
    fid = BigAutoField()
    modify_time = DateTimeField()
    number = CharField(index=True)

    class Meta:
        table_name = 'acquiring_card_qrcode'


class AcquiringLeshuaRegister(BaseModel):
    account_bank = CharField(null=True)
    account_bank_name = CharField(null=True)
    account_cellphone = CharField(null=True)
    account_img = CharField(null=True)
    account_img_path = CharField(null=True)
    account_name = CharField(null=True)
    account_name_id_num = CharField(null=True)
    account_number = CharField(null=True)
    address = CharField(null=True)
    cashier_pic = CharField(null=True)
    cashier_pic_path = CharField(null=True)
    city = CharField(null=True)
    contact_cellphone = CharField(null=True)
    contact_name = CharField(null=True)
    create_time = DateTimeField()
    description = CharField(null=True)
    district = CharField(null=True)
    entrance_pic = CharField(null=True)
    entrance_pic_path = CharField(null=True)
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    food_pic = CharField(null=True)
    food_pic_path = CharField(null=True)
    id_card_bak_img = CharField(null=True)
    id_card_bak_img_path = CharField(null=True)
    id_card_front_img = CharField(null=True)
    id_card_front_img_path = CharField(null=True)
    id_card_name = CharField(null=True)
    id_card_number = CharField(null=True)
    indoor_pic = CharField(null=True)
    indoor_pic_path = CharField(null=True)
    legal_flag = CharField(constraints=[SQL("DEFAULT '1'")])
    licence_address = CharField(null=True)
    licence_code = CharField(null=True)
    licence_img = CharField(null=True)
    licence_img_path = CharField(null=True)
    licence_name = CharField(null=True)
    licence_valid_time_begin = CharField(null=True)
    licence_valid_time_end = CharField(null=True)
    mcc_code = CharField(null=True)
    merchant_id = CharField(null=True)
    modify_time = DateTimeField()
    non_leg_auth = CharField(constraints=[SQL("DEFAULT ''")])
    non_leg_auth_path = CharField(constraints=[SQL("DEFAULT ''")])
    non_leg_id_card_back = CharField(constraints=[SQL("DEFAULT ''")])
    non_leg_id_card_back_path = CharField(constraints=[SQL("DEFAULT ''")])
    non_leg_id_card_front = CharField(constraints=[SQL("DEFAULT ''")])
    non_leg_id_card_front_path = CharField(constraints=[SQL("DEFAULT ''")])
    province = CharField(null=True)
    short_name = CharField(null=True)
    status = CharField(null=True)
    store_id = BigIntegerField()
    type = CharField(constraints=[SQL("DEFAULT '1'")])
    unionpay_code = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'acquiring_leshua_register'


class AcquiringLeshuaStore(BaseModel):
    channel_id = BigIntegerField(unique=True)
    create_time = DateTimeField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    leshua_merchant_id = CharField(index=True)
    modify_time = DateTimeField()

    class Meta:
        table_name = 'acquiring_leshua_store'


class AcquiringMerchant(BaseModel):
    account_bank = CharField(constraints=[SQL("DEFAULT ''")])
    account_bank_name = CharField(constraints=[SQL("DEFAULT ''")])
    account_img = CharField(constraints=[SQL("DEFAULT ''")])
    account_name = CharField(constraints=[SQL("DEFAULT ''")])
    account_number = CharField(constraints=[SQL("DEFAULT ''")])
    address = CharField(constraints=[SQL("DEFAULT ''")])
    city = CharField(constraints=[SQL("DEFAULT ''")])
    contact_cellphone = CharField(constraints=[SQL("DEFAULT ''")])
    contact_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField()
    district = CharField(constraints=[SQL("DEFAULT ''")])
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    hand_idcard_img = CharField(constraints=[SQL("DEFAULT ''")])
    hide_status = CharField(constraints=[SQL("DEFAULT '0'")])
    id_card_bak_img = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_front_img = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_name = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_number = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_valid_time_begin = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_valid_time_end = CharField(constraints=[SQL("DEFAULT ''")])
    licence_code = CharField(constraints=[SQL("DEFAULT ''")])
    licence_img = CharField(constraints=[SQL("DEFAULT ''")])
    licence_valid_time_begin = CharField(constraints=[SQL("DEFAULT ''")])
    licence_valid_time_end = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField()
    name = CharField(constraints=[SQL("DEFAULT ''")])
    province = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    short_name = CharField(constraints=[SQL("DEFAULT ''")])
    table_address = CharField(constraints=[SQL("DEFAULT ''")])
    table_name = CharField(constraints=[SQL("DEFAULT ''")])
    table_phone = CharField(constraints=[SQL("DEFAULT ''")])
    wechat_personal_img = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'acquiring_merchant'


class AcquiringMerchantBook(BaseModel):
    book_id = BigIntegerField(index=True)
    channel_type = IntegerField()
    create_time = DateTimeField()
    description = CharField(constraints=[SQL("DEFAULT ''")])
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    inside_modify_time = DateTimeField()
    modify_time = DateTimeField()
    register_modify_time = DateTimeField()
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    source_channel = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = CharField()
    step_flag = IntegerField(constraints=[SQL("DEFAULT 0")])
    store_id = BigIntegerField(index=True)
    submit_modify_time = DateTimeField()

    class Meta:
        table_name = 'acquiring_merchant_book'


class AcquiringMerchantChannel(BaseModel):
    account_id = BigIntegerField()
    channel_type = IntegerField()
    create_time = DateTimeField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    index_no = IntegerField()
    modify_time = DateTimeField()
    rate = DecimalField()
    store_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'acquiring_merchant_channel'


class AcquiringMerchantStore(BaseModel):
    cashier_pic = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField()
    description = CharField(constraints=[SQL("DEFAULT ''")])
    entrance_pic = CharField(constraints=[SQL("DEFAULT ''")])
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    food_pic = CharField(constraints=[SQL("DEFAULT ''")])
    indoor_pic = CharField(constraints=[SQL("DEFAULT ''")])
    merchant_id = BigIntegerField(index=True)
    modify_time = DateTimeField()
    name = CharField(constraints=[SQL("DEFAULT ''")])
    status = CharField()

    class Meta:
        table_name = 'acquiring_merchant_store'


class AcquiringMerchantStoreLog(BaseModel):
    create_time = DateTimeField()
    fid = BigAutoField()
    memo = CharField(constraints=[SQL("DEFAULT ''")])
    new_status = CharField()
    old_status = CharField()
    operation_name = CharField()
    operator = CharField(constraints=[SQL("DEFAULT ''")])
    store_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'acquiring_merchant_store_log'


class AcquiringPushAgent(BaseModel):
    agent_name = CharField(constraints=[SQL("DEFAULT ''")])
    bankcard = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    idcard = CharField(constraints=[SQL("DEFAULT ''")])
    license = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    phone = CharField(constraints=[SQL("DEFAULT ''")], index=True)

    class Meta:
        table_name = 'acquiring_push_agent'


class AcquiringPushAgentStaff(BaseModel):
    agent_id = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    phone = CharField(constraints=[SQL("DEFAULT ''")], index=True)

    class Meta:
        table_name = 'acquiring_push_agent_staff'


class AcquiringPushMerchant(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    staff_id = BigIntegerField(index=True)
    store_id = BigIntegerField()

    class Meta:
        table_name = 'acquiring_push_merchant'


class AcquiringSwiftpassRegister(BaseModel):
    account_bank = CharField(constraints=[SQL("DEFAULT ''")])
    account_code = CharField(constraints=[SQL("DEFAULT ''")])
    account_img = CharField(constraints=[SQL("DEFAULT ''")])
    account_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    account_name = CharField(constraints=[SQL("DEFAULT ''")])
    address = CharField(constraints=[SQL("DEFAULT ''")])
    bank_city = CharField(constraints=[SQL("DEFAULT ''")])
    bank_id = CharField(constraints=[SQL("DEFAULT ''")])
    bank_name = CharField(constraints=[SQL("DEFAULT ''")])
    bank_province = CharField(constraints=[SQL("DEFAULT ''")])
    cashier_pic = CharField(constraints=[SQL("DEFAULT ''")])
    cashier_pic_path = CharField(constraints=[SQL("DEFAULT ''")])
    city = CharField(constraints=[SQL("DEFAULT ''")])
    contact_line = CharField(constraints=[SQL("DEFAULT ''")])
    county = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField()
    customer_phone = CharField(constraints=[SQL("DEFAULT ''")])
    description = CharField(constraints=[SQL("DEFAULT ''")])
    email = CharField(constraints=[SQL("DEFAULT ''")])
    entrance_pic = CharField(constraints=[SQL("DEFAULT ''")])
    entrance_pic_path = CharField(constraints=[SQL("DEFAULT ''")])
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    hand_idcard_img = CharField(constraints=[SQL("DEFAULT ''")])
    hand_idcard_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    id_card = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_bak_img = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_bak_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_front_img = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_front_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_valid_time_begin = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_valid_time_end = CharField(constraints=[SQL("DEFAULT ''")])
    id_code = CharField(constraints=[SQL("DEFAULT ''")])
    indoor_pic = CharField(constraints=[SQL("DEFAULT ''")])
    indoor_pic_path = CharField(constraints=[SQL("DEFAULT ''")])
    industr_id = CharField(constraints=[SQL("DEFAULT ''")])
    licence_code = CharField(constraints=[SQL("DEFAULT ''")])
    licence_img = CharField(constraints=[SQL("DEFAULT ''")])
    licence_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    licence_valid_time_begin = CharField(constraints=[SQL("DEFAULT ''")])
    licence_valid_time_end = CharField(constraints=[SQL("DEFAULT ''")])
    mch_type = CharField(constraints=[SQL("DEFAULT ''")])
    merchant_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    merchant_name = CharField(constraints=[SQL("DEFAULT ''")])
    merchant_short_name = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField()
    out_merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    principal = CharField(constraints=[SQL("DEFAULT ''")])
    principal_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    province = CharField(constraints=[SQL("DEFAULT ''")])
    status = CharField(constraints=[SQL("DEFAULT '0'")])
    store_id = BigIntegerField(index=True)
    tel = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'acquiring_swiftpass_register'


class AcquiringSwiftpassStore(BaseModel):
    channel_id = BigIntegerField(unique=True)
    create_time = DateTimeField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField()
    swiftpass_merchant_id = CharField(index=True)

    class Meta:
        table_name = 'acquiring_swiftpass_store'


class AcquiringTradeLeshuaPay(BaseModel):
    active_flag = CharField(null=True)
    amount = IntegerField(null=True)
    attach = CharField(null=True)
    bank_type = CharField(null=True)
    channel_datetime = CharField(null=True)
    channel_order_id = CharField(null=True)
    coupon = IntegerField(null=True)
    create_time = DateTimeField()
    discount_amount = IntegerField(null=True)
    error_code = CharField(null=True)
    error_msg = CharField(null=True)
    fid = BigAutoField()
    goods_tag = CharField(null=True)
    leshua_order_id = CharField(null=True)
    merchant_id = CharField()
    modify_time = DateTimeField()
    openid = CharField(null=True)
    out_transaction_id = CharField(null=True)
    pay_time = DateTimeField(null=True)
    pay_way = CharField(null=True)
    promotion_detail = CharField(null=True)
    resp_code = IntegerField(null=True)
    resp_msg = CharField(null=True)
    result_code = IntegerField(null=True)
    settlement_amount = IntegerField(null=True)
    status = IntegerField(null=True)
    sub_openid = CharField(null=True)
    third_order_id = CharField(unique=True)
    trade_type = CharField(null=True)

    class Meta:
        table_name = 'acquiring_trade_leshua_pay'


class AcquiringTradeLeshuaRefund(BaseModel):
    create_time = DateTimeField()
    discount_refund_amount = IntegerField(null=True)
    error_code = CharField(null=True)
    error_msg = CharField(null=True)
    fid = BigAutoField()
    leshua_order_id = CharField(null=True)
    leshua_refund_id = CharField(null=True)
    merchant_id = CharField()
    merchant_refund_id = CharField(unique=True)
    modify_time = DateTimeField()
    refund_amount = IntegerField(null=True)
    refund_detail = CharField(null=True)
    refund_time = DateTimeField(null=True)
    resp_code = IntegerField(null=True)
    resp_msg = CharField(null=True)
    result_code = IntegerField(null=True)
    settlement_refund_amount = IntegerField(null=True)
    status = IntegerField(null=True)
    third_order_id = CharField()
    total_amount = IntegerField(null=True)

    class Meta:
        table_name = 'acquiring_trade_leshua_refund'


class AcquiringTradeLog(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    memo = CharField(null=True)
    new_status = IntegerField()
    old_status = IntegerField()
    request = TextField(null=True)
    response = TextField(null=True)
    trans_no = CharField(index=True)

    class Meta:
        table_name = 'acquiring_trade_log'


class AcquiringTradePay(BaseModel):
    amount = IntegerField()
    channel_id = BigIntegerField()
    channel_trade_no = CharField()
    create_time = DateTimeField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField()
    org_account = CharField()
    org_trade_no = CharField()
    pay_amount = IntegerField()
    pay_org = IntegerField()
    pay_status = IntegerField()
    pay_time = IntegerField()
    pay_type = IntegerField()
    trans_no = CharField(unique=True)

    class Meta:
        table_name = 'acquiring_trade_pay'


class AcquiringTradeRefund(BaseModel):
    amount = IntegerField()
    channel_id = BigIntegerField()
    channel_refund_no = CharField()
    create_time = DateTimeField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField()
    org_refund_no = CharField()
    refund_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    refund_status = IntegerField()
    refund_time = IntegerField()
    refund_trans_no = CharField(unique=True)
    trans_no = CharField(index=True)

    class Meta:
        table_name = 'acquiring_trade_refund'


class AcquiringTradeSwiftpassPay(BaseModel):
    appid = CharField(null=True)
    bank_billno = CharField(null=True)
    bank_type = CharField(null=True)
    coupon_fee = IntegerField(null=True)
    create_time = DateTimeField()
    err_code = CharField(null=True)
    err_msg = CharField(null=True)
    fee_type = CharField(null=True)
    fid = BigAutoField()
    is_subscribe = CharField(null=True)
    mch_id = CharField()
    message = CharField(null=True)
    modify_time = DateTimeField()
    openid = CharField(null=True)
    out_trade_no = CharField(unique=True)
    out_transaction_id = CharField(null=True)
    result_code = CharField(null=True)
    status = CharField(null=True)
    third_order_no = CharField(null=True)
    time_end = CharField(null=True)
    total_fee = IntegerField(null=True)
    trade_state = CharField(null=True)
    trade_type = CharField(null=True)
    transaction_id = CharField(null=True)

    class Meta:
        table_name = 'acquiring_trade_swiftpass_pay'


class AcquiringTradeSwiftpassRefund(BaseModel):
    coupon_refund_fee = IntegerField(null=True)
    create_time = DateTimeField()
    err_code = CharField(null=True)
    err_msg = CharField(null=True)
    fid = BigAutoField()
    mch_id = CharField()
    message = CharField(null=True)
    modify_time = DateTimeField()
    out_refund_no = CharField(unique=True)
    out_trade_no = CharField()
    refund_channel = CharField(null=True)
    refund_count = IntegerField(null=True)
    refund_fee = IntegerField(null=True)
    refund_id = CharField(null=True)
    refund_status = CharField(null=True)
    refund_time = CharField(null=True)
    result_code = CharField(null=True)
    status = CharField(null=True)
    transaction_id = CharField(null=True)

    class Meta:
        table_name = 'acquiring_trade_swiftpass_refund'


class AcquiringTradeYeepayPay(BaseModel):
    bank_card_no = CharField(null=True)
    bank_id = CharField(null=True)
    bank_order_id = CharField(null=True)
    bank_pay_success_date = CharField(null=True)
    bank_trx_id = CharField(null=True)
    biz_channel_id = CharField(null=True)
    cal_fee_merchant_no = CharField(null=True)
    card_type = CharField(null=True)
    cash_fee = CharField(null=True)
    code = CharField(null=True)
    create_time = DateTimeField()
    customer_fee = CharField(null=True)
    fid = BigAutoField()
    fund_process_type = CharField(null=True)
    have_accounted = CharField(null=True)
    merchant_fee = CharField(null=True)
    merchant_no = CharField(index=True)
    message = CharField(null=True)
    mobile_phone_no = CharField(null=True)
    modify_time = DateTimeField()
    open_id = CharField(null=True)
    order_amount = CharField(null=True)
    order_id = CharField(unique=True)
    pay_amount = CharField(null=True)
    pay_success_date = CharField(null=True)
    payment_product = CharField(null=True)
    payment_status = CharField(null=True)
    payment_sys_no = CharField(null=True)
    platform_type = CharField(null=True)
    request_date = CharField(null=True)
    residual_divide_amount = CharField(null=True)
    settlement_fee = CharField(null=True)
    status = CharField(null=True)
    union_id = CharField(null=True)
    unique_order_no = CharField(null=True)
    yp_settle_amount = CharField(null=True)

    class Meta:
        table_name = 'acquiring_trade_yeepay_pay'


class AcquiringTradeYeepayRefund(BaseModel):
    code = CharField(null=True)
    create_time = DateTimeField()
    dis_account_amount = CharField(null=True)
    fid = BigAutoField()
    merchant_no = CharField(index=True)
    message = CharField(null=True)
    modify_time = DateTimeField()
    order_id = CharField(index=True)
    real_deduct_amount = CharField(null=True)
    real_refund_amount = CharField(null=True)
    refund_amount = CharField(null=True)
    refund_request_date = CharField(null=True)
    refund_request_id = CharField(unique=True)
    refund_success_date = CharField(null=True)
    return_customer_fee = CharField(null=True)
    return_merchant_fee = CharField(null=True)
    status = CharField(null=True)
    unique_order_no = CharField(null=True)
    unique_refund_no = CharField(null=True)

    class Meta:
        table_name = 'acquiring_trade_yeepay_refund'


class AcquiringTransaction(BaseModel):
    account_id = BigIntegerField(index=True)
    app_id = IntegerField()
    balance_no = CharField()
    balance_status = IntegerField()
    balance_time = IntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    currency = CharField()
    discount_amount = IntegerField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_desc = CharField()
    order_name = CharField()
    order_no = CharField(index=True)
    order_type = IntegerField()
    pay_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_time = IntegerField()
    poundage_amount = IntegerField()
    rate = DecimalField()
    real_amount = IntegerField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    request_device = CharField(constraints=[SQL("DEFAULT ''")])
    request_ip = CharField(constraints=[SQL("DEFAULT ''")])
    total_amount = IntegerField()
    trans_no = CharField(unique=True)
    trans_type = IntegerField()

    class Meta:
        table_name = 'acquiring_transaction'


class AcquiringUser(BaseModel):
    create_time = DateTimeField()
    dbid = IntegerField()
    feidee_user = BigIntegerField(unique=True)
    fid = BigAutoField()
    modify_time = DateTimeField()

    class Meta:
        table_name = 'acquiring_user'


class AcquiringUserDayTrade(BaseModel):
    calc_date = CharField()
    cashback_amout = DecimalField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    trade_amount = DecimalField()

    class Meta:
        table_name = 'acquiring_user_day_trade'
        indexes = (
            (('calc_date', 'feidee_user'), True),
        )


class AcquiringYeepayRegister(BaseModel):
    account_img = CharField(constraints=[SQL("DEFAULT ''")])
    account_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    bank_city = CharField(constraints=[SQL("DEFAULT ''")])
    bank_province = CharField(constraints=[SQL("DEFAULT ''")])
    card_no = CharField(constraints=[SQL("DEFAULT ''")])
    cashier_pic = CharField(constraints=[SQL("DEFAULT ''")])
    cashier_pic_path = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField()
    description = CharField(constraints=[SQL("DEFAULT ''")])
    entrance_pic = CharField(constraints=[SQL("DEFAULT ''")])
    entrance_pic_path = CharField(constraints=[SQL("DEFAULT ''")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    hand_corp_code = CharField(constraints=[SQL("DEFAULT ''")])
    hand_corp_code_path = CharField(constraints=[SQL("DEFAULT ''")])
    head_bank_code = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_bak_img = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_bak_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_front_img = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_front_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    legal_id_card = CharField(constraints=[SQL("DEFAULT ''")])
    legal_name = CharField(constraints=[SQL("DEFAULT ''")])
    licence_img = CharField(constraints=[SQL("DEFAULT ''")])
    licence_img_path = CharField(constraints=[SQL("DEFAULT ''")])
    mer_address = CharField(constraints=[SQL("DEFAULT ''")])
    mer_cert_no = CharField(constraints=[SQL("DEFAULT ''")])
    mer_city = CharField(constraints=[SQL("DEFAULT ''")])
    mer_district = CharField(constraints=[SQL("DEFAULT ''")])
    mer_full_name = CharField(constraints=[SQL("DEFAULT ''")])
    mer_legal_phone = CharField(constraints=[SQL("DEFAULT ''")])
    mer_province = CharField(constraints=[SQL("DEFAULT ''")])
    mer_short_name = CharField(constraints=[SQL("DEFAULT ''")])
    merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField()
    request_no = CharField(constraints=[SQL("DEFAULT ''")])
    status = CharField(constraints=[SQL("DEFAULT '0'")])
    store_id = BigIntegerField()

    class Meta:
        table_name = 'acquiring_yeepay_register'


class AcquiringYeepayStore(BaseModel):
    channel_id = BigIntegerField(unique=True)
    create_time = DateTimeField()
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField()
    yeepay_hmac_key = CharField()
    yeepay_merchant_id = CharField(index=True)

    class Meta:
        table_name = 'acquiring_yeepay_store'


class BizAccount(BaseModel):
    amount = DecimalField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    currency = CharField()
    fid = BigAutoField()
    icon_name = CharField(constraints=[SQL("DEFAULT ''")])
    icon_url = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    system_type = IntegerField()
    the_group = IntegerField()
    the_order = IntegerField()
    trading_entity = BigIntegerField(index=True)
    type = IntegerField()

    class Meta:
        table_name = 'biz_account'


class BizBookAuthCode(BaseModel):
    auth_code = CharField(unique=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_book_auth_code'


class BizBookConfig(BaseModel):
    config_key = CharField()
    config_value = CharField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_book_config'
        indexes = (
            (('trading_entity', 'config_key'), True),
        )


class BizBookQrCode(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    db_id = IntegerField()
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    qr_code = CharField(unique=True)
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_book_qr_code'


class BizBookStoreAddress(BaseModel):
    address_no = CharField(primary_key=True)
    city = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    detailed_address = CharField(constraints=[SQL("DEFAULT ''")])
    district = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    province = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'biz_book_store_address'


class BizBookStoreInfo(BaseModel):
    address = CharField(constraints=[SQL("DEFAULT ''")])
    city = CharField(constraints=[SQL("DEFAULT ''")])
    county = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    db_id = IntegerField()
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    province = CharField(constraints=[SQL("DEFAULT ''")])
    store_code = CharField(unique=True)
    store_icon = CharField(constraints=[SQL("DEFAULT ''")])
    store_key = CharField(constraints=[SQL("DEFAULT ''")])
    store_name = CharField(constraints=[SQL("DEFAULT ''")])
    template_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(unique=True)

    class Meta:
        table_name = 'biz_book_store_info'


class BizBookStoreInfoExtend(BaseModel):
    address_no = CharField(constraints=[SQL("DEFAULT ''")])
    biz_hours_begin = CharField(constraints=[SQL("DEFAULT ''")])
    biz_hours_end = CharField(constraints=[SQL("DEFAULT ''")])
    fee = IntegerField(constraints=[SQL("DEFAULT 500")])
    fid = BigAutoField()
    logistics_begin = CharField(constraints=[SQL("DEFAULT ''")])
    logistics_end = CharField(constraints=[SQL("DEFAULT ''")])
    logistics_phone = CharField(constraints=[SQL("DEFAULT ''")])
    logistics_range_desc = CharField(constraints=[SQL("DEFAULT ''")])
    logistics_type = CharField(constraints=[SQL("DEFAULT '0'")])
    store_phone = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField(unique=True)

    class Meta:
        table_name = 'biz_book_store_info_extend'


class BizBookStoreRelation(BaseModel):
    account_id = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField()
    store_id = BigIntegerField()
    the_order = IntegerField()
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_book_store_relation'


class BizCardApply(BaseModel):
    address_id = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    express_name = CharField(constraints=[SQL("DEFAULT ''")])
    express_no = CharField(constraints=[SQL("DEFAULT ''")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    store_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_card_apply'


class BizCardApplyAddress(BaseModel):
    address = CharField(constraints=[SQL("DEFAULT ''")])
    channel = CharField(constraints=[SQL("DEFAULT '1'")])
    city = CharField(constraints=[SQL("DEFAULT ''")])
    county = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    phone = CharField(constraints=[SQL("DEFAULT ''")])
    province = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_card_apply_address'
        indexes = (
            (('feidee_user', 'trading_entity'), False),
        )


class BizCategory(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    icon_name = CharField(constraints=[SQL("DEFAULT ''")])
    icon_url = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField()
    parent = BigIntegerField()
    system_type = IntegerField()
    the_order = IntegerField()
    trading_entity = BigIntegerField(index=True)
    type = IntegerField()
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'biz_category'


class BizCoupon(BaseModel):
    code = CharField(unique=True)
    coupon_batch_id = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    freeze_time = DateTimeField()
    grant_time = DateTimeField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField()
    use_time = DateTimeField()

    class Meta:
        table_name = 'biz_coupon'
        indexes = (
            (('coupon_batch_id', 'status'), False),
        )


class BizCouponBatch(BaseModel):
    amount = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    batch_no = CharField()
    begin_time = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    discount = IntegerField(constraints=[SQL("DEFAULT 100")])
    end_time = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    platform_type = IntegerField()
    quantity = IntegerField()
    status = IntegerField()
    surplus_quantity = IntegerField()
    trading_entity = BigIntegerField()
    type = IntegerField()
    use_remark = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'biz_coupon_batch'
        indexes = (
            (('trading_entity', 'status'), False),
        )


class BizCouponGrantRecord(BaseModel):
    coupon_batch_id = BigIntegerField(index=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quantity = IntegerField()

    class Meta:
        table_name = 'biz_coupon_grant_record'


class BizCouponRule(BaseModel):
    coupon_batch_id = BigIntegerField(index=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    rule_key = CharField(constraints=[SQL("DEFAULT '0'")])
    rule_value = CharField(constraints=[SQL("DEFAULT '0'")])

    class Meta:
        table_name = 'biz_coupon_rule'


class BizDayCashbackRecord(BaseModel):
    calc_date = CharField(unique=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    limit_amount = DecimalField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remain_amount = DecimalField()

    class Meta:
        table_name = 'biz_day_cashback_record'


class BizFixedQrCode(BaseModel):
    batch_id = BigIntegerField()
    card_number = CharField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    qr_code = CharField(unique=True)
    status = IntegerField()

    class Meta:
        table_name = 'biz_fixed_qr_code'


class BizGroupUserComponent(BaseModel):
    activity_flag = CharField(index=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    device_id = CharField()
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    group_mark = CharField(index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    phone = CharField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'biz_group_user_component'
        indexes = (
            (('feidee_user', 'phone', 'device_id'), False),
        )


class BizLogisticsCustomerAddress(BaseModel):
    address = CharField()
    city = CharField()
    contact_name = CharField()
    contact_sex = IntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    customer_address_no = CharField(unique=True)
    district = CharField()
    fid = BigAutoField()
    house_no = CharField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    phone_no = CharField()
    province = CharField()
    remark = CharField()
    title = CharField()
    token = CharField()

    class Meta:
        table_name = 'biz_logistics_customer_address'


class BizLogisticsFlow(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    discription = CharField()
    fid = BigAutoField()
    flow_status = IntegerField()
    logistics_id = BigIntegerField(index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remark = CharField()

    class Meta:
        table_name = 'biz_logistics_flow'


class BizLogisticsOrder(BaseModel):
    arrival_time = DateTimeField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    customer_address_no = CharField()
    fee = IntegerField()
    fid = BigAutoField()
    flow_status = IntegerField()
    logistics_id = CharField(unique=True)
    logistics_time = CharField()
    logistics_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_number = CharField(unique=True)
    rang = CharField()
    remark = CharField()

    class Meta:
        table_name = 'biz_logistics_order'


class BizMerchantDevice(BaseModel):
    auth_code = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    device_no = CharField(index=True)
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_merchant_device'


class BizOrder(BaseModel):
    category_id = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    img_url = CharField(constraints=[SQL("DEFAULT ''")])
    logistics_order_number = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    order_code = CharField(constraints=[SQL("DEFAULT ''")])
    order_number = CharField()
    order_source = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    order_time = DateTimeField()
    pay_status = IntegerField()
    pay_time = DateTimeField(null=True)
    pay_way = IntegerField(constraints=[SQL("DEFAULT 0")])
    real_amount = DecimalField()
    refund_status = IntegerField()
    refund_time = DateTimeField(null=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    source_amount = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    supplier_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(index=True)
    type = IntegerField()
    vip_member_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'biz_order'
        indexes = (
            (('order_code', 'trading_entity'), False),
            (('order_number', 'trading_entity'), True),
            (('trading_entity', 'order_time'), False),
        )


class BizOrderDelete(BaseModel):
    category_id = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    img_url = CharField(constraints=[SQL("DEFAULT ''")])
    logistics_order_number = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    order_code = CharField(constraints=[SQL("DEFAULT ''")])
    order_number = CharField()
    order_source = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    order_time = DateTimeField()
    pay_status = IntegerField()
    pay_time = DateTimeField(null=True)
    pay_way = IntegerField(constraints=[SQL("DEFAULT 0")])
    real_amount = DecimalField()
    refund_status = IntegerField()
    refund_time = DateTimeField(null=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    source_amount = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    supplier_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(index=True)
    type = IntegerField()
    vip_member_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'biz_order_delete'
        indexes = (
            (('order_code', 'trading_entity'), False),
            (('order_number', 'trading_entity'), True),
        )


class BizOrderFrom(BaseModel):
    app_id = CharField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    device_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    fid = BigAutoField()
    ip_address = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_number = CharField(index=True)
    request_no = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_order_from'
        indexes = (
            (('app_id', 'request_no'), False),
        )


class BizOrderItem(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    image_url = CharField(constraints=[SQL("DEFAULT ''")])
    item_channel_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    item_name = CharField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_number = CharField(index=True)
    price = DecimalField()
    product_item_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    profit = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    quantity = DecimalField()
    return_number = CharField(constraints=[SQL("DEFAULT ''")])
    specification = CharField(constraints=[SQL("DEFAULT ''")])
    staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    total_stock_price = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    total_stock_quantity = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    trans_type = IntegerField(constraints=[SQL("DEFAULT 2")])

    class Meta:
        table_name = 'biz_order_item'


class BizOrderItemDelete(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    image_url = CharField(constraints=[SQL("DEFAULT ''")])
    item_channel_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    item_name = CharField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_number = CharField(index=True)
    price = DecimalField()
    product_item_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    profit = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    quantity = DecimalField()
    return_number = CharField(constraints=[SQL("DEFAULT ''")])
    specification = CharField(constraints=[SQL("DEFAULT ''")])
    staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    total_stock_price = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    total_stock_quantity = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    trans_type = IntegerField(constraints=[SQL("DEFAULT 2")])

    class Meta:
        table_name = 'biz_order_item_delete'


class BizPrinter(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    platform = CharField(constraints=[SQL("DEFAULT ''")])
    print_name = CharField(constraints=[SQL("DEFAULT ''")])
    print_number = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_printer'


class BizProduct(BaseModel):
    brand_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    category_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    channels = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    name_first_letter = CharField(constraints=[SQL("DEFAULT ''")])
    product_code = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    product_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    saleable = IntegerField(constraints=[SQL("DEFAULT 1")])
    spec_flag = IntegerField(constraints=[SQL("DEFAULT 0")])
    spu_code = CharField(constraints=[SQL("DEFAULT ''")])
    sub_name = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField()
    unit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    valid = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'biz_product'
        indexes = (
            (('trading_entity', 'name'), False),
        )


class BizProductBeauty(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_id = BigIntegerField(index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    service_time = IntegerField()

    class Meta:
        table_name = 'biz_product_beauty'


class BizProductBrand(BaseModel):
    brand_desc = CharField(constraints=[SQL("DEFAULT ''")])
    brand_name = CharField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    photo_url = CharField(constraints=[SQL("DEFAULT ''")])
    the_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_product_brand'
        indexes = (
            (('trading_entity', 'brand_name'), True),
        )


class BizProductCategory(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    leaf_flag = IntegerField()
    level = IntegerField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    parent_id = BigIntegerField(index=True)
    scene_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    the_order = IntegerField()
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_product_category'
        indexes = (
            (('trading_entity', 'name', 'level'), True),
        )


class BizProductChannel(BaseModel):
    channel_type = IntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    name_first_letter = CharField(constraints=[SQL("DEFAULT ''")])
    product_id = BigIntegerField(index=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    saleable = IntegerField(constraints=[SQL("DEFAULT 1")])
    sub_name = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField()
    valid = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'biz_product_channel'
        indexes = (
            (('trading_entity', 'name'), False),
        )


class BizProductItem(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    enable = IntegerField(constraints=[SQL("DEFAULT 1")])
    fid = BigAutoField()
    item_code = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    product_id = BigIntegerField(index=True)
    purchase_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    selling_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    sku_code = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_product_item'
        indexes = (
            (('trading_entity', 'sku_code'), False),
        )


class BizProductItemChannel(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    enable = IntegerField(constraints=[SQL("DEFAULT 1")])
    fid = BigAutoField()
    item_id = BigIntegerField(index=True)
    line_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    product_channel_id = BigIntegerField(index=True)
    product_id = BigIntegerField(index=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    selling_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_product_item_channel'


class BizProductItemChannelPic(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_channel_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    path = CharField(constraints=[SQL("DEFAULT ''")])
    product_channel_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    the_main = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(index=True)
    type = IntegerField()

    class Meta:
        table_name = 'biz_product_item_channel_pic'


class BizProductItemDiscount(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    discount = IntegerField(constraints=[SQL("DEFAULT 100")])
    fid = BigAutoField()
    item_id = BigIntegerField(index=True)
    level_id = BigIntegerField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'biz_product_item_discount'
        indexes = (
            (('level_id', 'item_id'), True),
        )


class BizProductItemPic(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    path = CharField(constraints=[SQL("DEFAULT ''")])
    product_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    the_main = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    type = IntegerField()

    class Meta:
        table_name = 'biz_product_item_pic'


class BizProductItemPicCopy(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_id = BigIntegerField(index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    path = CharField(constraints=[SQL("DEFAULT ''")])
    the_main = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField()

    class Meta:
        table_name = 'biz_product_item_pic_copy'


class BizProductItemVolume(BaseModel):
    channel_type = IntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_channel_id = BigIntegerField(index=True)
    item_id = BigIntegerField(index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    product_channel_id = BigIntegerField(index=True)
    product_id = BigIntegerField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    sales_volume = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_product_item_volume'
        indexes = (
            (('trading_entity', 'product_id'), False),
        )


class BizProductLibrary(BaseModel):
    bar_code = CharField(unique=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    unit_name = CharField()

    class Meta:
        table_name = 'biz_product_library'


class BizProductSerialNumber(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    next_number = BigIntegerField(constraints=[SQL("DEFAULT 1")])
    the_lock = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_type = CharField()
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_product_serial_number'
        indexes = (
            (('trading_entity', 'the_type'), True),
        )


class BizProductStock(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_id = BigIntegerField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    stock_quantity = DecimalField()
    version = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    warehouse_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'biz_product_stock'
        indexes = (
            (('item_id', 'warehouse_id'), False),
        )


class BizProductSupplier(BaseModel):
    contact_person = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    phone = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    supplier_name = CharField()
    the_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(index=True)
    valid = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'biz_product_supplier'


class BizProductUnit(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    the_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_product_unit'


class BizPushAgent(BaseModel):
    agent_code = CharField(unique=True)
    agent_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    license = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField()
    the_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_enabled = IntegerField(constraints=[SQL("DEFAULT 1")])
    the_source = IntegerField()

    class Meta:
        table_name = 'biz_push_agent'


class BizPushAgentStaff(BaseModel):
    agent_id = BigIntegerField(index=True)
    bankcard = CharField(constraints=[SQL("DEFAULT ''")])
    business_card_img = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField(index=True)
    fid = BigAutoField()
    id_card_bak_img = CharField(constraints=[SQL("DEFAULT ''")])
    id_card_front_img = CharField(constraints=[SQL("DEFAULT ''")])
    idcard = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    phone = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    the_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_source = IntegerField()
    the_type = IntegerField()
    wechat_id = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'biz_push_agent_staff'


class BizPushMerchant(BaseModel):
    agent_id = BigIntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    staff_id = BigIntegerField(index=True)
    store_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_push_merchant'
        indexes = (
            (('agent_id', 'staff_id', 'store_id'), True),
        )


class BizRedPacket(BaseModel):
    activity_flag = CharField(index=True)
    amount = DecimalField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remain_times = IntegerField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    the_times = IntegerField()

    class Meta:
        table_name = 'biz_red_packet'


class BizRedPacketJoin(BaseModel):
    activity_flag = CharField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'biz_red_packet_join'
        indexes = (
            (('activity_flag', 'feidee_user'), True),
        )


class BizRedPacketUser(BaseModel):
    activity_flag = CharField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    grab_date = CharField()
    group_mark = CharField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    red_packet_amount = DecimalField()
    red_packet_id = BigIntegerField(index=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    uniq_mark = CharField(index=True)

    class Meta:
        table_name = 'biz_red_packet_user'
        indexes = (
            (('activity_flag', 'group_mark'), True),
        )


class BizReturnOrder(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    img_url = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    order_number = CharField()
    order_staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    pay_status = IntegerField()
    pay_time = DateTimeField(null=True)
    real_amount = DecimalField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    return_number = CharField()
    return_time = DateTimeField()
    status = IntegerField(null=True)
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_return_order'


class BizReturnOrderDelete(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    img_url = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    order_number = CharField()
    order_staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    pay_status = IntegerField()
    pay_time = DateTimeField(null=True)
    real_amount = DecimalField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    return_number = CharField()
    return_time = DateTimeField()
    status = IntegerField(null=True)
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_return_order_delete'
        indexes = (
            (('trading_entity', 'order_number'), False),
            (('trading_entity', 'return_number'), False),
        )


class BizStaff(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    icon = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    nick_name = CharField(constraints=[SQL("DEFAULT ''")])
    phone = CharField(constraints=[SQL("DEFAULT ''")])
    the_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_staff'
        indexes = (
            (('trading_entity', 'feidee_user'), False),
        )


class BizStaffConfig(BaseModel):
    config_key = CharField()
    config_value = CharField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    role_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_staff_config'
        indexes = (
            (('trading_entity', 'staff_id', 'role_id', 'config_key'), True),
        )


class BizStaffCraftsman(BaseModel):
    commission_way = IntegerField(constraints=[SQL("DEFAULT -1")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    service_end_time = CharField(constraints=[SQL("DEFAULT ''")])
    service_start_time = CharField(constraints=[SQL("DEFAULT ''")])
    staff_id = BigIntegerField()
    trading_entity = BigIntegerField()
    working_time = IntegerField(constraints=[SQL("DEFAULT -1")])

    class Meta:
        table_name = 'biz_staff_craftsman'
        indexes = (
            (('trading_entity', 'staff_id'), True),
        )


class BizStaffItem(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_id = BigIntegerField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    staff_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_staff_item'
        indexes = (
            (('item_id', 'staff_id'), True),
        )


class BizStaffRole(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    role_name = CharField()
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_staff_role'
        indexes = (
            (('trading_entity', 'role_name'), True),
        )


class BizStaffRoleRelate(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    role_id = BigIntegerField(index=True)
    staff_id = BigIntegerField()

    class Meta:
        table_name = 'biz_staff_role_relate'
        indexes = (
            (('staff_id', 'role_id'), True),
        )


class BizTempOrderItem(BaseModel):
    check_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_channel_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    member_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quantity = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    trading_entity = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'biz_temp_order_item'
        indexes = (
            (('member_id', 'trading_entity', 'item_channel_id'), True),
        )


class BizTempOrderItemDelete(BaseModel):
    check_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    item_channel_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    member_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quantity = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    trading_entity = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'biz_temp_order_item_delete'
        indexes = (
            (('member_id', 'trading_entity', 'item_channel_id'), True),
        )


class BizTransaction(BaseModel):
    account_id = BigIntegerField()
    account_name = CharField()
    amount = DecimalField()
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    order_number = CharField()
    pay_amount = DecimalField()
    pay_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_time = DateTimeField(null=True)
    pay_trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    pay_user_id = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    return_number = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    subject_type = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField(index=True)
    trans_type = IntegerField()

    class Meta:
        table_name = 'biz_transaction'
        indexes = (
            (('order_number', 'trading_entity'), False),
        )


class BizTransactionDelete(BaseModel):
    account_id = BigIntegerField()
    account_name = CharField()
    amount = DecimalField()
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    order_number = CharField()
    pay_amount = DecimalField()
    pay_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_time = DateTimeField(null=True)
    pay_trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    pay_user_id = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    return_number = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    subject_type = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField(index=True)
    trans_type = IntegerField()

    class Meta:
        table_name = 'biz_transaction_delete'
        indexes = (
            (('order_number', 'trading_entity'), False),
        )


class BizUserCashback(BaseModel):
    activity_flag = CharField()
    cashback_amout_total = DecimalField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'biz_user_cashback'
        indexes = (
            (('activity_flag', 'feidee_user'), True),
        )


class BizUserCashbackDetail(BaseModel):
    activity_flag = CharField()
    cashback_amout = DecimalField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    day_trade_id = BigIntegerField()
    feidee_user = BigIntegerField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    trade_amount = DecimalField()
    uniq_mark = CharField(index=True)

    class Meta:
        table_name = 'biz_user_cashback_detail'
        indexes = (
            (('activity_flag', 'feidee_user'), False),
            (('feidee_user', 'day_trade_id'), True),
        )


class BizUserDayTrade(BaseModel):
    calc_date = CharField()
    cashback_amout = DecimalField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feidee_user = BigIntegerField(index=True)
    feidee_user_name = CharField(constraints=[SQL("DEFAULT ''")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    the_handle = IntegerField()
    trade_amount = DecimalField()

    class Meta:
        table_name = 'biz_user_day_trade'
        indexes = (
            (('calc_date', 'feidee_user'), True),
        )


class BizVipCoupon(BaseModel):
    coupon_grant_record_id = BigIntegerField()
    coupon_id = BigIntegerField(index=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    grant_time = DateTimeField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField()
    vip_id = BigIntegerField()

    class Meta:
        table_name = 'biz_vip_coupon'
        indexes = (
            (('vip_id', 'status'), False),
        )


class BizVipLevel(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    down_exponent = IntegerField()
    fid = BigAutoField()
    level_icon = CharField()
    level_name = CharField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    trading_entity = BigIntegerField()
    up_exponent = IntegerField(null=True)
    upgrade_condition = IntegerField()
    upgrade_exponent = IntegerField()

    class Meta:
        table_name = 'biz_vip_level'
        indexes = (
            (('level_name', 'trading_entity'), True),
            (('trading_entity', 'upgrade_exponent'), True),
        )


class BizVipMember(BaseModel):
    balance = DecimalField()
    city = CharField(constraints=[SQL("DEFAULT ''")])
    consumption_sum = DecimalField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    gender = IntegerField(constraints=[SQL("DEFAULT 0")])
    icon = CharField(constraints=[SQL("DEFAULT ''")])
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name_letter = CharField(constraints=[SQL("DEFAULT ''")])
    nick_name = CharField(constraints=[SQL("DEFAULT ''")])
    phone = CharField(constraints=[SQL("DEFAULT ''")])
    province = CharField(constraints=[SQL("DEFAULT ''")])
    score = IntegerField()
    source_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    the_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField()
    valid = IntegerField(constraints=[SQL("DEFAULT 1")])
    vip_number = CharField()

    class Meta:
        table_name = 'biz_vip_member'
        indexes = (
            (('trading_entity', 'phone'), False),
            (('trading_entity', 'vip_number'), True),
        )


class BizVipRecharge(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    donation_amount = DecimalField()
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    recharge_amount = DecimalField()
    trading_entity = BigIntegerField(index=True)

    class Meta:
        table_name = 'biz_vip_recharge'


class BizVipScoreChangeRecord(BaseModel):
    change_score = IntegerField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_number = CharField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    score = IntegerField()
    staff_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    trading_entity = BigIntegerField(index=True)
    type = IntegerField()
    vip_member_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'biz_vip_score_change_record'


class BizVipTag(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    tag_icon = CharField()
    tag_name = CharField()
    trading_entity = BigIntegerField()

    class Meta:
        table_name = 'biz_vip_tag'
        indexes = (
            (('trading_entity', 'tag_name'), True),
        )


class BizVipTagMember(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    member_id = BigIntegerField(index=True)
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    tag_id = BigIntegerField()

    class Meta:
        table_name = 'biz_vip_tag_member'
        indexes = (
            (('tag_id', 'member_id'), True),
        )


class BizVipThirdPart(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fid = BigAutoField()
    modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    open_id = CharField()
    source = IntegerField()
    trading_entity = BigIntegerField()
    union_id = CharField(constraints=[SQL("DEFAULT ''")])
    vip_member_id = BigIntegerField()

    class Meta:
        table_name = 'biz_vip_third_part'
        indexes = (
            (('trading_entity', 'open_id'), True),
        )


class SysDepartment(BaseModel):
    create_time = DateTimeField()
    id = BigAutoField()
    name = CharField()
    parent_id = BigIntegerField()

    class Meta:
        table_name = 'sys_department'
        indexes = (
            (('parent_id', 'name'), True),
        )


class SysLog(BaseModel):
    create_time = DateTimeField()
    id = BigAutoField()
    ip = CharField(constraints=[SQL("DEFAULT ''")])
    method = CharField()
    operation = CharField()
    use_time = BigIntegerField()
    username = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'sys_log'


class SysMenu(BaseModel):
    create_by = CharField()
    create_time = DateTimeField()
    icon = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    name = CharField()
    order_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    parent_id = BigIntegerField()
    perms = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField()
    update_by = CharField()
    update_time = DateTimeField()
    url = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'sys_menu'


class SysOperationLog(BaseModel):
    create_time = DateTimeField()
    fid = BigAutoField()
    ip = CharField(constraints=[SQL("DEFAULT ''")])
    operation_name = CharField()
    operator = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    store_id = BigIntegerField()

    class Meta:
        table_name = 'sys_operation_log'


class SysRole(BaseModel):
    create_by = CharField()
    create_time = DateTimeField()
    id = BigAutoField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    role_name = CharField()
    role_sign = CharField(constraints=[SQL("DEFAULT ''")])
    update_by = CharField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'sys_role'


class SysRoleMenu(BaseModel):
    id = BigAutoField()
    menu_id = BigIntegerField()
    role_id = BigIntegerField()

    class Meta:
        table_name = 'sys_role_menu'


class SysUser(BaseModel):
    create_time = DateTimeField()
    department_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    email = CharField()
    full_name = CharField()
    id = BigAutoField()
    mobile = CharField(constraints=[SQL("DEFAULT ''")])
    username = CharField(unique=True)

    class Meta:
        table_name = 'sys_user'


class SysUserRole(BaseModel):
    id = BigAutoField()
    role_id = BigIntegerField()
    user_id = BigIntegerField()

    class Meta:
        table_name = 'sys_user_role'


class TAccount(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_category = IntegerField(column_name='FCategory', null=True)
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_counted_out_assets = IntegerField(column_name='FCountedOutAssets', constraints=[SQL("DEFAULT 0")], null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_currency = CharField(column_name='FCurrency', constraints=[SQL("DEFAULT 'CNY'")])
    f_group = IntegerField(column_name='FGroup', null=True)
    f_hidden = IntegerField(column_name='FHidden', constraints=[SQL("DEFAULT 0")])
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_memo = TextField(column_name='FMemo', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_account'


class TAccountCreditCard(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountId', index=True)
    annual_fee_memo = CharField(column_name='annualFeeMemo')
    annual_fee_min_use_amount = DecimalField(column_name='annualFeeMinUseAmount')
    annual_fee_min_use_count = BigIntegerField(column_name='annualFeeMinUseCount')
    annual_fee_mode = IntegerField(column_name='annualFeeMode')
    annual_fee_pay_month_day = CharField(column_name='annualFeePayMonthDay')
    annual_fee_static_use_amount = DecimalField(column_name='annualFeeStaticUseAmount')
    annualfee = DecimalField()
    available_balance = DecimalField(column_name='availableBalance')
    available_points = BigIntegerField(column_name='availablePoints')
    bill_day = BigIntegerField(column_name='billDay')
    bill_day_in_current = IntegerField(column_name='billDayInCurrent')
    bill_day_type = IntegerField(column_name='billDayType')
    card_num = CharField(column_name='cardNum')
    cash_advance_limit = DecimalField(column_name='cashAdvanceLimit')
    group_uuid = CharField(column_name='groupUUID')
    house_holder = CharField(column_name='houseHolder')
    is_annual_fee_warn = IntegerField(column_name='isAnnualFeeWarn')
    is_primary_card = IntegerField(column_name='isPrimaryCard')
    issuing_bank = CharField(column_name='issuingBank')
    last_digits_of_card_number = CharField(column_name='lastDigitsOfCardNumber')
    limit_amount = DecimalField(column_name='limitAmount')
    minimum_payment = DecimalField(column_name='minimumPayment')
    period_surplus_payment = DecimalField(column_name='periodSurplusPayment')
    repay_amount = DecimalField(column_name='repayAmount')
    repay_date = DateTimeField(column_name='repayDate')
    repay_day = BigIntegerField(column_name='repayDay')
    repay_day_type = IntegerField(column_name='repayDayType')
    repay_state = IntegerField(column_name='repayState')
    repay_state_last_update_time = DateTimeField(column_name='repayStateLastUpdateTime')
    source_type = IntegerField(column_name='sourceType')
    status = IntegerField()
    surplus_payment = DecimalField(column_name='surplusPayment')
    validity_period = DateTimeField(column_name='validityPeriod')

    class Meta:
        table_name = 't_account_credit_card'


class TAccountCreditCardDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountId', index=True)
    annual_fee_memo = CharField(column_name='annualFeeMemo')
    annual_fee_min_use_amount = DecimalField(column_name='annualFeeMinUseAmount')
    annual_fee_min_use_count = BigIntegerField(column_name='annualFeeMinUseCount')
    annual_fee_mode = IntegerField(column_name='annualFeeMode')
    annual_fee_pay_month_day = CharField(column_name='annualFeePayMonthDay')
    annual_fee_static_use_amount = DecimalField(column_name='annualFeeStaticUseAmount')
    annualfee = DecimalField()
    available_balance = DecimalField(column_name='availableBalance')
    available_points = BigIntegerField(column_name='availablePoints')
    bill_day = BigIntegerField(column_name='billDay')
    bill_day_in_current = IntegerField(column_name='billDayInCurrent')
    bill_day_type = IntegerField(column_name='billDayType')
    card_num = CharField(column_name='cardNum')
    cash_advance_limit = DecimalField(column_name='cashAdvanceLimit')
    group_uuid = CharField(column_name='groupUUID')
    house_holder = CharField(column_name='houseHolder')
    is_annual_fee_warn = IntegerField(column_name='isAnnualFeeWarn')
    is_primary_card = IntegerField(column_name='isPrimaryCard')
    issuing_bank = CharField(column_name='issuingBank')
    last_digits_of_card_number = CharField(column_name='lastDigitsOfCardNumber')
    limit_amount = DecimalField(column_name='limitAmount')
    minimum_payment = DecimalField(column_name='minimumPayment')
    period_surplus_payment = DecimalField(column_name='periodSurplusPayment')
    repay_amount = DecimalField(column_name='repayAmount')
    repay_date = DateTimeField(column_name='repayDate')
    repay_day = BigIntegerField(column_name='repayDay')
    repay_day_type = IntegerField(column_name='repayDayType')
    repay_state = IntegerField(column_name='repayState')
    repay_state_last_update_time = DateTimeField(column_name='repayStateLastUpdateTime')
    source_type = IntegerField(column_name='sourceType')
    status = IntegerField()
    surplus_payment = DecimalField(column_name='surplusPayment')
    validity_period = DateTimeField(column_name='validityPeriod')

    class Meta:
        table_name = 't_account_credit_card_delete'


class TAccountDelete(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_category = IntegerField(column_name='FCategory', null=True)
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_counted_out_assets = IntegerField(column_name='FCountedOutAssets', constraints=[SQL("DEFAULT 0")], null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_currency = CharField(column_name='FCurrency', constraints=[SQL("DEFAULT 'CNY'")])
    f_group = IntegerField(column_name='FGroup', null=True)
    f_hidden = IntegerField(column_name='FHidden', constraints=[SQL("DEFAULT 0")])
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_memo = TextField(column_name='FMemo', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_account_delete'


class TAccountExtra(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_key = CharField(column_name='FKey')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    f_value = CharField(column_name='FValue')
    account_id = BigIntegerField(column_name='accountID', null=True)

    class Meta:
        table_name = 't_account_extra'


class TAccountExtraDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_key = CharField(column_name='FKey')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    f_value = CharField(column_name='FValue')
    account_id = BigIntegerField(column_name='accountID', null=True)

    class Meta:
        table_name = 't_account_extra_delete'


class TAccountFund(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    institution_name = CharField(column_name='institutionName', null=True)
    redemption_rate = DecimalField(column_name='redemptionRate', null=True)
    subscription_rate = DecimalField(column_name='subscriptionRate', null=True)

    class Meta:
        table_name = 't_account_fund'


class TAccountFundDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    institution_name = CharField(column_name='institutionName', null=True)
    redemption_rate = DecimalField(column_name='redemptionRate', null=True)
    subscription_rate = DecimalField(column_name='subscriptionRate', null=True)

    class Meta:
        table_name = 't_account_fund_delete'


class TAccountGroup(BaseModel):
    fid = AutoField(column_name='FID')
    f_name = CharField(column_name='FName', null=True)
    f_parent = IntegerField(column_name='FParent', null=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_account_group'


class TAccountInfo(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountId', index=True)
    institution_name = CharField(column_name='institutionName', null=True)

    class Meta:
        table_name = 't_account_info'


class TAccountInfoDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountId', index=True)
    institution_name = CharField(column_name='institutionName', null=True)

    class Meta:
        table_name = 't_account_info_delete'


class TAccountStock(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    institution_name = CharField(column_name='institutionName', null=True)
    redemption_rate = DecimalField(column_name='redemptionRate', null=True)
    subscription_rate = DecimalField(column_name='subscriptionRate', null=True)

    class Meta:
        table_name = 't_account_stock'


class TAccountStockDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    institution_name = CharField(column_name='institutionName', null=True)
    redemption_rate = DecimalField(column_name='redemptionRate', null=True)
    subscription_rate = DecimalField(column_name='subscriptionRate', null=True)

    class Meta:
        table_name = 't_account_stock_delete'


class TAccountTransMap(BaseModel):
    f_account = BigIntegerField(column_name='FAccount', null=True)
    f_amount = FloatField(column_name='FAmount', null=True)
    f_trans = BigIntegerField(column_name='FTrans', index=True, null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_account_trans_map'


class TAccountbooksetting(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    datasyncpush = IntegerField(constraints=[SQL("DEFAULT 0")])
    feidee_user = BigIntegerField(column_name='feideeUser', index=True)
    ssj_user = BigIntegerField(column_name='ssjUser')

    class Meta:
        table_name = 't_accountbooksetting'


class TAccountgrant(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    account_id = BigIntegerField(column_name='accountID', null=True)
    product_name = CharField(column_name='productName')
    product_version = CharField(column_name='productVersion')

    class Meta:
        table_name = 't_accountgrant'


class TAccountgrantDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    account_id = BigIntegerField(column_name='accountID', null=True)
    product_name = CharField(column_name='productName')
    product_version = CharField(column_name='productVersion')

    class Meta:
        table_name = 't_accountgrant_delete'


class TAclLinkRolePermission(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    permission_code = CharField(column_name='permissionCode')
    role_unique_name = CharField(column_name='roleUniqueName', constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 't_acl_link_role_permission'


class TAclLinkRolePermissionDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    permission_code = CharField(column_name='permissionCode')
    role_unique_name = CharField(column_name='roleUniqueName', constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 't_acl_link_role_permission_delete'


class TAclLinkUserRole(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    role_unique_name = CharField(column_name='roleUniqueName', constraints=[SQL("DEFAULT ''")])
    uid = CharField()

    class Meta:
        table_name = 't_acl_link_user_role'


class TAclLinkUserRoleDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    role_unique_name = CharField(column_name='roleUniqueName', constraints=[SQL("DEFAULT ''")])
    uid = CharField()

    class Meta:
        table_name = 't_acl_link_user_role_delete'


class TAclRole(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    created_source = IntegerField(column_name='createdSource', constraints=[SQL("DEFAULT 0")])
    ordered = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    role_name = CharField(column_name='roleName', constraints=[SQL("DEFAULT ''")])
    unique_name = CharField(column_name='uniqueName', constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 't_acl_role'


class TAclRoleDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    created_source = IntegerField(column_name='createdSource', constraints=[SQL("DEFAULT 0")])
    ordered = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    role_name = CharField(column_name='roleName', constraints=[SQL("DEFAULT ''")])
    unique_name = CharField(column_name='uniqueName', constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 't_acl_role_delete'


class TActivity(BaseModel):
    f_contact = CharField(column_name='FContact', null=True)
    f_content = TextField(column_name='FContent', null=True)
    f_date = DateTimeField(column_name='FDate', null=True)
    fid = AutoField(column_name='FID')
    f_modify_date = DateTimeField(column_name='FModifyDate', null=True)
    f_show_img_url = CharField(column_name='FShowImgUrl', null=True)
    f_title = CharField(column_name='FTitle', null=True)

    class Meta:
        table_name = 't_activity'


class TActivityComment(BaseModel):
    f_comment_id = IntegerField(column_name='FCommentId', null=True)
    f_competitor_id = IntegerField(column_name='FCompetitorId', null=True)
    f_content = TextField(column_name='FContent', null=True)
    f_datetime = DateTimeField(column_name='FDatetime', null=True)
    fid = AutoField(column_name='FID')

    class Meta:
        table_name = 't_activity_comment'


class TAddress(BaseModel):
    f_address = CharField(column_name='FAddress', null=True)
    fid = AutoField(column_name='FID')
    f_parent = IntegerField(column_name='FParent', null=True)

    class Meta:
        table_name = 't_address'


class TAppBind(BaseModel):
    f_bind_date = DateTimeField(column_name='FBindDate', null=True)
    f_bind_key = CharField(column_name='FBindKey', null=True)
    f_bind_plat = IntegerField(column_name='FBindPlat', null=True)
    f_bind_status = IntegerField(column_name='FBindStatus', null=True)
    f_bind_type = IntegerField(column_name='FBindType', null=True)
    f_bind_value = CharField(column_name='FBindValue', null=True)
    f_card_id = BigIntegerField(column_name='FCardId', null=True)
    f_confirm_num = CharField(column_name='FConfirmNum', null=True)
    f_id = BigAutoField(column_name='FId')
    f_user_id = BigIntegerField(column_name='FUserId')

    class Meta:
        table_name = 't_app_bind'


class TAppNotice(BaseModel):
    f_card_id = BigIntegerField(column_name='FCardId', null=True)
    f_id = BigAutoField(column_name='FId')
    f_notice_date = DateTimeField(column_name='FNoticeDate', null=True)
    f_notice_plat = IntegerField(column_name='FNoticePlat', null=True)
    f_notice_status = IntegerField(column_name='FNoticeStatus', null=True)
    f_notice_type = IntegerField(column_name='FNoticeType', null=True)
    f_user_id = BigIntegerField(column_name='FUserId')

    class Meta:
        table_name = 't_app_notice'


class TAppSync(BaseModel):
    f_bind_key = CharField(column_name='FBindKey', null=True)
    f_bind_value = CharField(column_name='FBindValue', null=True)
    f_card_id = BigIntegerField(column_name='FCardId', null=True)
    f_id = BigAutoField(column_name='FId')
    f_records = IntegerField(column_name='FRecords', null=True)
    f_sync_date = DateTimeField(column_name='FSyncDate', null=True)
    f_sync_num = BigIntegerField(column_name='FSyncNum', null=True)
    f_sync_plat = IntegerField(column_name='FSyncPlat', null=True)
    f_sync_status = IntegerField(column_name='FSyncStatus', null=True)
    f_sync_type = IntegerField(column_name='FSyncType', null=True)
    f_user_id = BigIntegerField(column_name='FUserId')

    class Meta:
        table_name = 't_app_sync'


class TAutosync(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_feidee_user_id = BigIntegerField(column_name='FFeideeUserID', null=True)
    fid = BigAutoField(column_name='FID')
    f_modify_time = DateTimeField(column_name='FModifyTime', null=True)
    f_state = IntegerField(column_name='FState', null=True)
    f_terminal = CharField(column_name='FTerminal', null=True)
    f_terminal_uid = CharField(column_name='FTerminalUID', null=True)
    f_user_name = CharField(column_name='FUserName', null=True)

    class Meta:
        table_name = 't_autosync'
        indexes = (
            (('f_feidee_user_id', 'f_terminal_uid'), False),
            (('f_user_name', 'f_terminal_uid'), False),
        )


class TBank(BaseModel):
    fid = BigAutoField(column_name='FID')
    bank_class = CharField(column_name='bankClass', null=True)
    bank_name = CharField(column_name='bankName', null=True)
    bank_no = CharField(column_name='bankNo', null=True)
    e_bank_url = CharField(column_name='eBankURL', null=True)
    hot_line = CharField(column_name='hotLine', null=True)
    icon_name = CharField(column_name='iconName', null=True)
    state = IntegerField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 't_bank'


class TBankCardBind(BaseModel):
    f_acount_id = BigIntegerField(column_name='FAcountId', null=True)
    f_card_num = CharField(column_name='FCardNum', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_id = BigAutoField(column_name='FId')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_user_id = BigIntegerField(column_name='FUserId', null=True)

    class Meta:
        table_name = 't_bank_card_bind'


class TBankUnionpayCode(BaseModel):
    area = CharField()
    area_code = CharField()
    bank_name = CharField()
    branch_name = CharField(index=True)
    city = CharField()
    city_code = CharField()
    fid = BigAutoField()
    unionpay_code = CharField()
    x_latitude = CharField()
    y_longitude = CharField()

    class Meta:
        table_name = 't_bank_unionpay_code'


class TBill(BaseModel):
    f_account = BigIntegerField(column_name='FAccount', index=True, null=True)
    f_account2 = BigIntegerField(column_name='FAccount2', null=True)
    f_category = BigIntegerField(column_name='FCategory', index=True, null=True)
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_del_status = IntegerField(column_name='FDelStatus', constraints=[SQL("DEFAULT 0")], index=True, null=True)
    f_due_date = DateTimeField(column_name='FDueDate')
    f_end_date = DateTimeField(column_name='FEndDate', null=True)
    f_from = CharField(column_name='FFrom', constraints=[SQL("DEFAULT 'web'")], null=True)
    fid = BigAutoField(column_name='FID')
    f_is_auto = IntegerField(column_name='FIsAuto', null=True)
    f_is_remind = IntegerField(column_name='FIsRemind', null=True)
    f_is_same = IntegerField(column_name='FIsSame', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_member = BigIntegerField(column_name='FMember', null=True)
    f_money = DecimalField(column_name='FMoney', constraints=[SQL("DEFAULT 0.00")], null=True)
    f_money2 = DecimalField(column_name='FMoney2', null=True)
    f_name = CharField(column_name='FName')
    f_pay_status = IntegerField(column_name='FPayStatus', constraints=[SQL("DEFAULT 0")], null=True)
    f_period = IntegerField(column_name='FPeriod', null=True)
    f_period_day = IntegerField(column_name='FPeriodDay', null=True)
    f_period_frequency = IntegerField(column_name='FPeriodFrequency', constraints=[SQL("DEFAULT 0")], null=True)
    f_period_month = IntegerField(column_name='FPeriodMonth', null=True)
    f_period_time = CharField(column_name='FPeriodTime', constraints=[SQL("DEFAULT '12:00'")], null=True)
    f_project = BigIntegerField(column_name='FProject', constraints=[SQL("DEFAULT 0")], null=True)
    f_remind_note = TextField(column_name='FRemindNote', null=True)
    f_status = IntegerField(column_name='FStatus', constraints=[SQL("DEFAULT 1")], null=True)
    f_store = BigIntegerField(column_name='FStore', constraints=[SQL("DEFAULT 0")], null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_type = IntegerField(column_name='FType', constraints=[SQL("DEFAULT -1")])

    class Meta:
        table_name = 't_bill'


class TBillRemind(BaseModel):
    f_bill_id = BigIntegerField(column_name='FBillID', index=True)
    f_content = CharField(column_name='FContent', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_frequency = IntegerField(column_name='FFrequency', null=True)
    f_from = CharField(column_name='FFrom', constraints=[SQL("DEFAULT 'web'")], null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_message = CharField(column_name='FMessage', null=True)
    f_replay = IntegerField(column_name='FReplay', constraints=[SQL("DEFAULT 0")])
    f_time = CharField(column_name='FTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', constraints=[SQL("DEFAULT 0")], index=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_bill_remind'


class TBillStory(BaseModel):
    f_amount = DecimalField(column_name='FAmount', null=True)
    f_bill_date = DateTimeField(column_name='FBillDate', null=True)
    f_bill_id = BigIntegerField(column_name='FBillID', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_del_status = IntegerField(column_name='FDelStatus', constraints=[SQL("DEFAULT 0")])
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_trans_date = DateTimeField(column_name='FTransDate', null=True)
    f_trans_id = BigIntegerField(column_name='FTransID', index=True, null=True)

    class Meta:
        table_name = 't_bill_story'
        indexes = (
            (('f_bill_id', 'f_bill_date'), True),
        )


class TBudgetEvent(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_poid = BigIntegerField(column_name='accountPOID', constraints=[SQL("DEFAULT 0")])
    bounded_type = IntegerField(column_name='boundedType', constraints=[SQL("DEFAULT 0")], null=True)
    category_poid = BigIntegerField(column_name='categoryPOID', constraints=[SQL("DEFAULT 0")])
    corporation_poid = BigIntegerField(column_name='corporationPOID', constraints=[SQL("DEFAULT 0")])
    created_source = IntegerField(column_name='createdSource', constraints=[SQL("DEFAULT 1")], null=True)
    event_end = DateTimeField(column_name='eventEnd')
    event_start = DateTimeField(column_name='eventStart')
    freq = IntegerField(null=True)
    member_poid = BigIntegerField(column_name='memberPOID', constraints=[SQL("DEFAULT 0")])
    parent_source_key = CharField(column_name='parentSourceKey', null=True)
    project_poid = BigIntegerField(column_name='projectPOID', constraints=[SQL("DEFAULT 0")])
    recurrence_id = BigIntegerField(column_name='recurrenceId', constraints=[SQL("DEFAULT 0")])
    root_type = IntegerField(column_name='rootType', constraints=[SQL("DEFAULT 0")])
    the_max_value = DecimalField(column_name='theMaxValue', null=True)
    the_min_value = DecimalField(column_name='theMinValue', null=True)
    transaction_type = IntegerField(column_name='transactionType', constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 't_budget_event'


class TBudgetEventDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_poid = BigIntegerField(column_name='accountPOID', constraints=[SQL("DEFAULT 0")])
    bounded_type = IntegerField(column_name='boundedType', constraints=[SQL("DEFAULT 0")], null=True)
    category_poid = BigIntegerField(column_name='categoryPOID', constraints=[SQL("DEFAULT 0")])
    corporation_poid = BigIntegerField(column_name='corporationPOID', constraints=[SQL("DEFAULT 0")])
    created_source = IntegerField(column_name='createdSource', constraints=[SQL("DEFAULT 1")], null=True)
    event_end = DateTimeField(column_name='eventEnd')
    event_start = DateTimeField(column_name='eventStart')
    freq = IntegerField(null=True)
    member_poid = BigIntegerField(column_name='memberPOID', constraints=[SQL("DEFAULT 0")])
    parent_source_key = CharField(column_name='parentSourceKey', null=True)
    project_poid = BigIntegerField(column_name='projectPOID', constraints=[SQL("DEFAULT 0")])
    recurrence_id = BigIntegerField(column_name='recurrenceId', constraints=[SQL("DEFAULT 0")])
    root_type = IntegerField(column_name='rootType', constraints=[SQL("DEFAULT 0")])
    the_max_value = DecimalField(column_name='theMaxValue', null=True)
    the_min_value = DecimalField(column_name='theMinValue', null=True)
    transaction_type = IntegerField(column_name='transactionType', constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 't_budget_event_delete'


class TBudgetItem(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_category = BigIntegerField(column_name='FCategory', index=True, null=True)
    f_end_time = DateTimeField(column_name='FEndTime', null=True)
    f_frequency = CharField(column_name='FFrequency', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_start_time = DateTimeField(column_name='FStartTime', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_budget_item'


class TBudgetItemDelete(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_category = BigIntegerField(column_name='FCategory', null=True)
    f_end_time = DateTimeField(column_name='FEndTime', null=True)
    f_frequency = CharField(column_name='FFrequency', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_start_time = DateTimeField(column_name='FStartTime', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_budget_item_delete'


class TCategory(BaseModel):
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_hidden = IntegerField(column_name='FHidden', constraints=[SQL("DEFAULT 0")])
    f_icon = CharField(column_name='FIcon', null=True)
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_category'


class TCategoryDelete(BaseModel):
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_hidden = IntegerField(column_name='FHidden', constraints=[SQL("DEFAULT 0")])
    f_icon = CharField(column_name='FIcon', null=True)
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_category_delete'


class TCategoryIcon(BaseModel):
    fid = AutoField(column_name='FID')
    f_icon = CharField(column_name='FIcon', null=True)

    class Meta:
        table_name = 't_category_icon'


class TCategoryTag(BaseModel):
    fid = AutoField(column_name='FID')
    f_icon = CharField(column_name='FIcon', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = IntegerField(column_name='FParent', constraints=[SQL("DEFAULT 0")], null=True)
    f_type = IntegerField(column_name='FType', null=True)
    f_user_acc_type = CharField(column_name='FUserAccType', null=True)

    class Meta:
        table_name = 't_category_tag'


class TConnectTableForC3P0(BaseModel):
    a = CharField(null=True)

    class Meta:
        table_name = 't_connect_table_for_c3p0'
        primary_key = False


class TCreditBillDetail(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_bill_id = BigIntegerField(column_name='FBillId', null=True)
    f_card_num = CharField(column_name='FCardNum', null=True)
    f_currency = CharField(column_name='FCurrency', null=True)
    f_description = CharField(column_name='FDescription', null=True)
    f_from = IntegerField(column_name='FFrom', null=True)
    f_id = BigAutoField(column_name='FId')
    f_mail_id = BigIntegerField(column_name='FMailId', null=True)
    f_post_date = DateTimeField(column_name='FPostDate', null=True)
    f_tally_status = IntegerField(column_name='FTallyStatus', null=True)
    f_trans_date = DateTimeField(column_name='FTransDate', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    f_user_id = BigIntegerField(column_name='FUserId', null=True)

    class Meta:
        table_name = 't_credit_bill_detail'


class TCreditBillMails(BaseModel):
    f_attach_path = CharField(column_name='FAttachPath', null=True)
    f_begin_date = DateTimeField(column_name='FBeginDate', null=True)
    f_body_path = CharField(column_name='FBodyPath', null=True)
    f_card_num = CharField(column_name='FCardNum', null=True)
    f_cardbank = CharField(column_name='FCardbank', null=True)
    f_credit_limit = DecimalField(column_name='FCreditLimit', null=True)
    f_currency = CharField(column_name='FCurrency', null=True)
    f_current_balance = DecimalField(column_name='FCurrentBalance', null=True)
    f_end_date = DateTimeField(column_name='FEndDate', null=True)
    f_entry_flag = IntegerField(column_name='FEntryFlag', null=True)
    f_from = IntegerField(column_name='FFrom', null=True)
    f_from_address = CharField(column_name='FFromAddress', null=True)
    f_id = BigAutoField(column_name='FId')
    f_mailbox_id = BigIntegerField(column_name='FMailboxId', null=True)
    f_parse_status = IntegerField(column_name='FParseStatus', null=True)
    f_read_status = IntegerField(column_name='FReadStatus', constraints=[SQL("DEFAULT 0")])
    f_repay_day = CharField(column_name='FRepayDay', null=True)
    f_scan_number = IntegerField(column_name='FScanNumber', null=True)
    f_subject = CharField(column_name='FSubject', null=True)
    f_time_parse = DateTimeField(column_name='FTimeParse', null=True)
    f_time_receive = DateTimeField(column_name='FTimeReceive', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fuid = CharField(column_name='FUID', null=True)
    f_user_id = BigIntegerField(column_name='FUserId', index=True, null=True)

    class Meta:
        table_name = 't_credit_bill_mails'


class TCreditCard(BaseModel):
    f_account = BigIntegerField(column_name='FAccount', null=True)
    f_adjust_amount = FloatField(column_name='FAdjustAmount', constraints=[SQL("DEFAULT 0.00")], null=True)
    f_bill_day = IntegerField(column_name='FBillDay', null=True)
    f_bill_day_in_current = IntegerField(column_name='FBillDayInCurrent', null=True)
    f_card_name = CharField(column_name='FCardName', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_if_remind = IntegerField(column_name='FIfRemind', null=True)
    f_interval_day = IntegerField(column_name='FIntervalDay', null=True)
    f_issuing_bank = IntegerField(column_name='FIssuingBank', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_limit_amount = FloatField(column_name='FLimitAmount', null=True)
    f_remind_time = TimeField(column_name='FRemindTime', null=True)
    f_remind_type = CharField(column_name='FRemindType', null=True)
    f_repay_day = IntegerField(column_name='FRepayDay', null=True)
    f_repay_day_type = IntegerField(column_name='FRepayDayType', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_terminal_id = BigIntegerField(column_name='FTerminalID', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_validity_period = DateTimeField(column_name='FValidityPeriod', null=True)
    autoincr_id = BigIntegerField(unique=True)
    bill_day_type = IntegerField(column_name='billDayType', null=True)
    card_num = CharField(column_name='cardNum', null=True)
    cash_advance_limit = FloatField(column_name='cashAdvanceLimit', constraints=[SQL("DEFAULT 0.00")], null=True)
    group_uuid = IntegerField(column_name='groupUUID', null=True)
    is_primary_card = IntegerField(column_name='isPrimaryCard', null=True)
    minimum_payment = FloatField(column_name='minimumPayment', constraints=[SQL("DEFAULT 0.00")], null=True)
    repay_amount = FloatField(column_name='repayAmount', constraints=[SQL("DEFAULT 0.00")], null=True)
    repay_date = DateTimeField(column_name='repayDate', null=True)
    repay_state = IntegerField(column_name='repayState', constraints=[SQL("DEFAULT 0")], null=True)
    repay_state_last_update_time = DateTimeField(column_name='repayStateLastUpdateTime', null=True)
    source_hash_id = TextField(column_name='sourceHashID', null=True)
    source_id = BigIntegerField(column_name='sourceID', null=True)
    source_type = IntegerField(column_name='sourceType', null=True)
    statement_balance = FloatField(column_name='statementBalance', constraints=[SQL("DEFAULT 0.00")], null=True)

    class Meta:
        table_name = 't_credit_card'
        indexes = (
            (('f_status', 'f_if_remind'), False),
        )


class TCreditCardRemind(BaseModel):
    f_content = CharField(column_name='FContent', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_credit_id = BigIntegerField(column_name='FCreditID', index=True)
    f_frequency = IntegerField(column_name='FFrequency', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_message = CharField(column_name='FMessage', null=True)
    f_replay = IntegerField(column_name='FReplay', constraints=[SQL("DEFAULT 0")])
    f_time = CharField(column_name='FTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', constraints=[SQL("DEFAULT 0")], index=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_credit_card_remind'


class TCreditCardTag(BaseModel):
    f_bill_day = IntegerField(column_name='FBillDay', null=True)
    f_bill_day_in_current = IntegerField(column_name='FBillDayInCurrent', constraints=[SQL("DEFAULT 0")], null=True)
    f_card_name = CharField(column_name='FCardName', null=True)
    fid = AutoField(column_name='FID')
    f_issuing_bank = IntegerField(column_name='FIssuingBank', null=True)
    f_limit_amount = FloatField(column_name='FLimitAmount', null=True)
    f_repay_day = IntegerField(column_name='FRepayDay', null=True)

    class Meta:
        table_name = 't_credit_card_tag'


class TCreditMailWhite(BaseModel):
    f_addresses = CharField(column_name='FAddresses', null=True)
    f_user_id = BigAutoField(column_name='FUserId')

    class Meta:
        table_name = 't_credit_mail_white'


class TCreditMailbox(BaseModel):
    f_address = CharField(column_name='FAddress', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_id = BigAutoField(column_name='FId')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_password = CharField(column_name='FPassword', null=True)
    f_user_id = BigIntegerField(column_name='FUserId', index=True, null=True)

    class Meta:
        table_name = 't_credit_mailbox'


class TCreditOldBill(BaseModel):
    f_begin_date = DateTimeField(column_name='FBeginDate', null=True)
    f_end_date = DateTimeField(column_name='FEndDate', null=True)
    fid = BigIntegerField(column_name='FID')
    f_interest = FloatField(column_name='FInterest', null=True)
    f_least_repay = FloatField(column_name='FLeastRepay', null=True)
    f_repayed = FloatField(column_name='FRepayed', null=True)
    f_should_repay = FloatField(column_name='FShouldRepay', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)

    class Meta:
        table_name = 't_credit_old_bill'
        indexes = (
            (('f_trading_entity', 'fid'), False),
        )
        primary_key = False


class TCurrency(BaseModel):
    fid = AutoField(column_name='FID')
    f_is_common = IntegerField(column_name='FIsCommon', null=True)
    f_no = CharField(column_name='FNo', index=True, null=True)
    f_rate = FloatField(column_name='FRate', null=True)
    f_symbol = CharField(column_name='FSymbol', null=True)
    fusd_rate = FloatField(column_name='FUSDRate', null=True)
    f_update_time = DateTimeField(column_name='FUpdateTime', null=True)
    fname = CharField(column_name='Fname', null=True)

    class Meta:
        table_name = 't_currency'


class TDefaultCurrency(BaseModel):
    f_currency = CharField(column_name='FCurrency', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_default_currency'


class TDiary(BaseModel):
    f_classify_id = BigIntegerField(column_name='FClassifyId', null=True)
    f_content = TextField(column_name='FContent', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_icon = CharField(column_name='FIcon', null=True)
    f_title = CharField(column_name='FTitle', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    f_update_time = DateTimeField(column_name='FUpdateTime', null=True)

    class Meta:
        table_name = 't_diary'


class TDiaryType(BaseModel):
    f_classify_name = CharField(column_name='FClassifyName', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigIntegerField(column_name='FID', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    f_update_time = DateTimeField(column_name='FUpdateTime', null=True)

    class Meta:
        table_name = 't_diary_type'
        primary_key = False


class TDictionary(BaseModel):
    f_foreign_id = IntegerField(column_name='FForeignID', null=True)
    fid = AutoField(column_name='FID')
    f_index = CharField(column_name='FIndex', null=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_dictionary'


class TDirtyBook(BaseModel):
    book_id = BigAutoField(column_name='bookId')
    book_name = CharField(column_name='bookName', null=True)
    db_id = IntegerField(column_name='dbId', null=True)
    register_date = DateTimeField(column_name='registerDate', null=True)
    user_id = BigIntegerField(column_name='userId', null=True)

    class Meta:
        table_name = 't_dirty_book'


class TEntityOptions(BaseModel):
    f_data = CharField(column_name='FData', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    ftype = IntegerField(column_name='Ftype', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_entity_options'
        indexes = (
            (('f_trading_entity', 'ftype'), False),
        )


class TEventLog(BaseModel):
    f_acc_type = CharField(column_name='FAccType', null=True)
    f_excutor = CharField(column_name='FExcutor', null=True)
    f_feidee_user = BigIntegerField(column_name='FFeideeUser', null=True)
    f_memo = CharField(column_name='FMemo', null=True)
    f_module = CharField(column_name='FModule', null=True)
    f_operation = CharField(column_name='FOperation', null=True)
    f_product_name = CharField(column_name='FProductName', null=True)
    f_product_version = CharField(column_name='FProductVersion', null=True)
    f_provider = CharField(column_name='FProvider', null=True)
    f_sync_flag = CharField(column_name='FSyncFlag', null=True)
    f_time = DateTimeField(column_name='FTime', index=True, null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    fudid = CharField(column_name='FUDID', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_event_log'
        indexes = (
            (('f_product_name', 'f_product_version'), False),
            (('f_trading_entity', 'f_time'), False),
        )


class TEventLogItem(BaseModel):
    f_count = IntegerField(column_name='FCount', null=True)
    f_event_log = BigIntegerField(column_name='FEventLog', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_event_log_item'


class TFinanceOrg(BaseModel):
    f_address = CharField(column_name='FAddress', null=True)
    f_code = CharField(column_name='FCode', null=True)
    fe_bank_url = CharField(column_name='FEBankURL', null=True)
    f_hot_telephone = CharField(column_name='FHotTelephone', null=True)
    f_icon = CharField(column_name='FIcon', null=True)
    f_id = BigAutoField(column_name='FId')
    f_memo = CharField(column_name='FMemo', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_simple_name = CharField(column_name='FSimpleName', null=True)
    f_sms_no = CharField(column_name='FSmsNo', null=True)
    furl = CharField(column_name='FURL', null=True)

    class Meta:
        table_name = 't_finance_org'


class TFundHolding(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    buy_amount = DecimalField(column_name='buyAmount', constraints=[SQL("DEFAULT 0.00")])
    buy_shares = DecimalField(column_name='buyShares', constraints=[SQL("DEFAULT 0.00")])
    fund_code = CharField(column_name='fundCode')
    fund_type = IntegerField(column_name='fundType', null=True)
    memo = TextField(null=True)
    sell_amount = DecimalField(column_name='sellAmount', constraints=[SQL("DEFAULT 0.00")])
    sell_shares = DecimalField(column_name='sellShares', constraints=[SQL("DEFAULT 0.00")])

    class Meta:
        table_name = 't_fund_holding'


class TFundHoldingDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    buy_amount = DecimalField(column_name='buyAmount', constraints=[SQL("DEFAULT 0.00")])
    buy_shares = DecimalField(column_name='buyShares', constraints=[SQL("DEFAULT 0.00")])
    fund_code = CharField(column_name='fundCode')
    fund_type = IntegerField(column_name='fundType', null=True)
    memo = TextField(null=True)
    sell_amount = DecimalField(column_name='sellAmount', constraints=[SQL("DEFAULT 0.00")])
    sell_shares = DecimalField(column_name='sellShares', constraints=[SQL("DEFAULT 0.00")])

    class Meta:
        table_name = 't_fund_holding_delete'


class TFundTrans(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    amount = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    commision = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    holding_id = BigIntegerField(column_name='holdingId', index=True)
    memo = TextField(null=True)
    price = DecimalField(constraints=[SQL("DEFAULT 0.0000")], null=True)
    qirishouyi = DecimalField(null=True)
    real_gain = DecimalField(column_name='realGain', constraints=[SQL("DEFAULT 0.00")], null=True)
    shares = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    tax = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    trans_id = BigIntegerField(column_name='transId', null=True)
    trans_time = DateTimeField(column_name='transTime')
    type = IntegerField()

    class Meta:
        table_name = 't_fund_trans'


class TFundTransDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    amount = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    commision = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    holding_id = BigIntegerField(column_name='holdingId', index=True)
    memo = TextField(null=True)
    price = DecimalField(constraints=[SQL("DEFAULT 0.0000")], null=True)
    qirishouyi = DecimalField(null=True)
    real_gain = DecimalField(column_name='realGain', constraints=[SQL("DEFAULT 0.00")], null=True)
    shares = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    tax = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    trans_id = BigIntegerField(column_name='transId', null=True)
    trans_time = DateTimeField(column_name='transTime')
    type = IntegerField()

    class Meta:
        table_name = 't_fund_trans_delete'


class TImportLog(BaseModel):
    f_time = DateTimeField(column_name='FTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    ftype = IntegerField(column_name='Ftype', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_import_log'
        indexes = (
            (('f_trading_entity', 'ftype'), False),
        )


class TInvestFundHolding(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    fundcode = CharField()
    fundtype = IntegerField()
    memo = TextField(null=True)
    provider_name = CharField(column_name='providerName', null=True)
    shares = DecimalField(null=True)

    class Meta:
        table_name = 't_invest_fund_holding'


class TInvestFundHoldingDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    fundcode = CharField()
    fundtype = IntegerField()
    memo = TextField(null=True)
    provider_name = CharField(column_name='providerName', null=True)
    shares = DecimalField(null=True)

    class Meta:
        table_name = 't_invest_fund_holding_delete'


class TInvestFundRecord(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    commision = DecimalField(null=True)
    holding_id = BigIntegerField(column_name='holdingID')
    memo = TextField(null=True)
    price = DecimalField(null=True)
    real_gain = DecimalField(column_name='realGain', null=True)
    seven_days_income = DecimalField(column_name='sevenDaysIncome', null=True)
    shares = DecimalField(null=True)
    tax = DecimalField(null=True)
    trans_id = BigIntegerField(column_name='transID', null=True)
    trans_time = DateTimeField(column_name='transTime')
    type = IntegerField()

    class Meta:
        table_name = 't_invest_fund_record'


class TInvestFundRecordDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    commision = DecimalField(null=True)
    holding_id = BigIntegerField(column_name='holdingID')
    memo = TextField(null=True)
    price = DecimalField(null=True)
    real_gain = DecimalField(column_name='realGain', null=True)
    seven_days_income = DecimalField(column_name='sevenDaysIncome', null=True)
    shares = DecimalField(null=True)
    tax = DecimalField(null=True)
    trans_id = BigIntegerField(column_name='transID', null=True)
    trans_time = DateTimeField(column_name='transTime')
    type = IntegerField()

    class Meta:
        table_name = 't_invest_fund_record_delete'


class TInvestP2PHolding(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    memo = TextField(null=True)
    the_code = CharField(column_name='theCode')
    the_name = CharField(column_name='theName')
    the_type = IntegerField(column_name='theType')

    class Meta:
        table_name = 't_invest_p2p_holding'


class TInvestP2PHoldingDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    memo = TextField(null=True)
    the_code = CharField(column_name='theCode')
    the_name = CharField(column_name='theName')
    the_type = IntegerField(column_name='theType')

    class Meta:
        table_name = 't_invest_p2p_holding_delete'


class TInvestP2PRecord(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountId', null=True)
    amount = DecimalField()
    cash_back = DecimalField(column_name='cashBack', constraints=[SQL("DEFAULT 0.00")])
    cash_in = DecimalField(column_name='cashIn', constraints=[SQL("DEFAULT 0.00")])
    holding_id = BigIntegerField(column_name='holdingId', index=True)
    maturity = DateTimeField()
    memo = TextField(null=True)
    parent_id = BigIntegerField(column_name='parentId', constraints=[SQL("DEFAULT 0")], index=True, null=True)
    product_name = CharField(column_name='productName', null=True)
    rate = DecimalField()
    rate_hike = DecimalField(column_name='rateHike', constraints=[SQL("DEFAULT 0.00")])
    term = BigIntegerField()
    the_status = IntegerField(column_name='theStatus')
    unit = IntegerField()

    class Meta:
        table_name = 't_invest_p2p_record'


class TInvestP2PRecordDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountId', null=True)
    amount = DecimalField()
    cash_back = DecimalField(column_name='cashBack', constraints=[SQL("DEFAULT 0.00")])
    cash_in = DecimalField(column_name='cashIn', constraints=[SQL("DEFAULT 0.00")])
    holding_id = BigIntegerField(column_name='holdingId', index=True)
    maturity = DateTimeField()
    memo = TextField(null=True)
    parent_id = BigIntegerField(column_name='parentId', constraints=[SQL("DEFAULT 0")], index=True, null=True)
    product_name = CharField(column_name='productName', null=True)
    rate = DecimalField()
    rate_hike = DecimalField(column_name='rateHike', constraints=[SQL("DEFAULT 0.00")])
    term = BigIntegerField()
    the_status = IntegerField(column_name='theStatus')
    unit = IntegerField()

    class Meta:
        table_name = 't_invest_p2p_record_delete'


class TInvestStockHolding(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    memo = TextField(null=True)
    provider_name = CharField(column_name='providerName', null=True)
    shares = DecimalField(null=True)
    stockcode = CharField()

    class Meta:
        table_name = 't_invest_stock_holding'


class TInvestStockHoldingDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    memo = TextField(null=True)
    provider_name = CharField(column_name='providerName', null=True)
    shares = DecimalField(null=True)
    stockcode = CharField()

    class Meta:
        table_name = 't_invest_stock_holding_delete'


class TInvestStockRecord(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    commision = DecimalField(null=True)
    holding_id = BigIntegerField(column_name='holdingID')
    memo = TextField(null=True)
    other_fee = DecimalField(column_name='otherFee', null=True)
    price = DecimalField(null=True)
    real_gain = DecimalField(column_name='realGain', null=True)
    shares = DecimalField(null=True)
    tax = DecimalField(null=True)
    total_fee = DecimalField(column_name='totalFee', null=True)
    trans_id = BigIntegerField(column_name='transID', null=True)
    trans_time = DateTimeField(column_name='transTime')
    transfer_fee = DecimalField(column_name='transferFee', null=True)
    type = IntegerField()

    class Meta:
        table_name = 't_invest_stock_record'


class TInvestStockRecordDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_id = BigIntegerField(column_name='accountID')
    amount = DecimalField(null=True)
    commision = DecimalField(null=True)
    holding_id = BigIntegerField(column_name='holdingID')
    memo = TextField(null=True)
    other_fee = DecimalField(column_name='otherFee', null=True)
    price = DecimalField(null=True)
    real_gain = DecimalField(column_name='realGain', null=True)
    shares = DecimalField(null=True)
    tax = DecimalField(null=True)
    total_fee = DecimalField(column_name='totalFee', null=True)
    trans_id = BigIntegerField(column_name='transID', null=True)
    trans_time = DateTimeField(column_name='transTime')
    transfer_fee = DecimalField(column_name='transferFee', null=True)
    type = IntegerField()

    class Meta:
        table_name = 't_invest_stock_record_delete'


class TJctClientdeviceregist(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)

    class Meta:
        table_name = 't_jct_clientdeviceregist'


class TJctClientdeviceregistDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)

    class Meta:
        table_name = 't_jct_clientdeviceregist_delete'


class TJctClientdevicestatus(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)
    login_status = IntegerField(column_name='loginStatus', constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 't_jct_clientdevicestatus'


class TJctClientdevicestatusDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)
    login_status = IntegerField(column_name='loginStatus', constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 't_jct_clientdevicestatus_delete'


class TJctSyncbookfilelist(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)
    file_name = CharField(column_name='fileName', null=True)

    class Meta:
        table_name = 't_jct_syncbookfilelist'


class TJctSyncbookfilelistDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)
    file_name = CharField(column_name='fileName', null=True)

    class Meta:
        table_name = 't_jct_syncbookfilelist_delete'


class TJctUsergrant(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    advance_func_service_time = DateTimeField(column_name='advanceFuncServiceTime')
    base_func_service_time = DateTimeField(column_name='baseFuncServiceTime')

    class Meta:
        table_name = 't_jct_usergrant'


class TJctUsergrantDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    advance_func_service_time = DateTimeField(column_name='advanceFuncServiceTime')
    base_func_service_time = DateTimeField(column_name='baseFuncServiceTime')

    class Meta:
        table_name = 't_jct_usergrant_delete'


class TJctUserlog(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)
    login_time = DateTimeField(column_name='loginTime', null=True)
    quit_time = DateTimeField(column_name='quitTime', null=True)

    class Meta:
        table_name = 't_jct_userlog'


class TJctUserlogDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    device_id = CharField(column_name='deviceID', null=True)
    login_time = DateTimeField(column_name='loginTime', null=True)
    quit_time = DateTimeField(column_name='quitTime', null=True)

    class Meta:
        table_name = 't_jct_userlog_delete'


class TKaniuBillDetail(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_card_num = CharField(column_name='FCardNum', null=True)
    f_currency = CharField(column_name='FCurrency', null=True)
    f_description = CharField(column_name='FDescription', null=True)
    f_id = BigAutoField(column_name='FId')
    f_mail_id = BigIntegerField(column_name='FMailId', null=True)
    f_post_date = DateTimeField(column_name='FPostDate', null=True)
    f_trans_date = DateTimeField(column_name='FTransDate', null=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_kaniu_bill_detail'


class TKaniuBillMails(BaseModel):
    f_attach_path = CharField(column_name='FAttachPath', null=True)
    f_begin_date = DateTimeField(column_name='FBeginDate', null=True)
    f_body_path = CharField(column_name='FBodyPath', null=True)
    f_card_num = CharField(column_name='FCardNum', null=True)
    f_cardbank = CharField(column_name='FCardbank', null=True)
    f_credit_limit = FloatField(column_name='FCreditLimit', null=True)
    f_currency = CharField(column_name='FCurrency', null=True)
    f_current_balance = FloatField(column_name='FCurrentBalance', null=True)
    f_end_date = DateTimeField(column_name='FEndDate', null=True)
    f_entry_flag = IntegerField(column_name='FEntryFlag', null=True)
    f_from_address = CharField(column_name='FFromAddress', null=True)
    f_id = BigAutoField(column_name='FId')
    f_mailbox_id = BigIntegerField(column_name='FMailboxId', null=True)
    f_parse_status = IntegerField(column_name='FParseStatus', null=True)
    f_read_status = IntegerField(column_name='FReadStatus', null=True)
    f_repay_day = DateField(column_name='FRepayDay', null=True)
    f_scan_number = IntegerField(column_name='FScanNumber', null=True)
    f_subject = CharField(column_name='FSubject', null=True)
    f_time_parse = DateTimeField(column_name='FTimeParse', null=True)
    f_time_receive = DateTimeField(column_name='FTimeReceive', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fuid = CharField(column_name='FUID', null=True)

    class Meta:
        table_name = 't_kaniu_bill_mails'


class TKaniuMailbox(BaseModel):
    f_address = CharField(column_name='FAddress', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    f_id = BigAutoField(column_name='FId')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    f_password = CharField(column_name='FPassword', null=True)

    class Meta:
        table_name = 't_kaniu_mailbox'


class TLibrary(BaseModel):
    f_charater = CharField(column_name='FCharater', null=True)
    fid = IntegerField(column_name='FID', null=True)
    f_pin_yin = CharField(column_name='FPinYin', null=True)

    class Meta:
        table_name = 't_library'
        primary_key = False


class TLoan(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    account_id = BigIntegerField(column_name='accountId', null=True)
    asset_equity = DecimalField(column_name='assetEquity', null=True)
    asset_name = CharField(column_name='assetName', null=True)
    asset_type = IntegerField(column_name='assetType', null=True)
    begin_date = DateTimeField(column_name='beginDate', null=True)
    contract_no = CharField(column_name='contractNo', null=True)
    currency_code = CharField(column_name='currencyCode', null=True)
    debtor = BigIntegerField(null=True)
    end_date = DateTimeField(column_name='endDate', null=True)
    frequency = IntegerField(null=True)
    init_balance = DecimalField(column_name='initBalance', null=True)
    init_date = DateTimeField(column_name='initDate', null=True)
    interest_rate = DecimalField(column_name='interestRate', null=True)
    loan_amount = DecimalField(column_name='loanAmount', null=True)
    loan_name = CharField(column_name='loanName', null=True)
    loan_type = CharField(column_name='loanType', null=True)
    loaner = CharField(null=True)
    memo = TextField(null=True)
    pay_account_id = BigIntegerField(column_name='payAccountId', null=True)
    payment_amount = DecimalField(column_name='paymentAmount', null=True)
    payment_every_amount = DecimalField(column_name='paymentEveryAmount', null=True)
    payment_method = IntegerField(column_name='paymentMethod', null=True)
    payment_number = IntegerField(column_name='paymentNumber', null=True)
    recognizor = BigIntegerField(null=True)
    remain_balance = DecimalField(column_name='remainBalance', null=True)
    state = IntegerField(null=True)
    term = IntegerField(null=True)

    class Meta:
        table_name = 't_loan'


class TLoanBill(BaseModel):
    bill_id = CharField(column_name='billId')
    book_id = BigIntegerField(column_name='bookId', index=True)
    create_time = DateTimeField(column_name='createTime')
    current_amount = DecimalField(column_name='currentAmount', constraints=[SQL("DEFAULT -999999.99")])
    current_period = IntegerField(column_name='currentPeriod', constraints=[SQL("DEFAULT -1")])
    due_date = DateTimeField(column_name='dueDate', constraints=[SQL("DEFAULT 1970-01-01 08:00:00")])
    fid = BigAutoField()
    loan_id = CharField(column_name='loanId')
    status = IntegerField(constraints=[SQL("DEFAULT -1")])
    suid = BigIntegerField(index=True)
    update_time = DateTimeField(column_name='updateTime')

    class Meta:
        table_name = 't_loan_bill'


class TLoanInfo(BaseModel):
    apply_date = DateTimeField(column_name='applyDate', constraints=[SQL("DEFAULT 1970-01-01 08:00:00")])
    bank_code = CharField(column_name='bankCode')
    book_id = BigIntegerField(column_name='bookId', index=True)
    create_time = DateTimeField(column_name='createTime')
    day = IntegerField()
    exceed = CharField(null=True)
    fid = BigAutoField()
    hidden = IntegerField(constraints=[SQL("DEFAULT 0")])
    loan_amount = DecimalField(column_name='loanAmount', constraints=[SQL("DEFAULT -999999.99")])
    loan_id = CharField(column_name='loanId')
    loan_name = CharField(column_name='loanName', null=True)
    loan_no = CharField(column_name='loanNo', constraints=[SQL("DEFAULT ''")], null=True)
    loan_user_name = CharField(column_name='loanUserName', constraints=[SQL("DEFAULT ''")])
    monthly_amount = DecimalField(column_name='monthlyAmount', constraints=[SQL("DEFAULT -999999.99")])
    remain = DecimalField(constraints=[SQL("DEFAULT -999999.99")])
    suid = BigIntegerField(index=True)
    total_repayment = DecimalField(column_name='totalRepayment', null=True)
    update_time = DateTimeField(column_name='updateTime')

    class Meta:
        table_name = 't_loan_info'


class TLoanInterestrate(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    account_id = BigIntegerField(column_name='accountID', null=True)
    memo = CharField(null=True)
    rate_date = DateTimeField(column_name='rateDate', null=True)
    rate_value = DecimalField(column_name='rateValue', null=True)

    class Meta:
        table_name = 't_loan_interestrate'


class TLoanPaymentmethod(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    description = CharField(null=True)
    name = CharField(null=True)
    type = IntegerField(null=True)

    class Meta:
        table_name = 't_loan_paymentmethod'


class TLoanTransaction(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    account_id = BigIntegerField(column_name='accountID', null=True)
    as_transaction_id = BigIntegerField(column_name='asTransactionID', null=True)
    current_interest = DecimalField(column_name='currentInterest', null=True)
    interest = DecimalField(null=True)
    pay_no = IntegerField(column_name='payNo', null=True)
    payed = IntegerField(null=True)
    payment = DecimalField(null=True)
    principal = DecimalField(null=True)
    remain_balance = DecimalField(column_name='remainBalance', null=True)
    state = IntegerField(null=True)
    tran_date = DateTimeField(column_name='tranDate', null=True)
    tran_memo = CharField(column_name='tranMemo', null=True)

    class Meta:
        table_name = 't_loan_transaction'


class TLoanType(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    atclass = CharField(null=True)
    memo = CharField(null=True)
    name = CharField(null=True)
    type = IntegerField(null=True)

    class Meta:
        table_name = 't_loan_type'


class TMobileBillDetail(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_bill_id = BigIntegerField(column_name='FBillId', null=True)
    f_card_num = CharField(column_name='FCardNum', null=True)
    f_currency = CharField(column_name='FCurrency', null=True)
    f_description = CharField(column_name='FDescription', null=True)
    f_from = IntegerField(column_name='FFrom', null=True)
    f_id = BigAutoField(column_name='FId')
    f_mail_id = BigIntegerField(column_name='FMailId', null=True)
    f_post_date = DateTimeField(column_name='FPostDate', null=True)
    f_tally_status = IntegerField(column_name='FTallyStatus', null=True)
    f_trans_date = DateTimeField(column_name='FTransDate', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    f_user_id = BigIntegerField(column_name='FUserId', null=True)

    class Meta:
        table_name = 't_mobile_bill_detail'


class TMobileBillMails(BaseModel):
    f_adjustment = DecimalField(column_name='FAdjustment', null=True)
    f_attach_path = CharField(column_name='FAttachPath', null=True)
    f_available_balance = DecimalField(column_name='FAvailableBalance', null=True)
    f_balance_bf = DecimalField(column_name='FBalanceBF', null=True)
    f_begin_date = DateTimeField(column_name='FBeginDate', null=True)
    f_body_path = CharField(column_name='FBodyPath', null=True)
    f_card_name = CharField(column_name='FCardName', null=True)
    f_card_num = CharField(column_name='FCardNum', null=True)
    f_cardbank = CharField(column_name='FCardbank', null=True)
    f_cash_credit_limit = DecimalField(column_name='FCashCreditLimit', null=True)
    f_credit_limit = DecimalField(column_name='FCreditLimit', null=True)
    f_currency = CharField(column_name='FCurrency', null=True)
    f_current_balance = DecimalField(column_name='FCurrentBalance', null=True)
    f_end_date = DateTimeField(column_name='FEndDate', null=True)
    f_entry_flag = IntegerField(column_name='FEntryFlag', null=True)
    f_from = IntegerField(column_name='FFrom', null=True)
    f_from_address = CharField(column_name='FFromAddress', null=True)
    f_house_holder = CharField(column_name='FHouseHolder', null=True)
    f_id = BigAutoField(column_name='FId')
    f_interest = DecimalField(column_name='FInterest', null=True)
    f_mailbox_id = BigIntegerField(column_name='FMailboxId', null=True)
    f_minimum_payment = DecimalField(column_name='FMinimumPayment', null=True)
    f_new_charges = DecimalField(column_name='FNewCharges', null=True)
    f_parse_status = IntegerField(column_name='FParseStatus', null=True)
    f_payment = DecimalField(column_name='FPayment', null=True)
    f_points_available = CharField(column_name='FPointsAvailable', null=True)
    f_points_deadline = CharField(column_name='FPointsDeadline', null=True)
    f_points_new = CharField(column_name='FPointsNew', null=True)
    f_read_status = IntegerField(column_name='FReadStatus', constraints=[SQL("DEFAULT 0")], null=True)
    f_repay_day = CharField(column_name='FRepayDay', null=True)
    f_scan_number = IntegerField(column_name='FScanNumber', null=True)
    f_subject = CharField(column_name='FSubject', null=True)
    f_time_parse = DateTimeField(column_name='FTimeParse', null=True)
    f_time_receive = DateTimeField(column_name='FTimeReceive', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    fuid = CharField(column_name='FUID', null=True)
    f_user_id = BigIntegerField(column_name='FUserId', index=True, null=True)

    class Meta:
        table_name = 't_mobile_bill_mails'


class TMobileMailbox(BaseModel):
    f_active_forward = IntegerField(column_name='FActiveForward', null=True)
    f_address = CharField(column_name='FAddress', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_forward_mail = CharField(column_name='FForwardMail', null=True)
    f_forward_mail_pw = CharField(column_name='FForwardMailPw', null=True)
    f_id = BigAutoField(column_name='FId')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_password = CharField(column_name='FPassword', null=True)
    f_set_forward = IntegerField(column_name='FSetForward', null=True)

    class Meta:
        table_name = 't_mobile_mailbox'


class TModuleDeposit(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account = BigIntegerField(null=True)
    delete_date = DateTimeField(column_name='deleteDate', null=True)
    deposit_no = CharField(column_name='depositNo', null=True)
    end_balance = DecimalField(column_name='endBalance', null=True)
    end_date = DateTimeField(column_name='endDate', null=True)
    every_money = DecimalField(column_name='everyMoney', null=True)
    frequency = IntegerField(null=True)
    init_balance = DecimalField(column_name='initBalance', null=True)
    init_date = DateTimeField(column_name='initDate', null=True)
    institution = CharField(null=True)
    interest_rate = DecimalField(column_name='interestRate', null=True)
    memo = TextField(null=True)
    owner = CharField(null=True)
    state = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    term = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    trans_account = BigIntegerField(column_name='transAccount', null=True)
    type = IntegerField()

    class Meta:
        table_name = 't_module_deposit'


class TModuleDepositTrans(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    amount = DecimalField()
    deposit_id = BigIntegerField(column_name='depositId', index=True)
    periods = IntegerField(null=True)
    trans_id = BigIntegerField(column_name='transId', index=True, null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 't_module_deposit_trans'


class TModuleStockHolding(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    companyid = BigIntegerField(null=True)
    defaultaccountid = BigIntegerField(null=True)
    memo = TextField(null=True)
    stockcode = CharField(index=True)

    class Meta:
        table_name = 't_module_stock_holding'


class TModuleStockHoldingDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    companyid = BigIntegerField(null=True)
    defaultaccountid = BigIntegerField(null=True)
    memo = TextField(null=True)
    stockcode = CharField(index=True)

    class Meta:
        table_name = 't_module_stock_holding_delete'


class TModuleStockTrans(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    amount = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commision = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    holding_id = BigIntegerField(column_name='holdingId', index=True)
    memo = TextField(null=True)
    other_fee = DecimalField(column_name='otherFee', constraints=[SQL("DEFAULT 0.00")])
    price = DecimalField(constraints=[SQL("DEFAULT 0.0000")], null=True)
    real_gain = DecimalField(column_name='realGain', constraints=[SQL("DEFAULT 0.00")], null=True)
    shares = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    tax = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    total_fee = DecimalField(column_name='totalFee', null=True)
    trans_id = BigIntegerField(column_name='transId', null=True)
    trans_time = DateTimeField(column_name='transTime')
    transfer_fee = DecimalField(column_name='transferFee', constraints=[SQL("DEFAULT 0.00")])
    type = IntegerField()

    class Meta:
        table_name = 't_module_stock_trans'


class TModuleStockTransDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    amount = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    commision = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    holding_id = BigIntegerField(column_name='holdingId', index=True)
    memo = TextField(null=True)
    other_fee = DecimalField(column_name='otherFee', constraints=[SQL("DEFAULT 0.00")])
    price = DecimalField(constraints=[SQL("DEFAULT 0.0000")], null=True)
    real_gain = DecimalField(column_name='realGain', constraints=[SQL("DEFAULT 0.00")], null=True)
    shares = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    tax = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    total_fee = DecimalField(column_name='totalFee', constraints=[SQL("DEFAULT 0.00")], null=True)
    trans_id = BigIntegerField(column_name='transId', null=True)
    trans_time = DateTimeField(column_name='transTime')
    transfer_fee = DecimalField(column_name='transferFee', constraints=[SQL("DEFAULT 0.00")])
    type = IntegerField()

    class Meta:
        table_name = 't_module_stock_trans_delete'


class TMultiProject(BaseModel):
    f_create_time = DateTimeField(column_name='FCreate_Time', null=True)
    f_desciption = CharField(column_name='FDesciption', null=True)
    f_image = CharField(column_name='FImage', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_project_no = CharField(column_name='FProject_no', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_multi_project'


class TMultiProjectUser(BaseModel):
    f_create_time = DateTimeField(column_name='FCreate_Time', null=True)
    f_invite_time = DateTimeField(column_name='FInvite_time', null=True)
    f_invitecode = CharField(column_name='FInvitecode', null=True)
    f_project_id = BigIntegerField(column_name='FProject_id', index=True, null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_user_name = CharField(column_name='FUser_Name', null=True)
    f_user_no = CharField(column_name='FUser_No', null=True)
    f_user_id = BigIntegerField(column_name='FUser_id', null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_multi_project_user'
        indexes = (
            (('f_user_id', 'f_status'), False),
        )


class TNewMccInfo(BaseModel):
    commission = IntegerField()
    daily_limit = IntegerField()
    father_code = CharField()
    father_txt = CharField()
    fid = BigAutoField()
    grandpa_code = CharField()
    grandpa_txt = CharField()
    max_commission_one_transaction = IntegerField()
    mcc_code = CharField()
    mcc_txt = CharField()
    mcc_type = IntegerField()
    mcc_type_txt = CharField()
    no_pin_flag = IntegerField()

    class Meta:
        table_name = 't_new_mcc_info'


class TPreference(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_key = CharField(column_name='FKey')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_value = TextField(column_name='FValue', null=True)

    class Meta:
        table_name = 't_preference'


class TPreferenceDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_key = CharField(column_name='FKey')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_value = TextField(column_name='FValue', null=True)

    class Meta:
        table_name = 't_preference_delete'


class TPreferenceIsolated(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_key = CharField(column_name='FKey')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_value = TextField(column_name='FValue', null=True)

    class Meta:
        table_name = 't_preference_isolated'


class TPreferenceIsolatedDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_key = CharField(column_name='FKey')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_value = TextField(column_name='FValue', null=True)

    class Meta:
        table_name = 't_preference_isolated_delete'


class TPushDevice(BaseModel):
    f_date = DateTimeField(column_name='FDate', null=True)
    f_device = CharField(column_name='FDevice')
    fid = BigAutoField(column_name='FID')
    f_model = CharField(column_name='FModel', null=True)
    f_product = CharField(column_name='FProduct', null=True)
    f_state = IntegerField(column_name='FState', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    f_udid = CharField(column_name='FUdid', null=True)
    f_user_name = CharField(column_name='FUserName', null=True)
    f_version = CharField(column_name='FVersion', null=True)

    class Meta:
        table_name = 't_push_device'
        indexes = (
            (('f_udid', 'f_type'), False),
        )


class TRecurrenceRule(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    end_date = DateTimeField(column_name='endDate')
    is_enable = IntegerField(column_name='isEnable', constraints=[SQL("DEFAULT 1")])
    start_date = DateTimeField(column_name='startDate')
    the_day = CharField(column_name='theDay', null=True)
    the_month = CharField(column_name='theMonth', null=True)
    the_weekday = CharField(column_name='theWeekday', null=True)
    the_year = CharField(column_name='theYear', null=True)

    class Meta:
        table_name = 't_recurrence_rule'


class TRecurrenceRuleDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_source_key = CharField(column_name='FSourceKey')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    end_date = DateTimeField(column_name='endDate')
    is_enable = IntegerField(column_name='isEnable', constraints=[SQL("DEFAULT 1")])
    start_date = DateTimeField(column_name='startDate')
    the_day = CharField(column_name='theDay', null=True)
    the_month = CharField(column_name='theMonth', null=True)
    the_weekday = CharField(column_name='theWeekday', null=True)
    the_year = CharField(column_name='theYear', null=True)

    class Meta:
        table_name = 't_recurrence_rule_delete'


class TRongtszapply(BaseModel):
    f_create_time = DateField(column_name='FCreateTime')
    f_last_modify_time = DateField(column_name='FLastModifyTime', index=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    apply_id = BigIntegerField(column_name='applyId')
    contact = CharField()
    fid = BigAutoField()
    income = DecimalField()
    loan_amount = DecimalField(column_name='loanAmount')
    loan_period = IntegerField(column_name='loanPeriod')
    name = CharField()
    product_name = CharField(column_name='productName')
    salary_type = IntegerField(column_name='salaryType')

    class Meta:
        table_name = 't_rongtszapply'


class TSendMailTask(BaseModel):
    f_email = CharField(column_name='FEmail', null=True)
    f_email_json_data = CharField(column_name='FEmailJsonData', null=True)
    f_email_template_name = CharField(column_name='FEmailTemplateName', null=True)
    fp_task_id = BigIntegerField(column_name='FPTaskId', constraints=[SQL("DEFAULT 0")], null=True)
    f_product_type = IntegerField(column_name='FProductType', constraints=[SQL("DEFAULT 0000000000")], null=True)
    f_send_priority = IntegerField(column_name='FSendPriority', constraints=[SQL("DEFAULT 0")], null=True)
    f_task_created_time = DateTimeField(column_name='FTaskCreatedTime', null=True)
    f_task_end_time = DateTimeField(column_name='FTaskEndTime', null=True)
    f_task_id = BigAutoField(column_name='FTaskId')
    f_task_start_time = DateTimeField(column_name='FTaskStartTime', null=True)
    f_task_state = IntegerField(column_name='FTaskState', null=True)
    f_task_type = IntegerField(column_name='FTaskType', constraints=[SQL("DEFAULT 1")], null=True)
    f_user_account = CharField(column_name='FUserAccount', null=True)
    f_user_id = BigIntegerField(column_name='FUserId', null=True)
    f_user_last_visit_time = DateTimeField(column_name='FUserLastVisitTime', null=True)
    f_user_latest_trans_time = DateTimeField(column_name='FUserLatestTransTime', null=True)
    f_user_registered_time = DateTimeField(column_name='FUserRegisteredTime', null=True)
    fvip = IntegerField(column_name='FVIP', constraints=[SQL("DEFAULT 0")], null=True)
    fterminal_report_id = BigIntegerField(column_name='FterminalReportId', null=True)

    class Meta:
        table_name = 't_send_mail_task'
        indexes = (
            (('f_product_type', 'f_task_type', 'fp_task_id', 'f_task_state', 'f_send_priority'), False),
            (('fp_task_id', 'f_email'), False),
        )


class TSharebookChange(BaseModel):
    f_create_time = DateTimeField(column_name='fCreateTime', index=True)
    f_trading_entity = BigIntegerField(column_name='fTradingEntity', index=True)
    ffeidee_id = BigIntegerField(column_name='ffeideeId')
    ffeidee_id2 = BigIntegerField(column_name='ffeideeId2', null=True)
    fid = BigAutoField()
    fmemo = CharField(null=True)
    ftype = IntegerField()

    class Meta:
        table_name = 't_sharebook_change'


class TSmsBag(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_from = CharField(column_name='FFrom', constraints=[SQL("DEFAULT 'web'")], null=True)
    fid = BigAutoField(column_name='FID')
    f_invite_num = IntegerField(column_name='FInviteNum', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_open_id = CharField(column_name='FOpenId')
    f_sms_num = IntegerField(column_name='FSmsNum', null=True)
    f_user_id = BigIntegerField(column_name='FUserId')

    class Meta:
        table_name = 't_sms_bag'


class TSyncBook(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_count = IntegerField(column_name='FSyncCount', constraints=[SQL("DEFAULT 0")], null=True)
    f_sync_type = CharField(column_name='FSyncType', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', unique=True)

    class Meta:
        table_name = 't_sync_book'


class TSyncChange(BaseModel):
    bookid = BigIntegerField(index=True)
    createtime = DateTimeField()
    fid = BigAutoField()
    syncid = CharField(index=True)
    synctime = DateTimeField()
    syncuserid = BigIntegerField()

    class Meta:
        table_name = 't_sync_change'


class TSyncChangeTransaction(BaseModel):
    buyeraccount = CharField(null=True)
    buyercategory = CharField(null=True)
    buyermoney = DecimalField(null=True)
    createtime = DateTimeField()
    fid = BigAutoField()
    memo = CharField(null=True)
    operatetype = IntegerField()
    selleraccount = CharField(null=True)
    sellercategory = CharField(null=True)
    sellermoney = DecimalField(null=True)
    syncid = CharField(index=True)
    transid = BigIntegerField(index=True)
    translastmodifytime = DateTimeField(null=True)
    transtime = DateTimeField()
    transtype = IntegerField()

    class Meta:
        table_name = 't_sync_change_transaction'


class TSyncLabel(BaseModel):
    f_app_name = CharField(column_name='FAppName', null=True)
    f_book_id = BigIntegerField(column_name='FBookId', index=True, null=True)
    fid = AutoField(column_name='FID')
    f_label = CharField(column_name='FLabel', index=True, null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_restored = IntegerField(column_name='FRestored', constraints=[SQL("DEFAULT 0")])
    f_sync_count = IntegerField(column_name='FSyncCount', constraints=[SQL("DEFAULT 0")], null=True)
    f_timestamp = BigIntegerField(column_name='FTimestamp', null=True)
    fudid = CharField(column_name='FUDID', null=True)
    f_user_name = CharField(column_name='FUserName', null=True)
    f_mirror = CharField(column_name='fMirror', null=True)
    fversion = CharField(null=True)

    class Meta:
        table_name = 't_sync_label'
        indexes = (
            (('f_app_name', 'fudid'), False),
        )


class TSyncPreSql(BaseModel):
    fid = BigAutoField(column_name='FID')
    fsql = CharField(column_name='FSQL', null=True)
    fudid = CharField(column_name='FUDID', null=True)
    ftradingentity = BigIntegerField(column_name='Ftradingentity', index=True, null=True)
    ftype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 't_sync_pre_sql'


class TSyncProfile(BaseModel):
    fi_pad_permit_count = IntegerField(column_name='FIPadPermitCount', null=True)
    fi_pad_permit_version = CharField(column_name='FIPadPermitVersion', null=True)
    fi_pad_version = CharField(column_name='FIPadVersion', null=True)
    fi_phone_permit_count = IntegerField(column_name='FIPhonePermitCount', null=True)
    fi_phone_permit_version = CharField(column_name='FIPhonePermitVersion', null=True)
    fi_phone_version = CharField(column_name='FIPhoneVersion', null=True)
    fjct_version = DecimalField(column_name='FJCTVersion', null=True)
    fkdjct_permit_count = IntegerField(column_name='FKDJCTPermitCount', null=True)
    fkdjct_permit_version = CharField(column_name='FKDJCTPermitVersion', null=True)
    fkdjct_version = DecimalField(column_name='FKDJCTVersion', null=True)
    f_only_vip = IntegerField(column_name='FOnlyVIP', null=True)
    fpc_version = DecimalField(column_name='FPCVersion', null=True)
    f_permit_count = IntegerField(column_name='FPermitCount', null=True)
    f_permit_version = CharField(column_name='FPermitVersion', null=True)
    f_stop_pc = IntegerField(column_name='FStopPC', null=True)
    f_version = CharField(column_name='FVersion', null=True)

    class Meta:
        table_name = 't_sync_profile'
        primary_key = False


class TSysNotify(BaseModel):
    f_content = TextField(column_name='FContent', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_expired_time = DateTimeField(column_name='FExpiredTime', null=True)
    fid = AutoField(column_name='FID')
    f_level = IntegerField(column_name='FLevel', null=True)
    f_notify_mode = IntegerField(column_name='FNotifyMode', null=True)
    f_pic = CharField(column_name='FPic', null=True)
    f_product = CharField(column_name='FProduct', null=True)
    f_receivers = CharField(column_name='FReceivers', null=True)
    f_status = IntegerField(column_name='FStatus', index=True, null=True)
    f_terminal = CharField(column_name='FTerminal', null=True)
    f_title = CharField(column_name='FTitle', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    f_url = CharField(column_name='FUrl', null=True)

    class Meta:
        table_name = 't_sys_notify'


class TSysServerMessage(BaseModel):
    f_db_id = IntegerField(column_name='FDbId')
    f_notify_id = BigIntegerField(column_name='FNotifyId')
    f_read_time = DateTimeField(column_name='FReadTime', null=True)

    class Meta:
        table_name = 't_sys_server_message'
        indexes = (
            (('f_notify_id', 'f_db_id'), False),
        )
        primary_key = False


class TSysTerminalMessage(BaseModel):
    f_device = CharField(column_name='FDevice', index=True, null=True)
    fid = BigAutoField(column_name='FID')
    fimei = CharField(column_name='FIMEI', null=True)
    f_model = CharField(column_name='FModel', null=True)
    f_msg_id = BigIntegerField(column_name='FMsgID', null=True)
    f_notify_id = BigIntegerField(column_name='FNotifyID', null=True)
    f_product_name = CharField(column_name='FProductName', null=True)
    f_product_version = CharField(column_name='FProductVersion', null=True)
    f_read_time = DateTimeField(column_name='FReadTime', null=True)
    f_system_name = CharField(column_name='FSystemName', null=True)
    f_system_version = CharField(column_name='FSystemVersion', null=True)
    fudid = CharField(column_name='FUDID', index=True, null=True)
    f_user_name = CharField(column_name='FUserName', null=True)

    class Meta:
        table_name = 't_sys_terminal_message'


class TTag(BaseModel):
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', constraints=[SQL("DEFAULT 0")])
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    f_user = BigIntegerField(column_name='FUser', index=True, null=True)

    class Meta:
        table_name = 't_tag'


class TTagDelete(BaseModel):
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = BigAutoField(column_name='FID')
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', constraints=[SQL("DEFAULT 0")])
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    f_user = BigIntegerField(column_name='FUser', index=True, null=True)

    class Meta:
        table_name = 't_tag_delete'


class TTerminal(BaseModel):
    f_content = CharField(column_name='FContent', null=True)
    f_is_verify = IntegerField(column_name='FIsVerify', constraints=[SQL("DEFAULT 0")])
    f_month_report = IntegerField(column_name='FMonthReport', constraints=[SQL("DEFAULT 1")], null=True)
    f_name = CharField(column_name='FName', null=True)
    f_receiv_notify = IntegerField(column_name='FReceivNotify', constraints=[SQL("DEFAULT 1")])
    f_receiv_report = IntegerField(column_name='FReceivReport', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_week_report = IntegerField(column_name='FWeekReport', constraints=[SQL("DEFAULT 0")], null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_terminal'


class TTerminalManage(BaseModel):
    fid = AutoField(column_name='FID')
    fimei = CharField(column_name='FIMEI', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_model = CharField(column_name='FModel', null=True)
    f_partner = CharField(column_name='FPartner', null=True)
    f_product_name = CharField(column_name='FProductName', null=True)
    f_product_version = CharField(column_name='FProductVersion', null=True)
    f_sign = CharField(column_name='FSign', null=True)
    f_system_name = CharField(column_name='FSystemName', null=True)
    f_system_version = CharField(column_name='FSystemVersion', null=True)
    f_token = CharField(column_name='FToken', null=True)
    fudid = CharField(column_name='FUDID', null=True)
    f_user_name = CharField(column_name='FUserName', null=True)

    class Meta:
        table_name = 't_terminal_manage'
        indexes = (
            (('f_product_name', 'fudid'), False),
        )


class TTerminalReport(BaseModel):
    f_content = CharField(column_name='FContent', index=True, null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_month_report = IntegerField(column_name='FMonthReport', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_receiv_notify = IntegerField(column_name='FReceivNotify', null=True)
    f_receiv_report = IntegerField(column_name='FReceivReport', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_week_report = IntegerField(column_name='FWeekReport', null=True)

    class Meta:
        table_name = 't_terminal_report'


class TTerminalRule(BaseModel):
    f_editor = CharField(column_name='FEditor', null=True)
    fid = AutoField(column_name='FID')
    fimei = CharField(column_name='FIMEI', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_partner = CharField(column_name='FPartner', null=True)
    f_product_name = CharField(column_name='FProductName', null=True)
    f_product_version = CharField(column_name='FProductVersion', null=True)
    f_right = IntegerField(column_name='FRight', null=True)
    f_sign = CharField(column_name='FSign', null=True)
    f_system_name = CharField(column_name='FSystemName', null=True)
    f_system_version = CharField(column_name='FSystemVersion', null=True)
    ftid = CharField(column_name='FTID', null=True)
    fudid = CharField(column_name='FUDID', null=True)
    f_user_name = CharField(column_name='FUserName', null=True)

    class Meta:
        table_name = 't_terminal_rule'


class TTerminalSign(BaseModel):
    fid = BigAutoField(column_name='FID')
    fimei = CharField(column_name='FIMEI', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_memory = CharField(column_name='FMemory', null=True)
    f_model = CharField(column_name='FModel', null=True)
    f_partner = CharField(column_name='FPartner', null=True)
    f_product_name = CharField(column_name='FProductName', null=True)
    f_product_version = CharField(column_name='FProductVersion', null=True)
    f_resolution = CharField(column_name='FResolution', null=True)
    f_sdk_version = CharField(column_name='FSdkVersion', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_system_name = CharField(column_name='FSystemName', null=True)
    f_system_version = CharField(column_name='FSystemVersion', null=True)
    fudid = CharField(column_name='FUDID', index=True, null=True)
    f_user_name = CharField(column_name='FUserName', null=True)

    class Meta:
        table_name = 't_terminal_sign'


class TTradingEntity(BaseModel):
    f_address = IntegerField(column_name='FAddress', index=True, null=True)
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_icon = CharField(column_name='FIcon', null=True)
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_identifier = IntegerField(column_name='FIdentifier', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_type = IntegerField(column_name='FType', index=True, null=True)
    f_user = BigIntegerField(column_name='FUser', index=True, null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_trading_entity'


class TTradingEntityDebt(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    buyer_account_poid = BigIntegerField(column_name='buyerAccountPOID', null=True)
    buyer_amount = DecimalField(column_name='buyerAmount', null=True)
    seller_account_poid = BigIntegerField(column_name='sellerAccountPOID', null=True)
    seller_amount = DecimalField(column_name='sellerAmount', null=True)
    trading_entity_poid = BigIntegerField(column_name='tradingEntityPOID')

    class Meta:
        table_name = 't_trading_entity_debt'


class TTradingEntityDebtDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime')
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    buyer_account_poid = BigIntegerField(column_name='buyerAccountPOID', null=True)
    buyer_amount = DecimalField(column_name='buyerAmount', null=True)
    seller_account_poid = BigIntegerField(column_name='sellerAccountPOID', null=True)
    seller_amount = DecimalField(column_name='sellerAmount', null=True)
    trading_entity_poid = BigIntegerField(column_name='tradingEntityPOID')

    class Meta:
        table_name = 't_trading_entity_debt_delete'


class TTradingEntityDelete(BaseModel):
    f_address = IntegerField(column_name='FAddress', index=True, null=True)
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_icon = CharField(column_name='FIcon', null=True)
    f_icon_url = CharField(column_name='FIconUrl', null=True)
    f_identifier = IntegerField(column_name='FIdentifier', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_name = CharField(column_name='FName', null=True)
    f_order = IntegerField(column_name='FOrder', null=True)
    f_parent = BigIntegerField(column_name='FParent', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_type = IntegerField(column_name='FType', index=True, null=True)
    f_user = BigIntegerField(column_name='FUser', index=True, null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_trading_entity_delete'


class TTransDebt(BaseModel):
    f_buyer_debt = BigIntegerField(column_name='FBuyerDebt', index=True, null=True)
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_debt_type = IntegerField(column_name='FDebtType', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_seller_debt = BigIntegerField(column_name='FSellerDebt', index=True, null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_trans = BigIntegerField(column_name='FTrans', index=True)

    class Meta:
        table_name = 't_trans_debt'


class TTransDebtDelete(BaseModel):
    f_buyer_debt = BigIntegerField(column_name='FBuyerDebt', index=True, null=True)
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_debt_type = IntegerField(column_name='FDebtType', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_seller_debt = BigIntegerField(column_name='FSellerDebt', index=True, null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_trans = BigIntegerField(column_name='FTrans')

    class Meta:
        table_name = 't_trans_debt_delete'


class TTransDebtGroup(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_group_type = IntegerField(column_name='FGroupType', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_trans = BigIntegerField(column_name='FTrans')
    f_trans_group = CharField(column_name='FTransGroup', null=True)

    class Meta:
        table_name = 't_trans_debt_group'


class TTransDebtGroupDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    f_group_type = IntegerField(column_name='FGroupType', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    f_trans = BigIntegerField(column_name='FTrans')
    f_trans_group = CharField(column_name='FTransGroup', null=True)

    class Meta:
        table_name = 't_trans_debt_group_delete'


class TTransDebtMap(BaseModel):
    f_amount = FloatField(column_name='FAmount', null=True)
    f_debt = BigIntegerField(column_name='FDebt', index=True, null=True)
    f_repay = BigIntegerField(column_name='FRepay', index=True, null=True)
    fid = BigAutoField()

    class Meta:
        table_name = 't_trans_debt_map'


class TTransExtendMap(BaseModel):
    f_extend1 = CharField(column_name='FExtend1', null=True)
    f_extend2 = CharField(column_name='FExtend2', null=True)
    f_extend3 = CharField(column_name='FExtend3', null=True)
    f_extend4 = BigIntegerField(column_name='FExtend4', null=True)
    f_extend5 = BigIntegerField(column_name='FExtend5', null=True)
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', constraints=[SQL("DEFAULT 2016-10-24 00:00:00")],
                                       index=True)
    f_photo_name = CharField(column_name='FPhotoName', null=True)
    f_trans_id = BigIntegerField(column_name='FTransId')
    f_user_id = BigIntegerField(column_name='FUserId')

    class Meta:
        table_name = 't_trans_extend_map'
        indexes = (
            (('f_user_id', 'f_trans_id'), True),
        )
        primary_key = CompositeKey('f_trans_id', 'f_user_id')


class TTransLog(BaseModel):
    f_event_log = BigIntegerField(column_name='FEventLog', index=True, null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_trans = BigAutoField(column_name='FTrans')

    class Meta:
        table_name = 't_trans_log'


class TTransTagMap(BaseModel):
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', constraints=[SQL("DEFAULT 2016-10-24 00:00:00")],
                                       index=True)
    f_tag = BigIntegerField(column_name='FTag', constraints=[SQL("DEFAULT 0")], index=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    f_trans = BigIntegerField(column_name='FTrans')
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_trans_tag_map'
        indexes = (
            (('f_trans', 'f_tag'), True),
            (('f_trans', 'f_type'), False),
        )
        primary_key = CompositeKey('f_tag', 'f_trans')


class TTransaction(BaseModel):
    f_asset_id = CharField(column_name='FAssetID', null=True)
    f_asset_money = DecimalField(column_name='FAssetMoney', null=True)
    f_asset_number = DecimalField(column_name='FAssetNumber', null=True)
    f_buyer = BigIntegerField(column_name='FBuyer', index=True, null=True)
    f_buyer_category = BigIntegerField(column_name='FBuyerCategory', null=True)
    f_buyer_money = DecimalField(column_name='FBuyerMoney', null=True)
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_content = TextField(column_name='FContent', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_debt = IntegerField(column_name='FDebt', null=True)
    f_extend1 = CharField(column_name='FExtend1', null=True)
    f_extend2 = DecimalField(column_name='FExtend2', null=True)
    f_from = CharField(column_name='FFrom', null=True)
    fid = BigIntegerField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_memo = TextField(column_name='FMemo', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_property = CharField(column_name='FProperty', null=True)
    f_relation = CharField(column_name='FRelation', null=True)
    f_relation_unit = BigIntegerField(column_name='FRelationUnit', null=True)
    f_seller = BigIntegerField(column_name='FSeller', index=True, null=True)
    f_seller_category = BigIntegerField(column_name='FSellerCategory', null=True)
    f_seller_money = DecimalField(column_name='FSellerMoney', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_split_id = CharField(column_name='FSplitID', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', constraints=[SQL("DEFAULT 0")])
    f_trans_time = DateTimeField(column_name='FTransTime', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    furl = CharField(column_name='FURL', null=True)

    class Meta:
        table_name = 't_transaction'
        indexes = (
            (('f_trading_entity', 'f_trans_time'), False),
            (('fid', 'f_trading_entity'), True),
        )
        primary_key = CompositeKey('f_trading_entity', 'fid')


class TTransactionAnalyse(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    fid = AutoField(column_name='FID')
    f_name = CharField(column_name='FName', null=True)
    f_parent_name = CharField(column_name='FParentName', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', null=True)
    f_transaction = BigIntegerField(column_name='FTransaction', null=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_transaction_analyse'


class TTransactionCredit(BaseModel):
    fid = BigAutoField(column_name='FID')
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_transaction_credit'


class TTransactionDelete(BaseModel):
    f_asset_id = CharField(column_name='FAssetID', null=True)
    f_asset_money = DecimalField(column_name='FAssetMoney', null=True)
    f_asset_number = DecimalField(column_name='FAssetNumber', null=True)
    f_buyer = BigIntegerField(column_name='FBuyer', index=True, null=True)
    f_buyer_category = BigIntegerField(column_name='FBuyerCategory', null=True)
    f_buyer_money = DecimalField(column_name='FBuyerMoney', null=True)
    f_client_id = CharField(column_name='FClientID', null=True)
    f_client_info = CharField(column_name='FClientInfo', null=True)
    f_content = TextField(column_name='FContent', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_debt = IntegerField(column_name='FDebt', null=True)
    f_extend1 = CharField(column_name='FExtend1', null=True)
    f_extend2 = DecimalField(column_name='FExtend2', null=True)
    f_from = CharField(column_name='FFrom', null=True)
    fid = BigIntegerField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True, null=True)
    f_memo = TextField(column_name='FMemo', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_property = CharField(column_name='FProperty', null=True)
    f_relation = CharField(column_name='FRelation', null=True)
    f_relation_unit = BigIntegerField(column_name='FRelationUnit', null=True)
    f_seller = BigIntegerField(column_name='FSeller', index=True, null=True)
    f_seller_category = BigIntegerField(column_name='FSellerCategory', null=True)
    f_seller_money = DecimalField(column_name='FSellerMoney', null=True)
    f_source_key = CharField(column_name='FSourceKey', null=True)
    f_split_id = CharField(column_name='FSplitID', null=True)
    f_status = IntegerField(column_name='FStatus', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity')
    f_trans_time = DateTimeField(column_name='FTransTime', null=True)
    f_type = IntegerField(column_name='FType', null=True)
    furl = CharField(column_name='FURL', null=True)

    class Meta:
        table_name = 't_transaction_delete'
        indexes = (
            (('f_trading_entity', 'f_trans_time'), False),
            (('fid', 'f_trading_entity'), True),
        )
        primary_key = CompositeKey('f_trading_entity', 'fid')


class TTransactionListTemplate(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_ids = TextField(column_name='accountIds', null=True)
    begin_time = DateTimeField(column_name='beginTime', null=True)
    corporation_ids = TextField(column_name='corporationIds', null=True)
    created_source = IntegerField(column_name='createdSource', constraints=[SQL("DEFAULT 0")], null=True)
    custom_config = TextField(column_name='customConfig', null=True)
    end_time = DateTimeField(column_name='endTime', null=True)
    first_category_ids = TextField(column_name='firstCategoryIds', null=True)
    max_money_amount = CharField(column_name='maxMoneyAmount', null=True)
    member_ids = TextField(column_name='memberIds', null=True)
    memo = TextField(null=True)
    min_money_amount = CharField(column_name='minMoneyAmount', null=True)
    name = CharField()
    ordered = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    project_ids = TextField(column_name='projectIds', null=True)
    second_category_ids = TextField(column_name='secondCategoryIds', null=True)
    source_type = IntegerField(column_name='sourceType', constraints=[SQL("DEFAULT 0")], null=True)
    time_period_type = IntegerField(column_name='timePeriodType', constraints=[SQL("DEFAULT 0")], null=True)
    transaction_type = IntegerField(column_name='transactionType', constraints=[SQL("DEFAULT 15")], null=True)

    class Meta:
        table_name = 't_transaction_list_template'


class TTransactionListTemplateDelete(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime')
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', index=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True)
    account_ids = TextField(column_name='accountIds', null=True)
    begin_time = DateTimeField(column_name='beginTime', null=True)
    corporation_ids = TextField(column_name='corporationIds', null=True)
    created_source = IntegerField(column_name='createdSource', constraints=[SQL("DEFAULT 0")], null=True)
    custom_config = TextField(column_name='customConfig', null=True)
    end_time = DateTimeField(column_name='endTime', null=True)
    first_category_ids = TextField(column_name='firstCategoryIds', null=True)
    max_money_amount = CharField(column_name='maxMoneyAmount', null=True)
    member_ids = TextField(column_name='memberIds', null=True)
    memo = TextField(null=True)
    min_money_amount = CharField(column_name='minMoneyAmount', null=True)
    name = CharField()
    ordered = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    project_ids = TextField(column_name='projectIds', null=True)
    second_category_ids = TextField(column_name='secondCategoryIds', null=True)
    source_type = IntegerField(column_name='sourceType', constraints=[SQL("DEFAULT 0")], null=True)
    time_period_type = IntegerField(column_name='timePeriodType', constraints=[SQL("DEFAULT 0")], null=True)
    transaction_type = IntegerField(column_name='transactionType', constraints=[SQL("DEFAULT 15")], null=True)

    class Meta:
        table_name = 't_transaction_list_template_delete'


class TTransactionTemplate(BaseModel):
    f_buyer = BigIntegerField(column_name='FBuyer', null=True)
    f_buyer_category = BigIntegerField(column_name='FBuyerCategory', null=True)
    f_buyer_money = DecimalField(column_name='FBuyerMoney', null=True)
    f_changed_log = TextField(column_name='FChangedLog', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_created_source = IntegerField(column_name='FCreatedSource', constraints=[SQL("DEFAULT 0")], null=True)
    f_first_reminder_time = DateTimeField(column_name='FFirstReminderTime', null=True)
    f_group = IntegerField(column_name='FGroup', constraints=[SQL("DEFAULT 0")], null=True)
    fid = BigAutoField(column_name='FID')
    f_lastmodify_time = DateTimeField(column_name='FLastmodifyTime', index=True, null=True)
    f_member = BigIntegerField(column_name='FMember', null=True)
    f_memo = TextField(column_name='FMemo', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_ordered = IntegerField(column_name='FOrdered', constraints=[SQL("DEFAULT 0")], null=True)
    f_relation_unit = BigIntegerField(column_name='FRelationUnit', null=True)
    f_repeat_type = IntegerField(column_name='FRepeatType', constraints=[SQL("DEFAULT 0")], null=True)
    f_seller = BigIntegerField(column_name='FSeller', null=True)
    f_seller_category = BigIntegerField(column_name='FSellerCategory', null=True)
    f_seller_money = DecimalField(column_name='FSellerMoney', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_tag = BigIntegerField(column_name='FTag', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_transaction_template'


class TTransactionTemplateDelete(BaseModel):
    f_buyer = BigIntegerField(column_name='FBuyer', null=True)
    f_buyer_category = BigIntegerField(column_name='FBuyerCategory', null=True)
    f_buyer_money = DecimalField(column_name='FBuyerMoney', null=True)
    f_changed_log = TextField(column_name='FChangedLog', null=True)
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_created_source = IntegerField(column_name='FCreatedSource', constraints=[SQL("DEFAULT 0")], null=True)
    f_first_reminder_time = DateTimeField(column_name='FFirstReminderTime', null=True)
    f_group = IntegerField(column_name='FGroup', constraints=[SQL("DEFAULT 0")], null=True)
    fid = BigAutoField(column_name='FID')
    f_lastmodify_time = DateTimeField(column_name='FLastmodifyTime', index=True, null=True)
    f_member = BigIntegerField(column_name='FMember', null=True)
    f_memo = TextField(column_name='FMemo', null=True)
    f_name = CharField(column_name='FName', null=True)
    f_ordered = IntegerField(column_name='FOrdered', constraints=[SQL("DEFAULT 0")], null=True)
    f_relation_unit = BigIntegerField(column_name='FRelationUnit', null=True)
    f_repeat_type = IntegerField(column_name='FRepeatType', constraints=[SQL("DEFAULT 0")], null=True)
    f_seller = BigIntegerField(column_name='FSeller', null=True)
    f_seller_category = BigIntegerField(column_name='FSellerCategory', null=True)
    f_seller_money = DecimalField(column_name='FSellerMoney', null=True)
    f_sync_time = DateTimeField(column_name='FSyncTime', null=True)
    f_tag = BigIntegerField(column_name='FTag', null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_type = IntegerField(column_name='FType', null=True)

    class Meta:
        table_name = 't_transaction_template_delete'


class TUBackupLog(BaseModel):
    fbackup_id = BigIntegerField(null=True)
    ffilename = CharField(null=True)
    fid = BigAutoField()
    fmemo = CharField(null=True)
    fnote = CharField(null=True)
    ftime = DateTimeField(null=True)
    ftradingentity = BigIntegerField(index=True)
    ftype = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    fuser_id = BigIntegerField(column_name='fuserId', null=True)
    fversion = CharField(null=True)

    class Meta:
        table_name = 't_u_backup_log'


class TURestoreLog(BaseModel):
    fbackup_id = BigIntegerField(null=True)
    fid = BigAutoField()
    fnote = CharField(null=True)
    ftime = DateTimeField(null=True)
    ftradingentity = BigIntegerField(index=True)
    fuser_id = BigIntegerField(column_name='fuserId', null=True)

    class Meta:
        table_name = 't_u_restore_log'


class TUploadFile(BaseModel):
    f_create_time = DateTimeField(column_name='FCreateTime', null=True)
    f_dir1 = CharField(column_name='FDir1', null=True)
    f_dir2 = CharField(column_name='FDir2', null=True)
    f_dir3 = CharField(column_name='FDir3', null=True)
    fid = BigAutoField(column_name='FID')
    f_last_modify_time = DateTimeField(column_name='FLastModifyTime', null=True)
    f_memo = CharField(column_name='FMemo', null=True)
    f_save_file_path = CharField(column_name='FSaveFilePath', index=True, null=True)
    f_trading_entity = BigIntegerField(column_name='FTradingEntity', index=True, null=True)
    f_upload_file_name = CharField(column_name='FUploadFileName', null=True)
    feidee_user = BigIntegerField(column_name='feideeUser', index=True, null=True)

    class Meta:
        table_name = 't_upload_file'


class TVersionTables(BaseModel):
    f_create_date = DateTimeField(column_name='FCreateDate', null=True)
    f_flag = IntegerField(column_name='FFlag', constraints=[SQL("DEFAULT 1")], null=True)
    f_group = CharField(column_name='FGroup', null=True)
    f_order = BigIntegerField(column_name='FOrder', constraints=[SQL("DEFAULT 0")], null=True)
    f_table_name = CharField(column_name='FTableName', primary_key=True)
    f_where = CharField(column_name='FWhere', null=True)

    class Meta:
        table_name = 't_version_tables'


class TVoting(BaseModel):
    f_competitor_id = IntegerField(column_name='FCompetitorId', null=True)
    f_content = IntegerField(column_name='FContent', null=True)
    fid = AutoField(column_name='FID')
    f_vote_time = DateTimeField(column_name='FVoteTime', null=True)
    f_voter_id = IntegerField(column_name='FVoterId', null=True)

    class Meta:
        table_name = 't_voting'


class TWeixinAuthorizerInfo(BaseModel):
    authorize_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    authorizer_access_token = CharField(constraints=[SQL("DEFAULT ''")])
    authorizer_appid = CharField(constraints=[SQL("DEFAULT ''")])
    authorizer_refresh_token = CharField(constraints=[SQL("DEFAULT ''")])
    component_appid = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expires_in = IntegerField(constraints=[SQL("DEFAULT 0")])
    expiry_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    last_modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    last_refresh_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    map_key = CharField(constraints=[SQL("DEFAULT ''")])
    setting_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    store_code = CharField(constraints=[SQL("DEFAULT ''")])
    trading_entity = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 't_weixin_authorizer_info'


class TWeixinAuthorizerUser(BaseModel):
    authorizer_appid = CharField(constraints=[SQL("DEFAULT ''")])
    component_appid = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    last_modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    openid = CharField(constraints=[SQL("DEFAULT ''")])
    session_key = CharField(constraints=[SQL("DEFAULT ''")])
    unionid = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 't_weixin_authorizer_user'
        indexes = (
            (('component_appid', 'authorizer_appid', 'openid'), True),
        )


class TWeixinComponentInfo(BaseModel):
    component_access_token = CharField(constraints=[SQL("DEFAULT ''")])
    component_appid = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    component_verify_ticket = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expires_in = IntegerField(constraints=[SQL("DEFAULT 0")])
    expiry_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    last_modify_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    last_refresh_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 't_weixin_component_info'


if __name__ == "__main__":
    tags = TCategoryTag.select()
    for tag in tags:
        print(model_to_dict(tag))
