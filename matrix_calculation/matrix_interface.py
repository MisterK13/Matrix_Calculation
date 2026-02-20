from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QComboBox,
                             QTextEdit, QMessageBox, QGroupBox)
from PyQt5.QtCore import Qt

from matrix_input_interface import MatrixInputInterface
from matrix_operations import MatrixOperations

class MatrixCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор матриц")
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        # Выбор операции
        operation_group = QGroupBox()
        operation_layout = QHBoxLayout()

        self.operation_combo = QComboBox()
        self.operation_combo.addItems([
            "Сложение матриц",
            "Вычитание матриц",
            "Умножение матриц",
            "Детерминант матрицы 1",
            "Детерминант матрицы 2"
        ])
        operation_layout.addWidget(QLabel("Операция"))
        operation_layout.addWidget(self.operation_combo)
        operation_group.setLayout(operation_layout)
        main_layout.addWidget(operation_group)

        # Ввод матриц
        matrices_layout = QHBoxLayout()

        self.matrix1_widget = MatrixInputInterface("Матрица 1")
        self.matrix2_widget = MatrixInputInterface("Матрица 2")

        matrices_layout.addWidget(self.matrix1_widget)
        matrices_layout.addWidget(self.matrix2_widget)

        main_layout.addLayout(matrices_layout)

        # Кнопка вычисления
        self.calculate_btn = QPushButton("Вычислить")
        self.calculate_btn.clicked.connect(self.calculate)
        self.calculate_btn.setFixedHeight(40)
        main_layout.addWidget(self.calculate_btn)

        # Поле для вывода результата
        result_group = QGroupBox("Результат")
        result_layout = QVBoxLayout()

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumHeight(150)
        result_layout.addWidget(self.result_text)

        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)

        central_widget.setLayout(main_layout)

        # Обработчик изменения операции
        self.operation_combo.currentIndexChanged.connect(self.on_operation_change)
        self.on_operation_change()

    def on_operation_change(self):
        operation = self.operation_combo.currentText()

        if operation == "Детерминант матрицы 1":
            self.matrix1_widget.show()
            self.matrix2_widget.hide()
        elif operation == "Детерминант матрицы 2":
            self.matrix1_widget.hide()
            self.matrix2_widget.show()
        else:
            self.matrix1_widget.show()
            self.matrix2_widget.show()

    def calculate(self):
        try:
            operation_text = self.operation_combo.currentText()

            matrix1, error1 = self.matrix1_widget.get_matrix()
            if error1:
                QMessageBox.critical(self, "Ошибка", f"Ошибка в матрице 1: {error1}")
                return

            matrix2 = None
            if operation_text != "Детерминант матрицы 1":  # Все кроме этой операции
                matrix2, error2 = self.matrix2_widget.get_matrix()
                if error2:
                    QMessageBox.warning(self, "Ошибка", f"Ошибка в матрице 2: {error2}")
                    return

            if operation_text == "Сложение матриц":
                result = MatrixOperations.add(matrix1, matrix2)
                result_str = f"Результат сложения:\n{format_matrix(result)}"

            elif operation_text == "Вычитание матриц":
                result = MatrixOperations.subtract(matrix1, matrix2)
                result_str = f"Результат вычитания (Матрица 1 - Матрица 2):\n{format_matrix(result)}"

            elif operation_text == "Умножение матриц":
                result = MatrixOperations.multiply(matrix1, matrix2)
                result_str = f"Результат умножения:\n{format_matrix(result)}"

            elif operation_text == "Детерминант матрицы 1":
                result = MatrixOperations.determinant(matrix1)
                result_str = f"Детерминант матрицы 1: {result:.2f}"

            elif operation_text == "Детерминант матрицы 2":
                result = MatrixOperations.determinant(matrix2)
                result_str = f"Детерминант матрицы 2: {result:.2f}"

            self.result_text.setPlainText(result_str)


        except ValueError as e:
            QMessageBox.critical(self, "Ошибка вычисления", str(e))

        except Exception as e:
            QMessageBox.critical(self, "Неизвестная ошибка", str(e))

def format_matrix(matrix):
    if not matrix:
        return ""

    result = []
    for row in matrix:
        row_str = "  ".join(f"{val:8.2f}" if isinstance(val, float) else f"{val:8}" for val in row)
        result.append(row_str)

    return "\n".join(result)


