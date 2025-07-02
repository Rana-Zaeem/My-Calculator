import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta
import time
import plotly.graph_objects as go

# Set page configuration for Streamlit app
st.set_page_config(
    page_title="Interactive Age Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling the app
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4CAF50;
        margin-top: 1.5rem;
    }
    .highlight {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
    }
    .result-card {
        background-color: #f0f8ff;
        padding: 2rem;
        border-radius: 10px;
        border: 2px solid #4CAF50;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1E88E5;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with app info and instructions
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/calendar-app.png")
    st.markdown("## About the App")
    st.info("""
    This advanced age calculator helps you determine your exact age with precision down to the second.
    
    **Features:**
    - Calculate age between any dates from 1900 to 2100
    - Account for leap years and time differences
    - Visualize age breakdown
    - Get precise measurements in years, months, days, hours, minutes, and seconds
    """)
    
    st.markdown("### How to use")
    st.markdown("""
    1. Enter your birth date and time
    2. Choose to use current time or a custom date
    3. Click "Calculate Age"
    4. View your detailed age breakdown
    """)

# Main app header and description
st.markdown("<h1 class='main-header'>✨ Interactive Age Calculator ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Calculate your precise age including years, months, days, hours, minutes, and seconds</p>", unsafe_allow_html=True)

# Set min and max dates for the date picker (1900 to 2100)
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2100, 12, 31)

# Get current date and time
current_datetime = datetime.datetime.now()

# --- Birth Information Section ---
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>🎂 Birth Information</h2>", unsafe_allow_html=True)

# Two columns for date and time inputs
birth_col1, birth_col2 = st.columns([3, 2])

with birth_col1:
    # Default to January 1, 2000 as a reasonable starting point
    default_date = datetime.date(2000, 1, 1)
    birth_date = st.date_input(
        "Select your birth date:",
        min_value=min_date,
        max_value=max_date,
        value=default_date,
        key="birth_date"
    )

with birth_col2:
    # Time presets for quick selection
    time_presets = st.selectbox(
        "Time presets:",
        ["Custom time", "Morning (8:00 AM)", "Noon (12:00 PM)", "Evening (6:00 PM)", "Night (10:00 PM)"]
    )
    
    # Set default time values based on preset
    if time_presets == "Morning (8:00 AM)":
        default_hour, default_minute, default_second = 8, 0, 0
    elif time_presets == "Noon (12:00 PM)":
        default_hour, default_minute, default_second = 12, 0, 0
    elif time_presets == "Evening (6:00 PM)":
        default_hour, default_minute, default_second = 18, 0, 0
    elif time_presets == "Night (10:00 PM)":
        default_hour, default_minute, default_second = 22, 0, 0
    else:
        default_hour, default_minute, default_second = 0, 0, 0

# Time inputs for birth in three columns
birth_time_col1, birth_time_col2, birth_time_col3 = st.columns(3)
with birth_time_col1:
    birth_hour = st.number_input("Birth Hour (0-23):", min_value=0, max_value=23, value=default_hour, key="birth_hour")
with birth_time_col2:
    birth_minute = st.number_input("Birth Minute (0-59):", min_value=0, max_value=59, value=default_minute, key="birth_minute")
with birth_time_col3:
    birth_second = st.number_input("Birth Second (0-59):", min_value=0, max_value=59, value=default_second, key="birth_second")

# Combine date and time for birth
birth_datetime = datetime.datetime.combine(
    birth_date, 
    datetime.time(hour=birth_hour, minute=birth_minute, second=birth_second)
)

# Display selected birth datetime in a friendly format
st.info(f"Selected birth date and time: **{birth_datetime.strftime('%A, %B %d, %Y at %I:%M:%S %p')}**")
st.markdown("</div>", unsafe_allow_html=True)

# --- Calculation Reference Date Section ---
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>📆 Calculation Reference Date</h2>", unsafe_allow_html=True)

# Option to use current date/time or custom date/time
use_current = st.toggle("Use current date and time", value=True)

if use_current:
    calculation_datetime = current_datetime
    st.success(f"Using current date and time: **{current_datetime.strftime('%A, %B %d, %Y at %I:%M:%S %p')}**")
