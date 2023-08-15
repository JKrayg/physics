# unit 1
import math

# 1. A small fly of mass 0.22 g is caught in a spider’s web.
# The web oscillates predominantly with a frequency of 4.0 Hz.
# (a) What is the value of the effective spring stiffness constant k for the web?
# (b) At what frequency would you expect the web to oscillate if an insect of mass
#     0.44 g were trapped? 

# (a)
massA = 2.2e-4 # kg
f = 4 # Hz
k = 4 * (math.pi**2) * f**2 * massA # N/m, spring stiffness constant k

# (b)
massB = 4.4e-4 # kg
f = (1 / (2 * math.pi)) * math.sqrt(k / massB) #Hz

print("1. A small fly of mass 0.22 g is caught in a spider’s web.\
      \nThe web oscillates predominantly with a frequency of 4.0 Hz.\
      \n\n(a) What is the value of the effective spring stiffness constant k for the web?\
      \n(b) At what frequency would you expect the web to oscillate if an insect of mass\
      \n    0.44 g were trapped?\n")
print("a: ", round(k, 3), " N/m")
print("b: ", round(f, 3), " Hz")
print("\n----------------------------------------------------------\n")


# 2. It takes a force of 91.0 N to compress the spring of a toy popgun
# 0.175 m to load a 0.160-kg ball.
# With what speed will the ball leave the gun if fired horizontally?

F = 91.0 # N
x = 0.175 # m
m = 0.160 # kg
a = F / m # m/s^2
k = ((a / x) * m) # N
v = math.sqrt((k * x**2) / m) # m/s


print("2. It takes a force of 91.0 N to compress the spring of a toy popgun\
      \n0.175 m to load a 0.160-kg ball.\
      \n\nWith what speed will the ball leave the gun if fired horizontally?\n")
print(round(v, 3), " m/s")
print("\n----------------------------------------------------------\n")


# 3. What is the period of a simple pendulum 47 cm long
# (a) on the Earth, and (b) when it is in a freely falling elevator?

l = 0.47 # m
gE = 9.8 # m/s^2
gFF = 0 # m/s^2

# (a)
Tearth = 2 * math.pi * math.sqrt(l / gE) # s, period on earth

# (b)
# Tfreefall = 2 * math.pi * math.sqrt(1 / gFF) # s, period in free fall, undefined

print("3. What is the period of a simple pendulum 47 cm long\
      \n(a) on the Earth, and (b) when it is in a freely falling elevator?\n")
print("on earth: ", round(Tearth, 3), " s")
print("\n----------------------------------------------------------\n")

# 4. A sound wave in air has a frequency of 282 Hz and travels with a speed of 343 m/s.
# How far apart are the wave crests (compressions)?

f = 282 # Hz
v = 343 # m/s
lam = v / f # m, wavelength

print("4. A sound wave in air has a frequency of 282 Hz and travels with a speed of 343 m/s.\
      \nHow far apart are the wave crests (compressions)?\n")
print(round(lam, 3), " m")
print("\n----------------------------------------------------------\n")

# 5. Two children are sending signals along a cord of total mass 0.50 kg tied between
# tin cans with a tension of 35 N. It takes the vibrations in the string 0.55 s to
# go from one child to the other. How far apart are the children?

m = 0.5 # kg
T = 35 # N, Tension
t = 0.55 # s

# mu = m / L
# v = L / t = sqrt(T / mu)
#   =>  L = (T * t^2) / m

L = (T * t**2) / m


print("5. Two children are sending signals along a cord of total mass 0.50 kg tied between\
      \ntin cans with a tension of 35 N. It takes the vibrations in the string 0.55 s to\
      \ngo from one child to the other. How far apart are the children?\n")
print(round(L, 3), " m")
print("\n----------------------------------------------------------\n")

# 6. If two successive overtones of a vibrating string are 280 Hz and 350 Hz,
# what is the frequency of the fundamental?

f1 = 280 # Hz
f2 = 350 # Hz
fb = f2 - f1 # Hz, frequency of the fundamental

print("6. If two successive overtones of a vibrating string are 280 Hz and 350 Hz,\
      \nwhat is the frequency of the fundamental?\n")
print(fb, " Hz")
print("\n----------------------------------------------------------\n")