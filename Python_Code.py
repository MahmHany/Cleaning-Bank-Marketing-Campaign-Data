import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("bank_marketing.csv")

# ----------------------- #
# Create the 'client' dataset
# ----------------------- #

# Select relevant client-related columns
client = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]

# Convert 'credit_default' and 'mortgage' to boolean: True if 'yes', else False
client['credit_default'] = (client['credit_default'].str.strip().str.lower() == 'yes').astype('boolean')
client['mortgage'] = (client['mortgage'].str.strip().str.lower() == 'yes').astype('boolean')

# Clean text columns: replace dots with underscores in 'job' and 'education'
client['job'] = client['job'].str.replace(".", "_")
client['education'] = client['education'].str.replace(".", "_")

# Replace 'unknown' in 'education' with NaN
client['education'] = client['education'].replace("unknown", np.nan)

# Save the cleaned client data to CSV
client.to_csv('client.csv', index=False)


# ----------------------- #
# Prepare campaign data
# ----------------------- #

# Ensure 'contact_duration' is numeric
df['contact_duration'] = pd.to_numeric(df['contact_duration'], errors='coerce')

# Create a synthetic 'full_date' column using month, day, and a fixed year (2022)
df['full_date'] = pd.to_datetime(df['month'] + ' ' + df['day'].astype(str) + ' 2022')

# Calculate 'last_contact_date' by subtracting contact duration (in days) from 'full_date'
df['last_contact_date'] = df['full_date'] - pd.to_timedelta(df['contact_duration'], unit='d')

# Format 'full_date' and 'last_contact_date' as strings in 'YYYY-MM-DD' format
df['full_date'] = df['full_date'].dt.strftime('%Y-%m-%d')
df['last_review'] = df['last_contact_date'].dt.strftime('%Y-%m-%d')


# ----------------------- #
# Create the 'campaign' dataset
# ----------------------- #

# Select relevant campaign-related columns
campaign = df[[
    "client_id",
    "number_contacts",
    "contact_duration",
    "previous_campaign_contacts",
    "previous_outcome",
    "campaign_outcome",
    "last_contact_date"
]]

# Convert 'previous_outcome' to boolean: True if 'success', else False
campaign['previous_outcome'] = (campaign['previous_outcome'].str.strip().str.lower() == 'success').astype('boolean')

# Convert 'campaign_outcome' to boolean: True if 'yes', else False
campaign['campaign_outcome'] = (campaign['campaign_outcome'].str.strip().str.lower() == 'yes').astype('boolean')

# Export campaign dataset
campaign.to_csv('campaign.csv', index=False)


# ----------------------- #
# Create the 'economics' dataset
# ----------------------- #

# Select relevant economic indicators
economics = df[["client_id", "cons_price_idx", "euribor_three_months"]]

# Export economic dataset
economics.to_csv('economics.csv', index=False)


# ----------------------- #
# Final Cleanup
# ----------------------- #

# Drop intermediate columns no longer needed
df = df.drop(['month', 'day', 'full_date'], axis=1)
