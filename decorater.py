def add_cookies(choco):
    def add_on(*args, **kwargs):
        print(f"you have addded {args} {kwargs}")
        choco(*args, **kwargs)
    return add_on
def add_spoon(choco):
    def spoon(*args, **kwargs):
        print(f"spoon is added {args} {kwargs}")
        choco(*args, **kwargs)
    return spoon

@add_cookies
@add_spoon
def get_icecream(flavour, toppins):
    print(f"here is your {flavour} ice cream with {toppins}")
get_icecream("vanilla", toppins="chip")