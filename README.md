# Student Performance and Attendance Analysis


## Project overview

This Python project reads student records from `students.csv`, summarizes marks and attendance, classifies results, and writes an analyzed copy to `student_analysis.csv`.

The script uses the dataset supplied with the project. It does not generate or replace the input data.

## Files

- `student analysis.py` — Python program that reads the dataset and performs the analysis.
- `students.csv` — input data. Keep this file in the same folder as the Python script.
- `student_analysis.csv` — output created when the script runs. It contains the original student data plus the analysis columns.
- `README.md` — these project instructions.

## Input data format

The input CSV must contain these column headers:

| Column | Purpose |
|---|---|
| `Roll_No` | Student roll number or identifier |
| `Name` | Student name |
| `Branch` | Student's branch or department |
| `Marks` | Student's marks, on a 0–100 scale for the categories used here |
| `Attendance` | Attendance percentage, on a 0–100 scale |

The header spelling must match, including underscores and capitalization. Each row after the header should contain one student's information.

## How to run

### Using IDLE

1. Keep `student analysis.py` and `students.csv` in the same folder.
2. Open `student analysis.py` in IDLE.
3. Choose **Run → Run Module** or press **F5**.
4. Read the summary in the IDLE Shell.
5. Find the generated `student_analysis.csv` in the same folder.

### Using Command Prompt or PowerShell

Change to the project folder, then run:

```powershell
py -3.15 "student analysis.py"
```

For example, if the folder is `C:\Users\anura\Documents\hcl_tech  project`:

```powershell
cd "C:\Users\anura\Documents\hcl_tech  project"
py -3.15 "student analysis.py"
```

Use the Python launcher version installed on your computer if it is not Python 3.15.

## What the program analyzes

1. Number of student records, number of columns, and number of unique branches.
2. The first 10 student records.
3. Average, highest, and lowest marks.
4. Average, highest, and lowest attendance.
5. Pass/fail counts using **40 marks** as the pass threshold.
6. Attendance eligibility using **75% attendance** as the threshold.
7. The 10 students with the highest marks.
8. Count and sample rows for students with attendance below 75%.
9. Student count, average marks, and average attendance for each branch.
10. Performance categories based on marks:

| Marks | Category |
|---:|---|
| 85 or more | Excellent |
| 70–84 | Very Good |
| 50–69 | Good |
| 40–49 | Average |
| Below 40 | Poor |

## Output columns

The output `student_analysis.csv` includes the input columns and adds:

- `Result` — `Pass` when marks are at least 40; otherwise `Fail`.
- `Attendance_Status` — `Eligible` when attendance is at least 75%; otherwise `Short Attendance`.
- `Performance` — category based on the marks table above.

## Troubleshooting

- **`FileNotFoundError` for `students.csv`:** Put `students.csv` in the same folder as `student analysis.py`.
- **Missing-column error:** Check that the CSV header contains all five required columns with the exact names shown above.
- **`ModuleNotFoundError` for pandas or NumPy:** Install the missing package for the same Python version used to run the script. For example, run `py -3.15 -m pip install pandas numpy` in Command Prompt or PowerShell.
- **Output looks unchanged:** Run the script again; it refreshes `student_analysis.csv` from the current `students.csv` data.

## Author

- **Name:** Anurag Yadav
- **Admission No.:** 2026B01010411
- **Branch:** B.Tech CSE







