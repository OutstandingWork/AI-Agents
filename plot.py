import os
import matplotlib.pyplot as plt
import pandas as pd

def load_stock_data(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"{file_name} not found. Please check the download step.")
    
    try:
        df = pd.read_csv(file_name)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        return df
    except Exception as e:
        raise Exception(f"Error reading {file_name}: {e}")

# Debugging output
print("Loading NVDA data...")
nvda_file = 'nvda.csv'
tsla_file = 'tsla.csv'

df_nvda = load_stock_data(nvda_file)
df_tsla = load_stock_data(tsla_file)

# Debugging output
print("Data loaded successfully.")

plt.figure(figsize=(14, 7))
plt.plot(df_nvda.index, df_nvda['Close'], label='NVDA')
plt.plot(df_tsla.index, df_tsla['Close'], label='TSLA')

plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('NVDA and TSLA Stock Price Change YTD')
plt.legend()
plt.show()
