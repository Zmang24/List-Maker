import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Monday.com configuration
MONDAY_API_TOKEN = os.getenv('MONDAY_API_TOKEN')
MONDAY_API_URL = 'https://api.monday.com/v2'

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///si_tracker.db')

# Application settings
APP_NAME = "ID3 Team SI Tracker"
APP_VERSION = "0.1.0"

# UI Configuration
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 800

# Colors - Updated for better contrast
COLORS = {
    'primary': '#1976D2',         # Darker blue
    'secondary': '#424242',       # Darker gray
    'background': '#FFFFFF',      # White
    'sidebar': '#E8EAF6',         # Light indigo
    'hover': '#C5CAE9',          # Slightly darker hover
    'border': '#9FA8DA',         # Indigo border
    'text': '#000000',           # Black text
    'text_secondary': '#424242',  # Dark gray text
    'button_text': '#FFFFFF',     # White text for buttons
    'error': '#D32F2F',          # Error red
    'success': '#388E3C',        # Success green
    'warning': '#F57C00'         # Warning orange
}

# Font settings
FONTS = {
    'family': 'Segoe UI',
    'size': {
        'small': 9,
        'normal': 10,
        'large': 12,
        'header': 14
    },
    'weight': {
        'normal': 400,
        'medium': 500,
        'bold': 600
    }
} 