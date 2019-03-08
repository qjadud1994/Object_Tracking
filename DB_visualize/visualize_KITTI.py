"""
KITTI dataset annotation visualizing code

KITTI annotations
frame(1), track id(1), type(1), truncated(1), occluded(1), alpha(1), bbox(4), dimensions(3), location(3), rotation_y(1), score(1)

"""

import os
import cv2

DB_dir = "./KITTI/"

folder = "0000"

gt_labels = open(DB_dir+folder+".txt", "r")

prev_frame = -1
cur_image = None
colors = [(0,0,255), (0,255,0), (255,0,0), (255,255,0), (255,0,255), (0,255,255),
          (128,0,0), (0,128,0), (0,0,128), (128,128,0), (128,0,128), (0,128,128),
          (64,0,0), (0,64,0), (0,0,64), (64,64,0), (64,0,64), (0,64,64)]

for label in gt_labels.readlines():

    frame, track_id, _type, truncated, occluded, alpha, bbox_left, bbox_right, bbox_top, bbox_bottom, *others = label.split(" ")

    frame, track_id = int(frame), int(track_id)
    bbox = [int(float(pt)) for pt in [bbox_left, bbox_right, bbox_top, bbox_bottom]]

    if prev_frame is not frame:
        if cur_image is not None:
            cv2.imshow("frame", cur_image)
            if cv2.waitKey(100) & 0xFF==ord('q'):
                break

        prev_frame = frame
        cur_image = cv2.imread(DB_dir+folder+"/"+str(frame).zfill(6)+".png")

    color = colors[track_id]
    if track_id is -1:  # DontCare -> ignore
        continue

    cur_image = cv2.rectangle(cur_image, tuple(bbox[0:2]), tuple(bbox[2:4]), color, 5)
    cur_image = cv2.putText(cur_image, _type+"_"+str(track_id), tuple(bbox[0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)