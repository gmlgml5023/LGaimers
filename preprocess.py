# 필요한 라이브러리 호출
import re

# customer_country 전처리 함수 정의
def pp_customer_country(text):
    # country_map 구축
    country_map = {
        'u.s.a': ['us', 'usa', 'united states', 'ave', 'dr.', 'dr ', 'drive', 'st', 'ct', 'nevada', 'diablo', 'enterprise dr', 'east fl', 'maxine dr', 'mishawum', 'montour', 'kimball', 'highlands', 'hempston', 'bucaramanga', 'florida', 'hampshire', 'ny', 'ohio', 'roadbostonma', 'ca'],
        'italy': ['italy', 'bari'],
        'u.a.e': ['dubai', 'saudi', 'uae'],
        'antigua and barbuda': ['antigua'],
        'turkey': ['türkiye'],
        'brazil': ['são', 'capão', 'aparecida', 'joão pessoa', 'horizonte', 'cuiabá', 'dourados', 'manaus', 'recife', 'janeiro', 'rj', 'paulo'],
        'spain': ['madrid', 'elche', 'agost', 'caceres', 'canarias', 'valencia'],
        'netherlands': ['netherlands', 'curaçao', 'aruba', 'maarten'],
        'vietnam': ['ha noi'],
        'congo': ['congo'],
        'colombia': ['colombia', 'barranquilla', 'carrera', 'cartagena'],
        'india': ['indore', 'lucknow', 'chennai', 'anand', 'bangalore', 'bhilwara', 'gujarat', 'gurgaon', 'hyderabad', 'kerela', 'mumbai', 'odisha', 'pune', 'telangana', 'pradesh'],
        'greece': ['θ'],
        'nigeria': ['benin'],
        'saint kitts and nevis': ['st kitts'],
        'nan': ['', 'nd', 'br', '5555', 'a']
    }

    # 모두 소문자로 변경 후 '/'로 분할
    text = str(text).lower().split('/')[-1].strip()

    for country, keys in country_map.items():
        for k in keys:
            if k in text:
                return country

    # 이메일 주소 기재 건    
    if '@' in text:
        return 'email'

    if re.search(r'\d{6,}', text) or re.search(r'\d{5,}', text):
        return 'u.s.a'
    
########################################################################################################################################

def pp_customer_job(row):
    customer_jobs = row['customer_job']
    
    if isinstance(customer_jobs, str):  # 문자열인지 확인
        categories = ['art and design', 'marketing', 'education', 'information technology', 'administrative', 'sales', 'operation', 'program and project management', 'film production', 'finance', 'human resources', 'accounting', 'media and communication', 'legal', 'biomedical', 'construction', 'property', 'R&D','other']
        display_keywords = {
            'art and design': ['arts', 'art', 'arts and design', 'arte y diseño', 'design', 'artist, lead on equipment selection', 'arte_e_design', 'művészet_és_design'],
            'marketing': ['marketing', 'advertising'],
            'education': ['educator', 'education', 'teacher'],
            'information technology': ['engineer', 'develop', 'si', 'it', 'technology', 'chief eng'],
            'administrative': ['administration', 'administración', 'admin', 'administrative'],
            'sales' : ['sales', 'sale', 'vendite', 'értékesítés', 'salesman'],
            'operation': ['operations executive', 'regional director of operations', 'operations manager', 'director of operations', 'strategy & operations specialist', 'facilities and operations', 'operaciones'],
            'program and project management': ['project', 'genel müdür', 'gestión_de_proyectos', 'programm'],
            'film production': ['film production'],
            'finance': ['finance','finanzas', 'finanzen', 'pénzügy', 'vertrieb'],
            'human resources': ['hr','human resources', 'human resource'],
            'accounting': ['account', 'accounting', 'account management', 'account manager'],
            'media and communication' : ['media', 'media e comunicazione', 'média és kommunikáció', 'medios de comunicación', 'medien und kommunikation', 'communication'],
            'legal' : ['legal'],
            'biomedical' : ['medical solution', 'healthcare', 'spécialiste_en_imagerie_médicale', 'medical imaging'], 
            'medical' : ['doctor', 'nurse', 'pathologist', 'profesional de cirugía', 'surgery professional\u200b', 'radiology professional', 'főorvos', 'clinic', 'radiology_professional', 'profesional de radiología', 'cirugano', 'chirurgien', 'surgery professional'],
            'construction' : ['architect', 'project architect', 'contractor' ],
            'property' : ['real estate', 'proprietário(a)'],
            'R&D': ['research', 'R&D', 'r&d', ],
            'other': ['other', 'others', 'otherss']
        }

        for category in categories:
            for keyword in display_keywords[category]:
                if keyword in customer_jobs:
                    return category

    return 'other'

########################################################################################################################################

