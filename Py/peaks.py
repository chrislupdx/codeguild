this_dict = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
peak = []
for n in range(1,len(this_dict)-1):
    if this_dict[n] > this_dict[n-1] and this_dict[n] > this_dict[n+1]:
        peak.append(n)
        # print(peak)
valley = []
for n in range(1,len(this_dict)-1):
    if this_dict[n] < this_dict[n-1] and this_dict[n] < this_dict[n+1]:
        valley.append(n)
        # print(valley)

combined = sorted(valley + peak)
print(combined)
