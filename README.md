# autoblog
# EmergentMind PDF Summarizer

This project fetches the top 3 posts from [EmergentMind.com](https://emergentmind.com), extracts and reads the content of linked PDFs, summarizes the content using a language model, and saves the summary to a text file.

## Features

- Fetch top 3 posts from EmergentMind.com.
- Extract and read PDF content from each post.
- Summarize PDF content using a pre-trained language model from Hugging Face.
- Save summaries to text files.

## Installation
- pip install -r requirements.txt

##Configuration
###Available Models
- facebook/bart-large-cnn: BART model fine-tuned on the CNN/DailyMail dataset.
- google/pegasus-xsum: PEGASUS model fine-tuned on the XSum dataset.
- t5-base or t5-large: T5 model suitable for summarization tasks.
- sshleifer/distilbart-cnn-12-6: DistilBART model, a smaller and faster version of BART.
### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/emergentmind-pdf-summarizer.git
cd emergentmind-pdf-summarizer

