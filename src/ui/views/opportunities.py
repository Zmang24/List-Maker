from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem,
    QComboBox, QLineEdit, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from src.config import COLORS, FONTS

class OpportunitiesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Header section
        header_layout = QHBoxLayout()
        
        # Title
        title = QLabel("SI Opportunities")
        title.setFont(QFont(FONTS['family'], FONTS['size']['header'], FONTS['weight']['bold']))
        header_layout.addWidget(title)
        
        # Add New button
        add_btn = QPushButton("+ New Opportunity")
        add_btn.setFont(QFont(FONTS['family'], FONTS['size']['normal'], FONTS['weight']['medium']))
        add_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {COLORS['primary']};
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: {COLORS['secondary']};
            }}
        """)
        header_layout.addStretch()
        header_layout.addWidget(add_btn)
        
        main_layout.addLayout(header_layout)
        
        # Filters section
        filters_layout = QHBoxLayout()
        filters_layout.setSpacing(10)
        
        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search opportunities...")
        self.search_box.setStyleSheet(f"""
            QLineEdit {{
                padding: 8px;
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                background-color: white;
            }}
        """)
        filters_layout.addWidget(self.search_box)
        
        # Status filter
        self.status_filter = QComboBox()
        self.status_filter.addItems(["All Status", "New", "In Progress", "Completed", "On Hold"])
        self.status_filter.setStyleSheet(f"""
            QComboBox {{
                padding: 8px;
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                background-color: white;
            }}
        """)
        filters_layout.addWidget(self.status_filter)
        
        # Priority filter
        self.priority_filter = QComboBox()
        self.priority_filter.addItems(["All Priority", "High", "Medium", "Low"])
        self.priority_filter.setStyleSheet(f"""
            QComboBox {{
                padding: 8px;
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                background-color: white;
            }}
        """)
        filters_layout.addWidget(self.priority_filter)
        
        main_layout.addLayout(filters_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setFrameShape(QFrame.Shape.NoFrame)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Title", "Status", "Priority", "Team Member", "Due Date", "Actions"
        ])
        
        # Sample data
        sample_data = [
            ["Project Alpha", "In Progress", "High", "John Doe", "2024-02-01", ""],
            ["Project Beta", "New", "Medium", "Jane Smith", "2024-02-15", ""],
            ["Project Gamma", "Completed", "Low", "Bob Wilson", "2024-01-30", ""],
        ]
        
        self.table.setRowCount(len(sample_data))
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                item.setFont(QFont(FONTS['family'], FONTS['size']['normal']))
                self.table.setItem(row, col, item)
        
        # Style the table
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: white;
                gridline-color: {COLORS['border']};
            }}
            QHeaderView::section {{
                background-color: {COLORS['sidebar']};
                padding: 8px;
                border: none;
                font-weight: bold;
            }}
        """)
        
        # Adjust column widths
        self.table.horizontalHeader().setStretchLastSection(True)
        for i in range(self.table.columnCount() - 1):
            self.table.horizontalHeader().setSectionResizeMode(i, self.table.horizontalHeader().ResizeMode.ResizeToContents)
        
        main_layout.addWidget(self.table) 