#-*- coding: utf-8 -*-
'''
Adapted from a Google Collab notebook.
'''
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
from scipy.special import factorial
import scipy.stats as stats
from scipy.stats import poisson
from scipy.interpolate import interp1d
from scipy.stats import chisquare
import math
import pandas as pd
# import time #check runtime
from collections import OrderedDict
from scipy.stats import chi2_contingency
# import mpld3 #this is for Jupyter notebook live viewing
# from mpld3 import plugins

#read shapefiles
df1a = gpd.read_file('1a.shp')
df1b = gpd.read_file('1b.shp')
df1c = gpd.read_file('1c.shp')
df2 = gpd.read_file('2.shp')
df3a = gpd.read_file('3a.shp')
df3b = gpd.read_file('3b.shp')
df4a = gpd.read_file('4a.shp')
df4b = gpd.read_file('4b.shp')
df4c = gpd.read_file('4c.shp')
df5a = gpd.read_file('5a.shp')
df5b = gpd.read_file('5b.shp')
df5c = gpd.read_file('5c.shp')
df6a = gpd.read_file('6a.shp')
df6b = gpd.read_file('6b.shp')
df7a = gpd.read_file('7a.shp')
df7b = gpd.read_file('7b.shp')

#make data list
data_list = [df1a, df1b, df1c, df2, df3a, df3b, df4a, df4b, \
             df4c, df5a, df5b, df5c, df6a, df6b, df7a, df7b]

def find_area(df_list):
  '''
  Finds area of inputted dataframes.
  Input:
    df_list: List of dataframes
  Output: Area
  '''
  total_area = 0
  for df in df_list:
    total_area += sum(df.Area)
  return total_area

area_counted = find_area(data_list)
area1 = find_area([df1a, df1b, df1c])
area1a = find_area([df1a])
area1b = find_area([df1b])
area1c = find_area([df1c])
area2 = find_area([df2])
area3 = find_area([df3a, df3b])
area3a = find_area([df3a])
area3b = find_area([df3b])
area4 = find_area([df4a, df4b, df4c])
area4a = find_area([df4a])
area4b = find_area([df4b])
area4c = find_area([df4c])
area5 = find_area([df5a, df5b, df5c])
area5a = find_area([df5a])
area5b = find_area([df5b])
area5c = find_area([df5c])
area6 = find_area([df6a, df6b])
area6a = find_area([df6a])
area6b = find_area([df6b])
area7 = find_area([df7a, df7b])
area7a = find_area([df7a])
area7b = find_area([df7b])


df1a_craters = gpd.read_file('1a_clipped_1.shp')
df1b_craters = gpd.read_file('1b_clipped_1.shp')
df1c_craters = gpd.read_file('1c_clipped_1.shp')
df2_craters = gpd.read_file('2_clipped.shp')
df3a_craters = gpd.read_file('3a_clipped_1.shp')
df3b_craters = gpd.read_file('3b_clipped.shp')
df4a_craters = gpd.read_file('4a_clipped.shp')
df4b_craters = gpd.read_file('4b_clipped_1.shp')
df4c_craters = gpd.read_file('4c_clipped_2.shp')
df5a_craters = gpd.read_file('5a_clipped.shp')
df5b_craters = gpd.read_file('5b_clipped_1.shp')
df5c_craters = gpd.read_file('5c_clipped.shp')
df6a_craters = gpd.read_file('6a_cliipped.shp')
df6b_craters = gpd.read_file('6b_clipped_1.shp')
df7a_craters = gpd.read_file('7a_clipped_1.shp')
df7b_craters = gpd.read_file('7b_clipped_1.shp')

# df1_craters = [df1a_craters, df1b_craters, df1c_craters]
df1a_craters['Region'] = '1a'
df1b_craters['Region'] = '1b'
df1c_craters['Region'] = '1c'
df1_craters = gpd.GeoDataFrame(pd.concat([df1a_craters, df1b_craters, df1c_craters], ignore_index=True), crs=df1a_craters.crs)
# df2_craters = [df2_craters]
df2_craters['Region'] = '2'

# df3_craters = [df3a_craters, df3b_craters]
df3a_craters['Region'] = '3a'
df3b_craters['Region'] = '3b'
df3_craters = gpd.GeoDataFrame(pd.concat([df3a_craters, df3b_craters], ignore_index=True), crs=df3a_craters.crs)

# df4_craters = [df4a_craters, df4b_craters, df4c_craters]
df4a_craters['Region'] = '4a'
df4b_craters['Region'] = '4b'
df4c_craters['Region'] = '4c'
df4_craters = gpd.GeoDataFrame(pd.concat([df4a_craters, df4b_craters, df4c_craters], ignore_index=True), crs=df4a_craters.crs)

