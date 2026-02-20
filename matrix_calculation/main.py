import sys

from PyQt5.QtWidgets import (QApplication)

from matrix_interface import MatrixCalculator

def main():
    app = QApplication(sys.argv)

    app.setStyle('Fusion')

    window = MatrixCalculator()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

