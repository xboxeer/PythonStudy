#coding=utf-8
import locale
import io
from datetime import date
halloween=date(2014,10,31)
for lang_country in ['en_us','fr_fr','de_de','zh_cn','is_is']:
    locale.setlocale(locale.LC_TIME,lang_country)
    print(halloween.strftime('%A %B %d'))