# df5_craters = [df5a_craters, df5b_craters, df5c_craters]
df5a_craters['Region'] = '5a'
df5b_craters['Region'] = '5b'
df5c_craters['Region'] = '5c'
df5_craters = gpd.GeoDataFrame(pd.concat([df5a_craters, df5b_craters, df5c_craters], ignore_index=True), crs=df5a_craters.crs)

# df6_craters = [df6a_craters, df6b_craters]
df6a_craters['Region'] = '6a'
df6b_craters['Region'] = '6b'
df6_craters = gpd.GeoDataFrame(pd.concat([df6a_craters, df6b_craters], ignore_index=True), crs=df6a_craters.crs)

# df7_craters = [df7a_craters, df7b_craters]
df7a_craters['Region'] = '7a'
df7b_craters['Region'] = '7b'
df7_craters = gpd.GeoDataFrame(pd.concat([df7a_craters, df7b_craters], ignore_index=True), crs=df7a_craters.crs)

dfall_craters_dup = gpd.GeoDataFrame(pd.concat([df1_craters,df2_craters,df3_craters,df4_craters,\
                    df5_craters,df6_craters,df7_craters], ignore_index=True))
dfall_craters = dfall_craters_dup.drop_duplicates()

def count_craters(df, min_diam=0.5, max_diam=False):
  '''
  Finds total number of craters in list of dataframes.
  Input:
    df: List of dataframes
    min_diam: minimum diameter (km)
    max_diam: max diameter
  Output: Total number of craters
  '''
  crater_count = 0
  red_df = df[(df.Diam_km >= min_diam) & (df.tag == 'standard')]
  if max_diam:
    red_df = red_df[red_df.Diam_km < max_diam]
  crater_count += len(red_df)
  return crater_count

#bin by bin Craters, H km^-2Ga^-1 numbers
bin_neg2 = 4.02 * 10**(-3) #craters between .5-.707km
bin_neg1 = 1.15 * 10**(-3) #0.707-1km
bin0 = 3.08 * 10**(-4) #1-1.41km
bin1 = 1.28 * 10**(-4) #1.41-2km
bin2 = 6.85 * 10**(-5) #2-2.83km
bin3 = 3.67 * 10**(-5) #2.83-4km
bin4 = 1.98 * 10**(-5) #4-5.66km
bin5 = 1.06 * 10**(-5) #5.66-8km
bin6 = 5.68 * 10**(-6) #8-11.3km
bin7 = 3.04 * 10**(-6) #11.3-16km
bin8 = 1.62 * 10**(-6) #16-22.6km
bin9 = 8.71 * 10**(-7) #22.6-32km
bin10 = 4.67 * 10**(-7) #32-45.3km
bin11 = 2.40 * 10**(-7) #45.3-64km
bin12 = 1.12 * 10**(-7) #64-90.5km
bin13 = 5.21 * 10**(-8) #90.5-128km

bin_constants = [bin_neg2, bin_neg1, bin0, bin1, bin2, bin3, bin4, bin5, bin6,\
            bin7, bin8, bin9, bin10, bin11, bin12, bin13]

bin_dict = OrderedDict()
bin_dict[-2] = [0.5 * 1000,0.707 * 1000]
bin_dict[-1] = [0.707 * 1000, 1. * 1000]
bin_dict[0] = [1. * 1000, 1.41 * 1000]
bin_dict[1] = [1.41 * 1000, 2. * 1000]
bin_dict[2] = [2. * 1000,2.83 * 1000]
bin_dict[3] = [2.83 * 1000, 4. * 1000]
bin_dict[4] = [4. * 1000, 5.66 * 1000]
bin_dict[5] = [5.66 * 1000, 8. * 1000]
bin_dict[6] = [8. * 1000, 11.3 * 1000]
bin_dict[7] = [11.3 * 1000, 16. * 1000]
bin_dict[8] = [16. * 1000, 22.6 * 1000]
bin_dict[9] = [22.6 * 1000, 32 * 1000]
bin_dict[10] = [32 * 1000, 45.3 * 1000]
bin_dict[11] = [45.3 * 1000, 64 * 1000]
bin_dict[12] = [64 * 1000, 90.5 * 1000]
bin_dict[13] = [90.5 * 1000, 128 * 1000]

bin_list = [bin_dict[-2], bin_dict[-1], bin_dict[0], bin_dict[1], bin_dict[2], \
            bin_dict[3], bin_dict[4], bin_dict[5], bin_dict[6], bin_dict[7],\
            bin_dict[8], bin_dict[9], bin_dict[10], bin_dict[11], bin_dict[12], bin_dict[13]]

