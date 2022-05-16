from fastapi import FastAPI
from api import posts, users
from core.config import settings



app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    terms_of_service=settings.TERMS_OF_SERVICE,
    contact=settings.CONTACT,
    license_info=settings.LICENCE_INFO,
)

app.include_router(posts.router, tags=["Posts"])
app.include_router(users.router, tags=["Users"])
