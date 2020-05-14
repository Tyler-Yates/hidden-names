import mongomock
import pytest

from application.data.dao import TEXT_FIELD, ApplicationDao


@pytest.fixture
def application_dao() -> ApplicationDao:
    # Code that will run before your test, for example:
    database = mongomock.MongoClient().db
    return ApplicationDao(database)


def test_insert_document(application_dao: ApplicationDao):
    text = "text123"
    result = application_dao.insert_document(text)
    inserted_document = application_dao.get_document(result.inserted_id)

    assert text == inserted_document[TEXT_FIELD]
