from PIL import Image, ImageColor

p = 255

resolution_x=1200
resolution_y=1000

center_x =-0.75
center_y = 0.1
zoom=500

def pixel_to_complex(x,y):
    return complex((x-resolution_x/2)/zoom+center_x,(y-resolution_y/2)/zoom+center_y)

def plot_pixel(x,y):
    z = pixel_to_complex(x,y)
    color = mandelbrot(z)
    im.putpixel((x,y), (color,))

def mandelbrot(c):
    z=0
    for i in range(p):
        z=z**2+c
        if abs(z) > 2:
            return i
    return p

im = Image.new('L', (resolution_x,resolution_y))
for x in range(resolution_x):
    for y in range(resolution_y):
        plot_pixel(x,y)
#im.show()
im.save('mandelbrot.png')



