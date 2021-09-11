from ind_volume_functions import tls, bs, pts, areas, area_names, sed_rate
area_names.pop()
from ind_volume_functions import find_thickness, calc_thick
import erosion_age
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ind_volume_plots import xs, ys, zs
# #If already successfully ran ind_volume_plots.py, then comment out the line above
# #and uncomment the following lines to shorten runtime.
# x1a, y1a, z1a = np.load('x1a.npy'), np.load('y1a.npy'), np.load('z1a.npy')
# x1b, y1b, z1b = np.load('x1b.npy'), np.load('y1b.npy'), np.load('z1b.npy')
# x1c, y1c, z1c = np.load('x1c.npy'), np.load('y1c.npy'), np.load('z1c.npy')
#
# x2, y2, z2 = np.load('x2.npy'), np.load('y2.npy'), np.load('z2.npy')
# x3, y3, z3 = np.load('x3.npy'), np.load('y3.npy'), np.load('z3.npy')
#
# x4a, y4a, z4a = np.load('x4a.npy'), np.load('y4a.npy'), np.load('z4a.npy')
# x4b, y4b, z4b = np.load('x4b.npy'), np.load('y4b.npy'), np.load('z4b.npy')
# x4c, y4c, z4c = np.load('x4c.npy'), np.load('y4c.npy'), np.load('z4c.npy')
#
# x5a, y5a, z5a = np.load('x5a.npy'), np.load('y5a.npy'), np.load('z5a.npy')
# x5b, y5b, z5b = np.load('x5b.npy'), np.load('y5b.npy'), np.load('z5b.npy')
# x5c, y5c, z5c = np.load('x5c.npy'), np.load('y5c.npy'), np.load('z5c.npy')
#
# x6a, y6a, z6a = np.load('x6a.npy'), np.load('y6a.npy'), np.load('z6a.npy')
# x6b, y6b, z6b = np.load('x6b.npy'), np.load('y6b.npy'), np.load('z6b.npy')
#
# x7, y7, z7 = np.load('x7.npy'), np.load('y7.npy'), np.load('z7.npy')
# xs = [x1a, x1b, x1c, x2, x3, x4a, x4b, x4c, x5a, x5b, x5c, x6a, x6b, x7]
# ys = [y1a, y1b, y1c, y2, y3, y4a, y4b, y4c, y5a, y5b, y5c, y6a, y6b, y7]
# zs = [z1a, z1b, z1c, z2, z3, z4a, z4b, z4c, z5a, z5b, z5c, z6a, z6b, z7]


def plot_vol(titles, t_start, t_end, pts, tls, sed_r, bs, areas, t_arrays, \
            b_arrays, z_arrays, n_points=1000, log=False):
  '''
  Plots cumulative volume for all areas.
  Inputs:
    titles: list of names of all regions
    t_start: start time
    t_end: end time
    pts: present thicknesses (m)
    tls: thicknesses lost (m)
    sed_r: global average sedimentation rate
    bs: best fit betas
    areas: areas (km^2) of regions
    t_arrays: age arrays
    b_arrays: beta arrays
    z_arrays: probability arrays
    n_points: number of points
    log: if True, sets x axis to be log
  '''
  age_array = np.linspace(t_start, t_end, n_points)
  df_list = []
  du_list = []
  dl_list = []
  for i, title in enumerate(titles):
    age, thick, vol = find_thickness(age_array, pts[i], tls[i], sed_rate, bs[i],areas[i])
    mint, maxt, plot_ages, ages, mina = calc_thick(title, age_array, age, thick, \
                                        vol, t_arrays[i], b_arrays[i], z_arrays[i], \
                                        areas[i], pts[i])
    vol_name = 'volume ' + str(title)
    d = pd.DataFrame({'age': plot_ages, vol_name: vol})
    df_list.append(d)
    maxv = maxt / 1000 * areas[i] #need to base on beta
    minv = mint /1000 * areas[i]
    vol_name_up = 'max error' + vol_name
    du = {'e_age': ages, vol_name_up: maxv}
    du_list.append(du)
    vol_name_low = 'min error' + vol_name
    dl = pd.DataFrame({'e_age':ages, vol_name_low:minv})
    dl[vol_name_low] = dl[vol_name_low].where(dl.e_age < mina, 0.0)
    dl_list.append(dl)
  for i, d in enumerate(df_list):
    if i ==0:
      df = d
    else:
      df = pd.merge(df, d,how='outer')
  for i, du in enumerate(du_list): #upper error
    du = pd.DataFrame.from_dict(du)
    if i==0:
      dfu = du
    else:
      dfu = pd.merge(dfu, du, how='outer')
  for i, dl in enumerate(dl_list): #lower error
    if i==0:
      dfl = dl
    else:
      dfl = pd.merge(dfl, dl, how='outer')
  dfu['total_err_up_vol'] = dfu.iloc[:,1:].sum(axis=1)
  dfl['total_err_low_vol'] = dfl.iloc[:,1:].sum(axis=1)
  df['total_volume'] = df.iloc[:,1:].sum(axis=1)
  ax = dfu.plot.area(x='e_age', y='total_err_up_vol', color='c', alpha=0.3, linewidth=0)
  if log:
    ax.set_xscale('log')
  df.plot.area(x='age', y='total_volume', ax=ax, linewidth=0, color='c')
  dfl.plot.area(x='e_age', y='total_err_low_vol', ax=ax, color='w', linewidth=0.5)
  ax.get_legend().remove()
  ax.set_xlabel('Age (yr)')
  ax.set_ylabel('Volume (km$^3$)')
  plt.savefig('cum_vol_error.png',dpi=300)
  return df, ax

#cumulative plot
df, ax = plot_vol(area_names, 0, 4.5e9, pts, tls, sed_rate, bs, areas, xs, ys, zs)
#individual volumes shown in cleaned cumulative plot, need to run above line first
df = df.drop(['total_volume'], axis=1)
dtrial = df.sort_values(by=['age'])
dtrial['volume 4b'][(dtrial['age'] > 1.7e9) & (dtrial['age'] < 1.92e9)].interpolate(method='linear', limit_direction='forward',axis=0)
dtrial['volume 4c'][(dtrial['age'] > 1.7e9) & (dtrial['age'] < 1.92e9)].interpolate(method='linear', limit_direction='forward',axis=0)
fig, ax2 = plt.subplots()
colormap = plt.cm.tab20
colors = [colormap(i) for i in np.linspace(0, 1,16)]
ax2.set_prop_cycle('color', colors)
ax2 = dtrial.plot.area(x='age',linewidth=0, stacked=True, color=colors)
ax2.get_legend().remove()
ax2.set_xlabel('Age (yr)')
ax2.set_ylabel('Volume (km$^3$)')
plt.legend(loc='upper left', bbox_to_anchor=(0.2, 1.1), ncol=3)
plt.savefig('sep_tot_vol.png', dpi=300,bbox_inches='tight')
