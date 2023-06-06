from django.shortcuts import render
import requests
from io import StringIO
from .models import yearly_temperature
# Create your views here.

def index(request):
    url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/England.txt'
    r= requests.get(url)
    a=r.text
    file = StringIO(a)
    x=0
    print('\n'*5)
    for lines in file:
        z=lines.split()
        if x<7:
            x=x+1
            continue
        if x==145:
            break
        x=x+1
        print(x)
        print(z)

        record = yearly_temperature(
            year=int(z[0]),
            jan_temp=(z[1]),
            feb_temp=(z[2]),
            mar_temp=(z[3]),
            apr_temp=(z[4]),
            may_temp=(z[5]),
            jun_temp=(z[6]),
            jul_temp=(z[7]),
            aug_temp=(z[8]),
            sep_temp=(z[9]),
            oct_temp=(z[10]),
            nov_temp=(z[11]),
            dec_temp=(z[12]),
            win_temp=(z[13]),
            spr_temp=(z[14]),
            sum_temp=(z[15]),
            aut_temp=(z[16]),
            ann_temp=(z[17]),
        )
        record.save()

    return render(request,'weather/index.html')


# record = yearly_temperature(
#             year=int(z[0]),
#             jan_temp=float(z[1]),
#             feb_temp=float(z[2]),
#             mar_temp=float(z[3]),
#             apr_temp=float(z[4]),
#             may_temp=float(z[5]),
#             jun_temp=float(z[6]),
#             jul_temp=float(z[7]),
#             aug_temp=float(z[8]),
#             sep_temp=float(z[9]),
#             oct_temp=float(z[10]),
#             nov_temp=float(z[11]),
#             dec_temp=float(z[12]),
#             win_temp=float(z[13]),
#             spr_temp=float(z[14]),
#             sum_temp=float(z[15]),
#             aut_temp=float(z[16]),
#             ann_temp=float(z[17]),
#         )