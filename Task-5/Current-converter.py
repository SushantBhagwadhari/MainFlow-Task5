import tkinter as tk
import requests

# Function to get the latest exchange rates from Fixer.io
def get_exchange_rate():
    api_key = "c41d6e0cf1007ad816a2324c6dd469ce"
    url = f"http://data.fixer.io/api/latest?access_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get('success'):
        return data['rates']
    else:
        return None

# Function to convert USD to the selected currency
def convert_currency(currency_code):
    try:
        usd_amount = float(entry.get())
        
        rates = get_exchange_rate()
        if rates:
            usd_to_eur = 1 / rates['USD']  # Convert USD to EUR
            eur_to_target = rates[currency_code]  # Convert EUR to the target currency
            
            usd_to_target_rate = usd_to_eur * eur_to_target
            converted_amount = usd_amount * usd_to_target_rate
            
            result_label.config(text=f"{usd_amount} USD = {converted_amount:.2f} {currency_code}")
        else:
            result_label.config(text="Error fetching exchange rate")
    except ValueError:
        result_label.config(text="Please enter a valid number")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Set up the GUI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x200")  # Set a fixed window size

# Add padding and spacing
padding = {'padx': 10, 'pady': 10}

tk.Label(root, text="Enter amount in USD:").grid(row=0, column=0, columnspan=2, **padding)
entry = tk.Entry(root)
entry.grid(row=0, column=2, columnspan=3, **padding)

tk.Label(root, text="Choose currency:").grid(row=1, column=0, columnspan=5, **padding)

# Add buttons for each currency and remove the Convert button
currencies = ["EUR", "GBP", "JPY", "INR", "RUB"]
for i, currency in enumerate(currencies):
    tk.Button(root, text=currency, command=lambda c=currency: convert_currency(c)).grid(row=2, column=i, **padding)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=5, **padding)

root.mainloop()
