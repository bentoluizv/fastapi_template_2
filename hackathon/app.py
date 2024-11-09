from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get(
    '/hackathon',
    response_class=RedirectResponse,
    status_code=HTTPStatus.OK,
)
def redirect_docs():
    return '/docs'