else:
    # Custom date and time inputs in columns
    calc_col1, calc_col2 = st.columns([3, 2])
    
    with calc_col1:
        calc_date = st.date_input(
            "Select calculation date:",
            min_value=min_date,
            max_value=max_date,
            value=current_datetime.date(),
            key="calc_date"
        )
    
    with calc_col2:
        # Time presets for calculation date
        calc_time_presets = st.selectbox(
            "Time presets:",
            ["Custom time", "Morning (8:00 AM)", "Noon (12:00 PM)", "Evening (6:00 PM)", "Night (10:00 PM)"],
            key="calc_time_presets"
        )
        
        # Set default time values based on preset
        if calc_time_presets == "Morning (8:00 AM)":
            default_calc_hour, default_calc_minute, default_calc_second = 8, 0, 0
        elif calc_time_presets == "Noon (12:00 PM)":
            default_calc_hour, default_calc_minute, default_calc_second = 12, 0, 0
        elif calc_time_presets == "Evening (6:00 PM)":
            default_calc_hour, default_calc_minute, default_calc_second = 18, 0, 0
        elif calc_time_presets == "Night (10:00 PM)":
            default_calc_hour, default_calc_minute, default_calc_second = 22, 0, 0
        else:
            default_calc_hour = current_datetime.hour
            default_calc_minute = current_datetime.minute
            default_calc_second = current_datetime.second
    
    # Time inputs for calculation date
    calc_time_col1, calc_time_col2, calc_time_col3 = st.columns(3)
    with calc_time_col1:
        calc_hour = st.number_input("Hour (0-23):", min_value=0, max_value=23, value=default_calc_hour, key="calc_hour")
    with calc_time_col2:
        calc_minute = st.number_input("Minute (0-59):", min_value=0, max_value=59, value=default_calc_minute, key="calc_minute")
    with calc_time_col3:
        calc_second = st.number_input("Second (0-59):", min_value=0, max_value=59, value=default_calc_second, key="calc_second")
    
    # Combine date and time for calculation
    calculation_datetime = datetime.datetime.combine(
        calc_date, 
        datetime.time(hour=calc_hour, minute=calc_minute, second=calc_second)
    )
    
    # Display selected calculation datetime in a friendly format
    st.info(f"Selected calculation date and time: **{calculation_datetime.strftime('%A, %B %d, %Y at %I:%M:%S %p')}**")

st.markdown("</div>", unsafe_allow_html=True)

# --- Calculate Button ---
st.markdown("<div style='text-align: center; margin: 30px 0;'>", unsafe_allow_html=True)
calculate_button = st.button("✨ Calculate My Age ✨", use_container_width=True, type="primary")
st.markdown("</div>", unsafe_allow_html=True)

