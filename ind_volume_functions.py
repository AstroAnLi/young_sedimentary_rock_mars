from erosion_age import multiply_bins
import erosion_age
import matplotlib.pyplot as plt
import numpy as np
from erosion_age import find_max

#defining variables
second = 1/60/60/24/365.2422/(10**9) #in Ga
start_time = second
end_time = 4.5
points = 1000

area1a = erosion_age.area1a
area1b = erosion_age.area1b
area1c = erosion_age.area1c
area2 = erosion_age.area2
area3 = erosion_age.area3
area4a = erosion_age.area4a
area4b = erosion_age.area4b
area4c = erosion_age.area4c
area5a = erosion_age.area5a
area5b = erosion_age.area5b
area5c = erosion_age.area5c
area6a = erosion_age.area6a
area6b = erosion_age.area6b
area7 = erosion_age.area7
areaall = erosion_age.find_area(erosion_age.data_list)
areas = [area1a, area1b, area1c, area2, area3, area4a, area4b, area4c, area5a, \
        area5b, area5c, area6a, area6b, area7]

def find_error(X,Y,Z, sigma=0.9545):
  '''
  Finds the min and max betas and times within a given sigma error, default is two sigma.
  '''
  z = Z.flatten()
  sig2 = (1 - sigma) * max(z)
  z2 = sorted(i for i in z if i >= sig2)
  max_p = max(z2)
  min_p = min(z2)
  z_2sigma_region = np.argwhere((Z>= min_p) & (Z <= max_p))
  t_indices = z_2sigma_region[:,0]
  b_indices = z_2sigma_region[:,-1]
  times = np.take(X, t_indices)
  betas = np.take(Y, b_indices)
  min_beta = min(betas)
  max_beta = max(betas)
  min_time = min(times)
  max_time = max(times)
  return min_beta, max_beta, min_time, max_time

#Finds the best fit age, beta, and thickness
def find_thickness_lost(time, beta):
  '''
  Returns thickness lost in meters.
  '''
  thickness = beta*time
  return thickness

area_names =  ['1a', '1b', '1c', '2', '3','4a','4b','4c', '5a', '5b', '5c', '6a', '6b',\
               '7', 'all']

#Finds best fit age and beta and multiplies for thickness lost
for area_name in area_names:
  area = globals()['area' + area_name]
  if area_name == 'all':
    X, Y, Z = multiply_bins(area_name, second, 4.5, 1, 13000, 1000, area, tlins=True,blins=True, all=True)
  else:
    X, Y, Z = multiply_bins(area_name, second, 4.5, 1, 13000, 1000, area, tlins=True,blins=True)
  a, b = find_max(X,Y,Z) #a is age, b is beta
  th = find_thickness_lost(a,b)
  globals()[f"b{area_name}"] = b / 1e9 #assigning beta variables
  globals()[f"t{area_name}"] = th #assigning thickness lost variables
  # print(a, b, th)

bs = [b1a, b1b, b1c, b2, b3, b4a, b4b, b4c, b5a, b5b, b5c, b6a, b6b, b7] #used in cum_vol_plots.py
tls = [t1a, t1b, t1c, t2, t3, t4a, t4b, t4c, t5a, t5b, t5c, t6a, t6b, t7]

#present thicknesses found outside of code in ArcGIS or literature values
#1 km for Upper Mt Sharp, 0.3 km for Aeolis Planum, and 1 km for Eastern Candor
pt1a = 599
pt1b = 2197
pt1c = 1973
pt2 = 0.3e3
pt3 = 1e3
pt4a = 1901
pt4b = 477.3333333
pt4c = 1232.333333
pt5a = 801.2636303393872
pt5b = 388.0972157604289
pt5c = 475.034930299745
pt6a = 1230
pt6b = 3909
pt7 = 1e3
pts = [pt1a, pt1b, pt1c, pt2, pt3, pt4a, pt4b, pt4c, pt5a, pt5b, pt5c, pt6a, pt6b, pt7]
ptall = sum(pts)

sed_rate= 0.0001797727273 #m/yr sedimentation rate #calculated using Aharonson & Lewis 2014 data

def find_thickness(T, pt, tl, sed_r, b, area):
  '''
  Finds the thickness over time.
  Inputs:
    T: time array
    pt: present thickness (m)
    tl: thickness lost (m)
    sed_r: global sedimentation rate
    b: beta
    area: area of site
  Output:
    age, thickness, and volume arrays
  '''
  maxt = pt + tl #max thickness = present thickness + thickness lost
  ys = []
  vs = []
  ages = []
  dummy_v = 0
  for i,age in enumerate(T):
    y = pt + b * age  #convert beta to meters
    if y < maxt:
      v = y / 1000 *area  #volume in km^3
      ys.append(y)
      vs.append(v)
      ages.append(age)
    else:
      if dummy_v == 0:
        age_offset = T[i]
        dummy_v += 1
      new_age = age-age_offset
      y = maxt - sed_r * new_age
      # y = maxt - sed_r * age
      v = y/1000 * area  #volume in km^3
      if y >= 0:
        ys.append(y)
        vs.append(v)
        ages.append(age)
      elif dummy_v == 1:
        last_age = maxt/sed_r + age_offset
        ages.append(last_age)
        ys.append(0.0)
        vs.append(0.0) #only works for positive volumes
        dummy_v += 1
      else:
        break
  return ages, ys, vs

