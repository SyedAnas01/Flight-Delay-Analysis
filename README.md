# Flight Delay Analysis and Prediction Project

## Description
This project analyzes airline delay data using Apache Hive and implements machine learning models to predict flight delays. The data is sourced from the Harvard Dataverse and processed collaboratively by team members. It showcases big data processing, transformation, and predictive analytics.

## Features
- **Data Extraction**: Downloaded and transformed raw flight delay data into a structured format using Hive.
- **Data Sampling and Transformation**: Created Hive tables, added delay indicators, and selected random samples for analysis.
- **Collaboration**: Combined samples from team members into a unified dataset for machine learning.
- **Machine Learning**: Built a Support Vector Machine (SVM) model to predict delays based on combined data.
- **Visualization**: Generated visual insights and summarized findings in a collaborative presentation.

## Repository Structure
- `hive/`: HiveQL scripts for table creation, data transformation, and export.
- `scripts/`: Python and shell scripts for data processing, sampling, and machine learning.
- `data/`: Raw, processed, and visualized data files.
- `models/`: Trained machine learning models.

## Prerequisites
- Apache Hive
- Python 3.x
- Required Python libraries: pandas, scikit-learn, matplotlib
- AWS CLI (optional, for managing remote Hive clusters)

## Usage
1. **Data Download**:
   - Run `scripts/data_download.sh` to download raw data from the Harvard Dataverse.
2. **Hive Table Creation**:
   - Use `hive/create_sample_table.hql` to create and load Hive tables.
3. **Data Transformation**:
   - Use `hive/transform_data.hql` to add delay indicators and sample records.
4. **Combine Data**:
   - Run `scripts/combine_samples.py` to combine sampled data from team members.
5. **Train Model**:
   - Run `scripts/train_svm_model.py` to train and evaluate the SVM model.

## Example Results
- Three airports and carriers with the highest delays identified per year.
- SVM model achieved precision and recall scores of over 90% on test data.
- Visualized delay trends and model performance in `data/visualizations`.

