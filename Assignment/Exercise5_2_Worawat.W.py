'''
v = s/t
v คืออัตราเร็วของการเคลื่อนที่ (m/s หรือ km/hr)
t คือเวลาที่วัตถุใช้เคลื่อนที่จริง (s หรือ hr)

'''

s = int(input("The distance that a car moves in km: "))  # s = distance
t = int(input("The time it takes in hours: ")) # t = time
v = int(s/t) # v = velocity
print(v, "km/h")
