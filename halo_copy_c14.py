import fitsio
from astropy.table import Table

campaign = 14
fname = 'c14_targets.csv'
tab = Table.read(fname,format='ascii')

ddir = '/kepler/kepler2/K2/C%02d/halo/' % (campaign)
lcdir = '/kepler/kepler2/K2/C%02d/light_curves/mast/' % (campaign)

for j, epic in enumerate(tab['EPIC']):
				
	hdrfile = '%sktwo%d-c%02d_llc.fits' % (lcdir,int(epic),int(campaign))
	hdr = fitsio.read_header(hdrfile)
	name = tab[j]['Name'].replace(' ','_')

	print epic,name

	try:
		fname = '%sreduced/%shalo_lc_o1.fits' % (ddir,name)
		lc = Table.read(fname)	

	except:
		fname = '%sreduced/%shalo_lc_o2.fits' % (ddir,name)
		lc = Table.read(fname)	

	outfile = '%sreduced/dummy/ktwo%d-c%02d_llc.fits' % (ddir,epic,campaign)
	f = fitsio.FITS(outfile,'rw',clobber=True)
	lc_formatted = {'TIME':lc['time'],
					'POS_CORR1':lc['x'],
					'POS_CORR2':lc['y'],
					'SAP_QUALITY':lc['quality'],
					'CADENCENO':lc['cadence'],
					'SAP_FLUX':lc['corr_flux'],
					'SAP_FLUX_ERR':0.001*lc['corr_flux'],
					'PDCSAP_FLUX':lc['corr_flux'],
					'PDCSAP_FLUX_ERR':0.001*lc['corr_flux']}

	f.write(lc_formatted,hdr=hdr,clobber=True)
	f.close()