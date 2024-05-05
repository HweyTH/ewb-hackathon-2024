from ultralytics import YOLO
import cv2

def obj_dec(target: list) -> list:
    cam = cv2.VideoCapture(0) # change number to different values to use different cameras

    for i in range(3):
        ret, img = cam.read()
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)

    model = YOLO("yolov8n.pt")
    obj_list = []

    res = model.predict(img)

        
    if res[0].boxes:
        #res[0].show() # for debug to see what are the actual object names
        for box in res[0].boxes:
            class_id = int(box.cls)
            object_name = model.names[class_id]
            if object_name in target:
                obj_list.append(object_name)

    return obj_list

if __name__ == "__main__":
    print(obj_dec(["person", "cell phone"]))