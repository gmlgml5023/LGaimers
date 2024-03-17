def split_word(temp):
    if isinstance(temp, str):  # 문자열인지 확인
        temp = [temp]  # 문자열을 리스트로 변환하여 단일 값도 처리 가능하도록 함
    result = []
    for item in temp:
        if isinstance(item, str):  # 문자열인지 다시 확인
            if "/" in item:
                sen_temp = item.split("/")
            elif "&" in item:
                sen_temp = item.split("&")
            elif "_" in item:
                sen_temp = item.split("_")
            elif "," in item:
                sen_temp = item.split(",")
            elif "." in item:
                sen_temp = item.split(".")
            else:
                sen_temp = [item]  # 위 조건에 해당되지 않으면 그대로 유지
            sen_temp = [word.strip() for word in sen_temp]
            result.append(" ".join(sen_temp))
        else:
            result.append(item)  # 문자열이 아닌 경우 그대로 유지
    return result