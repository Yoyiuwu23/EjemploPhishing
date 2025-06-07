# gui/main_window.py

from PyQt5 import QtWidgets

class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self, enviar_email_callback):
        super().__init__()
        self.enviar_email_callback = enviar_email_callback
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle("Phisban")
        self.setFixedSize(400, 300)
        self.setStyleSheet("""
            QWidget { background-color: #000000; color: #FFFFFF; font-family: 'Raleway', sans-serif; }
            QLabel { font-size: 20px; color: #00FF00; font-family: 'Orbitron', sans-serif; font-weight: bold; text-align: center; }
            QLineEdit { background-color: #1E1E1E; color: #00FF00; border: 2px solid #00FF00; padding: 5px; border-radius: 5px; font-family: 'Raleway', sans-serif; }
            QPushButton { background-color: #FF1493; color: #000000; border: none; padding: 10px; font-size: 16px; border-radius: 5px; font-family: 'Orbitron', sans-serif; }
            QPushButton:hover { background-color: #FF69B4; }
            QComboBox { background-color: #1E1E1E; color: #00FF00; border: 2px solid #00FF00; padding: 5px; border-radius: 5px; font-family: 'Raleway', sans-serif; }
        """)

        layout = QtWidgets.QVBoxLayout()

        label_destinatario = QtWidgets.QLabel("Correo del destinatario:")
        layout.addWidget(label_destinatario)

        self.entry_destinatario = QtWidgets.QLineEdit()
        layout.addWidget(self.entry_destinatario)

        label_plantilla = QtWidgets.QLabel("Seleccionar plantilla de correo:")
        layout.addWidget(label_plantilla)

        self.combo_plantillas = QtWidgets.QComboBox()
        self.combo_plantillas.addItems(["Correo AIEP", "Correo Banco", "Correo Netflix"])
        layout.addWidget(self.combo_plantillas)

        boton_enviar = QtWidgets.QPushButton("Enviar correo")
        boton_enviar.clicked.connect(self.enviar)
        layout.addWidget(boton_enviar)

        self.setLayout(layout)

    def enviar(self):
        destinatario = self.entry_destinatario.text()
        plantilla_seleccionada = self.combo_plantillas.currentText()
        if destinatario:
            self.enviar_email_callback(destinatario, plantilla_seleccionada)
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Por favor, ingrese el correo del destinatario.")
