

size(500, 800)
background(255)
image_names = ["image1.png","image2.png"]
images = []
for path in image_names:
    images.append(loadImage(path))
    print path
npoints = 20 #Number of dabs
fleckx = []  # position der ellipsen horizontal
flecky = []  # position der ellipsen vertikal
a = []#semiaxis  ellipses horizontal
b = []#semiaxis  ellipses vertikal
punktex = []  # position of black dots horizontal
punktey = []  # position of black dots vertikal
for i in range(0, npoints):
    #  distance "c" from the center of the ellipse blue dabs are drawn
    c = random(50,70)
    # size "d" of black dots
    d = random(15,23)

    # horizontal position of ellipse 
    fleckx.append(random(width))
    # vertical position of ellipse 
    flecky.append(random(height))
 
    # horizontal semiaxis of ellipses 
    a.append(random(40, 50))
    # vertical semiaxis of ellipses 
    b.append(random(40, 50))

    strokeWeight(0.2)
    noFill()
    # ellipse are drawn
    ellipse(fleckx[i], flecky[i], 2 * a[i], 2 * b[i])

    # choose of images.Blue dabs are drawn concerning to the center of the ellipse 
    img = image(images[int(random(0, len(images)))],
                fleckx[i], flecky[i], c, c)
    
    # position of black dots horizontal,
    # range between ellipseposition fleckx - ellipsewidth a unto ellipseposition fleckx + ellipsewidth a
    punktex.append(random(fleckx[i] - a[i], fleckx[i] + a[i]))
    
    # if question ; wich of two posibilities is choosen for black dots
    # y is asigned to mathematical value of x 
    # y is the result from x^2/a^2 + y^2/b^2 = 1
   
    if (int(random(0, 2)) == 1):
        punktey.append((b[i] ** 2 - (b[i] ** 2 / a[i] ** 2)
                        * (punktex[i] - fleckx[i]) ** 2) ** 0.5 + flecky[i])
    else:
        punktey.append(-(b[i] ** 2 - (b[i] ** 2 / a[i] ** 2)
                         * (punktex[i] - fleckx[i]) ** 2) ** 0.5 + flecky[i])
    # hier werden die schwarzen flecken gemalt 
    fill(random(0))                        
    ellipse(punktex[i], punktey[i], d, d)

    #black dots are connected with a line
    if (i > 0):
        strokeWeight(1.5) 
        color(250)
        line(punktex[i-1], punktey[i-1 ], punktex[i], punktey[i])
