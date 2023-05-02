from unittest import TestCase
from src.utils.validation import Validation


class TestValidation(TestCase):
    def test_validate_create_user_no_data(self):
        body = []
        result = Validation.validate_user(body)
        self.assertEqual(len(result), 1)
        expected = {
            "status": 400,
            "title": "Bad Request",
            "detail": "Post Record should Follow the JSONApi Standard and put the info inside a \"data\" object",
            "meta": {
                "json_api_link": "https://jsonapi.org/format/#crud-creating"
            }
        }
        self.assertEqual(result[0], expected)

    def test_validate_no_user(self):
        body = {"data": {"password": "fake"}}
        result = Validation.validate_user(body)
        self.assertEqual(len(result), 1)
        expected = {
            "status": 400,
            "title": "Bad Request",
            "detail": "Field \"username\" must be provided"
        }
        self.assertEqual(result[0], expected)

    def test_validata_no_password(self):
        body = {"data": {"username": "fake"}}
        result = Validation.validate_user(body)
        self.assertEqual(len(result), 1)
        expected = {
            "status": 400,
            "title": "Bad Request",
            "detail": "Field \"Password\" must be provided"
        }
        self.assertEqual(result[0], expected)

    def test_validate_no_errors(self):
        body = {
            "data": {
                "username": "fake",
                "password": "fake"
            }
        }
        result = Validation.validate_user(body)
        self.assertEqual(len(result), 0)

    def test_validated_no_user_nor_password(self):
        body = {'data': {}}
        result = Validation.validate_user(body)
        expected = [
            {
                "status": 400,
                "title": "Bad Request",
                "detail": "Field \"username\" must be provided"
            },
            {
                "status": 400,
                "title": "Bad Request",
                "detail": "Field \"Password\" must be provided"
            }
        ]
        self.assertEqual(result, expected)
