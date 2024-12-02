def main():
    with open("input.txt") as f:
        file_contents = f.read()
        reports = (list(file_contents.splitlines()))
        print(f"test: {reports}")
        safe_reports = 0
        for report in reports:
            report = list(map(int, report))
            if "insert magic here" is True:
                safe_reports += 1

        print(f"number of safe reports: {safe_reports}")


if __name__ == "__main__":
    main()
