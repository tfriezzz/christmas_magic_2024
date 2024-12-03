def difference_test(report, binary=True, previous=0):
    if len(report) <= 1 or binary is False:
        return binary
    else:
        #print(f"report: {report}")
        difference = (report[0]) - (report[1])
        #print(f"previous: {previous} difference: {difference}")
        #print(f"{report}: {-4 < difference < 4 and difference != 0}")
        if previous >= 0 and difference >= 0:
            return difference_test(report[1:], -4 < difference < 4 and difference != 0, difference)
        if previous == 0 and difference < 0 or previous < 0 and difference < 0:
            return difference_test(report[1:], -4 < difference < 4 and difference != 0, difference)
        if previous > 0 and difference < 0:
            #print(f"false_case_1")
            return False
        if previous < 0 and difference > 0:
            #print("false_case_2")
            return False
