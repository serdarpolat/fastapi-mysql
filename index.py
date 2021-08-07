from fastapi import FastAPI
from routes.index import user, credential, category, sub_category

app = FastAPI()

app.include_router(user)
app.include_router(credential)
app.include_router(category)
app.include_router(sub_category)
