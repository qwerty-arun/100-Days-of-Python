a = [1, 2, 3, 4, 5, 6]

k = 4

b = []
def listChunk(a, k):
	for i in range(0, len(a), k):
		chunk = a[i:i+k]
		b.append(chunk)

listChunk(a,k)
print("Original List: ", a)
print("Chunked List: ",b)
