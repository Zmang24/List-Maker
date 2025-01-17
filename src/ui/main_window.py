from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QPushButton, QStackedWidget,
    QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from src.config import COLORS, FONTS
from .views import DashboardView, OpportunitiesView

class NavButton(QPushButton):
    def __init__(self, text, icon_name=None):
        super().__init__(text)
        self.setFont(QFont(FONTS['family'], FONTS['size']['normal'], FONTS['weight']['medium']))
        self.setCheckable(True)
        if icon_name:
            self.setIcon(QIcon(f"assets/icons/{icon_name}"))
        self.setCursor(Qt.CursorShape.PointingHandCursor)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ID3 Team SI Tracker")
        self.setMinimumSize(1200, 800)
        
        # Set application-wide font
        self.setFont(QFont(FONTS['family'], FONTS['size']['normal']))
        
        # Main layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Navigation sidebar
        self.setup_navigation()
        layout.addWidget(self.nav_widget)
        
        # Main content area
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Header bar
        self.header_bar = QWidget()
        header_layout = QHBoxLayout(self.header_bar)
        header_layout.setContentsMargins(20, 10, 20, 10)
        
        self.header_title = QLabel("Dashboard")
        self.header_title.setFont(QFont(FONTS['family'], FONTS['size']['large'], FONTS['weight']['bold']))
        header_layout.addWidget(self.header_title)
        
        self.header_bar.setStyleSheet(f"""
            QWidget {{
                background-color: white;
                border-bottom: 1px solid {COLORS['border']};
            }}
        """)
        content_layout.addWidget(self.header_bar)
        
        # Content stack
        self.content_stack = QStackedWidget()
        content_layout.addWidget(self.content_stack)
        
        # Add views
        self.dashboard_view = DashboardView()
        self.opportunities_view = OpportunitiesView()
        
        self.content_stack.addWidget(self.dashboard_view)
        self.content_stack.addWidget(self.opportunities_view)
        
        layout.addWidget(content_widget)
        layout.setStretch(1, 4)  # Content area takes more space
        
        # Set the default view
        self.show_dashboard()
        
        # Apply global styles
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {COLORS['background']};
            }}
        """)
    
    def setup_navigation(self):
        self.nav_widget = QWidget()
        nav_layout = QVBoxLayout(self.nav_widget)
        nav_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        nav_layout.setSpacing(2)
        nav_layout.setContentsMargins(5, 20, 5, 20)
        
        # App title in nav bar
        app_title = QLabel("SI Tracker")
        app_title.setFont(QFont(FONTS['family'], FONTS['size']['large'], FONTS['weight']['bold']))
        app_title.setStyleSheet(f"color: {COLORS['primary']};")
        app_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav_layout.addWidget(app_title)
        
        nav_layout.addSpacing(30)
        
        # Navigation buttons
        self.nav_buttons = []
        self.add_nav_button("Dashboard", self.show_dashboard, "dashboard.png")
        self.add_nav_button("SI Opportunities", self.show_opportunities, "opportunities.png")
        self.add_nav_button("Reports", self.show_reports, "reports.png")
        self.add_nav_button("Settings", self.show_settings, "settings.png")
        
        # Push remaining buttons to bottom
        nav_layout.addStretch()
        
        # Profile section
        profile_widget = QWidget()
        profile_layout = QHBoxLayout(profile_widget)
        
        profile_label = QLabel("John Doe")
        profile_label.setFont(QFont(FONTS['family'], FONTS['size']['normal'], FONTS['weight']['medium']))
        profile_layout.addWidget(profile_label)
        
        nav_layout.addWidget(profile_widget)
        
        self.nav_widget.setMaximumWidth(250)
        self.nav_widget.setStyleSheet(f"""
            QWidget {{
                background-color: {COLORS['sidebar']};
                border-right: 1px solid {COLORS['border']};
            }}
            QPushButton {{
                text-align: left;
                padding: 12px 15px;
                border: none;
                border-radius: 6px;
                margin: 3px 5px;
                color: {COLORS['text']};
            }}
            QPushButton:hover {{
                background-color: {COLORS['hover']};
            }}
            QPushButton:checked {{
                background-color: {COLORS['primary']};
                color: {COLORS['button_text']};
            }}
        """)
    
    def add_nav_button(self, text, slot, icon_name=None):
        btn = NavButton(text, icon_name)
        self.nav_buttons.append(btn)
        self.nav_widget.layout().addWidget(btn)
        btn.clicked.connect(slot)
        btn.clicked.connect(lambda: self.update_header(text))
    
    def update_header(self, title):
        self.header_title.setText(title)
        
    def show_dashboard(self):
        self.content_stack.setCurrentWidget(self.dashboard_view)
        self.nav_buttons[0].setChecked(True)
        for btn in self.nav_buttons[1:]:
            btn.setChecked(False)
    
    def show_opportunities(self):
        self.content_stack.setCurrentWidget(self.opportunities_view)
        self.nav_buttons[1].setChecked(True)
        for btn in self.nav_buttons[::2]:
            btn.setChecked(False)
    
    def show_reports(self):
        # TODO: Implement reports view
        pass
    
    def show_settings(self):
        # TODO: Implement settings view
        pass 