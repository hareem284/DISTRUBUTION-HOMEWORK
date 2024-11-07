

#I DO NOT KNOW WAHT IS THE PROBLEM WITH THR BOX PLOT BUT ALL THE OTHER ONES ARE WORKING I EVEN TRIED THE BOXEN PLOT AND YOU WERE RIGHT IT WAS A PEICE OF CAKE!!!!!!



#importing matplotlib,seaborn and pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
#reading csv file
df=pd.read_csv('fuel.csv')
print(df.info())
df.isnull().any()
labels=['CO2EMISSIONS','FUELCONSUMPTION_COMB_MPG']
for h in labels:
    sb.kdeplot(df[h])
    plt.show()
sb.violinplot(data=df,x='CO2EMISSIONS',y='FUELCONSUMPTION_COMB_MPG',palette='viridis',width=5)
plt.show()
sb.boxplot(data=df,x='MODELYEAR',y='MODEL',palette='viridis',width=3)
plt.show()
sb.boxenplot(data=df,x='CYLINDERS',y='FUELTYPE',palette='viridis',width=2)
plt.show()