#defining values
second = 1/60/60/24/365.2422/(10**9) #in Ga
all_area = find_area(data_list) #total area
start_time = second
end_time = 4.5
points = 1000

def find_region_bin_craters(reg_n, all=False):
  '''
  Finds number of standard craters in each bin for a region.
  Input:
    reg_n: region number
    all: if True, then considers all craters, including marked craters
  Output:
    count_list: list of 16 numbers representing craters in each bin
  '''
  min_diam_list = [0.5,0.707,1,1.41,2,2.83,4,5.66,8,11.3,16,22.6,32,45.3,64,90.5]
  count_list = []
  str_n = str(reg_n)
  for i, diam in enumerate(min_diam_list):
    if i != len(min_diam_list) - 1:
      if not all:
        count_list.append(count_craters(dfall_craters[dfall_craters.Region.str.contains(str_n)], min_diam=diam, max_diam=min_diam_list[i+1]))
      else:
        count_list.append(count_craters(dfall_craters[dfall_craters.tag.str.contains('standard')], min_diam=diam, max_diam=min_diam_list[i+1]))
    else:
      if not all:
        count_list.append(count_craters(dfall_craters[dfall_craters.Region.str.contains(str_n)], min_diam=diam))
      else:
        count_list.append(count_craters(dfall_craters[dfall_craters.tag.str.contains('standard')], min_diam=diam))
  return count_list

def find_mid_depth(diam_min, diam_max):
  '''
  Takes minimum and maximum diameters in meters and returns log halfway depth.
  '''
  logmid_diam = 10**((np.log10(diam_min)+np.log10(diam_max))/2) / 1000 #in km
  if diam_min < 2822.21362731415: #D=2822 km is intersection
    logmid_depth = logmid_diam * 0.2
  else:
    logmid_depth = 0.323*logmid_diam**0.538
  return logmid_depth*1000.

def find_mid_diam(diam_min, diam_max):
  '''
  Takes minimum and maximum diameters in meters and returns log10 halfway diameter.
  Input:
    diam_min: minimum diameter
    diam_max: maximum diameter
  Output: Log halfway diameter.
  '''
  logmid_diam = 10**((np.log10(diam_min)+np.log10(diam_max))/2)
  return logmid_diam
#find_mid_diam(10, 1000)

def find_erosion_pdf(T_start, T_end, B_start, B_end, mid_depth, num_points, n, area_counted, cum_craters,  tlin=False, blin=False):
  '''
  Find Poisson probability array of observing n craters.
  Input:
    T_start: starting age
    T_end: ending age
    B_start: starting beta
    B_end: ending beta
    mid_depth: log10 mid-depth of the bin
    num_points: number of points to use in the age and beta arrays
    n: number of craters
    area_counted: area (km^2) of the site
    cum_craters: H value (craters/km^2) from Table 1 of Michael 2013
    tlin: if True then function uses a linear time array
    blin: if True then function uses a linear beta array
  Output:
    T: age array
    B: beta array
    P: probability array
  '''
  if tlin:
    T = np.linspace(T_start, T_end, num_points)
  else:
    T = np.geomspace(T_start, T_end, num_points)
  if blin:
    B = np.linspace(B_start, B_end, num_points) #trying linspace vs. geomspace
  else:
    B = np.geomspace(B_start, B_end, num_points)
  Z = np.zeros(len(T)*len(B))
  Z = Z.reshape((len(T), len(B)))
  for i, t in enumerate(T):
    for j, b in enumerate(B):
      exp_craters_erosion = cum_craters * mid_depth / b
      exp_craters_no_erosion = cum_craters * t
      if exp_craters_erosion < exp_craters_no_erosion:
        dbt = mid_depth / b
        N1db = 3.79e-14 * (np.exp(6.93*dbt) - 1) + 5.84e-4 * dbt
        N1_wrongdb = 5.84e-4 * dbt
        db_factor = N1db / N1_wrongdb
        mu = exp_craters_erosion * area_counted * db_factor
      else:
        N1 = 3.79e-14 * (np.exp(6.93*t) - 1) + 5.84e-4 * t
        N1_wrong = 5.84e-4 * t
        correction_factor = N1 / N1_wrong
        mu = exp_craters_no_erosion * area_counted * correction_factor
      Z[i][j] = mu
  P = poisson.pmf(n, Z)
  return T, B, P

def find_cdf(mult_prob):
  '''
  Create cdf.
  Inputs:
    T_start: Start time in Ga units
    T_end: End time in Ga units
    num_points: number of points within time array (and plot)
    n: number of craters
  Output:
    Plot of cdf, time array and probability array
  '''
  cdf = mult_prob.cumsum()
  #normalize
  scale = 1.0/cdf[-1]
  prob = scale * cdf  #this is normalized cdf
  return prob

