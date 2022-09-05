def test_new_user(app, new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the (username, email) and hashed password are correct
    """

    assert new_user.username == 'American Psycho'
    assert new_user.email == 'p.bateman@gmail.com'
    assert new_user.password != 'seaurchin1'
    assert new_user.is_editor == False


def test_new_editor(app, new_editor):
    """
    GIVEN a User model
    WHEN a new User (Editor) is created
    THEN make sure that he is actually an editor
    """

    assert new_editor.is_editor == True


def test_switching_editor_role(app, new_user):
    """
    GIVEN a User model
    WHEN a new User is created and switched editor's role
    THEN check if role switched correctly
    """

    assert new_user.is_editor == False
    new_user.set_editor_role(True)
    assert new_user.is_editor == True
    new_user.set_editor_role(False)
    assert new_user.is_editor == False
