from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(

    title="Enterprise AI Platform",

    version="1.0.0",

    description="AI Workflow Navigator powered by Local LLM"

)

app.include_router(

    router,

    prefix="/api",

    tags=["Workflow AI"]

)