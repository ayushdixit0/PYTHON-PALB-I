class Solution:
    def median(self, mat):
        list1=[]
    	for row in mat:
    	    list1.extend(row)
    	list1.sort()
    	mid=(0+len(list1)-1)//2
    	return list1[mid]
    	
