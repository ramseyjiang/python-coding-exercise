from assertpy import assert_that

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()

def test_invalid_splits():
    splitter = Splitter()

    # Test invalid cable length
    assert_that(splitter.split).raises(ValueError).when_called_with(Cable(1, "coconuts"), 1)

    # Test invalid split times
    assert_that(splitter.split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 65)

    # Test impossible split
    assert_that(splitter.split).raises(ValueError).when_called_with(Cable(2, "coconuts"), 5)


# Run the tests
test_invalid_splits()


def test_should_split_cable_evenly():
    result = Splitter().split(Cable(10, "coconuts"), 1)
    assert_that(result).is_length(2)
    assert_that(result[0].length).is_equal_to(5)
    assert_that(result[1].length).is_equal_to(5)
    assert_that(result[0].name).is_equal_to("coconuts-00")
    assert_that(result[1].name).is_equal_to("coconuts-01")


def test_should_split_cable_with_remainder():
    result = Splitter().split(Cable(7, "coconuts"), 2)
    assert_that(result).is_length(4)
    assert_that([c.length for c in result]).is_equal_to([2, 2, 2, 1])
    assert_that(result[0].name).is_equal_to("coconuts-00")
    assert_that(result[0].length).is_equal_to(2)
    assert_that(result[1].name).is_equal_to("coconuts-01")
    assert_that(result[1].length).is_equal_to(2)
    assert_that(result[2].name).is_equal_to("coconuts-02")
    assert_that(result[2].length).is_equal_to(2)
    assert_that(result[3].name).is_equal_to("coconuts-03")
    assert_that(result[3].length).is_equal_to(1)


def test_should_raise_error_if_cable_length_too_small():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(1, "coconuts"), 1)


def test_should_raise_error_if_too_many_splits():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 20)

def test_should_handle_large_remainder():
    cable = Cable(10, "coconuts")
    result = Splitter().split(cable, 3)
    assert_that(result).is_length(5)
    assert_that([c.length for c in result]).is_equal_to([2, 2, 2, 2, 2])
    assert_that(result[0].name).is_equal_to("coconuts-00")
    assert_that(result[4].name).is_equal_to("coconuts-04")
