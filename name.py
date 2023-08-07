import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"mercury",(120,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"venus",(320,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"earth",(420,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"mars",(520,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"juipiter",(620,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"saturn",(720,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"neptune",(820,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))
cv2.putText(img,"uranus",(920,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225))

cv2.imshow("output"img)
cv2.waitKey(0)