import pandas as pd

# Load dataset
df = pd.read_csv("netflix_data.csv")

# Show first 5 rows
print(df.head())

print(df.info())
print(df.describe())

import matplotlib.pyplot as plt

# Top titles
top_titles = df['Title'].value_counts().head(5)

plt.figure(figsize=(8, 5))
top_titles.plot(kind='bar', color='tomato')
plt.title("Top 5 Watched Titles")
plt.xlabel("Title")
plt.ylabel("Views")
plt.tight_layout()

# Save chart
plt.savefig("top_titles_chart.png")  # Same folder
plt.show()

user_watch = df.groupby('User_ID')['Duration'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
user_watch.plot(kind='bar', color='seagreen')
plt.title("Total Watch Time per User")
plt.xlabel("User ID")
plt.ylabel("Total Minutes Watched")
plt.tight_layout()

plt.savefig("user_watch_time.png")
plt.show()

df['Watch_Date'] = pd.to_datetime(df['Watch_Date'])
daily_watch = df.groupby('Watch_Date')['Duration'].sum()

plt.figure(figsize=(10, 5))
daily_watch.plot(marker='o')
plt.title("Daily Watch Time Trend")
plt.xlabel("Date")
plt.ylabel("Total Minutes")
plt.grid(True)
plt.tight_layout()

plt.savefig("watch_trend.png")
plt.show()

import seaborn as sns

plt.figure(figsize=(8, 5))
sns.histplot(df['Rating'], bins=5, kde=True, color='purple')
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("ratings_distribution.png")
plt.show()
