from difference_test import difference_test

def main():
    with open("input.txt") as f:
        file_contents = f.read()
        reports = (list(file_contents.splitlines()))
        #print(f"test: {reports}")
        safe_reports = 0
        for report in reports[:-1]:
            split_report = report.split()
            #print(f"split {split_report}")
            int_report = list(map(int, split_report))
            #print(f"integer {int_report}")
            if difference_test(int_report) is True:
                safe_reports += 1

        print(f"number of safe reports: {safe_reports}")


if __name__ == "__main__":
    main()
