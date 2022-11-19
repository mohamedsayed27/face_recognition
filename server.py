from fastapi import FastAPI
import uvicorn
from face_util import compare_faces
from urllib.request import urlopen

app = FastAPI()


@app.get('/index')
def hellow_world(name: str):
    return f"hellow {name}"


@app.post('/api/recognition/')
def recognition(f1: str, f2: str):
    res1 = urlopen(f1)
    res2 = urlopen(f2)
    x = compare_faces(res1, res2)
    return x


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
