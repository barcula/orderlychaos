# Orderly chaos

![](images/analogheader.jpg)





#1. Conceptual formulation

The first exercise in the course **"Eingabe-Ausgabe"** was to device an analogue algorithm.
It needs to be as precise and clear as possible for the people who put it into execution.

### Instructions of first version
( 5 minutes speed exercise)

+ Draw 10 or more circles on a squarish drawing surface
+ A circle have to touch or carve minimum one other circle
+ If there are generated more then 5 intersections hatch them blue
+ If there are generated less then 5 intersections hatch them red

These are the results of the very beginning:

![Imgur](http://i.imgur.com/0SmiFdv.jpg) ![Imgur](http://i.imgur.com/X53sdcI.jpg) ![Imgur](http://i.imgur.com/PfNRfgZ.jpg)
  ![Imgur](http://i.imgur.com/EuHadmv.jpg) ![Imgur](http://i.imgur.com/BDIKPKQ.jpg)
  
  These thing weren`t clear enough and could be understood in different ways:
  
  + Draw 10 or more circles on a squarish drawing surface
  + A => **Every circle** have to touch or carve minimum one other circle
  + If there are generated **overall** more then 5 intersections hatch them => **the intersections** blue
  + If there are generated **overall** less then 5 intersections hatch them => **the intersections** red
  
After the course discussed the results of everyone our task was to improve the algorithm and give it to 10 persons to put it into execution
  
### Instructions of the second version

Materials: white paper, green red and blue coloured felt pen, mix of different pens, ball pens and so on

+ Draw minimum 20 circles in different sizes on the sheet
+ Every circle have to touch or carve minimum one other circle
+ If there are generated more then 10 intersections hatch the intesections blue
+ If there are generated less then 10 intersections hatch the intesections red
+ Mark every point of intersection and osculation point with the green marker
+ Connect every green point with each other.

These are the results of the second version executed by ten different people:

![Imgur](http://i.imgur.com/lBnCcHw.jpg)![Imgur](http://i.imgur.com/19H62sU.jpg)![Imgur](http://i.imgur.com/HDQxzJ3.jpg)
![Imgur](http://i.imgur.com/eQZf0hV.jpg)![Imgur](http://i.imgur.com/B6QbuMV.jpg)![Imgur](http://i.imgur.com/67aGWg9.jpg)
![Imgur](http://i.imgur.com/ejLyWs3.jpg)![Imgur](http://i.imgur.com/b3xsz7x.jpg)![Imgur](http://i.imgur.com/9BthtOA.jpg)
![Imgur](http://i.imgur.com/yPhSqis.jpg)![Imgur](http://i.imgur.com/tDBUnSV.jpg)
  
  
  

### Instructions of the final version


**Materials: 3 different water-colour mix, pen, Setsquare, black felt pen, injection**

0. Write any number on the back of your paper

1. Take the injection and spread the colour with eyes closed drop per drop over the front side of the paper.
 (Min. 10 drops)

2. Let the dabs getting dry

3. Draw an ellipse around every dab whose range isn`t bigger as the range of the pen  Smaller dabs can be inside of an ellipse as well. Every ellipse needs to carve minimum one other ellipse. Ellipses can get over the end of the paper.

4. Mark every point of intersection with the black felt pen 

5. If you had written an even number on the back of your paper follow step **6a**
  Otherwise follow step **6b**

  6a Link all marked points of intersection with the black felt pen 

  6b Retrace every line which you have made before with your pen with the black felt pen.
  
  ![](http://i.imgur.com/1SBEXML.jpg)      ![](http://i.imgur.com/AmDdViQ.jpg)      ![](http://i.imgur.com/za4QzTZ.jpg)  
  ![](http://i.imgur.com/XtKB053.jpg)      ![](http://i.imgur.com/5L7FzwY.jpg)      ![](http://i.imgur.com/k82U9LI.jpg)
  ![](http://i.imgur.com/IaA6GE2.jpg)      ![](http://i.imgur.com/bkrQZuw.jpg)
  ![](http://i.imgur.com/hzGEiDu.jpg)      ![](http://i.imgur.com/LkFyeP2.jpg)
  
  
  
  
  

# Evaluation

I was really satisfied with the results I received. The algorithm was explicated mostly right and looked like the images I had in mind.
I could manage that the images do not all look the same but it is still clear that all the people who put the algorithm into execution had the same task.
![](images/header.jpg)


# Resume

I think it was a very good exercise to practise expressing myself.
It was necessary to think about every single word. *Is this information really needed or can i remove this?
Can this sentence be more short and precise? Would I understand this if i would read the instruction the first time?*
Keep things simple but not boring is one sentence which describes this exercise the best in my eyes.

![](Imagesdigital/headerdigital.jpg)

# 2. Conceptual formulation 

The next step was it to create a digital version of our analogue algorithm. 
We were not forced to do it exactly the same but it should have something to do with our first project.
My aim was it work close to my first exercise to see if I can manage it to tell the program "processing" 
exactly what I want to have and not to work with any random results.

# Development of the projekt

For me it was neccesairy to keep the optical look of paint dabs. 
So I decided to use png-Images of them and make them appear randomly on the white sheet. It was quite a long time for the next step: Put ellipses around every dab in different sizes and forms. But finally it worked.
The last thing I need to do was to mark the intersection points of two or more ellipses with a black dot. At this point I didn`t come forward so I decided to break this idea a little bit down. So I said make exactly one dot at every ellipse and connect these points with black lines. 

![Imgur](http://i.imgur.com/422dkN8.jpg)![Imgur](http://i.imgur.com/0M7uopc.jpg)
![Imgur](http://i.imgur.com/jrTtyg5.jpg)![Imgur](http://i.imgur.com/SDjCsJA.jpg)
#Installation

You need to download processing to put this code into execution
https://processing.org/download/

# Usage
You copy the folder **data** and **Finaldigital** to your desktop and open the file with processing.
I wrote the code in Python so it`s necessary to choose python in the upper right-hand corner and click the run button. 

![Imgur](http://i.imgur.com/mp9Ec2U.png)

#Resumee

I liked this exercise very much and I am quite confident with the results as well
especially because I had no experience with coding before at all. It was really useful to understand the language python and gain a small insight into the huge world of coding. I couldn`t achieve the image I had in mind completely but it comes close to it.

#For what can this code might be used?

For this you can have a look at my repository: **generative-Logo**

#Generative Logo 

After I had a second look at my results I had the idea to use this to generate Logos for a fictional company. For this I needed to reduce my code to bring more clearance in the generated image. Every employee gets his own logo which can be used for example for business cards or other print products. In this way every employee can choose his individual logo by clicking the play button as long as he finds the right one.
Here are some of an endless amount of examples: 



![](imagesgenerative/gl1.png)![](imagesgenerative/gl2.png)![](imagesgenerative/gl3.png)
![](imagesgenerative/gl4.png)![](imagesgenerative/gl5.png)![](imagesgenerative/gl6.png)

#Installation
You need to download processing to put this code into execution https://processing.org/download/

# Usage
You copy the folder **data** and **GenerativesLogo.pyde** to your desktop and open the file with processing.
I wrote this code in Python so it`s necessary to choose python in the upper right-hand corner and click the run button.

 

