
import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Analyzer")
st.write("Analyze academic performance and discover student insights.")

# --------------------------------
# 2. UPLOAD CSV FILE
# --------------------------------

st.sidebar.header("Upload Student Data")

uploaded_file = st.sidebar.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv("data/student_data.csv")
    except FileNotFoundError:
        st.info("Please upload a student CSV file to begin.")
        st.stop()

# Clean column names
df.columns = df.columns.str.strip()

# --------------------------------
# 3. DATA VALIDATION
# --------------------------------

required_columns = [
    "Name", "Maths", "Python", "SQL", "Attendance"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.stop()

# Remove duplicate records
original_count = len(df)
df = df.drop_duplicates().copy()
duplicate_count = original_count - len(df)

# Convert marks and attendance to numeric
numeric_columns = ["Maths", "Python", "SQL", "Attendance"]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Treat values outside 0-100 as invalid
for col in numeric_columns:
    df.loc[~df[col].between(0, 100), col] = np.nan

# Remove records without any subject marks
df = df.dropna(
    subset=["Maths", "Python", "SQL"],
    how="all"
).copy()

# Fill missing values using column medians
for col in numeric_columns:
    if df[col].notna().any(): 
        df[col] = df[col].fillna(df[col].median())

if df.empty:
    st.error("No valid student records found.")
    st.stop()

# --------------------------------
# 4. PERFORMANCE CALCULATION
# --------------------------------

subjects = ["Maths", "Python", "SQL"]

df["Average"] = df[subjects].mean(axis=1)

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(calculate_grade)

df["Result"] = np.where(
    df["Average"] >= 40,
    "Pass",
    "Fail"
)

df["Support_Status"] = np.where(
    (df["Average"] < 50) |
    (df["Attendance"] < 75),
    "Needs Support",
    "On Track"
)

# --------------------------------
# 5. SIDEBAR FILTERS
# --------------------------------

st.sidebar.header("Filters")

grades = ["All"] + ['A','B','C','D']

selected_grade = st.sidebar.selectbox(
    "Select Grade",
    grades
)

if selected_grade != "All":
    filtered_df = df[df["Grade"] == selected_grade].copy()
else:
    filtered_df = df.copy()

# --------------------------------
# 6. KEY PERFORMANCE INDICATORS
# --------------------------------

st.subheader("📊 Performance Overview")

col1, col2, col3, col4 = st.columns(4)
if filtered_df.empty:
    print(f"There are {len(filtered_df)} with {selected_grade}")
    col1.metric(
    "Total Students",
    len(filtered_df))

    col2.metric(
    "Average Marks",
    "N/A")

    col3.metric(
    "Pass Percentage",
    "N/A")

    col4.metric(
    "Needs Support", "N/A")
    st.divider()
else:
    col1.metric(
    "Total Students",
    len(filtered_df))

    col2.metric(
    "Average Marks",
    f"{filtered_df['Average'].mean():.2f}")

    col3.metric(
    "Pass Percentage",
    f"{(filtered_df['Result'] == 'Pass').mean() * 100:.1f}%")

    col4.metric(
    "Needs Support",
    int((filtered_df["Support_Status"] == "Needs Support").sum()))

    st.divider()

# --------------------------------
# 7. STUDENT PERFORMANCE TABLE
# --------------------------------

st.subheader("👩‍🎓 Student Performance Records")

search_name = st.text_input("Search student by name")

display_df = filtered_df.copy()

if search_name:
    display_df = display_df[
        display_df["Name"].str.contains(
            search_name,
            case=False,
            na=False
        )
    ]

display_columns = [
    "Name", "Maths", "Python", "SQL",
    "Attendance", "Average", "Grade",
    "Result", "Support_Status"
]

st.dataframe(
    display_df[display_columns].round(2),
    use_container_width=True,
    hide_index=True
)

# --------------------------------
# 8. TOP PERFORMERS
# --------------------------------

st.subheader("🏆 Top Performing Students")
top_students=filtered_df[filtered_df["Average"]>=75]
st.dataframe(
        top_students[["Name", "Average", "Grade"]].round(2),
        use_container_width=True,
        hide_index=True)

# --------------------------------
# 9. SUBJECT-WISE ANALYSIS
# --------------------------------

st.subheader("📚 Subject-wise Average Marks")

subject_average = (
    filtered_df[subjects].mean()
    .rename("Average Marks")
)

st.bar_chart(subject_average)

# --------------------------------
# 10. STUDENT PERFORMANCE CHART
# --------------------------------

st.subheader("📈 Student-wise Performance")

chart_data = filtered_df.set_index("Name")[["Average"]]

st.bar_chart(chart_data)

# --------------------------------
# 11. ATTENDANCE ANALYSIS
# --------------------------------

st.subheader("📅 Attendance Analysis")

st.scatter_chart(
    filtered_df,
    x="Attendance",
    y="Average",
    color="Grade"
)

# --------------------------------
# 12. GRADE DISTRIBUTION
# --------------------------------

st.subheader("📊 Grade Distribution")

grade_counts = (
    filtered_df["Grade"]
    .value_counts()
)

st.bar_chart(grade_counts)

# --------------------------------
# 13. STUDENTS NEEDING SUPPORT
# --------------------------------

st.subheader("⚠️ Students Needing Support")

weak_students = filtered_df[
    filtered_df["Support_Status"] == "Needs Support"
]

if not weak_students.empty:
    st.dataframe(
        weak_students[
            ["Name", "Average", "Attendance", "Support_Status"]
        ].round(2),
        use_container_width=True,
        hide_index=True
    )
else:
    st.success("No students currently meet the support criteria.")

# --------------------------------
# 14. DATA QUALITY REPORT
# --------------------------------

st.subheader("🧹 Data Quality Report")

col1, col2, col3 = st.columns(3)

col1.metric("Duplicate Rows Removed", duplicate_count)

col2.metric(
    "Missing Values Remaining",
    int(df[numeric_columns].isna().sum().sum())
)

col3.metric("Valid Student Records", len(df))

# --------------------------------
# 15. DOWNLOAD ANALYZED DATA
# --------------------------------

st.subheader("📥 Download Analysis")

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Student Analysis CSV",
    data=csv_data,
    file_name="student_analysis_results.csv",
    mime="text/csv"
)

st.success("Student Performance Analyzer is ready!")
