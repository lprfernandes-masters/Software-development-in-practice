

try:
    print("Trying to do this")
    this_will_throw = 1/2
except:
    print("This only executes in case of error")
finally:
    print("This executes always")
