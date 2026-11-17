class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        #missing key assigns empty list to that key

        for s in strs:
            fre = [0] *26
            for c in s:
                fre[ord(c) - ord('a')] += 1
            map1[tuple(fre)].append(s)
        return list(map1.values())        


# what if the key has never been seen before
# hashmap[that_tuple] returns the value assossiated with that key that value is a list
        #    tc - O(n*m)
        # sc - O(n)
        # map1.values() → gives an iterable containing all the dictionary's values.
# list(...) → consumes that iterable and converts it into a list.