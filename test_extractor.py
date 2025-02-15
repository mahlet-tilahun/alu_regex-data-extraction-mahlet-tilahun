import extractor  # Importing the extractor functions from extractor.py

# The text data 
text_data = """
- valid@example.com # Valid email
- invalid-email.com # Invalid email (missing '@')
- user@subdomain.example.co.uk # Valid email with subdomain and multiple TLDs


Some URLs:

- https://www.example.com # Valid URL
- http://subdomain.example.org/page # Valid URL with subdomain and path
- invalid-url.com # Invalid URL (missing scheme)


Phone numbers:

- (123) 456-7890 # Valid phone number with parentheses and dashes
- 123-456-7890 # Valid phone number with dashes
- 123.456.7890 # Valid phone number with dots
- 123-45-67890 # Invalid format (wrong number of digits)

Credit card numbers:

- 1234 5678 9012 3456 # Valid credit card number with spaces
- 1234-5678-9012-3456 # Valid credit card number with hyphens
- 1234 5678 9012 34567 # Invalid number (extra digit)


Times:

- 14:30 # Valid time in 24-hour format
- 2:30 PM # Valid time in 12-hour format
- 25:00 # Invalid time (hour exceeds 24)
- 2:61 PM # Invalid time (minute exceeds 59)
- 02:15 # Valid time with leading zero in 24-hour format

HTML tags:

- <div>Content</div>  # Valid HTML tag
- <img src="image.jpg" alt="description"> # Valid self-closing tag
- <p>This is a paragraph</p>  # Valid paragraph tag
- <br> # Valid break tag (self-closing)
- <div Content</div # Invalid tag (missing closing bracket)
"""

# Function to process and display the extracted information
def process_text_data(text):
    # Extract information using the functions from extractor.py
    emails = extractor.extract_emails(text)
    urls = extractor.extract_urls(text)
    phone_numbers = extractor.extract_phone_numbers(text)
    credit_cards = extractor.extract_credit_cards(text)
    times = extractor.extract_time(text)
    html_tags = extractor.extract_html_tags(text)
    
    # Print the extracted information
    print("Emails Found:")
    print(emails)
    print("\nURLs Found:")
    print(urls)
    print("\nPhone Numbers Found:")
    print(phone_numbers)
    print("\nCredit Card Numbers Found:")
    print(credit_cards)
    print("\nTimes Found:")
    print(times)
    print("\nHTML Tags Found:")
    print(html_tags)

# Call the function to process the data
if __name__ == "__main__":
    process_text_data(text_data)
