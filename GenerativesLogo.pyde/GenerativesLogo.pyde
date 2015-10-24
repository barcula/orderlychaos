

size(400, 400)
background(255)

image_names = ["image1.png","image2.png"]
images = []
for path in image_names:
    images.append(loadImage(path))
    print path

npoints = 3 #number of circles an black dots
fleckx = []
flecky = []
a = []#semiaxis ellipses horizontal
b = []#semiaxis ellipses vertical
punktex = []
punktey = []
for i in range(0, npoints):
    c = random(90,130) #size of dabs
    d = random(10,20) #size of dots
    fleckx.append(random(100,300))#range x
    flecky.append(random(100,300))#range y
 
    a.append(random(40, 80))#range width ellipse
    b.append(random(40, 80))#range hight ellipse
    strokeWeight(1.8)
    noFill()
    ellipse(fleckx[i], flecky[i],  2 *a[i], 2 * b[i])
    img = image(images[int(random(0, len(images)))],
                fleckx[i]-c/2, flecky[i]-c/2, c, c)
    punktex.append(random(fleckx[i] - a[i], fleckx[i] + a[i]))

    if (int(random(0, 2)) == 1):
        punktey.append((b[i] ** 2 - (b[i] ** 2 / a[i] ** 2)
                        * (punktex[i] - fleckx[i]) ** 2) ** 0.5 + flecky[i])
    else:
        punktey.append(-(b[i] ** 2 - (b[i] ** 2 / a[i] ** 2)
                         * (punktex[i] - fleckx[i]) ** 2) ** 0.5 + flecky[i])
    fill(0)                        
    ellipse(punktex[i], punktey[i], d, d)
    if (i > 0):
        strokeWeight(3.5) 
        color(250)
        line(punktex[i]-1, punktey[i]-1, punktex[i], punktey[i])
