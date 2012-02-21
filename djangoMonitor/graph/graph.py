#!/usr/bin/env python

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map=Basemap(projection='ortho',lat_0=40,lon_0=116,
              resolution='l',area_thresh=2000.)

map.drawcoastlines(color='blue')
map.drawcountries(color='red')
map.fillcontinents(color='yellow')

map.drawmapboundary()

map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))

plt.savefig('China')
plt.show()
