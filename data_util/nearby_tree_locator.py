import pandas as pd
import numpy as np
import math

'''
This is a basic calculation to find objects within a range of a specified point. The point is
defined by its GPS coordinates. The point GPS coordinate, desired range and objects GPS coordinates (CSV file) are
input. Out put is a list of objects within the specified range.
'''

#test
'''
# Inputs
dist = 150                           #desired range
longi=-81.554397                     #point longitude
lat=41.515645                       #point latitude
alt=0                               #point altitude
tree_address = '/home/arman/Desktop/Trial/image_location/image_location.csv'
'''


def nearby_trees(dist,longi,lat,alt,tree_address):
    # Constants
    R=6378100                           #earth radius
    meter_to_lat_deg=1/111318.84502145  #conversion factor of meter to latitude degree
    
    #calculating longitude range in degree of longitude 
    longi_deg_high=longi+(dist*360)/(2*math.pi*math.sin(math.radians(90-lat))*(R+alt))
    longi_deg_low=longi-(dist*360)/(2*math.pi*math.sin(math.radians(90-lat))*(R+alt))
    
    #reading the data file
    f_1=pd.read_csv(tree_address)
    
    nearby_tree_list=[]
    
    for i in range(f_1.shape[0]):
        if longi_deg_low<f_1.iloc[i][2] and f_1.iloc[i][2]<longi_deg_high: #find objects within the specified range in deg of longitude
            if (lat-dist*meter_to_lat_deg)<f_1.iloc[i][3] and f_1.iloc[i][3]<(lat+dist*meter_to_lat_deg): #find objects within the specified range in deg of latitude
                nearby_tree_list.append(f_1.iloc[i][0])
    return nearby_tree_list

#test
'''
nearby_tree_list=nearby_trees(dist,longi,lat,alt,tree_address)
print("the number of trees that are less than " + str(dist) + ' meters away from the taget is '
      + str(len(nearby_tree_list)))
'''