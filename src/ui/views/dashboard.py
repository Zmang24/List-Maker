from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame, QScrollArea, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from src.config import COLORS, FONTS

class StatCard(QFrame):
    def __init__(self, title, value, subtitle=None):
        super().__init__()
        self.setObjectName("statCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        
        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont(FONTS['family'], FONTS['size']['normal'], FONTS['weight']['medium']))
        title_label.setStyleSheet(f"color: {COLORS['text_secondary']};")
        layout.addWidget(title_label)
        
        # Value
        value_label = QLabel(str(value))
        value_label.setFont(QFont(FONTS['family'], FONTS['size']['header'], FONTS['weight']['bold']))
        layout.addWidget(value_label)
        
        # Subtitle (optional)
        if subtitle:
            sub_label = QLabel(subtitle)
            sub_label.setFont(QFont(FONTS['family'], FONTS['size']['small']))
            sub_label.setStyleSheet(f"color: {COLORS['text_secondary']};")
            layout.addWidget(sub_label)
        
        self.setStyleSheet(f"""
            QFrame#statCard {{
                background-color: white;
                border: 1px solid {COLORS['border']};
                border-radius: 8px;
            }}
        """)

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Header
        header = QLabel("Dashboard")
        header.setFont(QFont(FONTS['family'], FONTS['size']['header'], FONTS['weight']['bold']))
        main_layout.addWidget(header)
        
        # Stats section
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(15)
        
        # Add stat cards
        stats_layout.addWidget(StatCard("Total Opportunities", "24", "Last 30 days"))
        stats_layout.addWidget(StatCard("In Progress", "12", "Active opportunities"))
        stats_layout.addWidget(StatCard("Completed", "8", "This month"))
        stats_layout.addWidget(StatCard("Success Rate", "75%", "Last quarter"))
        
        main_layout.addLayout(stats_layout)
        
        # Recent Activity Section
        activity_label = QLabel("Recent Activity")
        activity_label.setFont(QFont(FONTS['family'], FONTS['size']['large'], FONTS['weight']['medium']))
        main_layout.addWidget(activity_label)
        
        # Activity list in a scrollable area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        activity_widget = QWidget()
        activity_layout = QVBoxLayout(activity_widget)
        
        # Add some sample activity items
        activities = [
            "New SI opportunity added - Project Alpha",
            "Status updated for Project Beta",
            "Report generated for Q3 opportunities",
            "Team meeting scheduled for Project Gamma"
        ]
        
        for activity in activities:
            item = QLabel(activity)
            item.setFont(QFont(FONTS['family'], FONTS['size']['normal']))
            item.setStyleSheet(f"""
                padding: 10px;
                background-color: {COLORS['background']};
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                margin: 2px 0;
            """)
            activity_layout.addWidget(item)
        
        activity_layout.addStretch()
        scroll.setWidget(activity_widget)
        main_layout.addWidget(scroll)
        
        # Set stretch factor for scroll area
        main_layout.setStretch(main_layout.count() - 1, 1) 