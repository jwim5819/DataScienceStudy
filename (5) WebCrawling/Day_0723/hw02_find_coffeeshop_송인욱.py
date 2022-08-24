import pandas as pd

data = pd.read_csv("./hw2_coffeshop_송인욱.csv", encoding="utf-8")


def find_list_make():
    """값 입력받아서 리스트 만들어주는 함수

    Raises:
        ValueError: 값이 2개 아닐때

    Returns:
        list: 도시, 지역 리스트
    """
    find_region = input("검색할 매장의 도시를 입력하세요: ")
    list = find_region.split()

    if len(list) != 2:
        raise ValueError

    return list


def set_data(data):
    """위치(시,구)를 지역, 도시로 나눠주는 함수

    Args:
        data (pd.DataFrame): 데이터

    Returns:
        df: 정제된 데이터
    """
    find_data = data["위치(시,구)"].str.split(expand=True)
    find_data.columns = ["지역", "도시"]
    new_data = pd.concat([data, find_data], axis=1)

    return new_data


def find_value(new_data, find_list):
    """데이터프레임에서 찾을 값 리스트 찾아주는 함수

    Args:
        new_data (pd.DataFrame): 데이터프레임
        find_list (list): 검색 값 리스트

    Returns:
        df: 결과 데이터프레임
    """
    val1 = find_list[0]
    val2 = find_list[1]
    new_data1 = new_data[new_data["지역"] == val1]
    new_data2 = new_data1[new_data1["도시"] == val2]
    result = new_data2.drop(columns="지역")
    result = result.drop(columns="도시")

    return result


def print_result(data: pd.DataFrame):
    """최종 결과 출력해주는 함수

    Args:
        data (pd.DataFrame): 데이터프레임
    """
    find_list = find_list_make()
    new_data = set_data(data)

    result = find_value(new_data, find_list)
    len = result.shape[0]

    print("-" * 20)
    print(f"검색된 매장 수: {len}")
    print("-" * 20)
    for i in range(len):
        print("[{0:3d}]: {1}, {2}".format(i + 1, result.iloc[i, 2], result.iloc[i, 3]))


print_result(data)
