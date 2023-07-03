import json
import time
import requests


def goods_details(goods_id, verify_auth_token, access_token, pdd_uid):
    url = f'https://mobile.yangkeduo.com/proxy/api/api/oak/integration/render?pdduid={pdd_uid}'

    data = {
        "page_version": 7,
        "goods_id": goods_id,
        "page_from": 0,
        "hostname": "mobile.yangkeduo.com",
        "client_time": int(time.time()),
        "extend_map": {}
    }
    data = json.dumps(data).encode('utf-8')
    # 设置请求头信息
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        'verifyauthtoken': verify_auth_token,
        'accesstoken': access_token,
    }
    response = requests.post(url=url, headers=header, data=data)
    response.encoding = 'utf-8'
    content = response.text
    json_str = json.loads(content)
    if 'error_code' in json_str and json_str['error_code'] == 54001:
        print("对不起拼多多的反爬虫机制已经触发了请去浏览器完成验证并且重新设置 verify_auth_token 参数")
        return 'error'
    elif 'status_explain' in json_str['goods'] and json_str['goods']['status_explain'] == '原商品已售罄，为你推荐相似商品':
        return 'void'

        # 已拼
    sold_quantity = json_str['goods']['sold_quantity']
    # 没有人拼
    if sold_quantity < 1:
        return "dissatisfy"

    # 商品名
    goods_name = json_str['goods']['goods_name']
    # 商品地址
    goods_url = f'https://mobile.yangkeduo.com/goods.html?goods_id={goods_id}'
    # 价格
    min_group_price = json_str['price']['min_group_price'] / 100
    # 正在拼单的数量
    group_total = json_str['neighbor_group']['neighbor_data']['combine_group']['group_total']
    # 商品评价数量
    review_num = json_str['review']['review_data']['review_num']
    print(f'我是满足条件商品地址：{goods_url}')
    return [goods_name, goods_url, min_group_price, sold_quantity, group_total, review_num]


def get_goods_detail(index, verify_auth_token, access_token, pdd_uid):
    """
    获得商品详情
    :param index: 当前商品的json
    :param verify_auth_token:  pdd 的接口密钥
    :param access_token:  pdd token
    :param pdd_uid: 拼多多用户ID
    :return: 拼多多商品详情数据
    """
    # 获得商品ID
    goods_id = index['goods_id']
    goods_detail = goods_details(goods_id=goods_id, verify_auth_token=verify_auth_token,
                                 access_token=access_token, pdd_uid=pdd_uid)
    if goods_detail == 'error':
        verify_auth_token = input("请完成浏览器的安全认证后重新设置请输入verifyauthtoken：")
        goods_detail = goods_details(goods_id=goods_id, verify_auth_token=verify_auth_token,
                                     access_token=access_token, pdd_uid=pdd_uid)
    elif goods_detail == 'void':
        return 'void'
    elif goods_detail == 'dissatisfy':
        return 'dissatisfy'
    return goods_detail
