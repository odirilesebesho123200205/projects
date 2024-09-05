from password_validator import is_password_secure

# the criteria are:
# - at least 8 characters long
# - contains both uppercase and lowercase letters
# - has at least one digit
# - has at least one special character


def test_valid_password():
    assert is_password_secure("06 - Tennessee Waltz"), "Password is valid"


def test_password_too_short():
    assert not is_password_secure("aA1!"), "Password is too short"


def test_password_no_uppercase():
    assert not is_password_secure(
        "07 - can't take my eyes off of you"), "Password has no uppercase"


def test_password_no_lowercase():
    assert not is_password_secure(
        "08 - I'M A BELIEVER"), "Password has no lowercase"


def test_password_no_digit():
    assert not is_password_secure(
        "- Somebody To Love"), "Password has no digits"


def test_password_no_special_character():
    assert not is_password_secure(
        "10 I Want To Hold Your Hand"), "Password has no special character"
