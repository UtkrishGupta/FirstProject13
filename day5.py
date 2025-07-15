import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Step :1 Create dataframes
data={
    'Name':['Anu','Ravi','Sita','Karan','Rahul'],
    'Maths':[89,56,95,96,53],
    'English':[96,36,25,68,78],
    'Science':[98,65,32,89,96],
    'Computer':[98,65,85,35,74],
}
df=pd.DataFrame(data)

#Step:2 
df['Total'] = df[['Maths', 'English', 'Science', 'Computer']].sum(axis=1)
df['Percentage']=df['Total']/4

#Step:3 Assign Grades
def assign_grades(p):
    if p>=90:
        return 'A+'
    elif p>=70:
        return 'A'
    elif p>=60:
        return 'B'
    elif p>=50:
        return 'C'        
    else:
        return 'F'

df['Grade']=df['Percentage'].apply(assign_grades)
print("Report Card")
print(df)

# #Step:4
# plt.figure(figsize=(10,6))
# sns.barplot(x='Name',y='Total',data=df,palette='Blues')#here can be countplot also
# plt.title('Total Marks of Students:')
# plt.ylabel('Total Marks')
# plt.xlabel('Student Name')
# plt.tight_layout()
# plt.show()

#Step:5
plt.plot(x='Grade',data=df,palette='Blues')
plt.title('Grade of Students:')
plt.ylabel('Number of Students')
plt.xlabel('Grade')
plt.tight_layout()
plt.show()





