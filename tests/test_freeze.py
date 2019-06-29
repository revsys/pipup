from pipup.freeze import Freeze


def test_freeze():
    f = Freeze()
    f.lines.append("Django==2.2")
    f.lines.append("pytest==5.0.0")
    f.lines.append("Click==7.0")

    # We should be able to find upper and lower case versions
    assert f.find("Django")
    assert f.find("django")

    # We should be able to find versions with and without the version numbers
    assert f.find("pytest")
    assert f.find("pytest==5.0.0")

    assert not f.find("not-found")
