import json
import time
from . import details_page
import requests

verify_auth_token_new = ''


def get_searcher_data(access_token, number, search_param, anti_content, verify_auth_token, pdd_uid):
    """
    获得搜索 的数据
    :param access_token: access_token
    :param number: 查询数量
    :param search_param: 搜索的参数
    :param anti_content: anti_content
    :param verify_auth_token: verify_auth_token
    :param pdd_uid: 拼多多用户ID
    :return: 数据列表
    """
    verify_auth_token_new = verify_auth_token

    request_size = int((number + 20 - 1) / 20)
    excel_data = []
    for page in range(1, request_size + 1):
        print(f'当前页数{page}: 总数 {request_size}')
        json_str = get_search_json(access_token=access_token, verify_auth_token=verify_auth_token_new,
                                   anti_content=anti_content,
                                   pdd_uid=pdd_uid, search_param=search_param, page=page)
        if 'error_code' in json_str and json_str['error_code'] == 40001:
            raise Exception(f'对不起您的access_token 已经失效了请重新设置 当前的access_token 为：{access_token}')
        elif 'error_code' in json_str and json_str['error_code'] == 40002:
            raise Exception("拼多多出现了未知异.....")
        elif 'error_code' in json_str and json_str['error_code'] == 54001:
            print("对不起拼多多的反爬虫机制已经触发了请去浏览器完成验证并且重新设置 verify_auth_token 参数")
            verify_auth_token_new = input("请重新输入verifyauthtoken参数：")
            json_str = get_search_json(access_token=access_token, verify_auth_token=verify_auth_token_new,
                                       anti_content=anti_content,
                                       pdd_uid=pdd_uid, search_param=search_param, page=page)
        print(json_str)
        items = json_str['items']
        for index in items:
            # 获得拼单数量
            sales = index['sales']
            # 进行第一步筛选 去除大于1500 和小于80 的商品
            if sales > 1500 or sales < 80:
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


def get_search_json(access_token, verify_auth_token, anti_content, pdd_uid, search_param, page):
    """
    发起搜索请求
    :param access_token:  access_token
    :param verify_auth_token: verify_auth_token
    :param anti_content: anti_content
    :param pdd_uid: 拼多多用户id
    :param search_param:  搜索参数
    :param page:  页数
    :return: json字符串
    """
    # 设置请求头信息
    header = {
        'accesstoken': access_token,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        'verifyauthtoken': verify_auth_token
    }
    url = f'https://mobile.yangkeduo.com/proxy/api/search?source=search&sort=default&anti_content={anti_content}&pdduid={pdd_uid}&q={search_param}&page={page}&is_new_query=1&size=50'
    # 获得request
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    # 处理响应数据的编码集
    content = response.text
    return json.loads(content)
