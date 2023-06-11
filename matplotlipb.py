#Xetti diaqramin qurulmasi
# import matplotlib.pyplot as plt
# # Veri seti
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Xətti diaqramı oluşturma
# plt.plot(x, y)

# # Grafik başlığı ve eksen etiketlerini ayarlama
# plt.title("Xətti Diaqram")
# plt.xlabel("X ekseni")
# plt.ylabel("Y ekseni")

# # Grafik gösterme
# plt.show()
#Modul Matplotlib. Nöqtəvari qrafiklərin qurulması.
# import matplotlib.pyplot as plt

# # Veri seti
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Nöqtəvari grafik oluşturma
# plt.scatter(x, y)

# # Grafik başlığı ve eksen etiketlerini ayarlama
# plt.title("Nöqtəvari Grafik")
# plt.xlabel("X ekseni")
# plt.ylabel("Y ekseni")

# # Grafik gösterme
# plt.show()
# 39.	Modul Matplotlib. Punktirli qrafiklərin qurulması.
# import matplotlib.pyplot as plt

# # Veri seti
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Punktirli grafik oluşturma
# plt.plot(x, y, linestyle='dotted')

# # Grafik başlığı ve eksen etiketlerini ayarlama
# plt.title("Punktirli Grafik")
# plt.xlabel("X ekseni")
# plt.ylabel("Y ekseni")

# # Grafik gösterme
# plt.show()
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.bar(x, y, color='blue')  # Sütunların dolgu rengini mavi olarak ayarla

# plt.show()

# import matplotlib.pyplot as plt

# # Çizgi stilini ayarlama
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], linestyle='-', color='blue', label='Çizgi Stili 1')
# plt.plot([1, 2, 3, 4], [2, 4, 6, 8], linestyle='--', color='red', label='Çizgi Stili 2')
# plt.plot([1, 2, 3, 4], [4, 2, 4, 1], linestyle=':', color='green', label='Çizgi Stili 3')
# plt.plot([1, 2, 3, 4], [8, 6, 4, 2], linestyle='-.', color='purple', label='Çizgi Stili 4')

# # Eksen etiketlerini ve başlığı ayarlama
# plt.xlabel('X ekseni')
# plt.ylabel('Y ekseni')
# plt.title('Çizgi Stilleri')

# # Lejantı gösterme
# plt.legend()

# # Grafiği gösterme
# plt.show()
# import matplotlib.pyplot as plt

# # Veri noktalarını tanımlama
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Xətti diaqramı oluşturma
# plt.plot(x, y)
# plt.scatter(x,y)
# plt.plot(x, y, color='blue')
# # Eksen etiketlerini ve başlığı ayarlama
# plt.xlabel('X ekseni')
# plt.ylabel('Y ekseni')
# plt.title('Xətti Diaqram')

# # Grafiği gösterme
# plt.show()
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, marker='o', markersize=8, markerfacecolor='red', markeredgewidth=2, markeredgecolor='black')

# plt.xlabel('X ekseni')
# plt.ylabel('Y ekseni')
# plt.title('Örnek Grafik')

# plt.show()
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [1,2,3,45,5]
# plt.plot(x,y,linestyle='dotted')
# # plt.scatter(x,y,color='red')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('okey')
# plt.show()
# import matplotlib.pyplot as plt

# labels = ['A', 'B', 'C', 'D']
# sizes = [15, 30, 45, 10]
# colors = ['red', 'green', 'blue', 'yellow']

# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# plt.axis('equal')  # Dairevi diaqramın yuvarlak şekilde görünmesini sağlar
# plt.title('Örnek Dairevi Diaqram')

# plt.show()

# import matplotlib.pyplot as plt
# labals = ['A','B','C','D','E']
# sizes = [20,20,20,20,20]
# colors = ['red', 'green', 'blue', 'yellow','pink']
# plt.pie(sizes ,labels=labals,colors=colors,autopct='%1.1f%%',startangle=90)
# plt.axis('equal')
# plt.title('x')
# plt.show()
# import matplotlib.pyplot as plt

# labels = ['A', 'B', 'C', 'D']
# sizes = [15, 30, 45, 10]
# colors = ['red', 'green', 'blue', 'yellow']
# explode = (0, 0.1, 0, 0.1)  # Hissələrin ayrılma dərəcəsi

# plt.pie(sizes, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%', startangle=90)

