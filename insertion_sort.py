def insertion_sort(L):
	
	n=len(L)
	
	for i in range(0,n-1):
		
		item=L[i]
		
		j=i-1
		
		while j>=0 and L[j]>L[j+1]:
			
			L[j+1]=L[j]
			j=j-1
			L[j+1]=item
			
			
	
	
if __name__ == "__main__":
	L=[3,7,9,1,0,6,2,4,5,8]
	print("Before sorting:", L)
	insertion_sort(L)
	print("After sorting:", L)
