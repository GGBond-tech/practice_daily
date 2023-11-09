import cv2

newin = cv2.namedWindow('video', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('new', 600, 400)
# cv2.imshow(newin, 0)


# while True:
#   key = cv2.waitKey(0)
#   print(key)
#   if( key& 0xff ==ord('q')):
#     print(123546)
#     # cv2.destroyAllWindows()
#     break

cap = cv2.VideoCapture("VID_20221103_205733.mp4")
while True:
  ret, frame = cap.read()
  cv2.imshow('video', frame)
  key = cv2.waitKey(24)
  if( key& 0xff ==ord('q')):
    break

cap.release()
cv2.destroyAllWindows()


# cv2.destroyAllWindows()