def calc_thick(name, beta_ages, age_list, thickness_list, vol_list, t_array, b_array, z_array, area, pt, sig=0.9545):
  '''
  Helper function for find_sedplot. Calculates the site's thickness over time.
  Input:
    name: name of region
    beta_ages: age array
    age_list: list of ages
    thickness_list: list of thicknesses
    vol_list: list of volumes
    t_array: age array that was used to find probability array
    b_array: beta array that was used to find beta array
    z_array: probability array
    area: site's area (km^2)
    pt: present thickness (m)
    sig: sigma value to use
  Output:
    mint: minimum thickness
    maxt: maximum thickness
    plot_ages: general list of ages
    ages: age array for ages less than or equal to the maximum age
    mina: minimum age
  '''
  plot_ages = np.array(age_list)
  minb, maxb, mina, maxa = find_error(t_array, b_array, z_array, sigma=sig) #2 beta values, replaced in_maxt, in_mint
  mina = mina * 1e9
  maxa = maxa * 1e9
  beta_ages = beta_ages[beta_ages <= maxa] / (1e9) #changed units y to Gyr
  mint = beta_ages * minb + pt
  maxt = beta_ages * maxb + pt
  ages = np.array(beta_ages) * 1e9
  return mint, maxt, plot_ages, ages, mina

def find_sedplot(name, beta_ages, age_list, thickness_list, vol_list, t_array, b_array, z_array, area, pt, volume=False):
  '''
  Helper function for join_all. Creates the volume or thickness plot for a particular region.
  Input:
    name: name of region
    beta_ages: age array
    age_list: list of ages
    thickness_list: list of thicknesses
    vol_list: list of volumes
    t_array: age array that was used to find probability array
    b_array: beta array that was used to find beta array
    z_array: probability array
    area: site's area (km^2)
    pt: present thickness (m)
    volume: if volume is True, finds volume plot not thickness plot
  '''
  in_mint, in_maxt, plot_ages, in_ages, in_mina = calc_thick(name, beta_ages, age_list, thickness_list, vol_list, t_array, b_array, z_array, area, pt)
  in_mint1, in_maxt1, plot_ages1, in_ages1, in_mina1 = calc_thick(name, beta_ages, age_list, thickness_list, vol_list, t_array, b_array, z_array, area, pt, sig=0.6827)
  fig,ax = plt.subplots()
  if volume:
    ax.plot(plot_ages, vol_list, color='k')
    in_maxv = in_maxt/1000 * area #km^3
    in_minv = in_mint/1000 * area #km^3
    in_maxv1 = in_maxt1/1000 * area
    in_minv1 = in_mint1/1000 * area
    ax.fill_between(in_ages, in_minv, in_maxv, where=in_ages<in_mina, color='c', alpha = 0.3, linewidth=0)
    ax.fill_between(in_ages, 0, in_maxv, where=in_ages>=in_mina, color='c', alpha=0.3,linewidth=0.6)
    #for one sigma:
    ax.fill_between(in_ages1, in_minv1, in_maxv1, where=in_ages1<in_mina1, color='c', alpha = 0.7, linewidth=0)
    ax.fill_between(in_ages1, 0, in_maxv1, where=in_ages1>=in_mina1, color='c',alpha=0.7,linewidth=0.6)
    plt.xlabel('Age (yr)')
    plt.ylabel('Volume (km$^3$)')
  else:
    ax.plot(plot_ages, thickness_list, color='k')
    ax.fill_between(in_ages, in_mint, in_maxt, where=in_ages<in_mina, color='c', alpha = 0.3, linewidth=0)
    ax.fill_between(in_ages1, in_mint1, in_maxt1, where=in_ages1<in_mina1, color='c', alpha = 0.3, linewidth=0)
    if pt > 0:
      ax.fill_between(in_ages, 0, in_maxt, where=in_ages>=in_mina, color='c', alpha=0.3, linewidth=0.6)
      #for one sigma:
      ax.fill_between(in_ages1, 0, in_maxt1, where=in_ages1>=in_mina1, color='c',alpha=0.7,linewidth=0.6)
    else:
      ax.fill_between(in_ages, pt, in_maxt, where=in_ages>=in_mina, color='c', alpha=0.3, linewidth=0)
      #for one sigma:
      ax.fill_between(in_ages1, pt, in_maxt1, where=in_ages1>=in_mina1, color='c', alpha = 0.7, linewidth=0)
    plt.xlabel('Age (yr)')
    plt.ylabel('Thickness (m)')
  area_name = name + '.png'
  fig.savefig(area_name, dpi=300, bbox_inches='tight')

def join_all(title, t_start, t_end, pt, tl, sed_r, b, area, t_array, b_array, z_array, vol_plot=False, n_points=1000):
  '''
  Joins find_thickness and find_sedplot functions as one function to plot thickness or volume.
  Input:
    title: name of region
    t_start: starting age
    t_end: ending age
    pt: present thickness (m)
    tl: thickness lost
    sed_r: global sedimentation rate
    b: best fit beta
    area: site's area (km^2)
    t_array: age array that was used to find probability array
    b_array: beta array that was used to find beta array
    z_array: probability array
    vol_plot: if True, finds volume plot not thickness plot
    n_points: number of points to put into age array
  '''
  age_array = np.linspace(t_start, t_end, n_points)
  age, thick, vol = find_thickness(age_array, pt, tl, sed_rate, b,area)
  find_sedplot(title, age_array, age, thick, vol, t_array, b_array, z_array, area, pt, volume=vol_plot)
