import cv2
import os

import PIL
import image
import os.path
from PIL import Image

def makevideo(image_folder):
    
    #image_folder = str(unsplash.main())
    for file in os.listdir(image_folder):
        f_img = os.path.join(image_folder, file)
        
        img = Image.open(f_img)
        img = img.resize((2296,1724))
        img.save(f_img)
        print('image saved')


    video_name = file+'-video.avi'
    each_image_duration = 1 # in secs
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # define the video codec

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")or img.endswith('.png') ]
    print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

    for image in images:
        for _ in range(each_image_duration):
            print(image)
            video.write(cv2.imread(os.path.join(image_folder, image)))

    
    video.release()
    cv2.destroyAllWindows()

#makevideo("images/sea")