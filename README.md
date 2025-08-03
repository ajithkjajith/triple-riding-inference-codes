# Triple riding real time detection

## Detection model trained using YOLO V8 with ~8000 images
## Model training results are in training-details folder

## Detection classes/labels
    {0: 'MORE_THAN_TWO_PERSONS',
    1: 'USING_MOBILE',
    2: 'WITHOUT_HELMET',
    3: 'WITH_HELMET',
    4: 'normal'}

# Mode of running 

1. Install latest python version (or preferably python - 3.10.11)
2. Install dependency
``` pip install -r requirements.txt ```

# To Run provide the best model and images path

3. Run the code for single image inference
## provide the best.pt model path to run
## provide the image path to run
``` python3 inference_code.py ```

4. Run the code for more than one images
## provide the best.pt model path to run
## provide the folder where multiple images are present
``` python3 inference_code_multiple.py ```