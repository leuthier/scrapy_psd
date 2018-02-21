import math
import refet
import datetime



T = temp_inst #25.3 Temperatura
Tdew = ponto_ovalho_inst #20.3 Ponto de ovalho
RsK = radiacao #0.0 #Negative value, we put 0 Radiação
uz = vento_vel #1.2 Velo Vento
altitude = altitude #95
latitude = -19.407181 
longitude = -40.539825
dia = 49
hora = 13


def teste():
    data = 24/11/1994
    fmt = '%Y.%m.%d'
    data.replace("/", ".")
    dt = datetime.datetime.strptime(s, fmt)
    tt = dt.timetuple()
    data = tt.tm_yday
    print(data)

#vapour pressure actual
ea = 0.6108 * math.exp(17.27 * Tdew / (Tdew + 237.3))
# Unit conversions
if RsK < 0:
    RsK = 0
RsM = RsK/1000.0 #in MJ m-2 hr-1

lat_radians = (latitude * math.pi / 180)      # degrees -> radians
lon_radians = (longitude * math.pi / 180)   # degrees -> radians

etr = refet.hourly(
    tmean=T, ea=ea, rs=RsM, uz=uz, zw=2, elev=altitude,
    lat=lat_radians, lon=lon_radians, doy=data, time=hora, ref_type='eto')

print('ETo: {:.2f} mm'.format(float(etr)))
teste()
