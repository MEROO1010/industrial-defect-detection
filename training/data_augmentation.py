from ultralytics.data.augment import Augmenter

def augment_data():
    augmenter = Augmenter(
        hflip=0.5,
        vflip=0.5,
        rotate=0.2,
        scale=0.1,
        mosaic=0.5
    )
    return augmenter