import pandas as pd

data = {
    'Date_Column': ['2026-06-24', '2026-06-25', '2026-06-26', '2026-06-27', '2026-06-28']
}
df = pd.DataFrame(data)

df['Date_Column'] = pd.to_datetime(df['Date_Column'], errors='coerce')

df['Year'] = df['Date_Column'].dt.year
df['Month'] = df['Date_Column'].dt.month
df['Day'] = df['Date_Column'].dt.day
df['Weekday'] = df['Date_Column'].dt.weekday
df['Month_Name'] = df['Date_Column'].dt.strftime('%B')
df['Quarter'] = df['Date_Column'].dt.quarter
df['Is_Weekend'] = df['Date_Column'].dt.weekday.isin([5, 6])

print(df)