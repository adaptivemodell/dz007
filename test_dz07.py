import zipfile
from zipfile import ZipFile

with ZipFile("tmp/dz.zip", 'w') as archive:
    archive.write("resources/Python Testing with Pytest (Brian Okken).pdf")
    archive.write("resources/Hello.txt")
    archive.write("resources/file_example_XLS_10.xls")
    archive.write("resources/file_example_XLSX_50.xlsx")

def test_files_in_archive():
    with zipfile.ZipFile("tmp/dz.zip", 'r') as archive:
        for name in archive.namelist():
            print(name)
            assert archive.getinfo(name)
