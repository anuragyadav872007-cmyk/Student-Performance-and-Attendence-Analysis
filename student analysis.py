import pandas as pd
import numpy as np

print("=" * 65)
print("       STUDENT PERFORMANCE AND ATTENDANCE ANALYSIS")
print("=" * 65)

from pathlib import Path

# Read your supplied dataset from the same folder as this script.
data_file = Path(__file__).resolve().parent / "students.csv"
df = pd.read_csv(data_file)

required_columns = {"Roll_No", "Name", "Branch", "Marks", "Attendance"}
missing_columns = required_columns.difference(df.columns)
if missing_columns:
    raise ValueError(f"students.csv is missing required columns: {', '.join(sorted(missing_columns))}")

total_students = len(df)
if total_students == 0:
    raise ValueError("students.csv does not contain any student records.")
# STEP 3: THE PROVIDED CSV IS ALREADY LOADED

print("\n1. DATASET INFORMATION")
print("Total Students:", len(df))
print("Total Columns:", len(df.columns))
print("Branches:", df["Branch"].nunique())

# STEP 4: DISPLAY FIRST 10 RECORDS

print("\n2. FIRST 10 STUDENT RECORDS")
print(df.head(10).to_string(index=False))

# STEP 5: PERFORMANCE ANALYSIS

print("\n3. PERFORMANCE ANALYSIS")

print("Average Marks:",
      round(np.mean(df["Marks"]), 2))

print("Highest Marks:",
      np.max(df["Marks"]))

print("Lowest Marks:",
      np.min(df["Marks"]))

# STEP 6: ATTENDANCE ANALYSIS

print("\n4. ATTENDANCE ANALYSIS")

print("Average Attendance:",
      round(np.mean(df["Attendance"]), 2), "%")

print("Highest Attendance:",
      np.max(df["Attendance"]), "%")

print("Lowest Attendance:",
      np.min(df["Attendance"]), "%")

# STEP 7: PASS AND FAIL ANALYSIS

df["Result"] = np.where(
    df["Marks"] >= 40,
    "Pass",
    "Fail"
)

passed = np.sum(df["Result"] == "Pass")
failed = np.sum(df["Result"] == "Fail")

print("\n5. PASS AND FAIL ANALYSIS")
print("Passed Students:", passed)
print("Failed Students:", failed)

print("Pass Percentage:",
      round((passed / total_students) * 100, 2), "%")

# STEP 8: ATTENDANCE ELIGIBILITY

df["Attendance_Status"] = np.where(
    df["Attendance"] >= 75,
    "Eligible",
    "Short Attendance"
)

eligible = np.sum(
    df["Attendance_Status"] == "Eligible"
)

not_eligible = total_students - eligible

print("\n6. ATTENDANCE ELIGIBILITY")
print("Eligible Students:", eligible)
print("Short Attendance:", not_eligible)

# STEP 9: TOP 10 PERFORMERS

print("\n7. TOP 10 PERFORMERS")

top_students = df.nlargest(10, "Marks")

print(
    top_students[
        ["Roll_No", "Name", "Branch", "Marks"]
    ].to_string(index=False)
)

# STEP 10: LOW ATTENDANCE STUDENTS

print("\n8. LOW ATTENDANCE STUDENTS")

low_attendance = df[df["Attendance"] < 75]

print("Students with low attendance:",
      len(low_attendance))

print(low_attendance.head(10).to_string(index=False))

# STEP 11: BRANCH-WISE PERFORMANCE

print("\n9. BRANCH-WISE PERFORMANCE")

branch_analysis = df.groupby("Branch").agg(
    Total_Students=("Roll_No", "count"),
    Average_Marks=("Marks", "mean"),
    Average_Attendance=("Attendance", "mean")
)

print(branch_analysis.round(2))

# STEP 12: PERFORMANCE CATEGORIES

df["Performance"] = np.select(
    [
        df["Marks"] >= 85,
        df["Marks"] >= 70,
        df["Marks"] >= 50,
        df["Marks"] >= 40
    ],
    [
        "Excellent",
        "Very Good",
        "Good",
        "Average"
    ],
    default="Poor"
)

print("\n10. PERFORMANCE CATEGORY ANALYSIS")

print(df["Performance"].value_counts())

# STEP 13: SAVE FINAL ANALYSIS

df.to_csv(data_file.parent / "student_analysis.csv", index=False)

# STEP 14: FINAL SUMMARY

print("\n" + "=" * 65)
print("                  FINAL PROJECT SUMMARY")
print("=" * 65)

print("Total Student Records:", len(df))
print("Total Branches:", df["Branch"].nunique())
print("Average Marks:", round(df["Marks"].mean(), 2))
print("Average Attendance:",
      round(df["Attendance"].mean(), 2), "%")
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Top Performer:", df.loc[df["Marks"].idxmax(), "Name"])

print("\nDataset Saved: students.csv")
print(f"Analysis Saved: {data_file.parent / 'student_analysis.csv'}")

print("\nPROJECT COMPLETED SUCCESSFULLY!")
print("=" * 65)

