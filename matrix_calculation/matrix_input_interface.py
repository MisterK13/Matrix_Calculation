from PyQt5.QtWidgets import (QWidget, QGridLayout, QLineEdit, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from matrix_operations import MatrixOperations

class MatrixInputInterface(QWidget):
    def __init__(self, title="Матрица", max_size=3):
        super().__init__()
        self.max_size = max_size
        self.inputs = []
        self.init_ui(title)

    def init_ui(self, title):
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Сетка матрицы
        self.grid_layout = QGridLayout()
        self.create_input_grid()
        layout.addLayout(self.grid_layout)

        # Кнопки для изменения размера
        button_layout = QHBoxLayout()

        add_row_btn = QPushButton("Добавить строку")
        add_row_btn. clicked.connect(self.add_row)
        button_layout.addWidget(add_row_btn)

        add_col_btn = QPushButton("Добавить столбец")
        add_col_btn.clicked.connect(self.add_column)
        button_layout.addWidget(add_col_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def create_input_grid(self):
        self.inputs = [[self.create_input_field(0,0)]]

    def create_input_field(self, row, col):
        input_field = QLineEdit()
        input_field.setFixedSize(50,30)
        input_field.setAlignment(Qt.AlignCenter)
        input_field.setPlaceholderText("0")
        self.grid_layout.addWidget(input_field, row, col)
        return input_field

    def add_row(self):
        if len(self.inputs) >= self.max_size:
            return

        new_row = []
        for col in range(len(self.inputs[0])):
            input_field = self.create_input_field(len(self.inputs), col)
            new_row.append(input_field)

        self.inputs.append(new_row)

    def add_column(self):
        if len(self.inputs[0]) >= self.max_size:
            return

        for row_index, row in enumerate(self.inputs):
            input_field = self.create_input_field(row_index, len(row))
            row.append(input_field)

    def get_matrix(self):
        matrix = []
        for row in self.inputs:
            matrix_row = []
            for input_field in row:
                text = input_field.text().strip()
                if text and text.replace('-', '').replace('.', '').isdigit():
                    try:
                        if "." in text:
                            value = float(text)
                        else:
                            value = int(text)
                        if value == 0:
                            return None, "Нулевое значение"

                        matrix_row.append(value)
                    except ValueError:
                        return None, "Некорректное значение"
                elif not text:
                    matrix_row.append(None)
                else:
                    return None, "Некорректное значение"

            matrix.append(matrix_row)

        if not matrix:
            return None, "Матрица пустая"

        cleaned_matrix = MatrixOperations.clean_matrix(matrix)

        if not cleaned_matrix:
            return None, "Пустая матрица после очистки"

        return cleaned_matrix, ""