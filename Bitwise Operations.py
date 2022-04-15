x = 10  # (0000 1010 in binary)
y = 4  # (0000 0100 in binary)


# bin (num) prints binary form
# for i in range (10):
#     print ('{:08d}'.format(int(bin (i)[2:])))  # 33

# back to decimal form
# str = '100101010'
# print (int (str, 2))


def print_xy (text):
    print ('x: {}'.format(x))
    print ('y: {}'.format (y))
    print(text)
    print()


# if x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
# print_xy(x & y)
# print_xy (x | y)
# print_xy (~x)
# print_xy (x ^ y)
# print_xy (x >> 2)  # = 2 (0000 0010)
# print_xy (x << 2)  # = 40 (0010 1000)
# print_xy (x &= 5)  #	x = x & 5
# print_xy (x |= 5)  #	x = x | 5
# print_xy (x ^= 5)  #	x = x ^ 5
# print_xy (x >>= 5) #
# print_xy (x <<= 5)  #
# x & y = 0 (0000 0000)
# x | y = 14 (0000 1110)
# ~x = -11 (1111 0101)
# x ^ y = 14 (0000 1110)
# x >> 2 = 2 (0000 0010)
# x << 2 = 40 (0010 1000)
# x &= 5	x = x & 5
# x |= 5	x = x | 5
# x ^= 5	x = x ^ 5
# x >>= 5	x = x >> 5
# x <<= 5	x = x << 5.

# To hex string. Note that you don't need to use x8 bits.
# print "0x%x" % int('11111111', 2)
# 0xff
# print "0x%x" % int('0110110110', 2)
# 0x1b6
# print "0x%x" % int('0010101110101100111010101101010111110101010101', 2)
# 0xaeb3ab57d55

# To character. 8 bits max.
# chr(int('111011', 2))
# ';'
# chr(int('1110110', 2))
# 'v'
# chr(int('11101101', 2))
# '\xed'
# Characters to integers, but not to strings of 1's and 0's.
#
#
# Toggle line numbers
#    1 >>> int('01110101', 2)
#    2 117
#    3 >>> chr(int('01110101', 2))
#    4 'u'
#    5 >>> ord('u')
#    6 117
# Individual bits.
#
#
# Toggle line numbers
#    1 >>> 1 << 0
#    2 1
#    3 >>> 1 << 1
#    4 2
#    5 >>> 1 << 2
#    6 4
#    7 >>> 1 << 3
#    8 8
#    9 >>> 1 << 4
#   10 16
#   11 >>> 1 << 5
#   12 32
#   13 >>> 1 << 6
#   14 64
#   15 >>> 1 << 7
#   16 128
#
#   x << y
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
# x >> y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
# x & y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
# Just remember about that infinite series of 1 bits in a negative number, and these should all make sense.
#
# Other/


# char to bin:
print ('char to bin ', ord ('m'))  # 109
# bin to char:
print ('bin to char ', chr (109))  # m
print()

# int to bin
print ('int to bin ', bin (109))  # '0b1101101'
# bin to int
print ('bin to int ', int ('1101101', 2)) # 109
print ()

# int to hex
print ('int to hex ', hex (109))  # '0x6d'
# hex to int
print ('hex to int ', int ('0x6d', 16))  # 109
print ()