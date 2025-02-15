import re

# Function to extract email addresses
def extract_emails(text):
    """
    Extracts email addresses from the given text.
    Supports standard email formats like 'user@example.com' and 'firstname.lastname@company.co.uk'.
    """
    
    pattern = r'\b[A-Za-z0-9_%+-](?:[A-Za-z0-9_%+-]*[A-Za-z0-9_%+-])?(?:\.[A-Za-z0-9_%+-]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,10}\b'
    return re.findall(pattern, text)

# Function to extract URLs
def extract_urls(text):
    """
    Extracts URLs from the given text.
    Supports both 'http' and 'https' with optional ports, paths, query strings, and fragments.
    """
    
    pattern = r'https?://(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?::\d{1,5})?(?:/[-A-Za-z0-9%._~+&=]*)*(?:\?[-A-Za-z0-9%._~+=&]*)?(?:#[-A-Za-z0-9%._~+&=]*)?'
    return re.findall(pattern, text)
    
# Function to extract phone numbers
def extract_phone_numbers(text):
    """
    Extracts phone numbers from the given text.
    Supports formats like (123) 456-7890, 123-456-7890, 123.456.7890, and optional country codes.
    """
    
    pattern = r'\+?\d{0,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

# Function to extract credit card numbers
def extract_credit_cards(text):
    """
    Extracts credit card numbers from the given text.
    Matches typical credit card formats with spaces or dashes separating groups of digits.
    """
    
    pattern = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    return re.findall(pattern, text)

# Function to extract time in 12-hour or 24-hour format
def extract_time(text):
    """
    Extracts time in 12-hour or 24-hour format from the given text.
    Supports formats like 14:30 (24-hour) or 2:30 PM (12-hour).
    """
    
    pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM))?\b"
    return re.findall(pattern, text)

# Function to extract HTML tags
def extract_html_tags(text):
    """
    Extracts HTML tags from the given text.
    Matches basic HTML tags like <p>, <div>, and <img>.
    """
    
    pattern = r"<[^>]+>"
    return re.findall(pattern, text)


