import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import sys
import pandas as pd

# Sample data for patient's medical history
data = {
    "Date of Visit": [
        "2023-01-10", "2023-02-15", "2023-04-01", "2023-06-12", "2023-08-05"
    ],
    "Blood Pressure (mmHg)": [140, 135, 130, 145, 120],
    "Cholesterol Level (mg/dL)": [250, 240, 230, 220, 200],
    "Heart Rate (BPM)": [80, 78, 75, 82, 70]
}

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert the "Date of Visit" column to datetime format
df['Date of Visit'] = pd.to_datetime(df['Date of Visit'])

print(df)



class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(10, 6), dpi=100)
        super().__init__(fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        # fill the fields with values
        data = {
            "Date of Visit": ["2023-01-10", "2023-02-15", "2023-04-01", "2023-06-12", "2023-08-05"],
            "Blood Pressure (mmHg)": [140, 135, 130, 145, 120],
            "Cholesterol Level (mg/dL)": [250, 240, 230, 220, 200],
            "Heart Rate (BPM)": [80, 78, 75, 82, 70]
        }

        df = pd.DataFrame(data)
        df['Date of Visit'] = pd.to_datetime(df['Date of Visit'])

        sns.set(style="whitegrid")

        # self.ax.clear()
        sns.lineplot(x="Date of Visit", y="Blood Pressure (mmHg)", data=df,
                     marker="o", label="Blood Pressure", ax=self.ax, color="red")
        sns.lineplot(x="Date of Visit", y="Cholesterol Level (mg/dL)", data=df,
                     marker="o", label="Cholesterol", ax=self.ax, color="blue")
        sns.lineplot(x="Date of Visit", y="Heart Rate (BPM)", data=df,
                     marker="o", label="Heart Rate", ax=self.ax, color="green")

        self.ax.set_title("Patient's Medical History", fontsize=16)
        self.ax.set_xlabel("Date of Visit", fontsize=12)
        self.ax.set_ylabel("Measurements", fontsize=12)
        self.ax.legend()

        self.draw()



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Patient Medical History')
        self.setGeometry(100, 100, 800, 600)

        widget = QWidget(self)

        layout = QVBoxLayout(widget)

        self.plot_canvas = PlotCanvas(self)
        layout.addWidget(self.plot_canvas)


if __name__ == 'visuals':
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())
