from ind_volume_functions import area_names, pts, tls, bs, areas, sed_rate
from ind_volume_functions import join_all
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

area_names.pop()
for area_name, pt, tl, b, area in zip(area_names, pts, tls, bs, areas):
  globals()[f"pt{area_name}"] = pt #assigning present thickness variables
  globals()[f"t{area_name}"] = tl #assigning thickness lost variables
  globals()[f"b{area_name}"] = b #assigning beta variables
  globals()[f"area{area_name}"] = area #assigning beta variables

#all thickness plots are commented out; volume plots below
x1a, y1a, z1a = multiply_bins('1a', 0.662, 3.66,147, 293, points, area1a, tlins=True, blins=True)
# join_all('1at', second, 4.5e9, pt1a, t1a, sed_rate, b1a, area1a, x1a, y1a, z1a)
join_all('1av',second, 4.5e9, pt1a, t1a, sed_rate, b1a, area1a, x1a, y1a, z1a, vol_plot=True)

x1b, y1b, z1b = multiply_bins('1b', 0.419, 4.09, 422, 762, points, area1b, tlins=True, blins=True)
# join_all('1bt',second, 4.5e9, pt1b, t1b, sed_rate, b1b, area1b, x1b, y1b, z1b)
join_all('1bv', second, 4.5e9, pt1b, t1b, sed_rate, b1b, area1b, x1b, y1b, z1b, vol_plot=True)

x1c, y1c, z1c = multiply_bins('1c', 0.635, 4.18, 491, 869, points, area1c, tlins=True, blins=True)
# join_all('1ct', second, 4.5e9, pt1c, t1c, sed_rate, b1c, area1c, x1c, y1c, z1c)
join_all('1cv', second, 4.5e9, pt1c, t1c, sed_rate, b1c, area1c, x1c, y1c, z1c, vol_plot=True)

x2, y2, z2 = multiply_bins(2, 0.060, 4.5, 0, 3580, points, area2, tlins=True, blins=True)
# join_all('2t', second, 4.5e9, pt2, t2, sed_rate, b2, area2, x2, y2, z2)
join_all('2v', second, 4.5e9, pt2, t2, sed_rate, b2, area2, x2, y2, z2, vol_plot=True)

x3, y3, z3 = multiply_bins(3, 0.017, 4.5, 0,8970, points, area3, tlins=True, blins=True)
# join_all('3t', second, 4.5e9, pt3, t3, sed_rate, b3, area3, x3, y3, z3)
join_all('3v', second, 4.5e9, pt3, t3, sed_rate, b3, area3, x3, y3, z3, vol_plot=True)

x4a, y4a, z4a = multiply_bins('4a', 0.548, 3.90, 298, 537, points, area4a, tlins=True, blins=True)
# join_all('4at', second, 5e9, pt4a, t4a, sed_rate, b4a, area4a, x4a, y4a, z4a)
join_all('4av', second, 4.5e9, pt4a, t4a, sed_rate, b4a, area4a, x4a, y4a, z4a, vol_plot=True)

x4b, y4b, z4b = multiply_bins('4b', 0.687, 4.13, 423, 720, points, area4b, tlins=True, blins=True)
# join_all('4bt', second, 4.5e9, pt4b, t4b, sed_rate, b4b, area4b, x4b, y4b, z4b)
join_all('4bv', 1, 4.5e9, pt4b, t4b, sed_rate, b4b, area4b, x4b, y4b, z4b, vol_plot=True)

x4c, y4c, z4c = multiply_bins('4c', 2.98, 3.51, 77.7, 99.2, points, area4c, tlins=True, blins=True)
# join_all('4ct', second, 4.5e9, pt4c, t4c, sed_rate, b4c, area4c, x4c, y4c, z4c)
join_all('4cv', second, 4.5e9, pt4c, t4c, sed_rate, b4c, area4c, x4c, y4c, z4c, vol_plot=True)

x5a, y5a, z5a = multiply_bins('5a', 0.063, 4.5, 0, 13000, points, area5a, tlins=True, blins=True)
# join_all('5at', second, 4.5e9, pt5a, t5a, sed_rate, b5a, area5a, x5a, y5a, z5a)
join_all('5av', second, 4.5e9, pt5a, t5a, sed_rate, b5a, area5a, x5a, y5a, z5a, vol_plot=True)

