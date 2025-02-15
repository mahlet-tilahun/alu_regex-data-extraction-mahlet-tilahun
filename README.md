# **Regex - Onboarding Hackathon** 
## Project Overview
This project is aimed at using Regular Expressions(Regex) to extract required data from string resposes obtained from all over the web. It processes large amounts of text from various sources, extracting key information such as:  
- Email Addresses 
- URLs  
- Phone Numbers
- Credit Card Numbers 
- Time (12-hour and 24-hour formats) 
- HTML Tags 

## Setup Instructions
### 1. Prerequisites
Ensure you have Python installed on your system. You can verify this by running:

`python --version`

This project uses built-in Python libraries, so no additional installations are required.
### 2. Clone the repository

Clone the project repository to your local machine using:

`git clone https://github.com/mahlet-tilahun/alu_regex-data-extraction-mahlet-tilahun.git` 

Then navigate to the folder using:

`cd alu_regex-data-extraction-mahlet-tilahun`

### 3. Run the script

To execute the script and extract data from sample text, run:

`python test_extractor.py`

## Script Descriptions
### `extractor.py`

This script contains functions that use regex patterns to extract different types of data:

`extract_emails(text)`: Extracts valid email addresses.

`extract_urls(text)`: Identifies valid URLs with HTTP/HTTPS schemes.

`extract_phone_numbers(text)`: Extracts phone numbers in various formats.

`extract_credit_cards(text)`: Identifies credit card numbers with different formatting styles.

`extract_time(text)`: Extracts time in both 12-hour and 24-hour formats.

`extract_html_tags(text)`: Finds and extracts HTML tags from text.

### `test_extractor.py`

This script imports functions from extractor.py and applies them to a predefined sample text containing emails, URLs, phone numbers, credit card numbers, times, and HTML tags. It prints the extracted information for verification.

#### Example Output
Upon running `test_extractor.py`, the script will display extracted data like:

```
Emails Found:
['valid@example.com', 'user@subdomain.example.co.uk']

URLs Found:
['https://www.example.com', 'http://subdomain.example.org/page']

Phone Numbers Found:
['(123) 456-7890', '123-456-7890', '123.456.7890']

Credit Card Numbers Found:
['1234 5678 9012 3456', '1234-5678-9012-3456']

Times Found:
['14:30', '2:30 PM', '02:15']

HTML Tags Found:
['<div>Content</div>', '<img src="image.jpg" alt="description">', '<p>This is a paragraph</p>', '<br>']
```
