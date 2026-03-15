from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_string_guess_against_int_secret():
    # String guess that can be converted to int should still work
    result = check_guess("50", 50)
    assert result == "Win"


def test_int_guess_against_string_secret():
    # String secret that can be converted to int should still work
    result = check_guess(50, "50")
    assert result == "Win"


def test_boundary_just_below_secret():
    # Guess one below the secret should be "Too Low"
    result = check_guess(49, 50)
    assert result == "Too Low"


def test_boundary_just_above_secret():
    # Guess one above the secret should be "Too High"
    result = check_guess(51, 50)
    assert result == "Too High"


def test_negative_guess_against_positive_secret():
    # Negative guesses are allowed by check_guess and should compare normally
    result = check_guess(-10, 50)
    assert result == "Too Low"
