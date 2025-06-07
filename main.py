import sys
from PyQt5 import QtWidgets
from gui.main_windows import VentanaPrincipal
from utils.email_utils import enviar_email
from utils.plantilla_utils import cargar_plantilla

def enviar_email_falso(destinatario, plantilla_seleccionada):
    cuerpo = cargar_plantilla(plantilla_seleccionada)
    enviar_email(destinatario, "Notificación Importante", cuerpo)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal(enviar_email_falso)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
