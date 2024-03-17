def pp_cp(text):
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