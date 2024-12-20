from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from app.main import app
import pytest
from app.database import Base



#We can hardcode our url
DATABASE_URL = f'postgresql://postgres:aysel123@localhost:5432/testdb'

engine = create_engine(DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()


#the client fixture will call session fixture before it runs
@pytest.fixture
def client(session):
    def overrid_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = overrid_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"email": "test123@gmail.com", 
                 "password": "12345", "phone_number": "00"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user