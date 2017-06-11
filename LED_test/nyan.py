import badge
import binascii
import time

def hex_to_rgb_tuple(hex_str):
    #r,g,b = map(ord, binascii.unhexlify(hex_str))
    r,g,b = binascii.unhexlify(hex_str)
    return (r,g,b)

white = hex_to_rgb_tuple("ffffff")
yellow = hex_to_rgb_tuple("fffc0b")
green = hex_to_rgb_tuple("5bff0b")
orange = hex_to_rgb_tuple("ffb70b")
red = hex_to_rgb_tuple("ff0b50")
blue = hex_to_rgb_tuple("330bff")

orig_colors = [white, yellow, green, orange, red, blue]

# Thanks to https://stackoverflow.com/questions/28015400/how-to-fade-color for the tip
def lerp(a, b, t):
    return a*(1 - t) + b*t

the_color = red 
colors = orig_colors
next_colors = orig_colors
while True:
    last = next_colors[0]
    next_colors = next_colors[1:]
    next_colors.append(last)
    for _ in range(16):
        new_colors = []
        for i, x in enumerate(colors):
            new_colors.append(tuple(lerp(c, w, 0.25) for c, w in zip(colors[i], next_colors[i])))
        colors = new_colors
        allcolors = ''.join([''.join(["{0:02x}".format(int(x)) for x in [r,g,b,48]]) for (r,g,b) in colors])
        badge.leds_set_state(binascii.unhexlify(allcolors))
        time.sleep(0.1)

