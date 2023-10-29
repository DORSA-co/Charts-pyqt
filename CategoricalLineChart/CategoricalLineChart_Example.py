from doctest import FAIL_FAST
from email.charset import QP
import time
from PySide6.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QPushButton
from CategoricalLineChart import Trend, CategoricalLineChart, Font
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_chart_widget = CategoricalLineChart(
                    chart_title = 'TEST',
                    chart_title_color = 'white',
                    chart_title_font = Font('Arial', 20, True),
                    axisX_label = 'Rages',
                    axisY_label = 'Percents',
                    chart_background_color = 'black',
                    chart_legend=True,
                    chart_legend_alignment='BOTTOM',
                    chart_legend_color='white',
                    axis_color = 'white',
                    axis_font=Font('Times New Roman', 10, False),
                    axisX_grid=False,
                    axisY_grid=True,
                    axisX_grid_color='red',
                    axisY_grid_color='yellow',
                    axisX_range=(0, 5.5),
                    axisY_range = (0, 100),
                    axisY_tickCount = 10,
                    animation = True,
                )

        self.frame = QFrame()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.line_chart_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)
        self.resize(800, 600)

        x_values = ['2023-10-22', '2023-10-23', '2023-10-24', '2023-10-25', '2023-10-27', '2023-10-29']
        y_values = [5, 10, 20, 40, 0, 80]
        
        trend1 = Trend(name='Red', line_color='red', line_width=2)
        trend1.add_data(x_values, y_values)
        self.line_chart_widget.add_trend(trend1)

        x_values = ['a', 'b', 'c', 'd', 'e', 'f']
        y_values = [5, 21, 50, 74, 69, 100]
        
        trend2 = Trend(name='Blue', line_color='blue', line_width=5)
        trend2.add_data(x_values, y_values)
        self.line_chart_widget.add_trend(trend2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())