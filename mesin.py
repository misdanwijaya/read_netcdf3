#Mencari data nc dari index
import numpy as np
import pandas as pd
import xarray as xr

#open data
ds = xr.open_dataset('/home/misdan/Documents/Data/data.nc')

#fungsi untuk mencari terdekat
def find_closest(A, target):
    #A must be sorted
    idx = A.searchsorted(target)
    idx = np.clip(idx, 1, len(A)-1)
    left = A[idx-1]
    right = A[idx]
    idx -= target - left < right - target
    return idx

#search latitude
def find_lat(cari_lat):
	lat = ds['XLAT'].data[0][:,0]
	hasil_lat = find_closest(lat,cari_lat)
	return hasil_lat

#search longitude
def find_long(cari_long):
	lg = ds['XLONG'].data[0][0,:]
	hasil_lg = find_closest(lg,cari_long)
	return hasil_lg

#search time
def find_time(cari_waktu):
	#convert waktu ke numpy datetime64
	convert_waktu = np.datetime64(cari_waktu)
	waktu = ds['XTIME'].data
	hasil_waktu = find_closest(waktu,convert_waktu)
	return hasil_waktu


index_lat = find_lat(2)
index_lon = find_long(97.28)
index_waktu = find_time('2018-05-25 02:00:00')

# south_north -> lat, west_east -> long
#search result
da = ds['SST'].sel(Time=index_waktu,west_east=index_lon,south_north=index_lat).data
#db = ds['water_u'].sel(time='1992-10-02',lat=-12.0, lon=95.12,method='nearest').NAVO_code
#dc = ds['u10'].sel(time='1992-02',latitude=6.0, longitude=95.20,method='nearest').time.data.astype(str).tolist()
#dd = ds['u10'].sel(time='1992-02',latitude=6.0, longitude=95.20,method='nearest').longitude.data.tolist()
#de = ds['u10'].sel(time='1992-02',latitude=6.0, longitude=95.20,method='nearest').latitude.data.tolist()
#df = ds['u10'].sel(time='1992-02',latitude=6.0, longitude=95.20,method='nearest').units

#z=dc[0]
#a=z.ndim
print('--------------------------')
print('hasilnya adalah : ')
print(da)