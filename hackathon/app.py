from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from hackathon.routers import auth, users

app = FastAPI()


@app.get(
    '/',
    response_class=RedirectResponse,
    status_code=HTTPStatus.OK,
)
def redirect_docs():
    return '/docs'


app.include_router(users.router)
app.include_router(auth.router)
