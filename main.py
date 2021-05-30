from fastapi import FastAPI , UploadFile , File
from Model.predict import predict  

app = FastAPI()


@app.post("/")
def home(photo: UploadFile = File(...)):
    with open("test_image.png","wb") as fp:
        fp.write(photo.file.read())

    prediction = predict()

    return prediction