def pp_customer_position(text):
    text = text.replace('/', ' ').lower()

    position_map = {
        'executive': ['ceo', 'executive', 'president', 'entrepre', 'found', 'gerente', 'proprie', 'genel', 'chairman', 'boss', 'vp'],
        'trainee': ['intern', 'unpaid'],
        'vice president': ['vicepresident'],
        'engineering': ['installer', 'técnico', 'tech', 'desarrollo'],
        'lecturer': ['profess', 'lecture', 'educa', 'teacher', 'principal', 'academic', 'prof', 'faculty', 'hon dean', 'exam', 'pgt'],
        'none': ['bulgaria', 'not applicable'],
        'manufacturer': ['manufacturer'],
        'customer': ['user'],
        'entry level': ['entry'],
        'consultant': ['consult', 'career coach'],
        'decision maker': ['decision'],
        'director': ['director'],
        'hospital': ['főorvos', 'tierarzt', 'medical'],
        'exhibition': ['exhibition'],
        'employee': ['this is', 'mindenes', 'no influence'],
        'sales': ['sales'],
        'research': ['research', 'pathologist'],
        'others': ['other'],
        'partner': ['distributor', 'partner'],
        'management': ['manage']
    }

    for position, keywords in position_map.items():
        for keyword in keywords:
            if keyword in text:
                return position

    return text

########################################################################################################################################

def pp_expected_timeline(text):
    text = str(text).replace('_', ' ').replace('.','').replace(' - ', ' ~ ')
    if text not in ['nan', 'less than 3 months', '3 months ~ 6 months', 'more than a year','9 months ~ 1 year', '6 months ~ 9 months', 'less than 6 months', 'etc','being followed up']:
        return 'memo'
    return text

########################################################################################################################################

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

########################################################################################################################################

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

########################################################################################################################################

def pp_product_category(row):
    category_dict = {
        'display': ['Display','video', 'signage', 'Signage', '43uh5f', '49uh', '49vl', '49vl', '55vm', '86uh', '98uh', 'display', 'uh5f', 'fhd', 'gsca',
                    'gscd', 'brightness', 'laec', 'leadallin', 'bloc', 'one:quick', 'lsca', 'screen', '顯示屏',
                    'one quick', 'onequick', 'led', 'lcd', 'oled', 'ultra stretch series', 'ur640', 'videowall', 'videwall', 'Monitors',
                    'virtual production', 'window facing', 'pol', '28mq780', 'monitor', 'UM3DG', 'UN880', 'MQ780', 'QP88D', 'ERGO', 'UH', '65EP5G',
                    'UL3J', 'WN780', 'svh7f', 'uh', '32SM5J', 'inch', 'essential series'],
        
        'tv': ['43uq751c0sb', 'lq621cbsb', '43us660h', '50uq801', '50us660', 'tv', 'TV', 'us670', 'pro centric', 'procentric', 'smart tv', '電視', 'CT5WJ', 'HT3WJ', 'uq801c0sb', 'uq751c0sf',
               'us660h0sd'],
        'temperature': ['definir', 'thermodynamic water heater', 'ac rumah', 'acondicionado', 'condicionado' 'vrf', 'aquecimento',
                        'calefacción', 'chiller', 'climatiseur', 'heating', 'isıtma', 'split', 'magnit', 'inverter', 'multi', 'aio',
                        'ogrzewanie', 'pendingin', 'rac', 'cac', 'conditioner', 'sac', 'scroll compressor', 'soğutucu',
                        'system ac', 'réfrigérant', 'cassete inverter', 'điều hòa', 'אחר', 'חימום', 'מזגנים ', 'מרובה ', 'تكييف وتبريد', 'تكييفات',
                        'เครื่องปรับอากาศเผื่อที่อยู่อาศัย', 'مبرد', 'reversible ac', 'single package', 'حلول التدفئة', 'פיצול מרובה', 'unitario'],
        'air': ['ahu', 'cac', 'air solution', 'air solution', 'ventilation', 'aircare', 'vrf'],
        'beam': ['bu50nst', 'projector', 'Beam', 'Projector'],
        'beauty' : ['beauty'],
        'board': ['createboard', 'idb', 'borad', 'tr3', '55tc3d'],
        'cloud': ['cloud', 'Cloud', 'id', 'cloud device', 'Thin Clients', 'Zero Clients'],
        'pc': ['laptop', 'pc', 'Laptops'],
        'software': ['pro centric', 'procentric', 'software', 'software solution', 'webos', '軟體', 'pro:centric', 'SuperSign'],
        'refrigerator': ['refrigerator'],
        'robot': ['robot'],
        'energy': ['solar', 'energy', 'energy storage system'],
        'other': ['autre', 'inne', 'khác', 'etc.', 'lainnya', 'not specified', 'other', 'Other', 'otros', 'outros', 'ฯลฯ', '其他'],
        'parts_and_accessories' : ['parts', 'accessories', 'Accessories', 'Antennas'],
        'plug' : ['SC-00DA'],
        'appliances' : ['washing machine', 'dryer', 'vb.', 'vacuum'],
        'hospital' : ['Medical', 'medical', 'hospital', 'X-ray', 'HN713D', 'HQ513D', 'surgical', 'จอภาพเพื่อการวินิจฉัย', 'จอภาพสำหรับการตรวจสอบทางคลินิก'],
        'services' : ['support', 'care program', 'Enqiry', 'inquiry', 'service', 'error']
    }
    
    for category, keywords in category_dict.items():
        for keyword in keywords:
            if keyword in row['product_category']:
                row[category] = 1
                break

    return row

########################################################################################################################################

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