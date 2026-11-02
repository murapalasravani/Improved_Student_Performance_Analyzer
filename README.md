# 📊 Student Performance Analyzer

An interactive data analysis application built using **Python, Pandas, and Streamlit** to explore, analyze, and visualize student academic performance.

## 🚀 Project Overview

The Student Performance Analyzer helps analyze student records from CSV files and presents meaningful insights through an interactive dashboard.

It performs data cleaning, handles missing values, calculates academic performance metrics, assigns grades, and allows users to explore student results using filters and visualizations.

## ✨ Key Features

- **CSV Data Handling:** Reads student records from CSV files using Pandas.
- **Data Cleaning:** Removes duplicate records and handles missing values.
- **Missing Value Imputation:** Uses median values to fill missing numerical data.
- **Performance Analysis:** Calculates average marks and percentages.
- **Grade Classification:** Assigns grades based on student performance.
- **Interactive Filtering:** Filters student records based on selected criteria.
- **Data Visualization:** Displays performance insights using interactive charts.
- **Performance Comparison:** Identifies and displays students based on their academic performance.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| Streamlit | Interactive web application |
| CSV | Dataset storage |

## 📁 Project Structure

```text
Improved_Student_Performance_Analyzer/
│
├── student_analyzer.py
├── student_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/murapalasravani/Improved_Student_Performance_Analyzer.git
```

**2. Navigate to the project folder**

```bash
cd Improved_Student_Performance_Analyzer
```

**3. Create a virtual environment (recommended)**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 Data Analysis Concepts Applied

- DataFrames and Series
- Data filtering and selection
- Handling missing values using `fillna()`
- Removing duplicate records using `drop_duplicates()`
- Statistical calculations using `mean()` and `median()`
- Boolean indexing
- Data preprocessing and transformation
- Interactive data visualization

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Working with real-world structured datasets.
- Performing data cleaning and preprocessing.
- Applying Pandas operations for data analysis.
- Building interactive applications using Streamlit.
- Translating raw data into meaningful insights.

## 🔮 Future Improvements

- Add more statistical analysis and visualizations.
- Include subject-wise performance comparisons.
- Add downloadable reports.
- Explore predictive analysis of student performance.

## 👩‍💻 About the Developer

I am an M.Tech Data Science student with a background in Computer Science Engineering, passionate about Python programming, data analysis, and building practical applications.

This project is part of my continuous learning journey in Data Science.

**Feedback and suggestions are always welcome!**

---

⭐ If you find this project interesting, consider giving the repository a star.

#Python #DataScience #Pandas #Streamlit #DataAnalysis