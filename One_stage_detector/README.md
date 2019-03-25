# One Stage Detector


### Pytorch implementation from github

- [YOLOv3](https://github.com/eriklindernoren/PyTorch-YOLOv3.git)
- [YOLOv2](https://github.com/marvis/pytorch-yolo2.git)
- [SSD](https://github.com/amdegroot/ssd.pytorch.git)
- [RetinaNet](https://github.com/kuangliu/pytorch-retinanet.git)


### Compare get from paper

| Network | Detail  | GPU   | FPS    | VOC mAP  | COCO mAP |
| :-----: | :----:  | :---: | :---:  | :------: | :------: |
| YOLOv3 | DarkNet 53, 320x320  |  Titan X   | 45 | - | 51.5 |
| YOLOv3 | DarkNet 53, 416x416  |  Titan X   | 35 | - | 55.3 |
| YOLOv3 | DarkNet 53, 608x608  |  Titan X   | 20 | - | 57.9 |
| YOLOv3 | DarkNet 53, spp(?)  |  Titan X   | 20 | - | 60.6 |
| YOLOv3 | DarkNet tiny  |  Titan X   | 220 | - | 33.1 |
|  |  |  |  |  |
| YOLOv2 | DarkNet 19, 608x608  |  Titan X | 40  | 78.6 | 48.1 |
| YOLOv2 | DarkNet 19, 480x480  |  Titan X | 59  |  77.8 | - |
| YOLOv2 | DarkNet 19, 416x416  |  Titan X | 67  | 76.8 | - |
| YOLOv2 | DarkNet 19, 352x352  |  Titan X | 81  | 73.7 | - |
| YOLOv2 | DarkNet 19, 288x288  |  Titan X | 91  | 69.0 | - |
| YOLOv2 | DarkNet tiny  |  Titan X | 244 | - | 23.7 |
|  |  |  |  |  |
| SSD | SSD 300  |  Titan X   | 46 | 77.2 | 41.2 |
| SSD | SSD 500  |  Titan X   | 19 | 79.8 | 46.5 |
|  |  |  |  |  |
| RetinaNet | ResNet-50-500  |  M40   | 14 | - | 50.9 |
| RetinaNet | ResNet-101-500  |  M40   | 11 | - | 53.1 |
| RetinaNet | ResNet-101-800  |  M40   | 5 | - | 57.5 |


### Compare using GTX-1080

| Network | Detail  | GPU   | FPS    | VOC mAP  | COCO mAP |
| :-----: | :----:  | :---: | :---:  | :------: | :------: |
| YOLOv3 | DarkNet 53, 320x320  |  1080   | 58 | - | 51.5 |
| YOLOv3 | DarkNet 53, 416x416  |  1080   | 49 | - | 55.3 |
| YOLOv3 | DarkNet 53, 608x608  |  1080   | 28 | - | 57.9 |
| YOLOv3 | DarkNet 53, 800x800  |  1080   | 19 | - | - |
| YOLOv3 | DarkNet 53, 1024x1024  |  1080   | 13 | - | - |
| YOLOv3 | DarkNet 53, 1280x1280  |  1080   | 9 | - | - |
| YOLOv3 | DarkNet 53, spp(?)  |  1080   | - | - | 60.6 |
| YOLOv3 | DarkNet tiny  |  1080   | - | - | 33.1 |
|  |  |  |  |  |
| YOLOv2 | DarkNet 19, 352x352  |  1080 | 84  | 73.7 | - |
| YOLOv2 | DarkNet 19, 416x416  |  1080 | 72  | 76.8 | - |
| YOLOv2 | DarkNet 19, 480x480  |  1080 | 62  |  77.8 | - |
| YOLOv2 | DarkNet 19, 608x608  |  1080 | 37  | 78.6 | 48.1 |
| YOLOv2 | DarkNet 19, 800x800  |  1080 | 24  | - | - |
| YOLOv2 | DarkNet 19, 1024x1024  |  1080 | 16  | - | - |
| YOLOv2 | DarkNet 19, 1280x1280  |  1080 | 9  | - | - |
| YOLOv2 | DarkNet tiny  |  1080 | 244 | - | 23.7 |
|  |  |  |  |  |
| SSD | SSD 300  |  1080 | 46 | 77.2 | 41.2 |
| SSD | SSD 500  |  1080 | 19 | 79.8 | 46.5 |
|  |  |  |  |  |
| RetinaNet | ResNet-50-500  |  1080   | 14 | - | 50.9 |
| RetinaNet | ResNet-101-500  |  1080   | 11 | - | 53.1 |
| RetinaNet | ResNet-101-800  |  1080   | 5 | - | 57.5 |
