class Solution:
    def commonElements(self, arr1, arr2, arr3):
        freq={}
        arr4=[]
        arr4.extend(list(set(arr1)))
        arr4.extend(list(set(arr2)))
        arr4.extend(list(set(arr3)))
        for i in arr4:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        arr4.clear()
        for i in freq:
            if freq[i]>2:
                arr4.append(i)
        arr4.sort()
        return arr4
        if arr4==None:
            return -1
