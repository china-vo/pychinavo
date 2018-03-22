import sys,os
sys.path.append(os.path.join(sys.path[0],'..'))
from pychinavo.lamost import lamost
lm=lamost()
lm.dataset=5

#Query interface
params={'output.fmt':'csv','obsidTextarea':'353301001'}
hl=lm.query(params)
print(hl)


params={'output.fmt':'csv','pos.type':'proximity'}
files={'pos.posfile':('sample.txt', open('sample.txt', 'r'))}
hl=lm.query2(params, files)
print(hl)

#SQL query interface
s=lm.sql("select c.obsid,c.obsdate, c.ra, c.dec, c.z, c.lmjd from catalogue c where spos(c.ra,c.dec) @ scircle '<(331.7d, -1.4d),0.2d>' limit 5")
print(s)

#simple information
info=lm.getInfo('353301001')
for k,v in info.items():
    print(k,':',v)

#download FITS file
lm.downloadFits(obsid='353301001',savedir='./')

#download png
lm.downloadPng(obsid='353301007',savedir='./')

#download csv format spectrum
csv = lm.getFitsCsv(obsid='353301007')

#Cone Search Protocol
cs = lm.conesearch(ra=10.0004738,dec=40.9952444,radius=0.2)

#Simple Spectral Access Protocol
ssap = lm.ssap(ra=10.0004738,dec=40.9952444,radius=0.2)

#read local spectrum fits to data array
wavelength, specflux, spec_smooth_7, spec_smooth_15=lm.readFits('spec-57278-EG224429N215706B01_sp01-001.fits.gz')

#plot local spectrum
lm.plotFits('spec-57278-EG224429N215706B01_sp01-001.fits.gz')

#download spectrum data and plot
lm.downloadAndPlotSpectrum('353301007')
