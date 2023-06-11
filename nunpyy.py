# import numpy as np

# arr = np.array([1,2,3,4,5,10])
# arr2 = np.array([2,3,4,5,6,7]) 
# matrix = np.array([[1, 2,3],
#                    [4, 5,6]])

#determinant
# det = np.linalg.det(matrix)
# print(det)
# print(np.sum(arr))
# print(np.mean(arr))
# print(arr*arr2)
#tersmatris
# ters = np.linalg.inv(matrix)
# print(ters)
#Transpolire
# ters = matrix.T
# print(ters)
# Modul NumPy. Matrisin məxsusi ədədlərinin tapılması
# matrix =np.array([[1,2],
#                   [3,4]])
# Mexsusi = np.linalg.eig(matrix)
# print(Mexsusi)
# Modul NumPy.  XCTS-nin həlli
# Matrix = np.array([[1,2],
#                    [3,4]])
# Matrix2 = np.array([1,2])
# Sum = np.linalg.solve(Matrix,Matrix2)
# print(Sum)
#Mean
# arr =np.array([1,2,3,4,4,5])
# Mean = np.mean(arr)
# print(Mean)
#Mode
# import numpy as np
# from scipy import stats

# # Örnek bir dizi oluşturalım
# arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 5])

# # Dizinin modunu hesaplayalım
# mode = stats.mode(arr)

# print(mode)
#Median
# arr = np.array([1,2,3,4,5])
# median = np.median(arr)
# print(arr)
# import numpy as np

# # 2x3'lük bir NumPy dizisi oluşturma
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# # Dizinin elemanlarının toplamını hesaplama
# toplam = np.sum(arr, axis=0)  # Sütun bazında toplam

# print("Dizinin toplamı:", toplam)

# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# hasil = np.multiply(arr1,arr2)
# print(hasil)
    
# import numpy as np
# arr1 = np.array[1,2,3,4]
# arr2=np.array[2,4,6,8]
# ferq =np.subtract(arr1,arr2)
# print(ferq)

# import numpy as np
# matrix = np.array([[1, 2,3],
#                    [4, 5,6]])

# det = np.linalg.det(matrix)
# print(det)
# import numpy as np
# arr1 = np.array[1,2,3]
# ters = np.linalg.inv(arr1)
# print(ters)
# import numpy as np
# arr = np.array([1,2,3,4,3,5,6])
# mod = np.argmax(np.bincount(arr))
