def pp_inquiry_type_1(df):
    # inquiry_type 열을 소문자로 변환
    df['inquiry_type'] = df['inquiry_type'].str.lower()
    
    # 대체할 문자열과 대상 문자열 정의
    replacement_mapping = {
        '(select id_needs)':'etc',
        'customer suggestions':'customer suggestions',
        'digital platform':'product information',
        'display product':'product information',
        'display textbook and photos':'product information',
        'educational equipments':'product information',
        'estoy buscando para ecuador este producto lg magnit micro led, para un cliente de 138 pulgadas, con envió marítimo.':'product purchase inquiry',
        'etc.':'etc',
        'event inquiry':'etc',
        'evento_sdelestero':'etc',
        'first info and pricing':'pricing and demo request',
        'for school':'product information',
        'high inch 86 / 98 or 110':'product information',
        'hola me pueden cotizar 19 pantallas interactivas de 100 pulgadas entregadas en guayaquil -ecuador.':'quotation and purchase Inquiry',
        'hospital tv':'product information',
        'hotel tv products':'product information',
        'i want to know the details about it':'product information',
        'idb':'product and technical support/consultation',
        'intégrateur historique du george v':'intégrateur historique du george v',
        'led signage':'product information',
        'media inquiry':'customer suggestions',
        'needs':'etc',
        'not specified':'other',
        'oem/odm request':'product and technical support/consultation',
        'one quick:flex':'product information',
        'other_':'other',
        'others':'other',
        'pantallas interactivas para clinicas':'product information',
        'preciso de um monitor médico para radiografia convencional e tomogrtafia.':'product information',
        'probeam precio':'pricing and demo request',
        'purchase or quotation':'purchase',
        'quotation or purchase consultation':'purchase',
        'quotation_':'purchase',
        'quotation_or_purchase_consultation':'purchase',
        'request a demo':'pricing and demo request',
        'request for distributorship':'partnership/distributorship request',
        'request for partnership':'partnership/distributorship request',
        'request for quotation or purchase':'quotation and purchase Inquiry',
        'request for technical consulting':'product and technical support/consultation',
        'sales inquiry':'sales',
        'services':'product and technical support/consultation',
        'solicito apoyo para realizar cotizacion de los dispositivos que ofrecen en la solución one quick: ':'quotation and purchase Inquiry',
        'standalone':'product information',
        'teach':'trainings',
        'technical consultation':'technical',
        'technical support':'technical',
        'technical_consultation':'technical',
        'toi muon tim hieu thong tin ky thuat, gia ca cua sp de su dung':'quotation and purchase Inquiry',
        'tv interactive':'product information',
        'tôi cần tham khảo giá và giải pháp từ lg':'quotation and purchase Inquiry',
        'usage or technical consultation':'product and technical support/consultation',
        'usage_or_technical_consultation':'product and technical support/consultation',
        'video wall':'product and technical support/consultation',
        'vrf':'product information',
        'vui lòng báo giá giúp mình sản phẩm đo thân nhiệt xin cảm ơn':'product information',
        'window facing product':'product information',
        'aio':'product information',
        'product purchase inquiry':'purchase',
        'purchaseor_purchase_consultation':'purchase',
        'quotation and purchase inquiry':'purchase',
        'solicito apoyo para realizar cotizacion de los dispositivos que ofrecen en la solución one quick: ':'purchase',
        'usage or technical':'technical',
        'usage_or_technical':'technical',
        'customer suggestions': 'etc',
        'intégrateur historique du george v': 'etc',
        'solicito apoyo para realizar cotizacion de los dispositivos que ofrecen en la solución\xa0one quick:\xa0': 'purchase',
        'product and technical support/consultation':'product and technical consultation',
        'product and technical/consultation':'product and technical consultation',
        'product and technical consultation':'technical',
        'technical':'product and technical consultation',
        'quotation and purchase inquiry':'purchase',
        'purchase':'quotation and purchase inquiry',
        'product and product and product and product and product and product and technical consultation':'product and technical consultation',
        'quotation and quotation and purchase inquiry inquiry':'quotation and purchase inquiry',
        'quotation and quotation and purchase inquiry inquiry':'quotation and purchase inquiry',
        'product and product and product and product and product and technical consultation':'product and technical consultation',
        'product and product and product and product and technical consultation':'product and technical consultation',
        'quotation and purchase inquiryor_quotation and purchase inquiry_consultation':'quotation and purchase inquiry',
        'quotation or quotation and purchase inquiry consultation':'quotation and purchase inquiry',
        'request for product and product and product and product and product and technical consultation consulting':'product and technical consultation',
        'request for quotation or quotation and purchase inquiry':'quotation and purchase inquiry',
        'usage or product and product and product and product and product and technical consultation':'product and technical consultation',
        'quotation and quotation and purchase inquiry inquiry':'quotation and purchase inquiry',
        'product and product and product and technical consultation':'product and technical consultation',
        'customer suggestions':'etc',
        'quotation and quotation and purchase inquiry inquiry':'product and technical consultation',
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