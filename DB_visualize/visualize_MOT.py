"""
MOT17 dataset annotation visualizing code

MOT17 annotations
Frame number, Identity number, BBox left, BBox top, BBox width, BBox height, Confidence score, Class, Visibility

"""

import os
import cv2


colors = [(55, 132, 192),(15, 99, 173),(175, 114, 137),(74, 214, 196),(234, 58, 140),(106, 216, 210),(218, 152, 15),
          (64, 58, 199),(39, 83, 178),(137, 191, 9),(100, 246, 111),(123, 212, 80),(40, 203, 50),(42, 241, 91),(147, 219, 165),
          (82, 64, 121),(79, 165, 136),(174, 41, 161),(51, 92, 33),(123, 151, 69),(105, 5, 35),(138, 105, 133),(210, 197, 56),
          (37, 229, 235),(48, 220, 241),(202, 134, 185),(254, 228, 239),(4, 236, 194),(145, 81, 142),(194, 41, 150),
          (209, 11, 213),(17, 0, 220),(31, 109, 181),(214, 29, 26),(80, 220, 188),(141, 56, 99),(24, 179, 197),(217, 101, 35),
          (113, 221, 196),(19, 144, 114),(251, 121, 118),(114, 205, 246),(221, 139, 17),(254, 236, 100),(36, 203, 152),
          (143, 92, 134),(17, 104, 44),(252, 189, 139),(200, 132, 239),(129, 4, 185),(10, 163, 41),(233, 110, 111),(148, 145, 122),
          (197, 70, 203),(69, 86, 142),(164, 192, 196),(252, 103, 110),(33, 116, 181),(92, 220, 183),(128, 125, 93),(27, 222, 196),
          (163, 157, 199),(59, 191, 26),(123, 209, 120),(225, 11, 138),(113, 182, 243),(49, 247, 53),(72, 59, 80),(102, 162, 8),
          (33, 248, 76),(152, 22, 91),(71, 8, 23),(181, 57, 180),(225, 221, 210),(65, 161, 41),(169, 236, 33),(73, 95, 88),
          (136, 160, 209),(254, 23, 251),(181, 128, 136),(213, 201, 141),(4, 60, 85),(24, 68, 69),(27, 130, 129),(163, 8, 78),
          (26, 24, 46),(142, 44, 100),(120, 99, 178),(140, 115, 204),(247, 124, 105),(230, 122, 159),(16, 129, 143),(139, 226, 24),
          (56, 8, 149),(109, 12, 78),(73, 59, 231),(51, 113, 146),(253, 128, 125),(35, 15, 146),(174, 149, 48)]


classes = [None, "Pedestrian", "Person on vehicle", "Car", "Bicycle", "Motorbike", "Non motorized vehicle",
           "Static person", "Distractor", "Occluder", "Occluder", "Occluder", "Reflection"]

DB_dir = "./MOT17/MOT17-02-DPM/"

img_dir = DB_dir + "img1/"
label_dir = DB_dir+"gt/gt.txt"

gt_labels = open(label_dir, "r")


# get all annotations from gt.txt
labels = [[]]

for label in gt_labels.readlines():

    frame_number, identity_number, bbox_left, bbox_top, bbox_width, bbox_height, score, _class, visibility = label.split(",")

    frame_number, identity_number, _class = int(frame_number), int(identity_number), int(_class)
    bbox = [int(float(pt)) for pt in [bbox_left, bbox_top, bbox_width, bbox_height]]
    bbox[2] += bbox[0]
    bbox[3] += bbox[1]

    if len(labels) <= frame_number:
        labels.append([])

    labels[frame_number].append({"id":identity_number, "bbox":bbox, "_class":_class})

# draw all annotations for each frame
for frame in range(1, len(labels)):

    cur_image = cv2.imread(img_dir + str(frame).zfill(6) + ".jpg")

    for anno in labels[frame]:

        color = colors[anno["id"]]
        if anno["_class"] > 7:  # remove occluder & distractor
            continue

        cur_image = cv2.rectangle(cur_image, tuple(anno["bbox"][0:2]), tuple(anno["bbox"][2:4]), color, 5)
        cur_image = cv2.putText(cur_image, classes[anno["_class"]], tuple(anno["bbox"][0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cur_image = cv2.resize(cur_image, (1200, 800))  # too big...
    cv2.imshow("frame", cur_image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break