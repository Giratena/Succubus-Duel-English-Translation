import argparse
import sys

def check_line(line: str, line_number: int) -> bool:
    parts = line.split(",")
    parts_number = len(parts)
    if parts_number == 2:
        # a correctly formatted CSV is the original text, a comma and the translation
        return True
    elif parts_number == 1:
        # note that this does accurately detect missing translations, because a line that is missing a translation would be:
        # something,
        # which is composed of two parts "something" and '' (which is nothing)
        print(f"The line {line_number} is missing a translation or is incorrectly formatted")
    elif parts_number > 2:
        # there is at least one comma that shouldn't be there
        print_wrong_comma(parts, line_number)
    else:
        print(f"There seems to be an unknown issue with the parsing of line {line_number}")
    # print a blank line to separate lines more easily (if there are multiple errors in a line, it's better like that)
    print("")
    return False

def print_wrong_comma(parts, line_number: int):
    # only go to len() - 1 because the last element won't end with a comma
    # ignore element 0 because it is supposed to have a comma after
    for splited_part in parts[1:len(parts)-1]:
        # print 3 word before comma by default, or less if it's not possible
        printed_word_number = min(3, len(splited_part)) 
        words = splited_part.split(' ') # split on space
        printed_words = ' '.join(words[-printed_word_number:])
        print(f"On line {line_number}, after \"{printed_words}\" : consider using ; instead of a comma")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="Comma checker",
            description="Checks that a file is correctly formatted in CSV formatted, prints lines that are not correctly formatted"
            )
    parser.add_argument('filename')
    args = parser.parse_args()
    # shouldn't be possible since argparse will require filename, but we never know
    if args.filename == None:
        print("Something went wrong with parsing the filename, use check_comma -h for more information")

    correctly_formatted: bool = True
    line_number: int = 2 # skip first line
    with open(args.filename, 'r') as file:
        # skip first line
        for line in file.readlines()[1:]:
            correctly_formatted = check_line(line, line_number) and correctly_formatted
            line_number = line_number + 1

    if correctly_formatted:
        print("All lines are correctly formatted, nothing to change!")
    else:
        sys.exit("There is at least one line that does not respect the CSV format, please refer to the log, exiting with error")

