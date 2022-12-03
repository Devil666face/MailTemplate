from datetime import datetime


def get_now_date():
    return datetime.today().strftime('%d.%m.%Y')

def get_now_month():
    month =  int(datetime.today().strftime('%m'))
    print(month)
    if month==1: return 'января'
    if month==2: return 'февраля'
    if month==3: return 'марта'
    if month==4: return 'апреля'
    if month==5: return 'мая'
    if month==6: return 'июня'
    if month==7: return 'июля'
    if month==8: return 'августа'
    if month==9: return 'сентября'
    if month==10: return 'октября'
    if month==11: return 'ноября'
    if month==12: return 'декабря'
    return ''

def get_enter_date():
    return datetime.today().strftime('.%m.%Y')
