# import seaborn as sns
# import matplotlib.pyplot as plt

# # Veri oluşturma
# x = ['A', 'B', 'C', 'D']
# y = [10, 7, 12, 8]

# # Dikey çubuk diyagramını oluşturma
# sns.barplot(x=x, y=y)

# # Grafiği gösterme
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# x =['A','B','C']
# y =[1,2,3]
# sns.barplot(x=x,y=y)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# X=[1,2,3]
# Y=['A','B','C']
# sns.barplot(x=X ,y=Y)
# plt.show()
# import seaborn as sns
# import matplotlib.pyplot as plt

# `tips` veri setini yükleme
# tips = sns.load_dataset("tips")

# # Yatay çubuk diyagramını oluşturma
# sns.barplot(x="day", y="total_bill", data=tips)

# # Grafiği gösterme
# plt.show()

#Cox olculu
# import seaborn as sns
# import matplotlib.pyplot as plt
# # `iris` veri setini yükleme
# iris = sns.load_dataset("iris")

# # Çokölçülü dağılım grafiği oluşturma
# sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species")

# # Grafiği gösterme
# plt.show()

# import seaborn as sb
# import matplotlib.pyplot as pl
# x = [1,2,3,4,5]
# y = ['A','B','C','D','E']
# sb.barplot(x=x,y=y)
# pl.show()

# import seaborn as sb
# import matplotlib.pyplot as pl
# x=['A','B','C']
# y=[1,2,3]
# sb.barplot(x=y,y=x)
# pl.show()

# import scipy as sns
# import matplotlib.pyplot as plt
# iris = sns.load_dataset('iris')
# sns.jointplot(data = iris,x='special_lemght',y='sepal_widh',hue='species')
# plt.show()

import seaborn as sb
x =['a','b','c']
y=[1,2,3]
iris = sb.load_dataset('iris')