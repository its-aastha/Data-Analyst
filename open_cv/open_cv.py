#day 7 
import cv2
video = cv2.VideoCapture(0)

i = 1
#r = photo click
#q = quite

while(True):
    ret,frame = video.read() #if fps = 32 then it store the 32 image at tat time
    cv2.imshow('frame',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):                      #when you click q it quite the screen
        break
    elif key == ord('r'):                      #when you click the r then it store the image
        filename = 'myimg_{}.jpg'.format(i)
        cv2.imwrite(filename, frame)
        print(f"{filename} saved successfully !")
        i = i+1 
        continue
    
video.release()
cv2.destroyAllWindows()
    

