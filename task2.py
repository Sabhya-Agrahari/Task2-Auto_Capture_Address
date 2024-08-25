import tkinter as tk
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderInsufficientPrivileges

def get_current_address():
    try:
        # For demonstration, using hardcoded coordinates
        latitude =  26.4789045
        longitude = 80.388953

        geolocator = Nominatim(user_agent="your_app_name")
        location = geolocator.reverse((latitude, longitude))
        return location.address
    except GeocoderInsufficientPrivileges as e:
        return f"Error: {e}"

def fill_delivery_address():
    current_address = get_current_address()
    delivery_address_entry.delete(0, tk.END)
    delivery_address_entry.insert(0, current_address)

# Create the main application window
app = tk.Tk()
app.title("Delivery Address Auto Fill")
app.geometry('1000x800')
app.resizable(False, False)

canvas = tk.Canvas(app,bg="white", width=600, height=420)
canvas.place(x=50,y=20)
canvas.pack()


heading_text = "Fill Address"
canvas.create_text(350, 40, text=heading_text, font=("Helvetica", 20), fill="blue")


# Label to display current address
current_address_label = tk.Label(canvas, text="Current Address:",padx=10, pady=5)
canvas.create_window(100, 90, window=current_address_label)
current_address_entry=tk.Entry(canvas, width=50)
canvas.create_window(350, 90, window=current_address_entry)



# Label for delivery address
delivery_address_label = tk.Label(canvas, text="Delivery Address:",padx=10, pady=5)
canvas.create_window(100, 140, window=delivery_address_label)
delivery_address_entry = tk.Entry(canvas, width=50)
canvas.create_window(350, 140, window=delivery_address_entry)

# Button to fill delivery address
button = tk.Button(app, text="Fill Delivery Address", command=fill_delivery_address)
canvas.create_window(350, 190, window=button)


# Set the current address in the entry widget
current_address_entry.insert(0, get_current_address())

# Start the GUI event loop
app.mainloop()
