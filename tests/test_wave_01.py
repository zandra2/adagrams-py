import pytest

from adagrams.game import draw_letters

def test_draw_letters_draws_ten():
    # Arrange/Act
    letters = draw_letters()

    # Assert
    assert len(letters) == 10

def test_draw_letters_is_list_of_letter_strings():
    # Arrange/Act
    letters = draw_letters()

    # Assert
    assert len(letters) == 10

    for elem in letters:
        assert type(elem) == str
        assert len(elem) == 1
