from hackathon.models import User


def test_database_session(session):
    user = User(
        username='bentoluizv',
        password='supersecretpwd',
        email='bentoluizv@gmail.com',
    )

    session.add(user)
    session.commit()
    user_from_db = session.get(User, user.id)

    assert user_from_db
    assert user_from_db.created_at
