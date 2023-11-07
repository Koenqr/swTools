import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.style as mplstyle
mplstyle.use('fast')


sep=';'


data=pd.read_csv('CSVS/AsteralPrint.LOG.csv',sep=';')
#data=pd.read_csv('test.csv',sep=';')

#print header using pandas
print(data.columns)

lenData=len(data['#'])

#header:#; time; x; y; z; ax; ay; az
#where ax,ay,az are the asteral coordinates and x,y,z are the corresponding regular coordinates

#scatter plot x,y,z if ax !=1 and !=-1 and ay!=0 and az!=-1 and !=1
''' #3D plot of the points that are in the corridor, lags like shit
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for k in range(lenData):
    ax_value = data['ax'][k]
    ay_value = data['ay'][k]
    az_value = data['az'][k]

    if ax_value == 1 or ax_value == -1:
        continue
    if ay_value == 0:
        continue
    if az_value == 1 or az_value == -1:
        continue

    print(k)
    ax.scatter(data['x'][k], data['y'][k], data['z'][k], c='r')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()'''

'''
#2D slice of corridor (z=0)
fig=plt.figure()
ax=fig.add_subplot()


for k in range(lenData):
    if data['ax'][k]==1 or data['ax'][k]==-1 or abs(data['ax'][k])>0.125:
        continue
    if data['ay'][k]==0:
        continue
    
    ax.scatter(data['x'][k],data['y'][k],c='r')


for k in range(lenData):
    if data['ax'][k]==1 or data['ax'][k]==-1 or abs(data['ax'][k]-0.875)>0.125:
        continue
    if data['ay'][k]==0:
        continue
    
    ax.scatter(data['x'][k],data['y'][k],c='blue')

    
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
'''

'''
fig=plt.figure()
ax=fig.add_subplot()

#copy data to new dataframe
dataEdit=data.copy()

#yeet out all points that have az==0 and ax!=1 and ax!=-1 and ay!=0
for k in range(lenData):
    if data['az'][k]==0:
        continue
    if data['ax'][k]==1 or data['ax'][k]==-1:
        continue
    if data['ay'][k]!=0:
        continue
    dataEdit=dataEdit.drop(k,axis="index")
    
dataEdit=dataEdit.reset_index(drop=True)
lenData=len(dataEdit['#'])


    
dataIdeal=dataEdit.copy()
for k in range(lenData):
    if abs(data['ax'][k])>0.125:
        dataIdeal=dataIdeal.drop(k,axis="index")
#sort data by ay
dataIdeal=dataIdeal.reset_index(drop=True)
dataIdeal=dataIdeal.sort_values(by=['ay'])

dataOffset=dataEdit.copy()
for k in range(lenData):
    if abs(data['ax'][k]-0.875)>0.125:
        dataOffset=dataOffset.drop(k,axis="index")
#sort data by ay
dataOffset=dataOffset.reset_index(drop=True)
dataOffset=dataOffset.sort_values(by=['ay'])
        
#plot the data
ax.plot(dataIdeal['x'],dataIdeal['y'],c='r')
ax.plot(dataOffset['x'],dataOffset['y'],c='b')

ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
'''
'''
#2D representation astro_y over alt
fig=plt.figure()
ax=fig.add_subplot()


for k in range(lenData):
    if data['ax'][k]==1 or data['ax'][k]==-1 or abs(data['ax'][k])>0.125:
        continue
    if data['ay'][k]==0:
        continue
    
    #print(str(data['y'][k])+sep+str(data['ay'][k]),file=open("red.csv","a"))
    
    ax.scatter(data['y'][k],data['ay'][k],c='r')


for k in range(lenData):
    if data['ax'][k]==1 or data['ax'][k]==-1 or abs(data['ax'][k]-0.875)>0.125:
        continue
    if data['ay'][k]==0:
        continue
    
    #print(str(data['y'][k])+sep+str(data['ay'][k]),file=open("blue.csv","a"))
        
    
    ax.scatter(data['y'][k],data['ay'][k],c='blue')
    
for k in range(lenData):
    if data['ax'][k]==1 or data['ax'][k]==-1 or abs(data['ax'][k]+0.875)>0.125:
        continue
    if data['ay'][k]==0:
        continue
    
    #print(str(data['y'][k])+sep+str(data['ay'][k]),file=open("green.csv","a"))
    
    ax.scatter(data['y'][k],data['ay'][k],c='green')

    
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
'''
'''
#2D representation astro_y over alt
fig=plt.figure()
ax=fig.add_subplot()


for k in range(lenData):
    if data['x'][k]!=0 and data['z'][k]!=0:
        continue
    
    #print(str(data['y'][k])+sep+str(data['ay'][k]),file=open("red.csv","a"))
    
    ax.scatter(data['y'][k],data['ax'][k],c='r')
    
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()'''

#using pandas correlation
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

# Drop # and time columns
data = data.drop(['#', 'time', 'z', 'az'], axis=1)
dataLen=len(data['x'])
# Remove rows with y<128000
for k in range(dataLen):
    if data['y'][k]<128000:
        data=data.drop(k,axis="index")
data=data.reset_index(drop=True)

# Split data into training and validation sets
train, val = train_test_split(data, test_size=0.2, random_state=42)

# Separate input and output variables
X_train = train[['x', 'y']]
y_train = train[['ax', 'ay']]
X_val = val[['x', 'y']]
y_val = val[['ax', 'ay']]

# Create polynomial features
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_val_poly = poly.transform(X_val)

# Fit the model
model = LinearRegression()
model.fit(X_train_poly, y_train)
coefficients = model.coef_
featureNames=poly.get_feature_names_out(input_features=['x', 'y'])
intercepts = model.intercept_
output_dims = ['ax', 'ay']

for i, output_dim in enumerate(output_dims):
    terms = [f"{intercepts[i]}"]  # Start with the intercept
    for coef, feature in zip(coefficients[i], featureNames):
        if coef != 0:  # Skip terms with a zero coefficient
            terms.append(f"{coef} * {feature}")
    formula = f"{output_dim}(x, y) = {' + '.join(terms)}"
    print("Formula:", formula)

# Make predictions
y_pred = model.predict(X_val_poly)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_val, y_pred))
print("RMSE:", rmse)