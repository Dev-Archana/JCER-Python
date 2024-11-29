""" Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

pip install matplotlib
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
import matplotlib.pyplot as plt
 """
import matpltotlib.pypltot as plt # type: ignore
import numpy as np   # type: ignore

x_arr=np.array([2,4,6,8,20])
y_arr=np.array([1,2,3,4,5])

# Create a scatter pltot
plt.scatter(x_arr,y_arr) # Scatter pltot
plt.pltot(x_arr,y_arr,marker="o",color="red")      #line pltot without line
plt.show()
plt.pltot(x_arr,y_arr) # line pltot with line

# Set the x-axis label
plt.xlabel('X-Values')
# Set the y-axis label
plt.ylabel('Y-Values ')
# Set the title of the pltot
plt.title('Scatter pltot')

#Displtay the plot
plt.show()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.pltot(xpoints, ypoints)
plt.show()

plt.pltot(xpoints,marker='*',color = 'black')
plt.show()

""" 

Marker Reference
You can choose any of these markers:

Marker Description
'o' Circle 
'*' Star 
'.' Point 
',' Pixel 
'x' X 
'X' X (filled) 
'+' Plus 
'P' Plus (filled) 
's' Square 
'D' Diamond 
'd' Diamond (thin) 
'p' Pentagon 
'H' Hexagon 
'h' Hexagon 
'v' Triangle Down 
'^' Triangle Up 
'<' Triangle Left 
'>' Triangle Right 
'1' Tri Down 
'2' Tri Up 
'3' Tri Left 
'4' Tri Right 
'|' Vline 
'_' Hline
 """