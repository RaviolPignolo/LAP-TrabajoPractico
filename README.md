# -=-=-= Tactical-RPG 1v1 entre campones de LoL =-=-=-

Simula un 1v1 entre los 170 campeones de League of Legends actualizado al parche xx.xx

## Installation

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
