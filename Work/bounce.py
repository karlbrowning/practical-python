# bounce.py
#
# Exercise 1.5

height = 100
bounce = 0

while bounce < 10:
    bounce = bounce + 1
    height = round(height * 0.6, 4)

    print(bounce, height)

