import requests
from bs4 import BeautifulSoup
import PyPDF2
from io import BytesIO
from transformers import pipeline

def get_top_posts_links():
    url = 'https://emergentmind.com'
    
    # Send a GET request to the website
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the top posts - adjust the selector according to the actual website structure
    post_elements = soup.select('div.top-post-container h2.post-title a')[:3]
    
    top_post_links = [post['href'] for post in post_elements]
    
    return top_post_links

def fetch_pdf_content(pdf_url):
    response = requests.get(pdf_url)
    response.raise_for_status()
    
    # Read the PDF content
    pdf_file = BytesIO(response.content)
    reader = PyPDF2.PdfFileReader(pdf_file)
    
    content = []
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        content.append(page.extract_text())
    
    return '\n'.join(content)

def extract_pdf_links_from_post(post_url):
    response = requests.get(post_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the link to the arXiv PDF - adjust the selector according to the actual website structure
    pdf_link = soup.find('a', string='PDF')  # Adjust based on actual link text or structure
    
    if pdf_link and 'href' in pdf_link.attrs:
        return pdf_link['href']
    else:
        return None

def summarize_content(content, model_name='facebook/bart-large-cnn'):
    # Initialize the summarization pipeline with the chosen model
    summarizer = pipeline("summarization", model=model_name)
    
    # Generate summary (for long documents, consider splitting the content into smaller chunks)
    summary = summarizer(content, max_length=512, min_length=30, do_sample=False)
    
    return summary[0]['summary_text']

def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    top_post_links = get_top_posts_links()
    
    for i, post_link in enumerate(top_post_links, start=1):
        pdf_url = extract_pdf_links_from_post(post_link)
        
        if pdf_url:
            pdf_content = fetch_pdf_content(pdf_url)
            summary = summarize_content(pdf_content, model_name='google/pegasus-xsum')
            filename = f"post_{i}_summary.txt"
            save_to_file(summary, filename)
            print(f"Summary of PDF from {post_link} saved to {filename}")
        else:
            print(f"No PDF link found on page: {post_link}")

if __name__ == '__main__':
    main()

