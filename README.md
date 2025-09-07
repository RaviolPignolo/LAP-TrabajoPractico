# ⚔️ Tactical-RPG 1v1 entre campeones de League of Legends

Simulador de combate 1v1 entre los 170 campeones de League of Legends (actualizado al parche XX.XX).

Este proyecto fue desarrollado como trabajo práctico para la materia **Laboratorio Avanzado de Programación** en la UDC.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Version](https://img.shields.io/badge/Versión-0.0.1-green)
![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)

---
## Instalación simple

1. Descargá el archivo `.exe` desde la sección de [Releases](https://github.com/RaviolPignolo/LAP-TrabajoPractico/releases)
2. Ejecutá el archivo descargado (`TFTdeLaSalada.exe`)


## Installation desarrolladores

- Clona el repositorio github
- Activa el entorno virtual en la consola usando

```python
    source venv/bin/activate
```

- Instala las dependencias con el comando:

```python
    pip install -r requirements.txt
```

## Correr el programa

- Posicionene en la consola en 'LAP-TrabajoPractico'
- Ejecute el siguiente comando para iniciar el juego

```python
    python3 -m src.Main
```

## Tests

- Podes ejectutar todos los test con el comando

```python
    python3 -m unittest discover tests/.
```

- O puedes hacer tests individuales con el comando

```python
    python3 -m unittest tests.test_champion.TestChampion.nombre_del_test
```

## Authors

- [@RaviolPignolo](https://github.com/RaviolPignolo)
