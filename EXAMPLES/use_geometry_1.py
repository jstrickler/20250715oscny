import sys
import alpha.mathlib.geometry as geometry # find and execute geometry.py

print(f"{geometry.PI = }")

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search order
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin locations (sys.prefix/<LIB>)
print(f"{sys.prefix = }")
print()
for path in sys.path:
    print(path)