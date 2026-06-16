from fastapi import FastAPI 
import uvicorn
from migrate.migrations import migrate
from dotenv import load_dotenv
import os 


load_dotenv()

if os.getenv("ENVIRONMENT") == "production":
    print("[+] migration started")
    migrate()
    

app = FastAPI()


@app.get("/")
def root():
    return {"status":"active"}



if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


