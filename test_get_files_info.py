from functions.get_files_info import get_files_info

def main():
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    
    print("\n".join("  " + line for line in result.splitlines()) if result else "  (no output)")
    print()

    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    print("\n".join("  " + line for line in result.splitlines()) if result else "  (no output)")
    print()

    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print("\n".join("  " + line for line in result.splitlines()) if result else "  (no output)")
    print()

    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")
    print("\n".join("  " + line for line in result.splitlines()) if result else "  (no output)")
    print()

if __name__ == "__main__":
    main()