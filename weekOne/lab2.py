#lab2 Ousman Touray
import math
def getCylinderVolume(radius, height):
    cylinderVolume = math.pi * radius**2 * height
    return cylinderVolume;

print("Cylinder Volume: ", getCylinderVolume(3.0, 3.0))
r = 7
h = 5
print("Cylinder Volume with rounding: ", round(getCylinderVolume(r, h)))
print("Cylinder Volume: ", getCylinderVolume(9.0, 16))
print("Cylinder Volume: ", getCylinderVolume(10.0, 16))
print("Cylinder Volume: ", getCylinderVolume(11.0, 32))