def multiply_bins(reg_n,t_start, t_end, b_start, b_end, num_points, area, tlins=False, blins=False, all=False):
  '''
  Loops through all 16 crater bins and finds the total probability.
  Inputs:
    reg_n: region number
    t_start: start time
    t_end: end time
    b_start: start beta
    b_end: end beta
    num_points: number of points
    area: area of site (km^2)
    tlins: if True, function creates linear time array otherwise log time
    blins: if True, function creates linear beta array, otherwise log beta
    all: if True, craters used include marked (not just standard)
  Output:
    X, Y, and probability arrays
  '''
  all_pdfs = []
  pdf_product = None
  crater_bins = find_region_bin_craters(reg_n, all)
  for i, crater_count in enumerate(crater_bins):
    mid_depth_val = find_mid_depth(bin_list[i][0], bin_list[i][-1])
    X,Y,P = find_erosion_pdf(t_start, t_end, b_start, b_end, mid_depth_val, num_points,\
                             crater_count, area_counted=area, cum_craters=bin_constants[i], tlin=tlins, blin=blins) #not actually cumulative anymore
    all_pdfs.append(P)
  for i, pdf in enumerate(all_pdfs):
    if i==0:
      pdf_product = pdf
    else:
      pdf_product = pdf_product * pdf
  return X, Y, pdf_product

def find_contours(z):
  '''
  Finds 1 sigma, 2 sigma, and 3 sigma error regions for function plot_contour.
  '''
  z = z.flatten()
  z = sorted(z)
  sig_1 = (1 - 0.6827) * max(z)
  sig_2 = (1 - 0.9545) * max(z)
  sig_3 = (1 - 0.9973) * max(z)
  return sig_1, sig_2, sig_3

def plot_contour(reg_n, T_start, T_end, B_start, B_end, num_points, area, log=False, tli=False,bli=False, all=False):
  '''
  Plots two-parameter contour plot.
  Inputs:
    reg_n: region number
    T_start: start time
    T_end: end time
    B_start: start beta
    B_end: end beta
    num_points: number of points
    area: area of site (km^2)
    tlins: if True, function creates linear time array otherwise log time
    blins: if True, function creates linear beta array, otherwise log beta
    all: if True, craters used include marked (not just standard)
  '''
  X, Y, Z = multiply_bins(reg_n, T_start, T_end, B_start, B_end, num_points, area, tlins=tli, blins=bli, all=all)
  fig,ax = plt.subplots()
  if log:
    ax.set_xscale('log')
  levels = np.linspace(np.min(Z), np.max(Z), 100)
  cp = ax.contourf(X, Y, Z.T, levels)
  cbar = plt.colorbar(cp)
  one_sig, two_sig, three_sig = find_contours(Z)
  cp2 = plt.contour(cp, levels=[one_sig, two_sig, three_sig], colors=['red', 'red','red'],\
                    linestyles=['solid','dashed',':'], origin='lower')
  cbar.add_lines(cp2)
  cbar.lines[-1].set_linestyles(cp2.linestyles)
  cbar.set_label('Probability')
  ax.axhline(y=1000, linestyle='--', color='white') #ice table
  if B_end <= 5000: #for plotting constant 5km of erosion line
    t5k = [1,5]
    b5k= [5000,1000]
    fx = interp1d(t5k, b5k, kind='linear')
    plt.plot(t5k, fx(t5k), color='dodgerblue',linestyle=':')
  else:
    t5km = [0.1,0.2, 0.45, 0.5, 0.6, 0.7, 0.8,0.9, 1,1.1, 1.5, 2,4,5]
    b5km = [50000,25000, 11111.11111111111, 10000, 8333.3333333333, 7142.857143, 6250,5555.555555, 5000,4545.45455,3333.333, 2500,1250, 1000]
    f = interp1d(t5km, b5km, kind='cubic')
    plt.plot(t5km, f(t5km), color='dodgerblue', linestyle = ':')
  ax.set_xlabel('Age (Ga)')
  ax.set_ylabel('β (nm/a)')
  fig_name = str(reg_n) +'_2dcontour' + '.png'
  ax.set_ylim(0,B_end)
  ax.set_xlim(0,T_end)
  plt.show()
  fig.savefig(fig_name, dpi=300, bbox_inches='tight')

def find_max(X,Y,Z):
  '''
  Finds best fit age and beta.
  '''
  z = max(Z.flatten())
  max_loc = np.where(Z == z)
  time_index = max_loc[0][0]
  time = X[time_index]
  beta_index = max_loc[1][0]
  beta = Y[beta_index]
  return time, beta
