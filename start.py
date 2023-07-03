from tool.seacher import get_searcher_data
import time
from tool import excel
from tool.grouping import get_grouping_data


class Start:
    access_token = ''
    search_param = ''
    anti_content = ''
    number = 0
    get_type = 0
    verify_auth_token = ''
    file_path = ''
    pdd_uid = 0
    class_number = 0

    def __init__(self, access_token, search_param, anti_content, number, get_type, verify_auth_token, file_path,
                 pdd_uid, class_number):
        print("欢迎使用pdd 数据挖掘 V1.0  biu ~~~")
        time.sleep(1)
        print("正在执行...")
        self.access_token = access_token
        self.search_param = search_param
        self.anti_content = anti_content
        self.number = number
        self.get_type = get_type
        self.verify_auth_token = verify_auth_token
        self.file_path = file_path
        self.pdd_uid = pdd_uid
        self.class_number = class_number

    def start(self):
        # 创建文件
        file_path = (self.file_path + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ".xls")
        excel.creat_excel(file_path)
        if self.number > 10000:
            raise Exception(f'需要分析的数据目前是：{self.number}, 需要解析的数据不能超过： 10000')

        # 搜索
        if self.get_type == 1:
            data_list = get_searcher_data(search_param=self.search_param, access_token=self.access_token,
                                          number=self.number,
                                          anti_content=self.anti_content, verify_auth_token=self.verify_auth_token,
                                          pdd_uid=self.pdd_uid)
            excel.write_excel_xls_append(file_path, data_list)
        else:
            # 分类
            data_list = get_grouping_data(access_token=self.access_token, verify_auth_token=self.verify_auth_token,
                                          anti_content=self.anti_content, pdd_uid=self.pdd_uid, number=self.number,
                                          class_number=self.class_number)
            excel.write_excel_xls_append(file_path, data_list)
