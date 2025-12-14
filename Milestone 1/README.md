# FitPulse: Health Anomaly Detection (Milestone 1)

## 📌 Objective
The primary objective of this milestone is to **ingest, clean, and preprocess wearable device data** (Heart Rate, Steps, Sleep, Calories) to establish a high-quality foundation for **Health Anomaly Detection**. By normalizing timestamps and aligning all metrics to a consistent 1-minute frequency, we enable granular analysis of user physiological patterns.

## 📂 Dataset Source
**Dataset Name**: FitPulse Wearable Device Data  
**Source**: [Kaggle - sanket28/fitpulse-wearable-device-data-csv](https://www.kaggle.com/datasets/sanket28/fitpulse-wearable-device-data-csv)  
**Description**: Contains time-series data from smart health devices, including metrics like:
- `time_stamp`: Timestamp of the record.
- `heart_rate`: Beats per minute (BPM).
- `step_count`: Number of steps taken.
- `calories_burned`: Energy expenditure.
- `sleep_tracking`: Sleep status/stage.
- `activity_status`: Activity classification (Resting, Exercise, etc.).

## 🛠️ process & Steps Performed
We implemented a robust data cleaning pipeline using **Python**.

### 1. Data Loading & Inspection
- Downloaded the dataset programmatically using `kagglehub`.
- Loaded raw CSV/JSON files into Pandas DataFrames.
- Verified column types and initial data shape.

### 2. Time Normalization
- Converted all `time_stamp` entries to **UTC** format to ensure consistency across different time zones.
- Removed rows with invalid or missing timestamps.

### 3. Data Cleaning
- Standardized the **User ID** column (mapped `Patient_ID`/`id` to a common `Id` column).
- Handled missing values (`NaN`) using appropriate imputation strategies (see below).

### 4. Resampling & Alignment (Granular Preprocessing)
To prepare the data for time-series analysis, we aligned all metrics to a **1-minute interval**:
- **Numeric Metrics** (Heart Rate, Steps, Calories): Applied **Linear Interpolation** to fill gaps smoothly between records.
- **Categorical Metrics** (Sleep, Activity Status): Applied **Forward-Fill (Pad)** logic to propagate the last known state.
- **Backfilling**: Handled edge cases (e.g., missing initial values) to ensuring zero null values in the final output.

## 🧰 Tools & Technologies Used
- **Python**: Core programming language.
- **Pandas**: Data manipulation, time-series resampling, and merging.
- **NumPy**: Numerical operations.
- **KaggleHub**: Dataset acquisition.
- **Matplotlib / Seaborn** (Future milestones): For visualization and exploratory data analysis (EDA).
- **Google Colab / Jupyter**: Development environment.

## 📊 Key Insights & Outputs
**Final Data Structure:**
The processed dataset (`cleaned_fitness_data.csv`) is now strictly aligned to 1-minute logic for every user.

**Sample Output:**
```csv
Id,time_stamp,heart_rate,step_count,calories_burned,Weight,Height,activity_status
P0001,2025-01-01 00:00:00+00:00,65.6,183.0,16.4,67.2,174.2,sleep
P0001,2025-01-01 00:01:00+00:00,65.6,184.2,16.4,67.2,174.2,sleep
```

**Outcome:**
- **Zero Null Values**: Complete dataset ready for ML models.
- **Consistent Frequency**: 1-minute intervals suitable for granular anomaly detection.
- **Structured Format**: `Id` as the primary grouping key.

---
<<<<<<< HEAD


# FitPulse-Health-Anomaly-Detection-from-Fitness-Devices
>>>>>>> f58501212036472bd215f82e09a8726b1e4f62d5
