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