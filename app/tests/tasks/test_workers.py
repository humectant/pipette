from app.tasks import util


def test_fuget_about_it():
    result = util.fuget_about_it()
    assert result == "Fugetaboutit!"

