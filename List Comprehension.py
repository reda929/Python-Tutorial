# List comprehension

squares = [x * x for x in range (10)]

# (values) = [(expression) for (value) in (collection)]

# equivalent to:
# (values) = []
# for (value) in (collection):
#     (values).append ((expression))


# equivalent to:
x = []
def x_y (x):
    # process x to something y
    return x + 1


map (x_y, x)