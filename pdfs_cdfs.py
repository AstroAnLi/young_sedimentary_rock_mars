from erosion_age import multiply_bins
import erosion_age
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

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
all_area = erosion_age.find_area(erosion_age.data_list)

def find_1d_pdf(reg_n, T_start, T_end, B_start, B_end, num_points, area, p=False, beta=False, tli=False, bli=False,all=False):
  '''
  Collapses two-parameter model probability predictions along one axis (either age or beta)
  to find a one-parameter probablity distribution.
  Inputs:
      reg_n: region number
      T_start: start time
      T_end: end time
      B_start: start beta
      B_end: end beta
      num_points: number of points
      area: area of site (km^2)
      p: if True, finds PDF. If False, finds CDF
      beta: default is False so that the output is time on x-axis. True is beta on x-axis
      tli: if True, function creates linear time array otherwise log time
      bli: if True, function creates linear beta array, otherwise log
      all: if True, includes marked craters with standard craters
  Output:
    x_val: age array
    prob: probability array
  '''
  X, Y, Z = multiply_bins(reg_n, T_start, T_end, B_start, B_end, num_points, area, tlins=tli, blins=bli,all=all) #can also output cdf....
  if beta:
    z = Z.sum(axis=0)
    x_val = Y
  else:
    z = Z.sum(axis=1)
    x_val = X
  if p:
    y_val = z
    scale = 1/np.sum(z)
    prob = scale * y_val
    a = np.where(prob.cumsum() == np.average(prob.cumsum()))
  else:
    cdf = z.cumsum()
    y_val = cdf
    scale = 1.0/y_val[-1]
    prob = scale * y_val
  return x_val, prob

def plot_1d_pdf(reg_n, T_start, T_end, B_start, B_end, num_points, area, p=False, beta=False, tli=False, bli=False):
  '''
  Plots one parameter PDF if p=True or CDF if p=False.
  Inputs:
    reg_n: region number
    T_start: start time
    T_end: end time
    B_start: start beta
    B_end: end beta
    num_points: number of points
    area: area of site (km^2)
    p: if True, finds PDF. If False, finds CDF
    beta: Default is False so that the output is time on x-axis. True is beta on x-axis
    tlin: if True, function creates linear time array otherwise log time
    blin: if True, function creates linear beta array, otherwise log beta
  '''
  fig, ax = plt.subplots()
  fig_name = str(reg_n)
  if beta:
    plt.xlabel('Beta (nm/a)')
    fig_name = fig_name + '_beta'
  else:
    plt.xlabel('Age (Ga)')
    fig_name = fig_name + '_age'
  if p:
    plt.ylabel('Probability')
    fig_name = fig_name + 'pdf'
  else:
    plt.ylabel('Cumulative Probability')
    plt.axhline(y=0.5, color='r', linestyle=':' )
    plt.axhline(y=0.841, color = 'r', linestyle=':')
    plt.axhline(y=0.159, color = 'r', linestyle=':' )
    fig_name = fig_name + 'cdf'
  x_array, prob_array = find_1d_pdf(reg_n, T_start, T_end, B_start, B_end, num_points, area, p, beta, tli, bli)
  ax.plot(x_array, prob_array) #for plotting, below is for aesthetics
  ax.grid(True)
  ax.xaxis.set_minor_locator(AutoMinorLocator())
  ax.yaxis.set_minor_locator(AutoMinorLocator())
  ax.grid(which='major', linewidth='1')
  ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  fig_name = fig_name + '.png'
  fig.savefig(fig_name, dpi=300)
  plt.show()

