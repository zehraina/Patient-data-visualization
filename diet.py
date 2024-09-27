from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

nutrition_data = {
    "Protein": ["Chicken", "Fish", "Eggs", "Tofu", "Lentils"],
    "Carbohydrates": ["Rice", "Bread", "Pasta", "Potatoes", "Quinoa"],
    "Fats": ["Avocado", "Olive oil", "Nuts", "Butter", "Cheese"],
    "Vitamin A": ["Carrots", "Sweet Potatoes", "Spinach"],
    "Vitamin B": ["Eggs", "Fish", "Meat", "Leafy greens"],
    "Vitamin C": ["Oranges", "Strawberries", "Bell Peppers"],
    "Vitamin D": ["Sunlight", "Mushrooms", "Fortified Milk"],
    "Vitamin E": ["Almonds", "Sunflower Seeds", "Spinach"],
    "Vitamin B12": ["Fish", "Eggs", "Dairy"],
    "Fibre": ["Oats", "Beans", "Apples", "Chia seeds", "Whole grains"]
}


class NutritionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_dos = []
        self.selected_donts = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Dos and Don\'ts')

        main_layout = QVBoxLayout()

        title = QLabel('Dos and Don\'ts:', self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(title)

        columns_layout = QHBoxLayout()

        # Do's column
        do_layout = QVBoxLayout()
        do_label = QLabel('Dos:', self)
        do_label.setAlignment(Qt.AlignCenter)
        do_layout.addWidget(do_label)

        # Don'ts column
        dont_layout = QVBoxLayout()
        dont_label = QLabel('Don\'ts:', self)
        dont_label.setAlignment(Qt.AlignCenter)
        dont_layout.addWidget(dont_label)

        for category in nutrition_data.keys():
            do_button = QPushButton(category, self)
            do_button.setStyleSheet(
                "background-color: green; color: white; padding: 10px;")
            do_button.clicked.connect(
                lambda checked, cat=category: self.handle_do_click(cat))
            do_layout.addWidget(do_button)

            dont_button = QPushButton(category, self)
            dont_button.setStyleSheet(
                "background-color: red; color: white; padding: 10px;")
            dont_button.clicked.connect(
                lambda checked, cat=category: self.handle_dont_click(cat))
            dont_layout.addWidget(dont_button)

        columns_layout.addLayout(do_layout)
        columns_layout.addLayout(dont_layout)

        main_layout.addLayout(columns_layout)

        self.flashcard_label = QLabel(self)
        self.flashcard_label.setStyleSheet(
            "font-size: 18px; padding: 15px; background-color: lightgray;")
        self.flashcard_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        main_layout.addWidget(self.flashcard_label)

        self.setLayout(main_layout)

    def handle_do_click(self, category):
        if category in self.selected_dos:
            self.selected_dos.remove(category)
        else:
            self.selected_dos.append(category)
            if category in self.selected_donts:
                self.selected_donts.remove(category)

        self.update_flashcard()

    def handle_dont_click(self, category):
        if category in self.selected_donts:
            self.selected_donts.remove(category)
        else:
            self.selected_donts.append(category)
            if category in self.selected_dos:
                self.selected_dos.remove(category)

        self.update_flashcard()

    def update_flashcard(self):
        flashcard_text = ""

        if self.selected_dos:
            flashcard_text += "Dos:\n"
            for category in self.selected_dos:
                flashcard_text += f"{category}: {', '.join(nutrition_data[category])}\n"

        if self.selected_donts:
            flashcard_text += "\nDon'ts:\n"
            for category in self.selected_donts:
                flashcard_text += f"{category}: {', '.join(nutrition_data[category])}\n"

        self.flashcard_label.setText(flashcard_text)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = NutritionApp()
    window.show()
    sys.exit(app.exec_())
