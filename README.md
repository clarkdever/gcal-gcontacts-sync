# gcal-gcontacts-sync
Python project to download Google Contacts and Calendar History and compare in Pandas

1. pip install -r requirements.txt
2. Create project credentials (See step-by-step instructions below)
3. Download credentials.json and place in env/


## How to create Projects Credentials

### Step 1: Access Google Cloud Console
1. Open your web browser and navigate to [Google Cloud Console](https://console.cloud.google.com/).
2. Log in with your Google account if you're not already logged in.

### Step 2: Create a New Project
1. Click on the "Select a project" dropdown near the top right corner.
2. In the modal that appears, click the "New Project" button.
3. Enter a project name and select a billing account if you have one. You can also choose the organization under which the project should reside.
4. Click "Create".

### Step 3: Enable APIs
1. In the Dashboard, click on the "Navigation Menu" (three horizontal lines at the top left corner).
2. Go to "APIs & Services" -> "Dashboard".
3. Click on "+ ENABLE APIS AND SERVICES" at the top.
4. In the search bar, type "Gmail API" and select it. Then click "Enable". Repeat this step for "Google Calendar API" and "Google People API".

### Step 4: Create OAuth2 Credentials

### Step 5: Download JSON Key

