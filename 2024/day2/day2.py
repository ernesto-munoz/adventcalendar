
def is_report_correct(report:list[int]) -> bool:
    
    order = (report[1] - report[0]) > 0
    for i in range(1, len(report)):
        previous = report[i - 1]
        current = report[i]
        diff = current - previous
        if abs(diff) < 1 or abs(diff) > 3 or order != (diff > 0):
            return False
    return True

def is_report_correct_dampener(report:list[int]) -> bool:
    if is_report_correct(report=report):
        return True
    
    for i in range(0, len(report)):
        if is_report_correct(report=report[0:i] + report[i+1:]):
            return True
    return False

def main() -> None:
    correct_reports = 0
    correct_reports_dampener = 0
    with open("input.txt") as f:
        for line in f:
            report = [int(f) for f in line.split()]
            if is_report_correct(report=report):
                correct_reports += 1
            if is_report_correct_dampener(report=report):
                correct_reports_dampener += 1
    print(f"Correct reports: {correct_reports}")
    print(f"Correct reports (Dampener): {correct_reports_dampener}")
            

if __name__ == "__main__":
    main()