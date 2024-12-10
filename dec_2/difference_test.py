
def is_safe(report):
    if len(report) < 2:
        return True  

    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False 
        if diff < 0:
            increasing = False
        if diff > 0:
            decreasing = False

    return increasing or decreasing


def difference_test(report, dampener_used=False):
    if is_safe(report):
        return True

    if dampener_used:
        return False

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True  
    return False 
