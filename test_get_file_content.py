from functions.get_file_content import get_file_content
from config import MAX_CHARS


def main():
    print("Result for 'lorem.txt' file:")
    result = get_file_content("calculator", "lorem.txt")
    print(result)
    print()

    print("Result for 'main.py' file:")
    result = get_file_content("calculator", "main.py")
    print(result)
    print()

    print("Result for 'pkg/calculator.py' file:")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print()

    print("Result for '/bin/cat' file:")
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print()

    print("Result for 'pkg/does_not_exist.py' file:")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
    print()

if __name__ == "__main__":
    main()
