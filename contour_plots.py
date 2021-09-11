import erosion_age
from erosion_age import plot_contour

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
all_area = erosion_age.find_area(erosion_age.data_list)

#area 1a Central Medusae Fossae 1
plot_contour('1a', start_time, 4.5, 1, 1100, points, area1a, log=False, tli=True,bli=True)
#comment out below for just one plot
#area 1b Central Medusae Fossae 1
plot_contour('1b', start_time, 4.5, 0, 1100, points, area1b, log=False, tli=True, bli=True)
#area 1c Central Medusae Fossae 1
erosion_age.plot_contour('1c', start_time, 4.5, 0, 1100, points, area1c, log=False, tli=True, bli=True)

#area 2 Aeolis Planum 3D
plot_contour(2, start_time, 4.5, 1, 3000, points, area2, log=False, tli=True, bli=True)

#area 3 Eastern Candor
plot_contour('3', start_time, 4.5, 1, 10000, points, area3, log=False, tli=True, bli=True)

#area 4a Central Medusae Fossae 2
plot_contour('4a', second, 4.5, second, 1100, points, area4a, log=False, tli=True, bli=True)
#area 4b Central Medusae Fossae 2
plot_contour('4b', start_time, 4.5, 1, 1100, points, area4b, log=False, tli=True, bli=True)
#area 4c Central Medusae Fossae 2
plot_contour('4c', start_time, 4.5, 1, 400, points, area4c, log=False, tli=True, bli=True)

#area 5a Far East Medusae Fossae
plot_contour('5a', start_time, 4.5, 1, 14000, points, area5a, log=False, tli=True, bli=True)
#area 5b Far East Medusae Fossae
plot_contour('5b', start_time, 4.5, 1, 1200, points, area5b, log=False, tli=True, bli=True)
#area 5c Far East Medusae Fossae
plot_contour('5c', start_time, 4.5, 1, 3000, points, area5c, log=False, tli=True, bli=True)

#area 6a East Medusae Fossae
plot_contour('6a', start_time, 4.5, 1, 1100, points, area6a, log=False, tli=True, bli=True)
#area 6b East Medusae Fossae
plot_contour('6b', start_time, 4.5, 1, 5000, points, area6b, log=False, tli=True, bli=True)

#area 7 Upper Mount Sharp
plot_contour(7, start_time, 4.5, 1, 1500, points, area7, log=False, tli=True, bli=True)

all areas
plot_contour('all_area', start_time, 4.5, 1, 1500, points, all_area, log=False, tli=True, bli=True, all=True)
