

size(500, 800)
background(255)

image_names = ["image1.png","image2.png"]
images = []
for path in image_names:
    images.append(loadImage(path))
    print path

npoints = 20 #Anzahl der Flecken und Kreise
fleckx = []
flecky = []
a = []#halbachsen ellipsen horizontal
b = []#halbachsen ellipsen vertikal
punktex = []
punktey = []
for i in range(0, npoints):
    c = random(50,70)
    d = random(15,23)
    fleckx.append(random(width))
    flecky.append(random(height))
 
    a.append(random(40, 50))
    b.append(random(40, 50))
    strokeWeight(0.2)
    noFill()
    ellipse(fleckx[i], flecky[i], 2 * a[i], 2 * b[i])
    img = image(images[int(random(0, len(images)))],
                fleckx[i], flecky[i], c, c)
    punktex.append(random(fleckx[i] - a[i], fleckx[i] + a[i]))
    # punktex.append(fleckx[i])
    # punktey.append(flecky[i]+b[i])v
    if (int(random(0, 2)) == 1):
        punktey.append((b[i] ** 2 - (b[i] ** 2 / a[i] ** 2)
                        * (punktex[i] - fleckx[i]) ** 2) ** 0.5 + flecky[i])
    else:
        punktey.append(-(b[i] ** 2 - (b[i] ** 2 / a[i] ** 2)
                         * (punktex[i] - fleckx[i]) ** 2) ** 0.5 + flecky[i])
    fill(random(0))                        
    ellipse(punktex[i], punktey[i], d, d)
    if (i > 0):
        strokeWeight(1.5) 
        color(250)
        line(punktex[i-1], punktey[i-1 ], punktex[i], punktey[i])
    #print img
  #  sleep(1.0)
    #pause
#    ellipse(punktex[i],punktey[i],10,10)
# for i in range(0, npoints):
#     for j in range(0, npoints):
#         if (i != j and abs(fleckx[i] - fleckx[j]) >= 0.5*a[i] and abs(flecky[i] - flecky[j]) >= 0.5*b[j] and
#                 abs(fleckx[i] - fleckx[j]) <= 2*a[i] and abs(flecky[i] - flecky[j]) <= 2*b[j]):
#             xn1 = fleckx[i]  - a[i]
#             yn1 = flecky[i]
#             xn2 = fleckx[i]  + a[i]
#             yn2 = flecky[i]
#             for k in range(0, 200):
#                 A1 = (2 * xn1 - 2 * (fleckx[i] )) / a[i] ** 2
#                 B1 = (2 * yn1 - 2 * (flecky[i] )) / b[i] ** 2
#                 C1 = (2 * xn1 - 2 * (fleckx[j] )) / a[j] ** 2
#                 D1 = (2 * yn1 - 2 * (flecky[j] )) / b[j] ** 2
#                 A2 = (2 * xn2 - 2 * (fleckx[i] )) / a[i] ** 2
#                 B2 = (2 * yn2 - 2 * (flecky[i] )) / b[i] ** 2
#                 C2 = (2 * xn2 - 2 * (fleckx[j] )) / a[j] ** 2
#                 D2 = (2 * yn2 - 2 * (flecky[j] )) / b[j] ** 2
#                 f11 = -(xn1 - (fleckx[i] )) ** 2 / a[i] ** 2 - \
#                     (yn1 - (flecky[i] )) ** 2 / b[i] ** 2 + 1
#                 f21 = -(xn1 - (fleckx[j] )) ** 2 / a[j] ** 2 - \
#                     (yn1 - (flecky[j] )) ** 2 / b[j] ** 2 + 1
#                 f12 = -(xn2 - (fleckx[i] )) ** 2 / a[i] ** 2 - \
#                     (yn2 - (flecky[i] )) ** 2 / b[i] ** 2 + 1
#                 f22 = -(xn2 - (fleckx[j] )) ** 2 / a[j] ** 2 - \
#                     (yn2 - (flecky[j] )) ** 2 / b[j] ** 2 + 1
#                 deltax1 = (f11 * D1 - f21 * B1) / (A1 * D1 - B1 * C1)
#                 deltay1 = (A1 * f21 - f11 * C1) / (A1 * D1 - B1 * C1)
#                 deltax2 = (f12 * D2 - f22 * B2) / (A2 * D2 - B2 * C2)
#                 deltay2 = (A2 * f22 - f12 * C2) / (A2 * D2 - B2 * C2)
#                 xn1 = deltax1 + xn1
#                 yn1 = deltay1 + yn1
#                 xn2 = deltax2 + xn2
#                 yn2 = deltay2 + yn2
#             punktex.append(xn1)
#             punktey.append(yn1)
#             punktex.append(xn2)
#             punktey.append(yn2)

# for i in range(0,len(punktex)):
#     ellipse(punktex[i],punktey[i],10,10)
#     for i in range(0,len(punktex)-1):
#         line(punktex[i],punktey[i],punktex[i+1],punktey[i+1])

