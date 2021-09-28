This is the code for An Y. Li's 2021 senior thesis:
"A New Probabilistic Model to Evaluate the Age and Erosion Rate of Young
Sedimentary Rock on Mars."

For any questions, contact An at anli7@uw.edu.

Before running any scripts, please make sure the following Python packages are
installed: matplotlib, numpy, scipy, pandas, math, and collections. If any of them
are not installed, in Terminal, run: "pip install _____" where the package
name goes in the blank.

Important: All scripts and data must be in the same folder. Download data file region_data.zip here: 
https://drive.google.com/file/d/109dBnRp7Fl4MPuyqZQ9MBn4_-ahN17sY/view?usp=sharing. 
After downloading, unzip and place scripts with data in same folder.

all_craters.csv, all_craters.xlsx: CSV and Excel files of crater dataset.

erosion_age.py: Contains important functions for the other ".py" scripts.

After navigating to the correct folder in Terminal, you can run the following
scripts. Note: all scripts are set to linearly spacing. Functions are written
so that log arrays may be used instead. Each single variable array has 1000 points.

contour_plots.py: Run the command "python contour_plots.py" in Terminal
to get the contour plots for each of the 14 regions and for all regions together.
To try running one area first, refer to the comment "comment out below..." and
comment out everything below it by highlighting and doing "Command" + "/".
Save file, and then run in Terminal.

best_fit_plots.py: Run "python best_fit_plots.py" in Terminal to get the
model's best fit plots for each of the 14 regions and for all regions together.
To try one area first, refer to the comment "comment out below..." and save
script, then run.

pdfs_cdfs.py: Run "python pdfs_cdfs.py" in Terminal to get the
model's PDFs and CDFs for all 14 regions with 1 line for all regions. In total,
this script will make 5 plots: 1 plot for all age PDFs, 1 plot for all age PDFs
without area 4, 1 plot for all beta PDFs, 1 plot for all age CDFs, and 1 plot
for all beta CDFs. Each plot can take upwards of 10-20 minutes to run. To try one
plot first, refer to the comment "comment out below..." and save script, then run.

ind_volume_plots.py: Only run "python best_fit_plots.py" in Terminal to get the
model's volume plots for each of the 14 regions and all 14 regions together. To
try one area first, refer to the comment "comment out below..." and save script, then run. 
ind_volume_plots.py uses scripts from ind_volume_functions.py.

cum_vol_plots.py: Run "python cum_vol_plots.py" in Terminal to get the
model's volume plots for a cumulative 14 regions plot and a cumulative 14 regions
displaying each individual area's contribution. To save run time, if you already
ran ind_volume_plots.py, then refer to the top of cum_vol_plots.py to know what
to comment out.

To time any process: Add "time" before the command in Terminal. Example:
"time python contour_plots.py" will give you all 14 contour plots and the time
it takes to run this script will be printed in Terminal.

All other files are data files. The folder "plots" contains previously created
plots used in the thesis.

Legend of areas:
1: Central Medusae Fossae 1
2: Aeolis Planum
3: Eastern Candor
4: Central Medusae Fossae 2
5: Far East Medusae Fossae
6: East Medusae Fossae
7: Gale's Mound/Upper Mount Sharp
