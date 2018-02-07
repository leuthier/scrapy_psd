import math
import refet

A = 8.07131
B = 1730.63
C = 233.426

T = 28.2 #25.3 Temperatura
Tdew = 21.1 #20.3 Ponto de ovalho
RsK = 2267.0 #0.0 #Negative value, we put 0 Radiação
uz = 1.6 #1.2 Velo Vento
altitude = 95
latitude = -19.407181 
longitude = -40.539825
dia = 49
hora = 13

#vapour pressure actual
ea = 0.6108 * math.exp(17.27 * Tdew / (Tdew + 237.3))
# Unit conversions
RsM = RsK/1000.0 #in MJ m-2 hr-1
lat_radians = (latitude * math.pi / 180)      # degrees -> radians
lon_radians = (longitude * math.pi / 180)   # degrees -> radians

#kpa = (10 **(A -(B/(C+T)))) * 0.1333223684

etr = refet.hourly(
    tmean=T, ea=ea, rs=RsM, uz=uz, zw=2, elev=altitude,
    lat=lat_radians, lon=lon_radians, doy=dia, time=hora, ref_type='eto')

print('ETo: {:.2f} mm'.format(float(etr)))
