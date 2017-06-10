import ugfx
ugfx.init()
# Based on http://0pointer.de/blog/projects/mandelbrot.html
#dimensions = (badge.BADGE_EINK_WIDTH, badge.BADGE_EINK_HEIGHT)
dimensions = (296, 128)
scale = 1.0/(dimensions[0]/3)
center = [2.2, 1.5]       # Use this for Mandelbrot set
#center = (1.5, 1.5)       # Use this for Julia set
iterate_max = 20

# Calculate the mandelbrot sequence for the point c with start value z
def iterate_mandelbrot(c, z = 0):
    for n in range(iterate_max + 1):
        z = z*z +c
        if abs(z) > 2:
            return n
    return None

## Draw our image
for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        c = complex(x * scale - center[0], y * scale - center[1])

        n = iterate_mandelbrot(c)            # Use this for Mandelbrot set
        #n = iterate_mandelbrot(complex(0.3, 0.6), c)  # Use this for Julia set

        if n is None:
            ugfx.pixel(x, y, ugfx.BLACK)
        else:
            ugfx.pixel(x, y, ugfx.WHITE)

ugfx.flush()
