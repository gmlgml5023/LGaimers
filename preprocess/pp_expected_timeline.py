def pp_et(text):
    text = str(text).replace('_', ' ').replace('.','').replace(' - ', ' ~ ')
    if text not in ['nan', 'less than 3 months', '3 months ~ 6 months', 'more than a year','9 months ~ 1 year', '6 months ~ 9 months', 'less than 6 months', 'etc','being followed up']:
        return 'memo'
    return text