# One Stage Detector


### Pytorch implementation from github

[YOLOv3](https://github.com/eriklindernoren/PyTorch-YOLOv3.git)

[YOLOv2](https://github.com/marvis/pytorch-yolo2.git)

[SSD](https://github.com/amdegroot/ssd.pytorch.git)

[RetinaNet](https://github.com/kuangliu/pytorch-retinanet.git)


### Compare

| Network | Detail  | GPU   | FPS    | VOC mAP  | COCO mAP |
| :-----: | :----:  | :---: | :---:  | :------: | :------: |
| YOLOv3 | ResNet 101  |  Titan X   | 53 | - | - |
| YOLOv3 | ResNet 152  |  Titan X   | 37 | - | - |
| YOLOv3 | DarkNet 53  |  1080ti   | 76 | - | - |
| YOLOv2 | DarkNet 19  |  -   | - | - | - |
| YOLOv2 | DarkNet tiny  |  -   | - | - | - |
| SSD | SSD 300  |  1060   | 46 | 77.2 | - |
| SSD | SSD 500  |  Titan X   | 19 | 79.8 | - |
| RetinaNet | ResNet-50-500  |  M40   | 14 | - | 32.5 |
| RetinaNet | ResNet-101-500  |  M40   | 11 | - | 34.4 |
| RetinaNet | ResNet-101-800  |  M40   | 5 | - | 37.8 |
