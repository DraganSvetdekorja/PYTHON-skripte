import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QVBoxLayout, QHBoxLayout, QButtonGroup, QPushButton, QMessageBox

class WallpaperCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wallpaper Calculator")
        self.setup_ui()

    def setup_ui(self):
        # Dimension inputs
        self.wall_width_input = QLineEdit(self)
        self.wall_width_input.setPlaceholderText("300")
        self.wall_height_input = QLineEdit(self)
        self.wall_height_input.setPlaceholderText("250")
        self.roll_width_input = QLineEdit(self)
        self.roll_width_input.setPlaceholderText("53")
        self.roll_length_input = QLineEdit(self)
        self.roll_length_input.setPlaceholderText("1005")

        # Matching type options
        self.match_no_radio = QRadioButton("No, tapeta nima ujemanja vzorca", self)
        self.match_yes_radio = QRadioButton("Da, tapeta ima ujemanje vzorca", self)
        self.match_yes_delay_radio = QRadioButton("Da, tapeta ima ujemanje vzorca in zamik", self)
        self.matching_input = QLineEdit(self)
        self.matching_input.setPlaceholderText("64")
        self.delay_input = QLineEdit(self)
        self.delay_input.setPlaceholderText("32")
        self.matching_input.setEnabled(False)
        self.delay_input.setEnabled(False)

        # Trimming input
        self.trimming_input = QLineEdit(self)
        self.trimming_input.setPlaceholderText("4")

        # Spare roll option
        self.spare_no_radio = QRadioButton("Ne", self)
        self.spare_yes_radio = QRadioButton("Da (+1 rola)", self)

        # Calculate button
        self.calculate_button = QPushButton("Calculate", self)

        # Result label
        self.result_label = QLabel("Število potrebnih rol:   2", self)

        # Layout setup
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Dimenzija stene"))
        main_layout.addWidget(QLabel("Širina stene"))
        main_layout.addWidget(self.wall_width_input)
        main_layout.addWidget(QLabel("Višina stene"))
        main_layout.addWidget(self.wall_height_input)
        main_layout.addWidget(QLabel("Dimenzija tapete"))
        main_layout.addWidget(QLabel("Širina tapete"))
        main_layout.addWidget(self.roll_width_input)
        main_layout.addWidget(QLabel("Dolžina tapete"))
        main_layout.addWidget(self.roll_length_input)
        main_layout.addWidget(QLabel("Ima tapeta ujemanje vzorca/zamik?"))
        main_layout.addWidget(self.match_no_radio)
        main_layout.addWidget(self.match_yes_radio)
        main_layout.addWidget(self.matching_input)
        main_layout.addWidget(self.match_yes_delay_radio)
        main_layout.addWidget(self.matching_input)
        main_layout.addWidget(self.delay_input)
        main_layout.addWidget(QLabel("Dodatek k obrezovanju robov"))
        main_layout.addWidget(QLabel("Odrez na pas"))
        main_layout.addWidget(self.trimming_input)
        main_layout.addWidget(QLabel("(max 10 cm)"))
        main_layout.addWidget(QLabel("Želite biti na varni strani (rezervna rola)?"))
        main_layout.addWidget(self.spare_no_radio)
        main_layout.addWidget(self.spare_yes_radio)
        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

        # Connect signals and slots
        self.match_group = QButtonGroup()
        self.match_group.addButton(self.match_no_radio)
        self.match_group.addButton(self.match_yes_radio)
        self.match_group.addButton(self.match_yes_delay_radio)
        self.match_group.buttonClicked.connect(self.on_matching_type_changed)
        self.spare_group = QButtonGroup()
        self.spare_group.addButton(self.spare_no_radio)
        self.spare_group.addButton(self.spare_yes_radio)

        self.calculate_button.clicked.connect(self.calculate_required_rolls)

    def on_matching_type_changed(self):
        if self.match_yes_radio.isChecked() or self.match_yes_delay_radio.isChecked():
            self.matching_input.setEnabled(True)
        else:
            self.matching_input.setEnabled(False)

        if self.match_yes_delay_radio.isChecked():
            self.delay_input.setEnabled(True)
        else:
            self.delay_input.setEnabled(False)

    def calculate_required_rolls(self):
        # Get dimension values
        wall_width = int(self.wall_width_input.text() or self.wall_width_input.placeholderText())
        wall_height = int(self.wall_height_input.text() or self.wall_height_input.placeholderText())
        roll_width = int(self.roll_width_input.text() or self.roll_width_input.placeholderText())
        roll_length = int(self.roll_length_input.text() or self.roll_length_input.placeholderText())

        # Get matching values
        match = self.match_group.checkedButton().text()
        matching = int(self.matching_input.text() or self.matching_input.placeholderText())
        delay = int(self.delay_input.text() or self.delay_input.placeholderText())

        # Get other values
        trimming = int(self.trimming_input.text() or self.trimming_input.placeholderText())
        spare = self.spare_group.checkedButton().text()

        # Calculate lines per wall
        lines_wall = 0
        if roll_width > 0:
            lines_wall = wall_width / roll_width

        # Calculate repeating of pattern
        repeating = 0
        if (matching + delay) > 0:
            repeating = wall_height / (matching + delay)

        # Calculate tape length
        tape_length = 0
        if match == "No, tapeta nima ujemanja vzorca":
            tape_length = wall_height + trimming
        elif match == "Da, tapeta ima ujemanje vzorca":
            tape_length = (repeating // 1) * matching + trimming
        elif match == "Da, tapeta ima ujemanje vzorca in zamik":
            tape_length = (repeating // 1) * (matching + delay) + trimming

        # Calculate tapes per roll
        tapes_rolls = 0
        if tape_length > 0:
            tapes_rolls = roll_length / tape_length

        # Calculate required rolls
        required_rolls = 0
        if tapes_rolls > 0:
            required_rolls = ((lines_wall // 1) + 1) // (tapes_rolls // 1)

        # Add spare roll
        if spare == "Da (+1 rola)":
            required_rolls += 1

        self.result_label.setText(f"Število potrebnih rol: {required_rolls}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = WallpaperCalculator()
    calculator.show()
    sys.exit(app.exec_())
