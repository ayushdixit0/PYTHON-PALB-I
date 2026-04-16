#Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i, j, k = 0, 0, 0
        res = []
        last_added = None # To track and skip duplicates
        
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            # Check if all three elements are equal
            if arr1[i] == arr2[j] == arr3[k]:
                # Handle duplicates: only add if it's different from the last one
                if arr1[i] != last_added:
                    res.append(arr1[i])
                    last_added = arr1[i]
                
                i += 1
                j += 1
                k += 1
            
            # If not equal, move the pointer with the smallest value
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        
        # Return -1 if no common elements were found
        return res if res else [-1]
