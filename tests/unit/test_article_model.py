def test_new_article(app, new_article):
    """
    GIVEN an Article model
    WHEN a new Article is created
    THEN check if created properly
    """

    assert new_article.title == 'Header'
    assert new_article.content == 'Some Text here'
