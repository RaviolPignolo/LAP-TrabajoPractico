import sys
import os

""" Variable que va a llevar el conteo de los turnos en el juego"""
turno_actual = 0


def resource_path(relative_path):
    """Devuelve la ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS  # PyInstaller crea esta variable
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)