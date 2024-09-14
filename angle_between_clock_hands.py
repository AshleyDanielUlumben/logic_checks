# Angle between Clock Hands

# In 60 mins -> long hand moves 360 degrees
# In 60 mins -> short hand moves 30 degrees

hour = 12
minutes = 30
# hr is at 15 degrees while
# mins is at 180 
# There the Expected result is 165 --> 180 - 15

def angleClock(hr, mins):
    lh = mins * 6 # per minute the long hand moves 6 degrees
    # per hour the hour hand moves 30 degrees
    sh = (hr * 30) + (mins * 0.5) # per minute the short hand moves 0.5 degrees
    ang = abs(lh - sh)
    res = min(ang, 360 - ang) # Taking the minimum, to measure the angle in counter clockwise direction
    return res

print(angleClock(hour, minutes))