if calculate_button:
    # Show spinner while calculating
    with st.spinner("Calculating your age with precision..."):
        time.sleep(0.8)  # Small delay for visual effect
    
    # Ensure birth date is before calculation date
    if birth_datetime > calculation_datetime:
        st.error("⚠️ Birth date and time must be before the calculation date and time! Please adjust your inputs.")
    else:
        # Calculate age using relativedelta for accurate years/months
        delta = relativedelta(calculation_datetime, birth_datetime)
        
        # Calculate seconds since birth
        seconds_diff = int((calculation_datetime - birth_datetime).total_seconds())
        
        # Constants for conversions
        seconds_in_minute = 60
        seconds_in_hour = 3600
        seconds_in_day = 86400
        days_in_month = 30.44  # Average
        days_in_year = 365.25  # Including leap years
        
        # Extract age components
        years_val = delta.years
        months_val = delta.months
        days_val = delta.days
        hours_val = delta.hours
        minutes_val = delta.minutes
        seconds_val = delta.seconds
        
        # Display results in a styled card
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #4CAF50;'>🎉 Your Precise Age 🎉</h2>", unsafe_allow_html=True)
        
        # Main age display
        st.markdown(f"""
        <div style='text-align: center; font-size: 1.8rem; margin: 1.5rem 0; padding: 1rem; background-color: #e8f5e9; border-radius: 10px;'>
            <span style='color: #2E7D32; font-weight: bold;'>{years_val}</span> years, 
            <span style='color: #2E7D32; font-weight: bold;'>{months_val}</span> months, 
            <span style='color: #2E7D32; font-weight: bold;'>{days_val}</span> days, 
            <span style='color: #2E7D32; font-weight: bold;'>{hours_val}</span> hours, 
            <span style='color: #2E7D32; font-weight: bold;'>{minutes_val}</span> minutes, and 
            <span style='color: #2E7D32; font-weight: bold;'>{seconds_val}</span> seconds
        </div>
        """, unsafe_allow_html=True)
        
        # Create two columns for metrics and visualization
        col1, col2 = st.columns([1, 1])
        
        # --- Metrics Column ---
        with col1:
            st.markdown("### Lifetime Statistics")
            
            # Create a metrics grid
            metric_cols1, metric_cols2 = st.columns(2)
            
            with metric_cols1:
                st.metric("Total Years", f"{years_val}")
                st.metric("Total Days", f"{(calculation_datetime - birth_datetime).days:,}")
                st.metric("Total Hours", f"{int(seconds_diff / 3600):,}")
            
            with metric_cols2:
                st.metric("Total Months", f"{years_val * 12 + months_val}")
                st.metric("Total Weeks", f"{int((calculation_datetime - birth_datetime).days / 7):,}")
                st.metric("Total Minutes", f"{int(seconds_diff / 60):,}")
            
            st.metric("Total Seconds Lived", f"{seconds_diff:,}")
            
            # Calculate heartbeats (average 70 bpm)
            heartbeats = int(seconds_diff / 60 * 70)
            st.metric("Estimated Heartbeats", f"{heartbeats:,}", 
                     help="Based on average resting heart rate of 70 beats per minute")
            
            # Calculate breaths (average 12 breaths per minute)
            breaths = int(seconds_diff / 60 * 12)
            st.metric("Estimated Breaths", f"{breaths:,}",
                     help="Based on average respiratory rate of 12 breaths per minute")
        
        # --- Visualization Column ---
        with col2:
            st.markdown("### Age Breakdown")
            
            # Create pie chart for age breakdown
            labels = ['Years', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds']
            
            # Convert all to seconds for proportional representation
            values = [
                years_val * days_in_year * seconds_in_day,
                months_val * days_in_month * seconds_in_day,
                days_val * seconds_in_day,
                hours_val * seconds_in_hour,
                minutes_val * seconds_in_minute,
                seconds_val
            ]
            
            # Only include non-zero values
            filtered_labels = [label for label, value in zip(labels, values) if value > 0]
            filtered_values = [value for value in values if value > 0]
            
            # Create a colorful pie chart
            fig = go.Figure(data=[go.Pie(
                labels=filtered_labels,
                values=filtered_values,
                hole=.3,
                marker_colors=['#1E88E5', '#43A047', '#FBC02D', '#E53935', '#8E24AA', '#00ACC1']
            )])
            
            fig.update_layout(
                title_text="Age Components",
                showlegend=True,
                height=300,
                margin=dict(t=40, b=0, l=0, r=0)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Age percentage visual using a gauge chart
            # Assuming average lifespan of 80 years
            lifespan_years = 80
            age_percentage = min(100, (years_val + (months_val / 12)) / lifespan_years * 100)
            
            gauge_fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = age_percentage,
                title = {'text': "Life Journey"},
                gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1},
                    'bar': {'color': "#43A047"},
                    'steps': [
                        {'range': [0, 25], 'color': "#e8f5e9"},
                        {'range': [25, 50], 'color': "#c8e6c9"},
                        {'range': [50, 75], 'color': "#a5d6a7"},
                        {'range': [75, 100], 'color': "#81c784"}
                    ],
                }
            ))
            
            gauge_fig.update_layout(
                height=250,
                margin=dict(t=40, b=0, l=0, r=0)
            )
            
            st.plotly_chart(gauge_fig, use_container_width=True)
        
        # --- Fun Facts Section ---
        st.markdown("### 🎨 Fun Age Facts")
        
        fact_col1, fact_col2, fact_col3 = st.columns(3)
        
        with fact_col1:
            # Earth orbits
            st.markdown(f"🌍 **Earth Orbits**: You've been around the Sun approximately **{years_val}** times!")
            
        with fact_col2:
            # Moon phases
            moon_cycles = int((calculation_datetime - birth_datetime).days / 29.53)
            st.markdown(f"🌙 **Moon Phases**: You've experienced about **{moon_cycles}** complete lunar cycles.")
            
        with fact_col3:
            # Seasonal changes
            seasons = int(years_val * 4 + (months_val / 3))
            st.markdown(f"🍂 **Seasons**: You've lived through approximately **{seasons}** seasons.")
        
        st.markdown("</div>", unsafe_allow_html=True)
                
else:
    # Initial state message before calculation
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background-color: #f5f5f5; border-radius: 10px; margin-top: 2rem;'>
        <img src="https://img.icons8.com/fluency/96/000000/hourglass.png" style='width: 64px;'>
        <h3>Enter your birth information and click "Calculate My Age" to see your detailed age breakdown.</h3>
        <p>This advanced calculator will determine your precise age including years, months, days, hours, minutes, and seconds.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer with copyright
st.markdown("""
<div style='text-align: center; margin-top: 3rem; padding: 1rem; font-size: 0.8rem; color: #666;'>
    <p>© 2025 Advanced Age Calculator | Accounts for leap years and precise time calculations</p>
</div>
""", unsafe_allow_html=True)
