from datetime import date
from cv2 import cv2
import os, glob 
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
 
font = ImageFont.truetype('arial.ttf', 60)
fps = 1 # frames per second
releaseDate = datetime(2022, 5, 13)
currentDate = datetime.now()
timeDiff = releaseDate - currentDate

#cleanup old files

if os.path.exists('countdownvideo.mp4'):
  os.remove('countdownvideo.mp4')
for oldfile in glob.glob('images/img*.png'):
    os.remove(oldfile)

#create images with decreasing timestamp strings
for x in range (10):
    img = Image.new('RGB', (1280, 720), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    #result of timeDiff operation is datetime.timedelta object, still has microseconds.  the .split lops them off 
    d.text((500,100), "Countdown", fill=(0,0,0), font=font)
    d.text((450,200), (str(timeDiff - timedelta(seconds=x)).split(".")[0]), fill=(0,0,0), font=font)
    img.save('images/img'+str(x)+'.png')

images = [img for img in os.listdir('images') if img.endswith(".png")]
frame = cv2.imread(os.path.join('images', images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc('X', '2', '6', '4')
video = cv2.VideoWriter('countdownvideo.mp4', fourcc, fps, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join('images', image)))

cv2.destroyAllWindows()
video.release()