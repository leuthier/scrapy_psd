import math
 
import refet
 

 
# conversoes 
tmin_c = (66.65 - 32) * (5.0 / 9)                          # F -> C
 
tmax_c = (102.80 - 32) * (5.0 / 9)                         # F -> C
 
tdew_c = (57.26 - 32) * (5.0 / 9)                          # F -> C
 
ea = dado_pressao*0.1                                      # Pressão em kPa(o inmet dá em hpa que é 10^2 mas queremos em 10^3)
 
rs = radSol_inmet * 0.001                                  # Radiação solar em MJ/m^2(milijoule por metro quadrado só que o inmet dá em Kj/m^2)
 
uz = velo_inmet                                            # Velo do vento em m/s
 
lat_radians = (latitude * math.pi / 180)                   # graus -> radianos
 

 
etr = refet.daily(
 
    tmin=tmin_c, tmax=tmax_c, ea=ea, rs=rs, uz=uz,
 
    zw=3, elev=1208.5, lat=lat_radians, doy=182, ref_type='etr')
 

 
print('ETr: {:.2f} mm'.format(float(etr)))
 
print('ETr: {:.2f} in'.format(float(etr) / 25.4))
 
