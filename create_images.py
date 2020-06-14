# Python code for Julia Fractal --adopted from online source,main difference is in varying hyper parameters 
#and creating multiple fractal images
from PIL import Image 

# driver function 
if __name__ == "__main__": 
    
    # setting the width, height and zoom 
    # of the image to be created 
    w, h, zoom = 1080,1080,1

    # creating the new image in RGB mode 
    bitmap = Image.new("RGB", (w, h), "white") 

    # Allocating the storage for the image and 
    # loading the pixel data. 
    pix = bitmap.load() 

    # setting up the variables according to 
    # the equation to create the fractal 
    cX, cY = -0.7, 0.22222
    moveX, moveY = 0.0, 0.0
    maxIter = 800
    k = 0
    n = 500
    
    while(k<n):
        cY = 0.2 + 0.002*k
        cX = -0.7
        for x in range(w): 
            for y in range(h): 
                zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
                zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY 
                i = maxIter 
                while zx*zx + zy*zy < 4 and i > 1: 
                    tmp = zx*zx - zy*zy + cX 
                    zy,zx = 2.0*zx*zy + cY, tmp 
                    i -= 1

                # convert byte to RGB (3 bytes), kinda 
                # magic to get nice colors 
                pix[x,y] = (i << 21) + (i << 10) + i*8

        # to display the created fractal 
        im1 = bitmap.save("fractal%s.jpg"%k,) 
        print("image_saved")
        k = k + 1