#time pdfs - run this
xall, pall = find_1d_pdf('area', start_time, 4.5, 1, 8000, 1000, all_area, p=True, beta=False, tli=False, bli=False, all=True)
x1a0, p1a0 = find_1d_pdf('1a', start_time, 4.5, 1, 8000, 1000, area1a, p=True)
x1b0, p1b0 = find_1d_pdf('1b', start_time, 4.5, 1, 8000, 1000, area1b, p=True)
x1c0, p1c0 = find_1d_pdf('1c', start_time, 4.5, 1, 8000, 1000, area1c, p=True)
x20, p20 = find_1d_pdf('2', start_time, 4.5, 1, 8000, 1000, area2, p=True)
x30, p30 = find_1d_pdf('3', start_time, 4.5, 1, 8000, 1000, area3, p=True)
x4a0, p4a0 = find_1d_pdf('4a', start_time, 4.5, 1, 8000, 1000, area4a, p=True)
x4b0, p4b0 = find_1d_pdf('4b', start_time, 4.5, 1, 8000, 1000, area4b, p=True)
x4c0, p4c0 = find_1d_pdf('4c', start_time, 4.5, 1, 8000, 1000, area4c, p=True)
x5a0, p5a0 = find_1d_pdf('5a', start_time, 4.5, 1, 8000, 1000, area5a, p=True)
x5b0, p5b0 = find_1d_pdf('5b', start_time, 4.5, 1, 8000, 1000, area5b, p=True)
x5c0, p5c0 = find_1d_pdf('5c', start_time, 4.5, 1, 8000, 1000, area5c, p=True)
x6a0, p6a0 = find_1d_pdf('6a', start_time, 4.5, 1, 8000, 1000, area6a, p=True)
x6b0, p6b0 = find_1d_pdf('6b', start_time, 4.5, 1, 8000, 1000, area6b, p=True)
x70, p70 = find_1d_pdf('7', start_time, 4.5, 1, 8000, 1000, area7, p=True)
fig, ax = plt.subplots()
plt.xlabel('Age (Ga)')
plt.ylabel('PDF')
colormap = plt.cm.tab20
colors = [colormap(i) for i in np.linspace(0, 1,16)]
ax.set_prop_cycle('color', colors)
ax.plot(x1a0, p1a0, label='1a')
ax.plot(x1b0, p1b0, label='1b')
ax.plot(x1c0, p1c0, label='1c')
ax.plot(x20, p20, label='2')
ax.plot(x30, p30, label='3')
ax.plot(x4a0, p4a0, label='4a')
ax.plot(x4b0, p4b0, label='4b')
ax.plot(x4c0, p4c0, label='4c')
ax.plot(x5a0, p5a0, label='5a')
ax.plot(x5b0, p5b0, label='5b')
ax.plot(x5c0, p5c0, label='5c')
ax.plot(x6a0, p6a0, label='6a')
ax.plot(x6b0, p6b0, label='6b')
ax.plot(x70, p70, label='7')
ax.plot(xall, pall, label='All 14 regions')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax.legend(loc='upper right',bbox_to_anchor=(1.15,1.05))
fig.savefig('age_pdfs.png',dpi=300, bbox_inches='tight')

#comment out below for just one plot
#run this - no 4c, but must run after above for with 4c is run already to
have variables saved
fig, ax = plt.subplots()
plt.xlabel('Age (Ga)')
plt.ylabel('PDF')
colormap = plt.cm.tab20
colors = [colormap(i) for i in np.linspace(0, 1,16)]
ax.set_prop_cycle('color', colors)
ax.plot(x1a0, p1a0, label='1a')
ax.plot(x1b0, p1b0, label='1b')
ax.plot(x1c0, p1c0, label='1c')
ax.plot(x20, p20, label='2')
ax.plot(x30, p30, label='3')
ax.plot(x4a0, p4a0, label='4a')
ax.plot(x4b0, p4b0, label='4b')
ax.plot(x5a0, p5a0, label='5a')
ax.plot(x5b0, p5b0, label='5b')
ax.plot(x5c0, p5c0, label='5c')
ax.plot(x6a0, p6a0, label='6a')
ax.plot(x6b0, p6b0, label='6b')
ax.plot(x70, p70, label='7')
ax.plot(xall, pall, label='All Areas')
ax.set_xlim(0,4.5)
ax.legend(loc='upper right',bbox_to_anchor=(1.15,1.05))
fig.savefig('agepdfs_no4c.png', dpi=300,bbox_inches='tight')

