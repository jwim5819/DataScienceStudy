import re
from collections import defaultdict
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup


def make_df_datas(dictData: defaultdict, htmlList: list, compi, column, index=False):
    """defalitdict에 html리스트 compile한 결과값 저장해주는 함수

    Args:
        dictData (defaultdict): defaultdict class list
        htmlList (list): html list
        compi (compile): compile pattern
        column (str): dict keys
        index (bool, optional): 값 없을때 Fasle 반환. Defaults to False.

    Returns:
        bool: index가 True일때 찾을 값이 없으면 False 반환 => break로 사용
    """
    for i in htmlList:
        i = str(i)
        m = compi.search(i)
        if index is False:
            if m is not None:
                if m.group() == 't"></td>':  # t"></td> = 비어있는 값
                    dictData[column].append(".")
                else:
                    dictData[column].append(m.group())
        else:  # index가 True일때 bool 값만 반환
            if m is not None:
                return True
            else:
                return False


def print_input_data(df_datas: dict, last_count, pre_count):
    """들어오는 데이터 출력해주는 함수

    Args:
        df_datas (dict): 데이터 입력받는 dict
        last_count (int): 데이터 추가된후 갯수
        pre_count (int): 데이터 추가되기 전 갯수
    """
    index = last_count - pre_count  # df_datas에서 값 찾아올 인덱스
    for i in range(pre_count, last_count):  # 계속 증가하는 번호 적용
        print(
            "[{0:3d}]: 매장이름: {1}, 지역: {2}, 주소: {3}, 전화번호: {4}".format(
                i, df_datas["매장이름"][-index], df_datas["위치(시,구)"][-index], df_datas["주소"][-index], df_datas["전화번호"][-index]
            )
        )
        index = index - 1  # 뒤로 찾아가야하기 때문에 -1


def final_do(a=1):
    """최종 실행 및 데이터 반환 함수

    Args:
        a (int, optional): 시작할 페이지. Defaults to 1.

    Returns:
        dict: 최종 데이터
    """
    countinue = True
    df_datas = defaultdict(list)

    while countinue:
        html = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=" + str(a) + "&sido=&gugun=&store="

        hollys_url = urlopen(html)
        hollys = BeautifulSoup(hollys_url, "html.parser")

        # 정규식 패턴 생성
        p_name = re.compile(r"\w+([점]|[페])(?=[<]/a)")
        p_region = re.compile(r"\w{2}\s\w+\s?\w?(?=[<]/td)")
        p_locate = re.compile(r"(?<=[>])\w+\s\w+\s.*(?=[<]/a)")
        p_number = re.compile(
            r"(\d{0,4}[-]?[)]?\s?\d{2,4}[-]?\s?\d{4}\s?(?=[<]))|(t\"></td>)|(?<=[>])[.](?=[<])|(?<=[>])[없][음](?=[<])|(?<=[>])[xX](?=[<])"
        )

        p_list = [p_name, p_region, p_locate, p_number]
        columns = ["매장이름", "위치(시,구)", "주소", "전화번호"]

        hollys_table = hollys.find("tbody").find_all("td", {"class": "center_t"})
        hollys_region = hollys.find("tbody").find_all("td", {"class": "noline"})

        pre_count = len(df_datas["매장이름"])  # 이전에 저장된 데이터 갯수

        for p in p_list:
            column = columns[p_list.index(p)]
            if p != p_region:
                make_df_datas(df_datas, hollys_table, p, column)
            else:
                cout = make_df_datas(df_datas, hollys_region, p, column, index=True)  # region을 index로 설정해 데이터 존재유무 파악
                if cout is True:
                    make_df_datas(df_datas, hollys_region, p, column)
                else:
                    print(f"전체 매장 수: {pre_count}")  # region 패턴에서 값이 안나왔을때 False 반환 및 전체 매장 수 출력
                    countinue = cout

        last_count = len(df_datas["매장이름"])  # 한페이지 저장하고 난 후 데이터 갯수

        print_input_data(df_datas, last_count, pre_count)

        a += 1

    return df_datas


def data_to_csv(dict_data):
    """데이터 프레임 생성 및 csv로 저장

    Args:
        dict_data (dict): 변환 및 저장할 dict 데이터
    """
    result = pd.DataFrame(dict_data)
    result.to_csv("./hw2_coffeshop_송인욱.csv", encoding='cp949', index=False)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

result = final_do(1)
data_to_csv(result)
