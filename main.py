from fastapi import FastAPI
import model
from config import engine
from router.book_management import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Home/welcome route
@app.get("/")
def read_root():
    return {"greetings": "Welcome to Rapid-learnings."}


app.include_router(router, prefix="/book", tags=["Book"])