# plt.axis('equal')  # Dairevi diaqramın yuvarlak şekilde görünmesini sağlar
# plt.title('Örnek Dairevi Diaqram')

# plt.show()
# import matplotlib.pyplot as plt

# labels = ['A', 'B', 'C', 'D']
# sizes = [15, 30, 45, 10]
# colors = ['red', 'green', 'blue', 'yellow']

# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# plt.axis('equal')  # Dairevi diaqramın yuvarlak şekilde görünmesini sağlar
# plt.title('Örnek Dairevi Diaqram')

# # Leqendanın oluşturulması
# plt.legend(labels, title="Kategoriler", loc="upper right")

# plt.show()
# import matplotlib.pyplot as plt

# categories = ['A', 'B', 'C', 'D']
# values = [20, 35, 30, 25]

# plt.bar(categories, values)
# plt.xlabel('Kategoriler')
# plt.ylabel('Değerler')
# plt.title('Sütun Formalı Vertical Diaqram')

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Verileri oluşturma
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # Alt grafikleri oluşturma
# plt.subplot(2, 1, 1)  # 2 satır, 1 sütunlu figürde 1. alt grafik
# plt.plot(x, y1)
# plt.title('Sin(x)')

# plt.subplot(2, 1, 2)  # 2 satır, 1 sütunlu figürde 2. alt grafik
# plt.plot(x, y2)
# plt.title('Cos(x)')

# plt.tight_layout()  # Grafiklerin düzgün bir şekilde yerleştirilmesi

# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# # Rastgele veri oluşturma
# np.random.seed(0)
# data = np.random.randn(1000)

# # Histogram oluşturma
# plt.hist(data, bins=30, edgecolor='black')

# plt.xlabel('Değer Ara')
# plt.ylabel('Frekans')
# plt.title('Histogram')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# # Təsadüfi ədədlər generasiyası
# data = np.random.normal(loc=0, scale=1, size=1000)  # Ortaqiymət=0, standart səhvət=1, ölçü=1000

# # Histogramın yaradılması
# plt.hist(data, bins=30, edgecolor='black')

# plt.xlabel('Değer Aralığı')
# plt.ylabel('Frekans')
# plt.title('Histogram')

# plt.show()

# import matplotlib.pyplot as plt
# x= ['a','b','c']
# y =[1,2,3]
# plt.scatter(x,y,marker='o')
# plt.xlabel('X label')
# plt.ylabel('Y label')
# plt.show()
# import matplotlib.pyplot as plt
# labels =['A','B','C']
# sizes = [33.3,30,36.7]
# colors = ['red','BLue','yellow']
# plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90)
# plt.title('Qrafik')
# plt.legend()
# plt.axis('equal')
# plt.show()
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=['A','B','C','D']
# plt.bar(x,y)
# width=20

# import matplotlib.pyplot as plt
# import numpy as np

# Təsadüfi ədədlər generasiyası
# data = np.random.normal(loc=0, scale=1, size=1000)  # Ortaqiymət=0, standart səhvət=1, ölçü=1000

# # Histogramın yaradılması
# plt.hist(data, bins=30, edgecolor='black')

# plt.xlabel('Değer Aralığı')
# plt.ylabel('Frekans')
# plt.title('Histogram')

# # plt.show()
# import numpy as np
# import matplotlib.pyplot as plt

# # Təsadüfi ədədlər yaratma
# np.random.seed(42)  # Sonuclarin tekrarlanabilir olmasi icin seed ayarlaniyor
# data = np.random.normal(0, 1, 1000)  # Ortalama=0, standart sapma=1 olan 1000 təsadüfi ədəd

# # Histoqram yaratma
# plt.hist(data, bins=20, edgecolor='black')  # Veriyi 20 bins ile histograma çeviriyoruz
# plt.xlabel('ədəd')  # x-əksi etiketi
# plt.ylabel('Say')  # y-əksi etiketi
# plt.title('Təsadüfi Ədədlərin Histoqramı')  # Grafik başlığı

# plt.show()


import matplotlib.pyplot as plt

# Verileri oluşturma
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
explode = [0, 0.1, 0, 0]  # Ayrılan hissələrin oranları

# Dairəvi diaqramı oluşturma
plt.pie(sizes, labels=labels, explode=explode, shadow=True)

# Grafik görüntüsünü gösterme
plt.show()
