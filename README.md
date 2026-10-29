# IRRIBIO — AI-Based Smart Irrigation (Synthetic Demonstration)

A Python prototype exploring soil moisture prediction using soil-related features and an **illustrative microbial activity index**. This is a **new reference implementation** based on the described IRRIBIO concept, not a restoration of the author's original dataset or trained model.

> No field trials, real soil microbial assays, sensor integrations, or validated performance claims are included. This project uses **synthetic generated samples** only.

## Features
- Soil moisture regression using a Random Forest
- Interactive Streamlit inputs and prediction display
- Demonstration moisture-based irrigation guidance
- Reproducible seeded synthetic data generation, held-out synthetic evaluation, and unit tests

## Tech
Python, scikit-learn, Streamlit, joblib.

## Install and run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m irribio.model
streamlit run app.py
```
The training command prints MAE and R² on a synthetic holdout set; these numbers must **not** be reported as accuracy on real soil measurements.

## Tests
```bash
python -m unittest discover -s tests -v
```

## Model inputs
- Microbial activity **index (invented synthetic feature, not a measured biomarker)**
- Soil temperature (°C)
- Air relative humidity (%)
- Recent rainfall (mm)
- Previous soil moisture (%)

## Architecture
`Synthetic feature generator -> model training -> saved local model -> Streamlit prediction -> illustrative decision rule`

## Team contributions and future improvements
The author described involvement in machine-learning/data-analysis aspects of IRRIBIO. The actual original sensor datasets, feature definitions, training notebooks, model evaluations, and hardware details have not been provided. They are **not** reproduced here. Future work includes replacing synthetic examples with properly collected, licensed, documented measurements; verifying the microbial feature's measurement meaning; field-validating predictions; and testing decisions against crop-specific thresholds.

## Limitations
The synthetic formula is a teaching example, not a scientific soil-microbe relationship. This cannot be used to decide irrigation in a real farm.
