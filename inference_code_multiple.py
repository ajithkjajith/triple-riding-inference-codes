from ultralytics import YOLO

model = YOLO("t")  
results = model.predict(
    source=r"",  # path to your test images folder
    show=True,         # display results in a window 
    save=True,         # save results
    conf=0.25          # confidence threshold (optional - default is 0.25)
)