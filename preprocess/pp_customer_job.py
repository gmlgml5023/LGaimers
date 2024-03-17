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
