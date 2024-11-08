from jwt import decode

from hackathon.security import create_access_token
from hackathon.settings import Settings


def test_jwt():
    settings = Settings()  # type: ignore
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )

    assert decoded['test'] == data['test']
    assert decoded['exp']
