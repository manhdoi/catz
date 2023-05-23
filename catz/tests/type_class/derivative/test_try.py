from unittest import TestCase, mock
from catz.type_class.derivative.failure import exception_handling, Success, Error


class TestTry(TestCase):
    def test_exception_handling(self):
        success_mock = mock.Mock()
        success_mock.return_value = "hello world"

        exception_mock = mock.Mock()
        exception_mock.side_effect = Exception("File Not Found")

        @exception_handling
        def success() -> str:
            return success_mock()

        @exception_handling
        def error() -> str:
            return exception_mock()

        self.assertEqual(success(), Success("hello world"))
        self.assertIsInstance(error(), Error)
