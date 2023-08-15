# unit 2
import math

# 1. A person, with his ear to the ground, sees a huge stone strike the concrete pavement.
# A moment later two sounds are heard from the impact: one travels in the air and
# the other in the concrete, and they are 0.80 s apart.
# How far away did the impact occur? (air: 343 m/s, concrete 3000 m/s)

vAIR = 343 # m/s
vCONC = 3000 # m/s
t = 0.80 # s

# tAIR = tCONC + t
# dAIR = vAIR * tAIR
# dCONC = vCONC * tCONC
# vAIR * tAIR = vCONC * tCONC
# => vAIR * (tCONC + t) = vCONC * tCONC
# => tCONC = (t * vAIR)/ (vCONC - vAIR)
tCONC = (t * vAIR) / (vCONC - vAIR) # s
dCONC = vCONC * tCONC # m

print("1. A person, with his ear to the ground, sees a huge stone strike the concrete pavement.\
      \nA moment later two sounds are heard from the impact: one travels in the air and\
      \nthe other in the concrete, and they are 0.80 s apart.\
      \nHow far away did the impact occur? (air: 343 m/s, concrete 3000 m/s)\n")
print(round(dCONC, 3), " m")
print("\n----------------------------------------------------------\n")


# 2. You are trying to decide between two new stereo amplifiers.
# One is rated at 75 W per channel and the other is rated at 120 W per channel.
# In terms of dB, how much louder will the more powerful amplifier be
# when both are producing sound at their maximum levels?

P1 = 75 # W
P2 = 120 # W

# beta = 10log(P2 / P1)
beta = 10 * math.log10(P2 / P1) # dB, difference

print("2. You are trying to decide between two new stereo amplifiers.\
      \nOne is rated at 75 W per channel and the other is rated at \
      120 W per channel.\nIn terms of dB, how much louder will the \
      more powerful amplifier be\nwhen both are producing sound at \
      their maximum levels?\n")
print(round(beta, 3), " dB")
print("\n----------------------------------------------------------\n")


# 3. Estimate the frequency of the “sound of the ocean”
# when you put your ear very near a 15-cm-diameter seashell.

L = 0.15 # m
vAIR = 343 # m/s

# L = 1/4 * lambda
# lambda = 4L
lam = 4 * L # m

# v = lambda * f
# f = v / lambda
f = vAIR / lam # Hz

print("3. Estimate the frequency of the “sound of the ocean” \
      \nwhen you put your ear very near a 15-cm-diameter seashell.\n")
print(round(f, 3), " Hz")
print("\n----------------------------------------------------------\n")


# 4. A pipe in air at 23.0°C is to be designed to produce two successive
# harmonics at 280 Hz and 320 Hz. How long must the pipe be?

vAIR = 343 # m/s
f1 = 280 # Hz
f2 = 320 # Hz
fb = f2 - f1 # Hz

# v = f * lambda
# lambda = v / f
lam = vAIR / fb # m

# lambda = 2L
# L = (1/2)lambda
L = (1 / 2) * lam # m

print("4. A pipe in air at 23.0°C is to be designed to produce two successive\
      \nharmonics at 280 Hz and 320 Hz. How long must the pipe be?\n")
print(round(L, 3), " m")
print("\n----------------------------------------------------------\n")


# 5. Determine the fundamental and first overtone frequencies when you are in
# a 9.0-m-long hallway with all doors closed. Model the hallway as a tube
# closed at both ends.

L = 9 # m
vAIR = 343 # m/s

# L = 2(1/4)lambda = lambda / 2
# lambda = 2L
lam = 2 * L # m

# v = lamda * f
# f = v / lambda
fb = vAIR / lam # Hz

# 2nd harmonic = first overtone
# L = 4(1/4) * lambda = lambda
lam = L # m

# f = v / lambda
f1 = vAIR / lam # Hz

print("5. Determine the fundamental and first overtone frequencies when you are in\
      \na 9.0-m-long hallway with all doors closed. Model the hallway as a tube\
      \nclosed at both ends.\n")
print("fundamental: ", round(fb, 3), " Hz")
print("first overtone freq: ", round(f1, 3), " Hz")
print("\n----------------------------------------------------------\n")


#6.  A piano tuner hears one beat every 2.0 s when trying to adjust two strings,
# one of which is sounding 350 Hz. How far off in frequency is the other string?

# fb = # of events / time between events = one beat / 2.0 s
t = 2 # s
fb = 1 / t

print("6. A piano tuner hears one beat every 2.0 s when trying to adjust two strings,\
      \none of which is sounding 350 Hz. How far off in frequency is the other string?\n")
print(round(fb, 3), " Hz")
print("\n----------------------------------------------------------\n")


# 7. Two automobiles are equipped with the same single-frequency horn.
# When one is at rest and the other is moving toward the first at 18 m/s,
# the driver at rest hears a beat frequency of 4.5 Hz. What is the frequency the horns emit?

vAIR = 343 # m/s
v1 = 0 # m/s
v2 = 18 # m/s
f1 = 1 # Hz
fb = 4.5 # Hz

# f' = f2((vAIR - v1) / (vAIR - v2))
# fb = f2 - f1 = f2((vAIR - v1) / (vAIR - v2)) - f1
# f2 = fb / ((vAIR - v1) / (vAIR - v2))
f2 = fb / ((vAIR - v1) / (vAIR - v2) - f1)

print("7. Two automobiles are equipped with the same single-frequency horn.\
      \nWhen one is at rest and the other is moving toward the first at 18 m/s,\
      \nthe driver at rest hears a beat frequency of 4.5 Hz. What is the frequency the horns emit?\n")
print(round(f2, 3), " Hz")
