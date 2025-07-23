# 🤖 Artificial Intelligence Projects – ENCS3340

This repository contains two major projects developed for the Artificial Intelligence course (ENCS3340) in the Department of Electrical and Computer Engineering.


---

## 🧠 Project 1 – Job Shop Scheduling Using Genetic Algorithm

### 📘 Description

This project applies a **Genetic Algorithm** to solve the Job Shop Scheduling Problem (JSSP), where a set of jobs with defined sequences must be scheduled across multiple machines to minimize total completion time.

### ⚙️ Key Features

- **Initial population** of schedules is randomly generated.
- **Fitness function** evaluates chromosome performance based on waiting time.
- **Selection, crossover, and mutation** are used to evolve better generations.
- The solution is refined over multiple generations.

### 📄 Files

- `main.py`: Runs the full genetic algorithm including selection, crossover, and mutation.
- `genes.py`: Class definition representing a job operation.
- `jobs.txt`: Input job specifications (job ID, machine ID, duration).
- `Aiproject1report.pdf`: Report explaining implementation details and results.

---

## 🧠 Project 2 – Machine Learning for Medical Classification

### 📘 Description

This project compares the performance of three machine learning models on the **Early Stage Diabetes Risk Prediction Dataset**:

- Decision Tree (J48)
- Naive Bayes
- Multilayer Perceptron (MLP)

All models were evaluated using WEKA with cross-validation and multiple error metrics.

### 📊 Dataset Attributes

- Binary and categorical features (e.g., age, gender, symptoms).
- Target class: **Positive** (diabetic risk) or **Negative**.

### 🧪 Metrics Reported

- Accuracy
- Precision / Recall / F1-score
- Kappa statistic
- Mean Absolute Error
- RMSE

### 📝 Key File

- `Ai_Machine_1193191_1201462.pdf`: Technical report with methodology, parameter tuning, and comparative results.

---

## 🧾 Tools & Technologies

- Python (for Project 1)
- WEKA (for Project 2)
- NumPy, Random, Genetic Operators
- Evaluation through fitness and error metrics



