import pytest

from unittest import mock

from catz.type_class.derivative.maybe import Nothing, Just, Maybe


@pytest.fixture(scope="module")
def nothing():
    return Nothing()


@pytest.fixture(scope="module")
def just():
    return Just(1)


def return_mock():
    func_mock = mock.Mock()
    func_mock.return_value = Nothing()
    return func_mock


def return_just_mock():
    func_mock = mock.Mock()
    func_mock.return_value = Just(1)
    return func_mock


@pytest.fixture(scope="module")
def func_just():
    return return_just_mock()


@pytest.fixture(scope="module")
def func_just_g():
    return return_just_mock()


@pytest.fixture(scope="module")
def func_just_h():
    return return_just_mock()


@pytest.fixture(scope="module")
def func():
    return return_mock()


@pytest.fixture(scope="module")
def func_g():
    return return_mock()


@pytest.fixture(scope="module")
def func_h():
    return return_mock()


def test_create_nothing(nothing: Nothing):
    assert nothing is not None


def test_fmap(nothing: Nothing):
    res = nothing.fmap(lambda x: x + 1)
    assert isinstance(res, Nothing)


def test_left_id(nothing: Nothing, func):
    assert Nothing.ret("x").bind(func) == func(nothing)


def test_right_id(nothing: Nothing, func):
    assert nothing.bind(Nothing.ret) == nothing


def test_associativity(nothing, func_g, func_h):
    assert nothing.bind(func_g).bind(func_h) == nothing.bind(lambda x: func_g(x).bind(func_h))


def test_create_just(just: Just):
    assert just is not None


def test_fmap_just(just: Just):
    res = just.fmap(lambda x: x + 1)
    assert isinstance(res, Just)
    assert res == Just(2)


def test_left_id_just(just: Just, func_just):
    assert Just.ret("x").bind(func_just) == func_just(just)


def test_right_id_just(just: Just):
    assert just.bind(Just.ret) == just


def test_accociativity_just(just: Just, func_just_g, func_just_h):
    assert just.bind(func_just_g).bind(func_just_h) == just.bind(lambda x: func_just_g(x).bind(func_just_h))


@pytest.fixture(scope="module")
def just_1():
    return Just(1)


@pytest.fixture(scope="module")
def just_2():
    return Just(2)


@pytest.fixture(scope="module")
def just_3():
    return Just(3)


def test_do(just_1, just_2, just_3):
    assert next(Just.ret(x + y) for x in just_1 for y in just_2) == just_3
