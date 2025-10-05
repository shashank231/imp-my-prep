


# 💭 Intuition
# Two intervals overlap if one starts before the other one ends.
# So the key idea:
# Sort intervals by their start time.
# Compare each interval with the last one added to the result.
# If they overlap → merge them by taking the max end time.
# If they don’t → just add it as a new interval.

# 🧠 Step-by-step Example
# Input:
# [[1,3], [2,6], [8,10], [15,18]]
# Step 1️⃣ — Sort by start time
# After sorting:
# [[1,3], [2,6], [8,10], [15,18]]

# Step 2️⃣ — Initialize merged list
# merged = [[1,3]]
# Step 3️⃣ — Iterate from the second interval
# Compare [2,6] with [1,3] → Overlaps (because 2 ≤ 3)
# → Merge them → [1, max(3,6)] = [1,6]
# → merged = [[1,6]]

# Next [8,10] with [1,6] → No overlap (8 > 6)
# → Add it → merged = [[1,6], [8,10]]

# Next [15,18] with [8,10] → No overlap (15 > 10)
# → Add it → merged = [[1,6], [8,10], [15,18]]
# ✅ Final result: [[1,6], [8,10], [15,18]]


def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    # Step 2: iterate through intervals
    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # overlap
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged



class Solution:
    
    def main(self, arr2):
        arr2 = [tuple(x) for x in arr2]
        dict1 = {}
        
        def recn(arr):
            hash_value = tuple(arr)

            if hash_value in dict1:
                return dict1[hash_value]
            
            lArr = len(arr)
            if lArr == 1:
                dict1[hash_value] = arr
                return arr 

            firstEle = arr[0]
            newArr = arr[1:]      
            nw2 = newArr[:]       
            mergedIntervalsArr = recn(nw2)

            # Adjust firstEle in mergedIntervalsArr
            firstEle_fst = firstEle[0]
            firstEle_scd = firstEle[1]
            found = False
            index = 0
        
            while index < len(mergedIntervalsArr):
                currEle = mergedIntervalsArr[index]
                if firstEle_scd < currEle[0]:
                    found = True
                if firstEle_scd < currEle[1]:
                    found = True
                if found:
                    break
                index += 1
            
            if index == len(mergedIntervalsArr):
                index = len(mergedIntervalsArr) - 1
        
            cutOffIndex = index        
            if mergedIntervalsArr[cutOffIndex][0] > firstEle_scd:
                cutoffSmallerNestedIndex = 0
            elif mergedIntervalsArr[cutOffIndex][1] > firstEle_scd:
                cutoffSmallerNestedIndex = 1
            else:
                dict1[hash_value] = [firstEle]
                return [firstEle]

            arr_first_part = [firstEle_fst, firstEle_scd]
            if cutoffSmallerNestedIndex == 1:
                arr_first_part[1] = mergedIntervalsArr[cutOffIndex][1]
            if cutoffSmallerNestedIndex == 0:
                arr_second_part = mergedIntervalsArr[cutOffIndex:]
            if cutoffSmallerNestedIndex == 1:
                arr_second_part = mergedIntervalsArr[cutOffIndex+1:]
        
            answerArr = [arr_first_part] + arr_second_part
            dict1[hash_value] = answerArr
            return answerArr

        return recn(arr2)

    def mergeOverlap(self, arr1):
        arr = sorted(arr1, key=lambda x: x[0])
        ans = self.main(arr)
        return ans
