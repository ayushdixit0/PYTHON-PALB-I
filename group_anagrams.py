class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict1={}
        for string in strs:
            key=''.join(sorted(string))
            if key not in dict1:
                dict1[key]=[]
            dict1[key].append(string)
        anagrams=dict1.values()
        return list(anagrams)
