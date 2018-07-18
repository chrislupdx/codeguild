# bfast: 700-900 am
#lunch: 1200 pm -1400 pm
#dinner: 1900 pm -2100 pm
#hammer: 2200 pm -400 am
time = input('Tell me what time it is (example:1200)').lower()
hour = int(time[:-2])
meridian = time[-2:]

if hour in range(7,10) and meridian == 'am':
    print('bfast')
elif hour in [12,1,2,3] and meridian == 'pm':
    print('lunch')
elif hour in range(7,10) and meridian == 'pm':
    print('Dinner')
elif hour in [10, 11, 12, 1, 2, 3, 4] and meridian == 'pm' or 'am':
    print('hammer')
print(meridian)
print(hour)
