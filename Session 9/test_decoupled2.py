from decoupled2 import DataReader
import pytest

def test_unknown_file_type_must_fail():
    reader = DataReader("data.docx")
    with pytest.raises(ValueError):
        reader.read_data()