"""Data manager functions"""


def get_table_from_file():
    """Read data from file"""
    with open("story.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def write_table_to_file(table):
    """Write given table to file"""
    with open("story.csv", "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def main():
    story = [["1", "Cats", "Nowhere", "Must have 2 at least", "800", "13.5", "Planning"],
             ["2", "Programming issues", "It is not possible to guess random and meaningless variables",
              "Cats are needed for random generating. At least one cat/person.", "300", "30", "Review"],
             ["3", "Cat feeding", "They are totally idiots", "4 times. Do you understand? Give me food 4 times a day.",
              "1500", "0.5", "TODO"]
             ]
    write_table_to_file(story)

if __name__ == '__main__':
    main()
