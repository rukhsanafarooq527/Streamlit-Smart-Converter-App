import streamlit as st

# Page Config
st.set_page_config(page_title="Smart Converter App", page_icon="🧠", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f6f7;
    }
    .category-box {
        border: 2px solid #1ABC9C;
        padding: 10px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        padding: 10px;
        color: gray;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Smart Unit Converter & Tools")

# Session state to control button clicks
if 'selected_tool' not in st.session_state:
    st.session_state.selected_tool = None

def set_tool(tool_name):
    st.session_state.selected_tool = tool_name

# === Common Section ===
st.subheader("🟢 Common Conversions")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⚖️ Weight"):
            set_tool("Weight")
        if st.button("📏 Length"):
            set_tool("Length")
        if st.button("💨 Speed"):
            set_tool("Speed")
    with col2:
        if st.button("⛽ Fuel"):
            set_tool("Fuel")
        if st.button("💵 Currency"):
            set_tool("Currency")
        if st.button("🍳 Cooking"):
            set_tool("Cooking")
    with col3:
        if st.button("🌍 Area"):
            set_tool("Area")
        if st.button("🧃 Volume"):
            set_tool("Volume")
        if st.button("🔣 Prefix"):
            set_tool("Prefix")
            

# === Engineering Section ===
st.subheader("🔴 Engineering Conversions")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌡️ Temperature"):
            set_tool("Temperature")
        if st.button("📐 Angle"):
            set_tool("Angle")
        if st.button("🔵 Pressure"):
            set_tool("Pressure")
    with col2:
        if st.button("💪 Force"):
            set_tool("Force")
        if st.button("🔍 Torque"):
            set_tool("Torque")
        if st.button("🔊 Sound"):
            set_tool("Sound")
    with col3:
        if st.button("🧱 Density"):
            set_tool("Density")
        if st.button("🔥 Heat Density"):
            set_tool("Heat Density")
        if st.button("⚙️ Inertia"):
            set_tool("Inertia")

# === Tools Section ===
st.subheader("🧰 Tools")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🧭 Compass"):
            set_tool("Compass")
        if st.button("📏 Bubble Level"):
            set_tool("Bubble Level")
        if st.button("🌀 Inductor Codes"):
            set_tool("Inductor Codes")
    with col2:
        if st.button("🔴 Resistor Codes"):
            set_tool("Resistor Codes")
        if st.button("🧬 Periodic Table"):
            set_tool("Periodic Table")
        if st.button("🔡 Case Converter"):
            set_tool("Case Converter")
    with col3:
        if st.button("🔐 Cryptography"):
            set_tool("Cryptography")
        if st.button("🔋 Battery Status"):
            set_tool("Battery Status")
        if st.button("🌐 Time Zone"):
            set_tool("Time Zone")

# === Render Selected Tool ===
st.markdown("---")
tool = st.session_state.selected_tool

if tool == "Weight":
    st.header("⚖️ Weight Converter")
    weight = st.number_input("Enter weight in kilograms:")
    st.write(f"Grams: {weight * 1000} g")
    st.write(f"Pounds: {weight * 2.20462} lbs")
    st.write(f"Ounces: {weight * 35.274} oz")

elif tool == "Length":
    st.header("📏 Length Converter")
    length_km = st.number_input("Enter length in kilometers:")
    st.write(f"Meters: {length_km * 1000} m")
    st.write(f"Centimeters: {length_km * 100000} cm")
    st.write(f"Miles: {length_km * 0.621371} miles")

elif tool == "Speed":
    st.header("💨 Speed Converter")
    speed_kph = st.number_input("Enter speed in kilometers per hour (km/h):")
    st.write(f"Meters per second: {speed_kph / 3.6} m/s")
    st.write(f"Miles per hour: {speed_kph * 0.621371} mph")
    st.write(f"Knots: {speed_kph * 0.539957} knots")

elif tool == "Currency":
    st.header("💵 Currency Converter")
    amount_pkr = st.number_input("Enter amount in Pakistani Rupees (PKR):")
    usd_rate = 280  # Example fixed rate
    eur_rate = 300
    st.write(f"US Dollars (USD): {amount_pkr / usd_rate:.2f}")
    st.write(f"Euros (EUR): {amount_pkr / eur_rate:.2f}")

elif tool == "Calculator":
    st.header("🧮 Simple Calculator")
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter First Number", key="num1")
    with col2:
        num2 = st.number_input("Enter Second Number", key="num2")

    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Undefined"
        st.success(f"Result: {result}")

elif tool == "Fuel":
    st.header("⛽ Fuel Efficiency Converter")
    fuel_kmpl = st.number_input("Enter fuel efficiency in kilometers per liter (km/l):")
    st.write(f"Miles per gallon (US): {fuel_kmpl * 2.35215:.2f} mpg")
    st.write(f"Miles per gallon (UK): {fuel_kmpl * 2.82481:.2f} mpg (UK)")
    st.write(f"Liters per 100km: {100 / fuel_kmpl if fuel_kmpl != 0 else 'Undefined'} L/100km")

elif tool == "Area":
    st.header("🌍 Area Converter")
    area_sq_m = st.number_input("Enter area in square meters:")
    st.write(f"Square Kilometers: {area_sq_m / 1e6} km²")
    st.write(f"Hectares: {area_sq_m / 10000} ha")
    st.write(f"Acres: {area_sq_m * 0.000247105} acres")

elif tool == "Volume":
    st.header("🧃 Volume Converter")
    volume_liters = st.number_input("Enter volume in liters:")
    st.write(f"Milliliters: {volume_liters * 1000} ml")
    st.write(f"Cubic Meters: {volume_liters / 1000} m³")
    st.write(f"Gallons (US): {volume_liters * 0.264172} gal")

elif tool == "Cooking":
    st.header("🍳 Cooking Measurement Converter")
    quantity_cups = st.number_input("Enter quantity in cups:")
    st.write(f"Tablespoons: {quantity_cups * 16} tbsp")
    st.write(f"Teaspoons: {quantity_cups * 48} tsp")
    st.write(f"Milliliters: {quantity_cups * 236.588} ml")
    st.write(f"Liters: {quantity_cups * 0.236588} L")

elif tool == "Prefix":
    st.header("🔣 Metric Prefix Converter")
    number = st.number_input("Enter base value (in meters/grams/bytes etc.):")
    st.write(f"Kilo (k): {number * 1e3}")
    st.write(f"Mega (M): {number * 1e6}")
    st.write(f"Giga (G): {number * 1e9}")
    st.write(f"Milli (m): {number * 1e-3}")
    st.write(f"Micro (µ): {number * 1e-6}")
    st.write(f"Nano (n): {number * 1e-9}")

# === Engineering Section Functionality ===

elif tool == "Temperature":
    st.header("🌡️ Temperature Converter")
    celsius = st.number_input("Enter temperature in Celsius:")
    st.write(f"Fahrenheit: {(celsius * 9/5) + 32} °F")
    st.write(f"Kelvin: {celsius + 273.15} K")

elif tool == "Angle":
    st.header("📐 Angle Converter")
    degrees = st.number_input("Enter angle in degrees:")
    st.write(f"Radians: {degrees * 3.14159 / 180} rad")
    st.write(f"Gradians: {degrees * (10/9)} grad")

elif tool == "Pressure":
    st.header("🔵 Pressure Converter")
    pascal = st.number_input("Enter pressure in Pascals:")
    st.write(f"Bar: {pascal / 100000} bar")
    st.write(f"Atmosphere: {pascal / 101325} atm")
    st.write(f"PSI: {pascal / 6894.76} psi")

elif tool == "Force":
    st.header("💪 Force Converter")
    newton = st.number_input("Enter force in Newtons:")
    st.write(f"Kilogram-force: {newton / 9.80665} kgf")
    st.write(f"Pound-force: {newton * 0.224809} lbf")

elif tool == "Torque":
    st.header("🔍 Torque Converter")
    torque_nm = st.number_input("Enter torque in Newton-meters:")
    st.write(f"Pound-foot: {torque_nm * 0.737562} lb·ft")
    st.write(f"Pound-inch: {torque_nm * 8.85075} lb·in")

elif tool == "Sound":
    st.header("🔊 Sound Level (dB) Calculator")
    intensity = st.number_input("Enter intensity (W/m²):")
    if intensity > 0:
        db = 10 * (st.math.log10(intensity / 1e-12))
        st.write(f"Sound Level: {db} dB")
    else:
        st.warning("Intensity must be greater than 0.")

elif tool == "Density":
    st.header("🧱 Density Converter")
    density = st.number_input("Enter density in kg/m³:")
    st.write(f"g/cm³: {density / 1000}")
    st.write(f"lb/ft³: {density * 0.062428}")

elif tool == "Heat Density":
    st.header("🔥 Heat Density Converter")
    heat_density = st.number_input("Enter heat density in J/m³:")
    st.write(f"kJ/m³: {heat_density / 1000}")
    st.write(f"cal/cm³: {heat_density / 41860}")

elif tool == "Inertia":
    st.header("⚙️ Moment of Inertia Converter")
    inertia = st.number_input("Enter inertia in kg·m²:")
    st.write(f"g·cm²: {inertia * 1e7}")
    st.write(f"lb·ft²: {inertia * 0.737562}")

# === Tools Section ===

elif tool == "Compass":
    st.header("🧭 Compass")
    st.info("Compass functionality is limited in Streamlit. Try using a mobile app or device with sensors.")


elif tool == "Bubble Level":
    st.header("📏 Bubble Level")
    st.info("Bubble level requires device sensors, which are not supported in Streamlit web apps.")

elif tool == "Inductor Codes":
    st.header("🌀 Inductor Color Code Calculator")
    st.write("Select colors to decode inductor values.")
    st.warning("Coming soon! This tool is under development.")

elif tool == "Resistor Codes":
    st.header("🔴 Resistor Color Code Calculator")
    st.write("Select bands to decode resistor values.")
    st.warning("Coming soon! This tool is under development.")

elif tool == "Periodic Table":
    st.header("🧬 Periodic Table")
    st.markdown("Explore the [interactive periodic table](https://ptable.com/) 🔗")

elif tool == "Case Converter":
    st.header("🔡 Text Case Converter")
    text = st.text_area("Enter your text here:")
    st.write("UPPER CASE:", text.upper())
    st.write("lower case:", text.lower())
    st.write("Title Case:", text.title())
    st.write("Sentence case:", text.capitalize())

elif tool == "Cryptography":
    st.header("🔐 Simple Cryptography")
    action = st.radio("Choose action:", ["Encrypt", "Decrypt"])
    text = st.text_input("Enter text:")
    shift = st.slider("Shift (Caesar Cipher)", 1, 25, 3)

    def caesar_cipher(text, shift, encrypt=True):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift_val = shift if encrypt else -shift
                result += chr((ord(char) - base + shift_val) % 26 + base)
            else:
                result += char
        return result

    if st.button("Go"):
        if action == "Encrypt":
            result = caesar_cipher(text, shift, True)
        else:
            result = caesar_cipher(text, shift, False)
        st.success(f"Result: {result}")


elif tool == "Battery Status":
    st.header("🔋 Battery Status")
    st.info("Battery status is not accessible in web apps. Try a native app for real battery info.")

elif tool == "Time Zone":
    st.header("🌐 Time Zone Converter")
    import pytz
    from datetime import datetime

    timezones = pytz.all_timezones
    from_zone = st.selectbox("From Time Zone", timezones, index=timezones.index("UTC"))
    to_zone = st.selectbox("To Time Zone", timezones, index=timezones.index("Asia/Karachi"))

    input_time = st.time_input("Select Time")
    today = datetime.today().date()
    dt = datetime.combine(today, input_time)

    from_zone_obj = pytz.timezone(from_zone)
    to_zone_obj = pytz.timezone(to_zone)

    dt_aware = from_zone_obj.localize(dt)
    converted = dt_aware.astimezone(to_zone_obj)
    st.success(f"Converted Time: {converted.strftime('%Y-%m-%d %H:%M:%S')}")

elif tool:
    st.info(f"{tool} tool will be added soon. Stay tuned! 🚀")








# === Footer ===
st.markdown('<div class="footer">Made with ❤️ by Rukhsana Shaheen | rukhsanafsarooq527@gmail.com</div>', unsafe_allow_html=True)