#all beta pdfs - run this
x1a, p1a = find_1d_pdf('1a', start_time, 4.5, 1, 8000, 1000, area1a, p=True, beta=True, tli=False, bli=False)
x1b, p1b = find_1d_pdf('1b', start_time, 4.5, 1, 8000, 1000, area1b, p=True, beta=True, tli=False, bli=False)
x1c, p1c = find_1d_pdf('1c', start_time, 4.5, 1, 8000, 1000, area1c, p=True, beta=True, tli=False, bli=False)
x2, p2 = find_1d_pdf('2', start_time, 4.5, 1, 8000, 1000, area2, p=True, beta=True, tli=False, bli=False)
x3, p3 = find_1d_pdf('3', start_time, 4.5, 1, 8000, 1000, area3, p=True, beta=True, tli=False, bli=False)
x4a, p4a = find_1d_pdf('4a', start_time, 4.5, 1, 8000, 1000, area4a, p=True, beta=True, tli=False, bli=False)
x4b, p4b = find_1d_pdf('4b', start_time, 4.5, 1, 8000, 1000, area4b, p=True, beta=True, tli=False, bli=False)
x4c, p4c = find_1d_pdf('4c', start_time, 4.5, 1, 8000, 1000, area4c, p=True, beta=True, tli=False, bli=False)
x5a, p5a = find_1d_pdf('5a', start_time, 4.5, 1, 8000, 1000, area5a, p=True, beta=True, tli=False, bli=False)
x5b, p5b = find_1d_pdf('5b', start_time, 4.5, 1, 8000, 1000, area5b, p=True, beta=True, tli=False, bli=False)
x5c, p5c = find_1d_pdf('5c', start_time, 4.5, 1, 8000, 1000, area5c, p=True, beta=True, tli=False, bli=False)
x6a, p6a = find_1d_pdf('6a', start_time, 4.5, 1, 8000, 1000, area6a, p=True, beta=True, tli=False, bli=False)
x6b, p6b = find_1d_pdf('6b', start_time, 4.5, 1, 8000, 1000, area6b, p=True, beta=True, tli=False, bli=False)
x7, p7 = find_1d_pdf('7', start_time, 4.5, 1, 8000, 1000, area7a, p=True, beta=True, tli=False, bli=False)
xall, pall = find_1d_pdf('area', start_time, 5, 1, 8000, 1000, all_area, p=True, beta=True, tli=False, bli=False, all=True)
fig, ax = plt.subplots()
ax.set_xscale('log')
colormap = plt.cm.tab20
colors = [colormap(i) for i in np.linspace(0, 1,16)]
ax.set_prop_cycle('color', colors)
plt.xlabel('\u03B2 (nm/a)')
plt.ylabel('PDF')
ax.plot(x1a, p1a, label='1a')
ax.plot(x1b, p1b, label='1b')
ax.plot(x1c, p1c, label='1c')
ax.plot(x2, p2, label='2')
ax.plot(x3, p3, label='3')
ax.plot(x4a, p4a, label='4a')
ax.plot(x4b, p4b, label='4b')
ax.plot(x4c, p4c, label='4c')
ax.plot(x5a, p5a, label='5a')
ax.plot(x5b, p5b, label='5b')
ax.plot(x5c, p5c, label='5c')
ax.plot(x6a, p6a, label='6a')
ax.plot(x6b, p6b, label='6b')
ax.plot(x7, p7, label='7')
ax.plot(xall, pall, label='All Areas')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax.legend(loc='upper left')
fig.savefig('beta_pdfs.png',dpi=300)


#age cdfs - run this
x1a, c1a = find_1d_pdf('1a', start_time, 4.5, 1, 8000, 1000, area1a, p=False)
x1b, c1b = find_1d_pdf('1b', start_time, 4.5, 1, 8000, 1000, area1b, p=False)
x1c, c1c = find_1d_pdf('1c', start_time, 4.5, 1, 8000, 1000, area1c, p=False)
x2, c2 = find_1d_pdf('2', start_time, 4.5, 1, 8000, 1000, area2, p=False)
x3, c3 = find_1d_pdf('3', start_time, 4.5, 1, 8000, 1000, area3, p=False)
x4a, c4a = find_1d_pdf('4a', start_time, 4.5, 1, 8000, 1000, area4a, p=False)
x4b, c4b = find_1d_pdf('4b', start_time, 4.5, 1, 8000, 1000, area4b, p=False)
x4c, c4c = find_1d_pdf('4c', start_time, 4.5, 1, 8000, 1000, area4c, p=False)
x5a, c5a = find_1d_pdf('5a', start_time, 4.5, 1, 8000, 1000, area5a, p=False)
x5b, c5b = find_1d_pdf('5b', start_time, 4.5, 1, 8000, 1000, area5b, p=False)
x5c, c5c = find_1d_pdf('5c', start_time, 4.5, 1, 8000, 1000, area5c, p=False)
x6a, c6a = find_1d_pdf('6a', start_time, 4.5, 1, 8000, 1000, area6a, p=False)
x6b, c6b = find_1d_pdf('6b', start_time, 4.5, 1, 8000, 1000, area6b, p=False)
x7, c7 = find_1d_pdf('7', start_time, 4.5, 1, 8000, 1000, area7, p=False)
testing here
xcball, cball = find_1d_pdf('area', start_time, 4.5, 1, 8000, 1000, all_area, p=False, all=True)
fig, ax = plt.subplots()
colormap = plt.cm.tab20
colors = [colormap(i) for i in np.linspace(0, 1,16)]
ax.set_prop_cycle('color', colors)
plt.xlabel('Age (Ga)')
plt.ylabel('Cumulative Probability')
ax.plot(x1a, c1a, label='1a')
ax.plot(x1b, c1b, label='1b')
ax.plot(x1c, c1c, label='1c')
ax.plot(x2, c2, label='2')
ax.plot(x3, c3, label='3')
ax.plot(x4a, c4a, label='4a')
ax.plot(x4b, c4b, label='4b')
ax.plot(x4c, c4c, label='4c')
ax.plot(x5a, c5a, label='5a')
ax.plot(x5b, c5b, label='5b')
ax.plot(x5c, c5c, label='5c')
ax.plot(x6a, c6a, label='6a')
ax.plot(x6b, c6b, label='6b')
ax.plot(x7, c7, label='7')
ax.grid(True)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.grid(which='major', linewidth='1', linestyle=':', color='black')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.axhline(y=0.5, color='r', linestyle='--' )
plt.axhline(y=0.841, color = 'r', linestyle='dotted')
plt.axhline(y=0.159, color = 'r', linestyle='dotted' )
ax.legend()
fig.savefig('age_cdfs.png', dpi=300)

