from chapter2.preprocessing_helpers import row_to_list, convert_to_int


@pytest.fixture
def raw_and_clean_data_file(tmpdir):
    raw_path = tmpdir.join("raw.txt")
    clean_path = tmpdir.join("clean.txt")
    with open(raw_path, "w") as f:
        f.write("1,801\\t201,411\\n"
                "1,767565,112\\n"
                "2,002\\t333,209\\n"
                "1990\\t782,911\\n"
                "1,285\\t389129\\n"
                )
        return raw_path, clean_path


def preprocess(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file:
        rows = input_file.readlines()
        with open(output_file_path, "w") as output_file:
            for row in rows:
                row_as_list = row_to_list(row)
                if row_as_list is None:
                    continue
                area = convert_to_int(row_as_list[0])
                price = convert_to_int(row_as_list[1])
                if area is None or price is None:
                    continue
                output_file.write("{0}\\t{1}\\n".format(area, price))
