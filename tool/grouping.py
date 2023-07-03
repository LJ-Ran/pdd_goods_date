import json
from . import details_page
import requests
import time

verify_auth_token_new = ''


def get_grouping_data(access_token, number, class_number, anti_content, verify_auth_token, pdd_uid):
    verify_auth_token_new = verify_auth_token
    """
    获得分类商品
    :param access_token:
    :param number:
    :param search_param:
    :param anti_content:
    :param verify_auth_token:
    :param pdd_uid:
    :return:
    """
    page_number = int((number + 20 - 1) / 20)
    excel_data = []
    for page in range(1, page_number + 1):
        print(f'当前页数{page}: 总数 {page_number}')
        json_str = get_grouping_json(access_token=access_token, verify_auth_token=verify_auth_token_new,
                                     anti_content=anti_content, pdd_uid=pdd_uid, off_set=page * 20,
                                     class_number=class_number)
        if 'error_code' in json_str and json_str['error_code'] == 40001:
            raise Exception(f'对不起您的access_token 已经失效了请重新设置 当前的access_token 为：{access_token}')
        elif 'error_code' in json_str and json_str['error_code'] == 40002:
            raise Exception("拼多多出现了未知异.....")
        elif 'error_code' in json_str and json_str['error_code'] == 54001:
            print("对不起拼多多的反爬虫机制已经触发了请去浏览器完成验证并且重新设置 verify_auth_token 参数")
            verify_auth_token_new = input("请重新输入verifyauthtoken参数：")
            json_str = get_grouping_json(access_token=access_token, verify_auth_token=verify_auth_token_new,
                                         anti_content=anti_content, pdd_uid=pdd_uid, off_set=page * 20,
                                         class_number=class_number)
        goods_list = json_str['goods_list']
        for index in goods_list:
            cnt = index['cnt']
            if cnt > 1500 or cnt < 80:
                continue

            goods_detail = details_page.get_goods_detail(index=index, verify_auth_token=verify_auth_token,
                                                         access_token=access_token,
                                                         pdd_uid=pdd_uid)
            if goods_detail == 'void':
                continue
            elif goods_detail == 'dissatisfy':
                continue
            excel_data.append(goods_detail)
            # 暂停1秒
            time.sleep(1)
    return excel_data


def get_grouping_json(access_token, verify_auth_token, anti_content, pdd_uid, off_set, class_number):
    """
    发起搜索请求
    :param class_number: 分类号
    :param access_token:  access_token
    :param verify_auth_token: verify_auth_token
    :param anti_content: anti_content
    :param pdd_uid: 拼多多用户id
    :param off_set:  页数
    :return: json字符串
    """
    # 设置请求头信息
    header = {
        'accesstoken': access_token,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        'verifyauthtoken': verify_auth_token
    }
    url = f'https://mobile.yangkeduo.com/proxy/api/api/search/opt/{class_number}/groups?pdduid={pdd_uid}&source=search&offset={off_set}&count=20&sort=default&anti_content={anti_content}'
    # 获得request
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    # 处理响应数据的编码集
    content = response.text
    return json.loads(content)
