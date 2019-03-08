"""
DETRAC dataset annotation visualizing code

DETRAC annotations xml

"""
import cv2
import xml.etree.ElementTree as ET

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

DB_dir = "./DETRAC/"

folder = "MVI_20011"


# get all annotations from xml

e = ET.parse(DB_dir+folder+".xml")

root = e.getroot()

labels = [[]]
ignored_region = []

for region in root.find("ignored_region"):
    ignored_region.append(region.attrib)


for frame in root.findall("frame"):
    frame_num = int(frame.attrib['num'])
    labels.append([])

    for target in frame.find('target_list'):
        # target.attrib : target id
        # target[0].attrib : bbox info (left, top, width, height)
        # target[1].attrib : object info (orientation, speed, trajectory_length, truncation_ratio, vehicle_type)
        labels[frame_num].append({'id':int(target.attrib['id']),
                                  'bbox':target[0].attrib,
                                  '_class':target[1].attrib['vehicle_type']})


# draw all annotations for each frame
for frame in range(1, len(labels)):

    cur_image = cv2.imread(DB_dir + folder + "/img" + str(frame).zfill(5) + ".jpg")

    # draw ignored region in black
    for ignore in ignored_region:
        ignore_xmin = int(float(ignore['left']))
        ignore_ymin = int(float(ignore['top']))
        ignore_xmax = ignore_xmin + int(float(ignore['width']))
        ignore_ymax = ignore_ymin + int(float(ignore['height']))

        cur_image = cv2.rectangle(cur_image, (ignore_xmin, ignore_ymin), (ignore_xmax, ignore_ymax), 0, -1)

    # draw vehicles
    for anno in labels[frame]:
        color = colors[anno["id"]]

        bbox_xmin = int(float(anno['bbox']['left']))
        bbox_ymin = int(float(anno['bbox']['top']))
        bbox_xmax = bbox_xmin + int(float(anno['bbox']['width']))
        bbox_ymax = bbox_ymin + int(float(anno['bbox']['height']))

        cur_image = cv2.rectangle(cur_image, (bbox_xmin, bbox_ymin), (bbox_xmax, bbox_ymax), color, 5)
        cur_image = cv2.putText(cur_image, anno['_class'], (bbox_xmin, bbox_ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow("frame", cur_image)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
