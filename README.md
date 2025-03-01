# **LinkedIn Job Extractor 🚀**  

## **Overview**  
This Python script automates the process of extracting **LinkedIn job postings** based on specific filters. It logs into LinkedIn, scrapes job postings for **Data Analysts** (or any specified role), filters them based on the **number of applicants**, and then saves the results in a **Google Sheet**.  

## **Features**  
👉 **Automates job scraping** every day at **8 AM** using Windows Task Scheduler  
👉 **Filters jobs with fewer applicants** so you apply before everyone else  
👉 **Extracts job details** (title, location, application count, etc.)  
👉 **Saves job data** to Google Sheets for easy tracking  

## **Prerequisites**  
Ensure you have the following installed before running the script:  

### **Required Libraries**  
```bash
pip install pandas requests gspread gspread_dataframe selenium webdriver-manager beautifulsoup4 oauth2client google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pyautogui
```

### **WebDriver**  
- **ChromeDriver**: Ensure Google Chrome is installed and ChromeDriver matches your version.  
- The script **automatically installs** it using `webdriver-manager`.  

---

## **Setup Instructions**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/mayankci/linkdien_job_extractor.git
cd linkedin-job-extractor
```

### **2️⃣ Set Up Google Sheets API Credentials**  
- Generate a **Service Account JSON key** from Google Cloud.  
- Save the JSON file (e.g., `your_cred.json`) and update the script:  
  ```python
  sheet_creds = r"path/to/your_cred.json"
  ```
- **Share your Google Sheet** with the service account email.

### **3️⃣ Update LinkedIn Credentials**  
Edit the script to enter your **LinkedIn email and password**:  
```python
email_input.send_keys("Your_email")
password_input.send_keys("Your_Password")
```
*(For security, consider using environment variables instead of hardcoding credentials.)*  

### **4️⃣ Automate with Windows Task Scheduler (Runs Daily at 8 AM) 🚀**  
1. **Open Task Scheduler** (`Win + R`, type `taskschd.msc`, and press Enter).  
2. Click **"Create Basic Task"** (right panel).  
3. **Name**: "LinkedIn Job Extractor" → **Next**  
4. **Trigger**: Select **Daily** → Set time to **08:00 AM** → **Next**  
5. **Action**: Select **Start a program** → Browse to **python.exe**  
6. In the **"Add arguments"** field, enter:  
   ```
   "C:\path\to\linkedin_job_extractor.py"
   ```
7. Click **Finish**.  

💡 Now, your script **automatically runs every morning at 8 AM** and updates your Google Sheet!  

---

## **How It Works**  
- The script **logs into LinkedIn** using Selenium.  
- It **searches for job postings** in the last 24 hours.  
- Extracts **job title, location, number of applicants, and job link**.  
- Saves the cleaned **job data to Google Sheets**.  

### **Example Output (Google Sheets)**  
| Job Title        | Job Link                       | Location  | Time               | Click Count |  
|-----------------|--------------------------------|----------|--------------------|-------------|  
| Data Analyst    | [Link](https://linkedin.com/job/12345) | Remote   | 2024-03-01 08:00:00 | 10  |  
| Business Analyst | [Link](https://linkedin.com/job/67890) | New York | 2024-03-01 08:30:00 | 5  |  

---

## **Contributing**  
Feel free to open issues or submit pull requests if you'd like to improve the project!  

💎 **Want Naukri platform automation? DM me on Linkedin https://www.linkedin.com/in/mayanksharma177/ **  
