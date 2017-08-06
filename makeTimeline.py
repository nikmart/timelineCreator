"""
Make a "broken" horizontal bar plot, i.e., one with gaps
"""
import csv
import matplotlib.pyplot as plt
# Say, "the default sans-serif font is ..."
plt.rcParams['font.sans-serif'] = "Adobe Gothic Std"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "sans-serif"

# CONSTANTS
SECTION_NAME_IDX = 0
DURATION_IDX = 1
COLOR_IDX = 3

row_num = 0
time_list = [] # list of the timeblocks to plot
section_colors = [] # list of the colors for each block
section_labels = [] # list of x,y,text for section labels
y = 12 # how tall is the plot

time = 0

with open('productiveCar.csv', 'rb') as csvfile:
    timereader = csv.reader(csvfile, delimiter=',')
    for row in timereader:
        # skip the header row
        if row_num == 0:
            pass
        else:
            dur = float(row[DURATION_IDX])
            time_list.append( (time, dur) )
            section_colors.append(row[COLOR_IDX])
            section_labels.append( (time+dur/2, y/2, row[SECTION_NAME_IDX]) )
            time += int(row[DURATION_IDX])
        row_num += 1

fig, ax = plt.subplots()
ax.broken_barh(time_list, (1, 10), facecolors = section_colors)
ax.set_ylim(0, y)
ax.set_xlim(-1, time+1)
ax.set_xlabel('minutes')
ax.grid(False)
ax.yaxis.set_visible(False)
plt.tight_layout()

# create the section labels
idx = 0
for x,y,label in section_labels:
    ax.text(x, y, label, ha='center', va='center', rotation='vertical')
    idx += 1

plt.show()
