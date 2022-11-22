from fastapi import FastAPI
import uvicorn
from face_util import compare_faces

app = FastAPI()


@app.get('/api/recognition/')
def recognition(photo: str,url: str):
    x = compare_faces(photo,url)
    return x


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')