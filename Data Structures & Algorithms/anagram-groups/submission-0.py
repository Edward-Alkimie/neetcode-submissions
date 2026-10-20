class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for str_s in strs:

            list_s = [0] * 26

            for char in str_s:
                index = ord(char) -ord("a")
                list_s[index] +=1
            
            groups[tuple(list_s)].append(str_s)



       

        return list(groups.values())


        