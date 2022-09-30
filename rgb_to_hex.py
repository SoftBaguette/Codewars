'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

def rgb(r, g, b):
    if r < 0: r = 0
    elif r > 255: r = 255

    if g < 0: g = 0
    elif g > 255: g = 255

    if b < 0: b = 0
    elif b > 255: b = 255
    
    if r >= 16: r = str(hex(r).split('x')[-1]).upper()
    else: r = '0' + str(hex(r).split('x')[-1]).upper()
    
    if g >= 16: g = str(hex(g).split('x')[-1]).upper()
    else: g = '0' + str(hex(g).split('x')[-1]).upper()

    if b >= 16: b = str(hex(b).split('x')[-1]).upper()
    else: b = '0' + str(hex(b).split('x')[-1]).upper()

    return (r+g+b)

print(rgb(0,0,0))
print(rgb(1,2,3))
print(rgb(255,255,255))
print(rgb(-20,255,255))
print(rgb(456,255,255))