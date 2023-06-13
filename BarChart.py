import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QChartView,
    QValueAxis,
)
from PySide6.QtGui import QPainter, QCursor
from PySide6.QtCharts import *
from PySide6.QtWidgets import *


class BarChart(QChart):
    """
    An implementation of Bar chart in Qt
    """

    def __init__(self, parent=None):
        super().__init__()
        self.__texts = []
        self.__bar_series = QBarSeries()
        self.__bar_set = None
        self.__all_dic = {}
        self.__bar_series.hovered.connect(
            lambda state, index: self.__barseries_hovered(state, index)
        )
        self.__tooltip = QToolTip()

    def add_ser(self, str, list):
        self.__bar_set = QBarSet(str)
        self.__bar_set.append(list)
        self.add_series(self.__bar_set)
        self.__texts.append(f"{str}: {list}")  # Show tooltip on Barchart
        self.__tooltip.showText(QCursor().pos(), "\n".join(self.__texts))
        self.__all_dic[str] = list

    def __barseries_hovered(self, state, index):
        if state:
            texts = []
            for key, values in self.__all_dic.items():
                if values[index] > 0:
                    texts.append(f"{key}: {values[index]}")
            self.__tooltip.showText(QCursor().pos(), "\n".join(texts))
        else:
            self.__tooltip.hideText()

    def add_series(self, sett):
        self.__bar_series.append(sett)

    def add_title(self, str):
        self.addSeries(self.__bar_series)
        self.setTitle(str)

    def add_axis_x(self, CategoryList, min, max, text=None):
        self.categories = CategoryList
        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.categories)
        # self._axis_x.setTitleText(title)
        self.addAxis(self._axis_x, Qt.AlignBottom)
        self.__bar_series.attachAxis(self._axis_x)
        self._axis_x.setRange(min, max)

    def add_axis_y(self, min, max, text=None):
        self._axis_y = QValueAxis()
        self.addAxis(self._axis_y, Qt.AlignLeft)
        self.__bar_series.attachAxis(self._axis_y)
        self._axis_y.setRange(min, max)
        self._axis_y.setTitleText(text)

    def add_legend(self, alignment):
        self.legend().setVisible(True)
        alignment_name = Qt.AlignTop
        if alignment == "Top":
            alignment_name = Qt.AlignTop
        elif alignment == "Bottom":
            alignment_name = Qt.AlignBottom
        elif alignment == "Left":
            alignment_name = Qt.AlignLeft
        elif alignment == "Right":
            alignment_name = Qt.AlignRight

        if alignment_name != None:
            self.legend().setAlignment(alignment_name)

    def ActiveAnimation(self):
        self.setAnimationOptions(QChart.AllAnimations)


class AddItem:
    def __init__(self):
        self.point = []

    def additem(self, value, list):
        self.point.append((value, list))

    def returnitem(self):
        return self.point


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    chart = BarChart()
    chart.setTitle("BarChart")

    additemobj = AddItem()
    additemobj.additem("Jane", [1, 2, 3, 4, 5, 6])
    additemobj.additem("John", [5, 1, 1, 4, 1, 7])
    additemobj.additem("Axel", [3, 5, 8, 13, 8, 5])
    # additemobj.additem("Axel", [3, 5, 8, 13, 8, 5])

    data_list = additemobj.returnitem()
    for i in range(len(data_list)):
        chart.add_ser(data_list[i][0], data_list[i][1])

    st = "Bar Chart example"
    chart.add_title(st)
    Categorylist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    chart.add_axis_x(Categorylist, "Jan", "Jun")
    chart.add_axis_y(0, 20, "Type1")
    chart.add_legend("Right")
    chart.ActiveAnimation()
    chart_view = QChartView(chart)
    chart_view.setRenderHint(QPainter.Antialiasing)
    window.setCentralWidget(chart_view)
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
