from pathlib import Path
from pipup.req_files import ReqFile


def test_find_package_requirements():
    """ Find the requirements file in this package """
    r = ReqFile(auto_read=False)

    assert r.exists

    # Our valid path
    p = Path(__file__).parent / "../requirements.txt"
    p = p.resolve()

    assert r.file_path == str(p)
