from transformers import pipeline
from preprocess import clean_text, chunk_text

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):
    text = clean_text(text)
    chunks = chunk_text(text)

    summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=150,
            min_length=50,
            do_sample=False
        )
        summaries.append(summary[0]['summary_text'])

    final_summary = " ".join(dict.fromkeys(summaries))
    return final_summary
