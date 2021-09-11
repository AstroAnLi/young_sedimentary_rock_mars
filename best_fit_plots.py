import erosion_age
from erosion_age import find_max
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
from scipy.stats import poisson


#defining variables
second = 1/60/60/24/365.2422/(10**9) #in Ga
start_time = second
end_time = 4.5
points = 1000
bin_list = erosion_age.bin_list
bin_constants = erosion_age.bin_constants

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
all_area = erosion_age.find_area(erosion_age.data_list)

def find_crater_density(H, depth, time, beta=False):
  '''
  Finds crater density.
  Input:
    H: incremental value from Michael et al. 2013 in craters/km^2/Ga
    depth: mid-depth (m)
    time: age (Ga)
    beta: erosion rate (nm/a)
  Output:
    crater_density: density of craters (craters/km^2)
  '''
  dbt = depth / beta #depth/beta to replace t above used to find N1
  N1db = 3.79e-14 * (np.exp(6.93*dbt) - 1) + 5.84e-4 * dbt
  N1_wrongdb = 5.84e-4 * dbt
  db_factor = N1db / N1_wrongdb
  N1 = 3.79e-14 * (np.exp(6.93*time) - 1) + 5.84e-4 * time
  N1_wrong = 5.84e-4 * time
  correction_factor = N1 / N1_wrong
  if beta is False:
    crater_density = H * correction_factor * time
    return crater_density
  craters_erosion =  H * db_factor * depth / beta
  craters_no_erosion = H * correction_factor * time
  if craters_erosion < craters_no_erosion:
    crater_density = craters_erosion
  else:
    crater_density = craters_no_erosion
  return crater_density

def find_best_fit(reg_n, T_start, T_end, B_start, B_end, num_points, area, tli=False,bli=False, all=False):
  '''
  Finds the model's best fit prediction for the 16 crater bins.
  Input:
      reg_n: region number
      T_start: start time
      T_end: end time
      B_start: start beta
      B_end: end beta
      num_points: number of points
      area: area of site (km^2)
      tli: if True, function creates linear time array otherwise log time
      bli: if True, function creates linear beta array, otherwise log beta
      all: if True, includes marked craters with standard craters.
  Output:
     mid_diams: list of mid-log diameters
     best_crater_density: best fit crater densities
     data_crater_densities: data crater densities
     error_list: list of tuples of lower and upper error
  '''
  X, Y, Z = erosion_age.multiply_bins(reg_n, T_start, T_end, B_start, B_end, num_points, area, tlins=tli, blins=bli,all=all)
  t, b = find_max(X,Y,Z)
  # print('age,beta',t,b) #prints best fit age and beta
  mid_diams = []
  best_crater_density = []
  for i in range(16):
    mid_diam = erosion_age.find_mid_diam(bin_list[i][0], bin_list[i][-1])
    mid_diams.append(mid_diam/1000.0)
    mid_depth = erosion_age.find_mid_depth(bin_list[i][0], bin_list[i][-1])
    H_craters = bin_constants[i]
    #for testing age correction factor
    crater_density = find_crater_density(H_craters, mid_depth, t, b)
    best_crater_density.append(crater_density)
  crater_bins = erosion_age.find_region_bin_craters(reg_n,all=all)
  data_crater_densities = []
  error_list = []
  for i, num in enumerate(crater_bins):
    data_density = num/area
    data_crater_densities.append(data_density)
    if num > 100:
      min_n = num - num
      max_n = num + num
    else:
      min_n = 0
      max_n = 100
    n = np.linspace(0.1, max_n, 1000)
    mu = num
    cdf = poisson.cdf(n, mu)
    upper = np.interp(0.8413, cdf, n)
    center = np.interp(0.5, cdf, n)
    lower = np.interp(0.1587, cdf, n)
    upper = (upper-center) / area
    lower = (center - lower) / area
    if lower < 1e-8: #dealing with 0 craters case, should make into function
      mid_diam = erosion_age.find_mid_diam(bin_list[i][0], bin_list[i][-1])
      mid_depth = erosion_age.find_mid_depth(bin_list[i][0], bin_list[i][-1])
      H_craters = bin_constants[i]
      t = np.linspace(T_start, T_end, 1000)
      x,y,p = erosion_age.find_erosion_pdf(T_start, T_end, B_start, B_end, mid_depth, num_points, 0, area, H_craters,  tlin=tli, blin=bli)
      p = p.sum(axis=1)
      c = erosion_age.find_cdf(p)
      upper_t = np.interp(0.8413, c, x) - np.interp(0.5, c,x)
      upper = find_crater_density(H_craters, mid_depth, upper_t)
      lower = upper
    error_pair = (lower,upper)
    error_list.append(error_pair)
  return mid_diams, best_crater_density, data_crater_densities, error_list

def plot_best_fit(reg_n,T_start, T_end, B_start, B_end, num_points, area, tli=False,bli=False,all=False):
  '''
  Plots the model's best fit prediction along the data's crater distribution on a log scale.
  for all 16 crater bins.
  Input:
      reg_n: region number
      T_start: start time
      T_end: end time
      B_start: start beta
      B_end: end beta
      num_points: number of points
      area: area of site (km^2)
      tli: if True, function creates linear time array otherwise log time
      bli: if True, function creates linear beta array, otherwise log beta
      all: if True, includes marked craters with standard craters.
  '''
  mid_diams, best_crater_density, data_crater_densities, error_list = find_best_fit(reg_n,T_start, T_end, B_start, B_end, num_points, area,tli=False,bli=False, all=all)
  fig,ax = plt.subplots()
  ax.set_xscale('log')
  ax.set_yscale('log')
  ax.set_xlabel('Crater Diameter (km)')
  ax.set_ylabel('Crater Density (craters km$^{-2}$)')
  ax.plot(mid_diams, best_crater_density, color='mediumturquoise')
  yerr = np.array(error_list).T
  ax.errorbar(mid_diams, data_crater_densities, yerr, fmt='.', color='k', ecolor='k')
  name = str(reg_n) + 'best_fit.png'
  plt.savefig(name,dpi=300,bbox_inches='tight')

plot_best_fit('1a', second, 4.5, 1, 1500, 1000, area1a)
#comment out below for just one plot
plot_best_fit('1b', second, 4.5, 1, 3000, 1000, area1b)
plot_best_fit('1c', second, 4.5, 1, 5000, 1000, area1c)
plot_best_fit('2', second, 4.5, 1, 5000, 1000, area2)
plot_best_fit('3a', second, 4.5, 1, 6000, 1000, area3a)
plot_best_fit('3b', second, 4.5, 1, 5000, 1000, area3b)
plot_best_fit('4a', second, 4.5, 1, 5000, 1000, area4a)
plot_best_fit('4b', second, 4.5, 1, 5000, 1000, area4b)
plot_best_fit('4c', second, 4.5, 1, 500, 1000, area4c)
plot_best_fit('5a', second, 4.5, 1, 10000, 1000, area5a)
plot_best_fit('5b', second, 4.5, 1, 5000, 1000, area5b)
plot_best_fit('5c', second, 4.5, 1, 5000, 1000, area5c)
plot_best_fit('6a', second, 4.5, 1, 5000, 1000, area6a)
plot_best_fit('6b', second, 4.5, 1, 5000, 1000, area6b)
plot_best_fit('7', second, 4.5, 1, 10000, 1000, area7)
plot_best_fit('area', second,4.5, 1, 2000, 1000, total_area, tli=False, bli=False, all=True)
