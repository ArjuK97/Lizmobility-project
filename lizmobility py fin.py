import yfinance as yf
import csv

# Fetch overview information for Canoo stock
canoo_stock = yf.Ticker("GOEV")
canoo_info = canoo_stock.info

# Save overview information to a CSV file
with open("canoo_overview.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Attribute", "Value"])
    for key, value in canoo_info.items():
        writer.writerow([key, value])