#beta cdfs - run this
x1a, c1a = find_1d_pdf('1a', start_time, 4.5, 1, 8000, 1000, area1a, p=False, beta=True, tli=False, bli=False)
x1b, c1b = find_1d_pdf('1b', start_time, 4.5, 1, 8000, 1000, area1b, p=False, beta=True, tli=False, bli=False)
x1c, c1c = find_1d_pdf('1c', start_time, 4.5, 1, 8000, 1000, area1c, p=False, beta=True, tli=False, bli=False)
x2, c2 = find_1d_pdf('2', start_time, 4.5, 1, 8000, 1000, area2, p=False, beta=True, tli=False, bli=False)
x3, c3 = find_1d_pdf('3', start_time, 4.5, 1, 8000, 1000, area3, p=False, beta=True, tli=False, bli=False)
x4a, c4a = find_1d_pdf('4a', start_time, 4.5, 1, 8000, 1000, area4a, p=False, beta=True, tli=False, bli=False)
x4b, c4b = find_1d_pdf('4b', start_time, 4.5, 1, 8000, 1000, area4b, p=False, beta=True, tli=False, bli=False)
x4c, c4c = find_1d_pdf('4c', start_time, 4.5, 1, 8000, 1000, area4c, p=False, beta=True, tli=False, bli=False)
x5a, c5a = find_1d_pdf('5a', start_time, 4.5, 1, 8000, 1000, area5a, p=False, beta=True, tli=False, bli=False)
x5b, c5b = find_1d_pdf('5b', start_time, 4.5, 1, 8000, 1000, area5b, p=False, beta=True, tli=False, bli=False)
x5c, c5c = find_1d_pdf('5c', start_time, 4.5, 1, 8000, 1000, area5c, p=False, beta=True, tli=False, bli=False)
x6a, c6a = find_1d_pdf('6a', start_time, 4.5, 1, 8000, 1000, area6a, p=False, beta=True, tli=False, bli=False)
x6b, c6b = find_1d_pdf('6b', start_time, 4.5, 1, 8000, 1000, area6b, p=False, beta=True, tli=False, bli=False)
x7, c7 = find_1d_pdf('7', start_time, 4.5, 1, 8000, 1000, area7, p=False, beta=True, tli=False, bli=False)
xcball, cball = find_1d_pdf('area', start_time, 4.5, 1, 8000, 1000, all_area, p=False, beta=True, tli=False, bli=False, all=True)
fig, ax = plt.subplots()
ax.set_xscale('log')
colormap = plt.cm.tab20
colors = [colormap(i) for i in np.linspace(0, 1,16)]
ax.set_prop_cycle('color', colors)
plt.xlabel('\u03B2 (nm/a)')
plt.ylabel('Cumulative Probability')
ax.plot(x1a, c1a, label='1a')
ax.plot(x1b, c1b, label='1b')
ax.plot(x1c, c1c, label='1c')
ax.plot(x2, c2, label='2')
ax.plot(x3, c3, label='3')
ax.plot(x4a, c4a, label='4a')
ax.plot(x4b, c4b, label='4b')
ax.plot(x4c, c4c, label='4c')
ax.plot(x5a, c5a, label='5a')
ax.plot(x5b, c5b, label='5b')
ax.plot(x5c, c5c, label='5c')
ax.plot(x6a, c6a, label='6a')
ax.plot(x6b, c6b, label='6b')
ax.plot(x7, c7, label='7')
ax.plot(xcball,cball, label='All Areas')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.axhline(y=0.5, color='r', linestyle='--' )
ax.axhline(y=0.841, color = 'r', linestyle='dotted')
ax.axhline(y=0.159, color = 'r', linestyle='dotted' )
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax.legend(loc='upper right',bbox_to_anchor=(1.15,1.05))
fig.savefig('beta_cdfs.png', dpi=300)
