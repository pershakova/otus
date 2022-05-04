from fastapi import FastAPI
import uvicorn

PORT = 8000

app = FastAPI()

@app.get('/health')
async def health():
    return {'status': 'OK'}

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=PORT)