# LinkedIn Job Extractor 🚀

## Overview
This Python script automates the process of extracting LinkedIn job postings based on specific filters. It logs into LinkedIn, scrapes job postings for Data Analysts (or any specified role), filters them based on the number of applicants, and then saves the results in a Google Sheet.

## Features
- **Automated LinkedIn job scraping** using Selenium and BeautifulSoup
- **Filters jobs with fewer applicants** to improve application success rate
- **Extracts job details** (title, location, application count, etc.)
- **Saves the job data** to a Google Sheet automatically

## Prerequisites
Ensure you have the following installed on your system before running the script:

### Required Libraries
```bash
pip install pandas requests gspread gspread_dataframe selenium webdriver-manager beautifulsoup4 oauth2client google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pyautogui
```

### WebDriver
- **ChromeDriver**: Ensure you have Google Chrome installed and ChromeDriver compatible with your version.
- The script automatically installs it via `webdriver-manager`.

## Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/linkedin-job-extractor.git
cd linkedin-job-extractor
```

2. **Set Up Google Sheets API Credentials**
- Generate a **Service Account JSON key** from Google Cloud.
- Save the JSON file (e.g., `your_cred.json`) and update the script's path:
  ```python
  sheet_creds = r"path/to/your_cred.json"
  ```
- Share your Google Sheet with the service account email.

3. **Update LinkedIn Credentials**
- Edit the script to enter your LinkedIn email and password:
  ```python
  email_input.send_keys("Your_email")
  password_input.send_keys("Your_Password")
  ```
  *(For security, consider using environment variables instead of hardcoding credentials.)*

4. **Run the Script**
```bash
python linkedin_job_extractor.py
```

## How It Works
- The script logs into **LinkedIn** using Selenium.
- It **searches for job postings** in the last 24 hours.
- Extracts **job title, location, number of applicants, and job link**.
- Saves the cleaned **job data to Google Sheets** for easy tracking.

## Example Output (Google Sheets)
| Job Title | Job Link | Location | Time | Click Count |
|-----------|---------|---------|------|-------------|
| Data Analyst | [Link](https://linkedin.com/job/12345) | Remote | 2024-03-01 08:00:00 | 10 |
| Business Analyst | [Link](https://linkedin.com/job/67890) | New York | 2024-03-01 08:30:00 | 5 |


## Contributing
Feel free to open issues or submit pull requests if you'd like to improve the project!


