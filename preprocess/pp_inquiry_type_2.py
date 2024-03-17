def pp_inquiry_type_2(df):
    # inquiry_type 열을 소문자로 변환
    df['inquiry_type'] = df['inquiry_type'].str.lower()
    
    # 대체할 문자열과 대상 문자열 정의
    replacement_mapping = {
        'customer suggestions':'etc',
        'quotation and quotation and purchase inquiry inquiry':'quotation and purchase inquiry',
    }

    # 대상 문자열에 대해 대체 수행
    for old_str, new_str in replacement_mapping.items():
        # 괄호가 있는 경우
        if '(' in old_str:
            df['inquiry_type'] = df['inquiry_type'].replace(r'\('+old_str.strip('()')+r'\)', new_str, regex=True)
        # 괄호가 없는 경우
        else:
            df['inquiry_type'] = df['inquiry_type'].replace(old_str, new_str, regex=True)

    # inquiry_type 열의 값을 소문자로 변환하여 Counter에 전달
    inquiry_type_counts = Counter(str(value).lower() for value in df['inquiry_type'] if not isinstance(value, float))

    # 총 고유값 개수 확인
    total_unique_values = len(inquiry_type_counts)
    print("총 고유값 개수:", total_unique_values)
    

    # 각 고유값과 빈도수 출력
    print("고유값 및 빈도수:")
    for value, count in sorted(inquiry_type_counts.items()):
        print(f"'{value}':'{count}'")

    # 최빈값 계산
    mode_value = df['inquiry_type'].mode()[0]

    # 결측치를 최빈값으로 대체
    df['inquiry_type'].fillna(mode_value, inplace=True)
    print('---------------------')
    return df
