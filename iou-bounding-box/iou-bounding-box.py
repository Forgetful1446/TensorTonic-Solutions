def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    box = [x1, y1, x2, y2]
    """

    # Intersection coordinates
    inter_x1 = max(box_a[0], box_b[0])
    inter_y1 = max(box_a[1], box_b[1])
    inter_x2 = min(box_a[2], box_b[2])
    inter_y2 = min(box_a[3], box_b[3])

    # Compute width & height
    inter_width = max(0, inter_x2 - inter_x1)
    inter_height = max(0, inter_y2 - inter_y1)

    inter_area = inter_width * inter_height

    # Areas of boxes
    box_a_area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    box_b_area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    # IoU
    return inter_area / (box_a_area + box_b_area - inter_area)