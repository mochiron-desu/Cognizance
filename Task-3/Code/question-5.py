import numpy as mochi

arr1=mochi.array([[2, -7, 10], [12, -4, 0]])
arr2=mochi.array([[2, -3, 5], [-10, 42, 3]])

arrAdd=mochi.add(arr1,arr2)
arrMul=mochi.multiply(arr1,arr2)
print("Addition of two array:\n",arrAdd)
print("Multiplication of two array:\n",arrMul)