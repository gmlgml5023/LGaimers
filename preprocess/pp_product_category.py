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
