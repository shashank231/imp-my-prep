

def fun1(n):
    lst1 = [int(i) for i in str(n)]

    def isMonotonicList(lst1):
        len1 = len(lst1)
        if len1 == 1: return True

        isMonotonic = True
        for i in range(1, len1):
            if lst1[i] < lst1[i-1]:
                isMonotonic = False

        return isMonotonic 

    len2 = len(lst1)
    while not isMonotonicList(lst1):
        for i in range(1, len2):
            if not(lst1[i]>=lst1[i-1]):
                lst1[i-1] = lst1[i-1]-1
                for j in range(i, len2):
                    lst1[j] = 9
                break
    
    solutionStr = ""
    for k in lst1:
        solutionStr += str(k)
    return int(solutionStr)

a = fun1(1234)
print(a)


def processLogs(logs, threshold):
    logs_metadata = {}

    for log in logs:
        user_id, rcpnt_id, _ = log.split(" ")
        unique_users = {user_id, rcpnt_id}

        for uid in unique_users:
            logs_metadata[uid] = logs_metadata.get(uid, 0) + 1

    # Filter and sort numerically
    result = [uid for uid, count in logs_metadata.items() if count >= threshold]
    return sorted(result, key=int)
