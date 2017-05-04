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
    story = [["1", "asd", "asd", "ezazmukodik", "800", "13.5", "Planning"],
             ["2", "gre", "gre", "gre", "300", "30", "Review"],
             ]
    write_table_to_file(story)

if __name__ == '__main__':
    main()
