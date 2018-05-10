import numpy as np

a = np.random.rand(5,4)

print(a)


for row,index in enumerate(a) :
	print("[")
	for col in a[row] :
		print(str(col) + ",")
		print("]")

print("Row " + str(row) + " : "  + str(a[row]))

# Using Transpose 

b = np.random.rand(5,4)
print("Original 5x4 matrix")
print(b)
c = b.T
print("Transpose matrix")
print(c)