x5b, y5b, z5b = multiply_bins('5b', 0.305, 4.24, 570, 1020, points, area5b, tlins=True, blins=True)
# join_all('5bt', second, 4.5e9, pt5b, t5b, sed_rate, b5b, area5b, x5b, y5b, z5b)
join_all('5bv', second, 4.5e9, pt5b, t5b, sed_rate, b5b, area5b, x5b, y5b, z5b, vol_plot=True)

x5c, y5c, z5c = multiply_bins('5c', 0.111, 4.5, 1220, 2440, points, area5c, tlins=True, blins=True)
# join_all('5ct', 1, 4.5e9, pt5c, t5c, sed_rate, b5c, area5c, x5c, y5c, z5c)
join_all('5cv', second, 4.5e9, pt5c, t5c, sed_rate, b5c, area5c, x5c, y5c, z5c, vol_plot=True)

x6a, y6a, z6a = multiply_bins('6a', 0.32, 4.12, 500, 885, points, area6a, tlins=True, blins=True)
# join_all('6at', second, 4.5e9, pt6a, t6a, sed_rate, b6a, area6a, x6a, y6a, z6a)
join_all('6av', second, 4.5e9, pt6a, t6a, sed_rate, b6a, area6a, x6a, y6a, z6a, vol_plot=True)

x6b, y6b, z6b = multiply_bins('6b', 0.202, 4.5, 1790, 3890, points, area6b, tlins=True, blins=True)
# join_all('6bt', second, 4.5e9, pt6b, t6b, sed_rate, b6b, area6b, x6b, y6b, z6b)
join_all('6bv', second, 4.5e9, pt6b, t6b, sed_rate, b6b, area6b, x6b, y6b, z6b, vol_plot=True)

x7, y7, z7 = multiply_bins(7, 0.146, 4.5, 0, 1308, points, area7, tlins=True, blins=True)
# join_all('7t', second, 4.5e9, pt7, t7, sed_rate, b7, area7, x7, y7, z7)
join_all('7v', second, 4.5e9, pt7, t7, sed_rate, b7, area7, x7, y7, z7, vol_plot=True)

xs = [x1a, x1b, x1c, x2, x3, x4a, x4b, x4c, x5a, x5b, x5c, x6a, x6b, x7]
ys = [y1a, y1b, y1c, y2, y3, y4a, y4b, y4c, y5a, y5b, y5c, y6a, y6b, y7]
zs = [z1a, z1b, z1c, z2, z3, z4a, z4b, z4c, z5a, z5b, z5c, z6a, z6b, z7]

#saving files to save time when running cum_vol_plots.py, refer to cum_vol_plots.py
#for what to (un)comment there to use saved files below
np.save('x1a', x1a)
np.save('y1a', y1a)
np.save('z1a', z1a)
np.save('x1b', x1b)
np.save('y1b', y1b)
np.save('z1b', z1b)
np.save('x1c', x1c)
np.save('y1c', y1c)
np.save('z1c', z1c)

np.save('x2', x2)
np.save('y2', y2)
np.save('z2', z2)

np.save('x3', x3)
np.save('y3', y3)
np.save('z3', z3)

np.save('x4a', x4a)
np.save('y4a', y4a)
np.save('z4a', z4a)
np.save('x4b', x4b)
np.save('y4b', y4b)
np.save('z4b', z4b)
np.save('x4c', x4c)
np.save('y4c', y4c)
np.save('z4c', z4c)

np.save('x5a', x5a)
np.save('y5a', y5a)
np.save('z5a', z5a)
np.save('x5b', x5b)
np.save('y5b', y5b)
np.save('z5b', z5b)
np.save('x5c', x5c)
np.save('y5c', y5c)
np.save('z5c', z5c)

np.save('x6a', x6a)
np.save('y6a', y6a)
np.save('z6a', z6a)
np.save('x6b', x6b)
np.save('y6b', y6b)
np.save('z6b', z6b)

np.save('x7', x7)
np.save('y7', y7)
np.save('z7', z7)
