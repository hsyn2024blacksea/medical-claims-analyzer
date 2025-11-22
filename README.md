# Medical Claims Analyzer

A simple **medical claims CSV analyzer** built with Python and packaged with **PyInstaller**.  
It loads a medical claims dataset from `claims.csv`, prints a quick overview, and calculates basic statistics that can be used in healthcare analytics or insurance operations.

---

## 🔧 Features

- Loads data from `claims.csv`
- Shows:
  - First 5 rows of the dataset
  - Total number of rows
  - List of all columns
- (Optional) Financial summary if `claim_amount` column exists:
  - Average claim amount  
  - Minimum claim amount  
  - Maximum claim amount
- Can be run:
  - Directly with Python  
  - As a standalone Windows `.exe` (no Python required)

---

## 📁 Project Structure

```text
medical-claims-analyzer/
├── claims.csv              # Sample medical claims dataset
├── csv_quick_analyzer.py   # Main analysis script
├── requirements.txt        # Python dependencies (pandas)
└── README.md               # Project documentation
