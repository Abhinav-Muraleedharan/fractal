#this code is to generate videos from already generated fractal images.
import cv2
import os

image_folder = 'fractal_images_2'
video_name = 'video2.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort(key=natural_keys)

frame = cv2.imread(os.path.join(image_folder,images[0]))
height, width, layers = frame.shape

# video = cv2.VideoWriter(video_name, 0, 1, (width,height))
video = cv2.VideoWriter('fractal2.mp4',cv2.VideoWriter_fourcc('D','I','V','X'), 10, (width,height))
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
