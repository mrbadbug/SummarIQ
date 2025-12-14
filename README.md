**SummarIQ: NLP-Based Text Summarization** is a Python project that performs **abstractive text summarization** using **pre-trained transformer models**. It can generate concise summaries from long documents or articles. The project uses the **CNN/DailyMail dataset** for testing purposes, but **no training is required**, as the summarization model is pre-trained.

**Objective:**
 - Automatically generate readable and concise summaries from long text.

**Approach:** 
 - Preprocess input text and split long documents into smaller chunks.
 - Summarize each chunk using a **BART transformer model**.
 - Merge the summaries into a final, coherent output.

**Technologies Used:**
 - Python
 - Transformers (Hugging Face)
 - Streamlit (for user interface)
 - Pandas, NLTK

**Dataset**
**CNN/DailyMail Dataset**
 - Used for testing and evaluation.
 - Only **small sample CSV files** are included in this repository (`cnn_test.csv`).
**Columns:**
 - `article`: Original news article.
 - `highlights`: Reference human-written summary.

**Full dataset download link** (if needed):
 - [CNN/DailyMail Dataset on Hugging Face](https://huggingface.co/datasets/abisee/cnn_dailymail)
 - You need to run huggingface.ipynb to convert dataset to csv.
**The full dataset will include:**
 - cnn_test.csv
 - cnn_train.csv
 - cnn_validation.csv
 - Large CSV files (train/validation) are not included to keep the repository lightweight and GitHub-friendly.

**Installation**
 - Clone the repository: git clone https://github.com/<USERNAME>/SummarIQ.git
 - cd SummarIQ
 - pip install -r requirements.txt

 - streamlit run app.py(runs the project)
