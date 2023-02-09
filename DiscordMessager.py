import re
import xml.etree.ElementTree as ET
import collections
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Replace with the path to your XML file
xml_file = 'C:/Users/admin/Desktop/example.xml'

# Read the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Get the text content of the XML file
text = ""
for para in root.findall('./para'):
    text += para.text

# Extract the dates and names from the text
dates_and_names = re.findall(r'\w+\s----\s\d{2}/\d{2}/\d{4}', text)

# Count the frequency of each name
names = [dn.split(" ---- ")[0] for dn in dates_and_names]
engagement_count = len(names)

# Count the frequency of each date
dates = [datetime.strptime(dn.split(" ---- ")[1], '%d/%m/%Y') for dn in dates_and_names]
date_counts = collections.Counter(dates)

# Check if dates is empty
if not dates:
    print("Error: No dates found in the XML file.")
    exit()

# Group dates into days
start_date = min(dates)
end_date = max(dates)
current_date = start_date
day = 1
days = {}
while current_date <= end_date:
    day_dates = [d for d in dates if d == current_date]
    day_count = sum([date_counts[d] for d in day_dates])
    days[day] = day_count
    current_date += timedelta(days=1)
    day += 1

# Plot engagement over time (split by days) into a line chart
plt.plot(list(days.keys()), list(days.values()))
plt.xticks(range(len(days)), list(days.keys()), rotation=90)
plt.xlabel('Day')
plt.ylabel('Engagement')
plt.title('Engagement Over Time (Split by Days)')
plt.show()

# List of most engaged people over a period of time
top_names = name_counts.most_common(10)
print("Most engaged people over the period of time:")
for name, count in top_names:
    print("{}: {}".format(name, count))

# Output the total engagement
total_engagement = sum(date_counts.values())
print("Total engagement:", total_engagement)
