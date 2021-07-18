import uvicorn
API_HOST_IP = '0.0.0.0'
API_HOST_PORT = 8000


if __name__ == "__main__":
    uvicorn.run("main:app", host=API_HOST_IP, port=API_HOST_PORT, reload=True)
