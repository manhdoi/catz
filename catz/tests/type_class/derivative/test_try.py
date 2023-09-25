from functools import reduce
from unittest import TestCase, mock
from catz.type_class.derivative.failure import exception_handling, Success, Error, Try


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
        self.assertEqual(Try.ret(10).fmap(lambda x: x + 1), Success(11))

    def test_exception_handling_without_return(self):
        exception_mock = mock.Mock()
        exception_mock.side_effect = Exception("File Not Found")

        @exception_handling
        def success():
            print("Hello, world!")

        @exception_handling
        def error() -> str:
            return exception_mock()

        self.assertEqual(success(), Success(None))
        self.assertIsInstance(error(), Error)

    def test_try_without_return(self):
        exception_mock = mock.Mock()
        exception_mock.side_effect = Exception("File Not Found")

        def void_function():
            print("Hello, world!")

        def error_function():
            return exception_mock()

        print("1")
        self.assertEqual(Try.ret(void_function()).bind(lambda _: Try.ret(void_function())), Success(None))

        print("2")
        self.assertIsInstance(exception_handling(error_function)(), Error)

        print("3")
        self.assertIsInstance(
            Try(void_function)().bind(lambda _: Try(error_function)()).bind(lambda _: Try(void_function)()), Error)

    def test_reduce(self):
        a = [1, 2, 3, 4, 5]

        def hello():
            print("Hello, world!")

        result = reduce(lambda r, x: r.bind(lambda _: Try(hello)()), a, Try.ret(None))
        self.assertIsInstance(result, Success)

    def test_do(self):
        def void_function():
            print("Hello, world!")

        def ret_func():
            return 1

        def error_function():
            raise Exception("File Not Found")

        t1 = Try.ret(ret_func)
        t2 = Try.ret(ret_func)
        self.assertEqual(next(Try.ret(x() + y()) for x in t1 for y in t2), Try.ret(2))
