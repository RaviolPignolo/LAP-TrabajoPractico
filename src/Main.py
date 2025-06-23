from src.Modelo.Champion import Champion
from src.Modelo.Item import Item
from src.Modelo.Champion import load_champion
from src.Modelo.Item import load_item
from src.Vista.vistaCampeon import vistaCampeon
from src.Vista.vistaCampeonList.vistaKarthus import vistaKarthus
from src.Vista.vistaItem import vistaItem
from src.Vista.vistaCampeon import champions_list
from src.Vista.vistaItem import items_list
from src.Controlador.controlCampeon import controlCampeon
from src.Modelo import globals as globals_var
from src.Modelo.ChampionsList.Karthus import Karthus
import pygame
import sys

pygame.init()

PANTALLA_ANCHO = 1280
PANTALLA_ALTO = 720

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)

FONT  = pygame.font.Font("src/Vista/Assets/Fonts/BeaufortforLOL-Medium.ttf", 24)

# Configuración de la pantalla
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("TFT de la salada")

# Opciones principales
menu_options = ['Iniciar', 'Campeones', 'Items', 'Guía', 'Salir']
selected_option = 0

# Configuración del botón para retroceder
def back_button_draw(surface, font, color_fondo, color_texto):
    back_button_rect = pygame.Rect(10, 10, 100, 40)
    pygame.draw.rect(surface, color_fondo, back_button_rect)
    back_text = FONT.render('Atrás',True, color_texto)
    back_text_rect = back_text.get_rect(center=back_button_rect.center)
    surface.blit(back_text, back_text_rect)
    return back_button_rect
def back_button_event(event, back_button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if back_button_rect.collidepoint(event.pos):
            return True
    return False


def menu():
    pantalla.fill(NEGRO)
    for i, option in enumerate(menu_options):
        if i == selected_option:
            text  = FONT.render(option, True, BLANCO)
        else:
            text = FONT.render(option, True, GRIS)
        text_rect = text.get_rect(center=(PANTALLA_ANCHO // 2, PANTALLA_ALTO // 2 + i * 40))
        pantalla.blit(text, text_rect)

def main():
    "Menú principal"
    global selected_option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == 'Salir':
                        pygame.quit()
                        sys.exit()
                    elif menu_options[selected_option] == 'Iniciar':
                        pantalla_juego()
                        pass
                    elif menu_options[selected_option] == 'Campeones':
                        champion_list_menu()
                        pass
                    elif menu_options[selected_option] == "Items":
                        items_list_menu()
                        pass
                    elif menu_options[selected_option] == 'Diccionario':
                        #diccionario()
                        pass

        menu()
        pygame.display.update()

def champion_list_menu():
    selected_champion = 0
    champions_per_row = 5
    x_offset = 150
    y_offset = 200
    spacing_x = 140
    spacing_y = 120
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if(selected_champion + champions_per_row) < len(champions_list):
                        selected_champion += champions_per_row
                elif event.key == pygame.K_UP:
                    if(selected_champion - champions_per_row) >= 0:
                        selected_champion -= champions_per_row
                elif event.key == pygame.K_RIGHT:
                    if(selected_champion % champions_per_row) < (champions_per_row - 1) and (selected_champion + 1) < len(champions_list):
                        selected_champion += 1
                elif event.key == pygame.K_LEFT:
                    if(selected_champion % champions_per_row) > 0:
                        selected_champion -= 1
                elif event.key == pygame.K_RETURN:
                    champion_details(champions_list[selected_champion])
            if back_button_event(event, back_button_rect):
                return
        
        pantalla.fill(NEGRO)
        back_button_rect = back_button_draw(pantalla, FONT, GRIS, NEGRO)
        
        for i, Champion in enumerate(champions_list):
            # Calculo la posición en la cuadrilla
            row = i // champions_per_row
            col = i % champions_per_row
            x_position = x_offset + col * spacing_x
            y_position = y_offset + row * spacing_y
            
            # Carga y dibujo de la imagen del campeon
            image = pygame.image.load(Champion['image'])
            image_rect = image.get_rect(center=(x_position, y_position))
            pantalla.blit(image, image_rect)
            
            # Dibujar el nombre del campeon
            if i == selected_champion:
                text = FONT.render(Champion['name'], True, BLANCO)
            else:
                text = FONT.render(Champion['name'], True, GRIS)
            text_rect = text.get_rect(midtop=(x_position, y_position + 40))
            pantalla.blit(text, text_rect)
        
        pygame.display.update()

def items_list_menu():
    """Lista de los items disponibles para ver sus estadisticas"""
    selected_item = 0
    item_per_row = 5
    x_offset = 150
    y_offset = 200
    spacing_x = 140  # Espacio horizontal entre items
    spacing_y = 120  # Espacio vertical entre filas
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if (selected_item + item_per_row) < len(items_list):
                        selected_item += item_per_row
                elif event.key == pygame.K_UP:
                    if (selected_item - item_per_row) >= 0:
                        selected_item -= item_per_row
                elif event.key == pygame.K_RIGHT:
                    if (selected_item % item_per_row) < (item_per_row - 1) and (selected_item + 1) < len(items_list):
                        selected_item += 1
                elif event.key == pygame.K_LEFT:
                    if (selected_item % item_per_row) > 0:
                        selected_item -= 1
                elif event.key == pygame.K_RETURN:
                    items_details(items_list[selected_item])
            if back_button_event(event, back_button_rect):
                return

        pantalla.fill(NEGRO)
        back_button_rect = back_button_draw(pantalla, FONT, GRIS, NEGRO)
        
        for i, Item in enumerate(items_list):
            # Calcula la posición en la cuadrícula
            row = i // item_per_row
            col = i % item_per_row
            x_position = x_offset + col * spacing_x
            y_position = y_offset + row * spacing_y
            
            # Cargar y dibujar la imagen del item
            image = pygame.image.load(Item['image'])
            image_rect = image.get_rect(center=(x_position, y_position))
            pantalla.blit(image, image_rect)
            
            # Dibujar el nombre del item
            if i == selected_item:
                text = FONT.render(Item['name'], True, BLANCO)
            else:
                text = FONT.render(Item['name'], True, GRIS)
            text_rect = text.get_rect(midtop=(x_position, y_position + 40))
            pantalla.blit(text, text_rect)
        
        pygame.display.update()

def champion_details(champion):
    "Estadisticas y habilidades del campeón seleccionado"
    campeon_instancia = load_champion(champion['name'])
    ocultar_stats = ["Health Growth", "Health Regen Growth", "Mana Growth", "Mana Regen Growth", "Attack Damage Growth", "Base Attack Speed", "Attack Speed Ratio", "Bonus Attack Speed", "Armor Growth", "Magic Resistance Growth"]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if back_button_event(event, back_button_rect):
                return

        pantalla.fill(NEGRO)
        back_button_rect = back_button_draw(pantalla, FONT, GRIS, NEGRO)
        
        image = pygame.image.load(champion['image'])
        image_rect = image.get_rect(center=(100, 200))
        pantalla.blit(image, image_rect)
        
        champion_info_list = vistaCampeon.base_stats(campeon_instancia)
        champion_info_list = [
            stat for stat in champion_info_list
            if stat.get("name") not in ocultar_stats
        ]
        y_offset = 300
        for stat in champion_info_list:
            if stat["icon"]:
                icon_img = pygame.image.load(stat["icon"])
                icon_img  = pygame.transform.scale(icon_img, (25, 25))
                pantalla.blit(icon_img, (100, y_offset))
                text_x = 140
            else:
                text_x = 100
                
            value_text = FONT.render(str(stat["value"]), True, BLANCO)
            pantalla.blit(value_text, (text_x, y_offset))
            y_offset += 40
        
        pygame.display.update()

def items_details(item):
    "Estadisticas del item seleccionado"
    item_instancia = load_item(item['name'])
    while True:
        pantalla.fill(NEGRO)
        back_button_rect = back_button_draw(pantalla, FONT, GRIS, NEGRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if back_button_event(event, back_button_rect):
                return
        
        image = pygame.image.load(item['image'])
        image_rect = image.get_rect(center=(100, 200))
        pantalla.blit(image, image_rect)
        
        item_info_list = vistaItem.item_info(item_instancia)
        y_offset = 300
        for stat in item_info_list:
            if stat["icon"]:
                icon_img = pygame.image.load(stat["icon"])
                icon_img = pygame.transform.scale(icon_img, (25, 25))
                pantalla.blit(icon_img, (100, y_offset))
                text_x = 140
            else:
                text_x = 100
            
            value_text = FONT.render(str(stat["value"]), True, BLANCO)
            pantalla.blit(value_text, (text_x, y_offset))
            y_offset += 40
        
        pygame.display.update()

def pantalla_juego():
    "Pantalla del juego"
    
    globals_var.turno_actual = 1
    
    CELDA_ANCHO = 80
    CELDA_ALTO = 80
    MAX_CELDAS_X = PANTALLA_ANCHO // CELDA_ANCHO
    MAX_CELDAS_Y = int(PANTALLA_ALTO / 1.5) // CELDA_ALTO

    campeon1_select: str
    campeon2_select: str
    
    # Le paso los campeones que se usarán, más adelante la idea es que reciba una lista
    campeon1_select = "Karthus" 
    campeon2_select = "Twitch"

    # Busco los campeones seleccionados en la lista
    campeon1_dict = next(c for c in champions_list if c['name'] == campeon1_select)
    campeon2_dict = next(c for c in champions_list if c['name'] == campeon2_select)
    
    # Les asigno la imagen, modelo y lógica a los campeones
    if campeon1_select == "Karthus":
        campeon1_modelo = load_champion(campeon1_select)
        campeon1_vista = vistaKarthus(3 * CELDA_ANCHO, 2 * CELDA_ALTO, campeon1_modelo, None)
    else:
        campeon1_modelo = load_champion(campeon1_select)
        campeon1_vista = vistaCampeon(3 * CELDA_ANCHO, 2 * CELDA_ALTO, campeon1_dict)
    campeon1_control = controlCampeon(campeon1_vista)
    
    campeon2_vista = vistaCampeon(6 * CELDA_ANCHO, 4 * CELDA_ALTO, campeon2_dict)
    campeon2_control = controlCampeon(campeon2_vista)
    campeon2_modelo = load_champion(campeon2_select)
    
    arena_imagen = pygame.image.load('src/Vista/Assets/Images/Arena.png') # Cargo la imagen de la zona de pelea
    arena_imagen = pygame.transform.scale(arena_imagen, (PANTALLA_ANCHO, int(PANTALLA_ALTO / 1.5)))
    
    turno_campeon1 = True
    estado_turno = "seleccion_accion" # puede variar entre seleccion_accion, seleccion_habilidad, esperando
    accion_seleccionada = 0
    acciones = ["Moverse", "Ataque básico", "Habilidad"]
    habilidad_seleccionada = 0
    habilidades = ["Q", "W", "E", "R"]
    
    # NUEVO: Variables para selección y animación de la Q de Karthus
    seleccionando_casilla_q = False
    q_cursor_x, q_cursor_y = 3, 2  # Por defecto, donde está Karthus
    q_anim_en_progreso = False
    q_anim_frame = 0
    q_anim_pos = (0, 0)
    q_anim_timer = 0
    q_anim_duracion = 9  # 3x3 frames
    
    
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.KEYDOWN):
                if estado_turno == "seleccion_accion":
                    if event.key == pygame.K_DOWN:
                        accion_seleccionada = (accion_seleccionada + 1) % len(acciones)
                    elif event.key == pygame.K_UP:
                        accion_seleccionada = (accion_seleccionada - 1) % len(acciones)
                    elif event.key == pygame.K_RETURN:
                        if acciones[accion_seleccionada] == "Moverse":
                            estado_turno = "movimiento_libre"
                        elif acciones[accion_seleccionada] == "Ataque básico":
                            estado_turno = "esperando"
                            if turno_campeon1:
                                campeon1_modelo.aa(campeon2_modelo)
                            else:
                                campeon2_modelo.aa(campeon1_modelo)
                        elif acciones[accion_seleccionada] == "Habilidad":
                            estado_turno = "seleccion_habilidad"
                elif estado_turno == "movimiento_libre":
                    moved = False
                    if event.key == pygame.K_DOWN:
                        if turno_campeon1:
                            moved = campeon1_control.mover("down", 1, campeon2_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                        else:
                            moved = campeon2_control.mover("down", 1, campeon1_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                    elif event.key == pygame.K_UP:
                        if turno_campeon1:
                            moved = campeon1_control.mover("up", 1, campeon2_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                        else:
                            moved = campeon2_control.mover("up", 1, campeon1_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                    elif event.key == pygame.K_RIGHT:
                        if turno_campeon1:
                            moved = campeon1_control.mover("right", 1, campeon2_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                        else:
                            moved = campeon2_control.mover("right", 1, campeon1_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                    elif event.key == pygame.K_LEFT:
                        if turno_campeon1:
                            moved = campeon1_control.mover("left", 1, campeon2_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                        else:
                            moved = campeon2_control.mover("left", 1, campeon1_control, MAX_CELDAS_X, MAX_CELDAS_Y)
                    # Si se movió, termina el turno
                    if moved:
                        estado_turno = "esperando"
                elif estado_turno == "seleccion_habilidad":
                    if event.key == pygame.K_DOWN:
                        habilidad_seleccionada = (habilidad_seleccionada + 1) % len(habilidades)
                    elif event.key == pygame.K_UP:
                        habilidad_seleccionada = (habilidad_seleccionada - 1) % len(habilidades)
                    elif event.key == pygame.K_RETURN:
                        if habilidades[habilidad_seleccionada] == "Q" and turno_campeon1 and campeon1_modelo.name == "Karthus":
                            estado_turno = "seleccion_casilla_q"
                            q_cursor_x, q_cursor_y = campeon1_control.x // CELDA_ANCHO, campeon1_control.y // CELDA_ALTO
                        else:
                            estado_turno = "esperando"
                        # Lógica de habilidad seleccionada
                elif estado_turno == "seleccion_casilla_q":
                    if event.key == pygame.K_DOWN:
                        q_cursor_y = min(q_cursor_y + 1, MAX_CELDAS_Y -1)
                    elif event.key == pygame.K_UP:
                        q_cursor_y = max(q_cursor_y - 1, 0)
                    elif event.key == pygame.K_RIGHT:
                        q_cursor_x = min(q_cursor_x + 1, MAX_CELDAS_X - 1)
                    elif event.key == pygame.K_LEFT:
                        q_cursor_x = max(q_cursor_x - 1, 0)
                    elif event.key == pygame.K_RETURN:
                        # Detectar si el otro campeon está en la celda seleccionada
                        campeon2_celda_x = campeon2_control.x // CELDA_ANCHO
                        campeon2_celda_y = campeon2_control.y // CELDA_ALTO
                        if q_cursor_x == campeon2_celda_x and q_cursor_y == campeon2_celda_y:
                            campeon1_modelo.q(campeon2_modelo)
                        else:
                            campeon1_modelo.q(None) # Solo la animación
                        # Inicia la animación
                        q_anim_en_progreso = True
                        q_anim_frame = 0
                        q_anim_timer = pygame.time.get_ticks()
                        q_anim_pos = (q_cursor_x, q_cursor_y)
                        estado_turno = "animacion_q"
                elif estado_turno == "animacion_q":
                    # No aceptar input hasta que termine la animación
                    pass
                elif estado_turno == "esperando":
                    globals_var.turno_actual += 1
                    
                    for campeon in [campeon1_modelo, campeon2_modelo]:
                        if isinstance(campeon, Karthus):
                            campeon.actualizar_estado()
                    
                    if not campeon1_modelo.its_alive:
                        pantalla_ganador(campeon2_modelo)
                        return
                    if not campeon2_modelo.its_alive:
                        pantalla_ganador(campeon1_modelo)
                        return
                    
                    turno_campeon1 = not turno_campeon1
                    estado_turno = "seleccion_accion"
                    accion_seleccionada = 0
                    habilidad_seleccionada = 0
            
            
        pantalla.fill(NEGRO)
        pantalla.blit(arena_imagen, (0, 0))
        campeon1_vista.dibujar(pantalla)
        campeon2_vista.dibujar(pantalla)
        
        # Dibujo la cuadrilla del juego
        for x in range(0, PANTALLA_ANCHO, CELDA_ANCHO):
            for y in range(0, int(PANTALLA_ALTO / 1.5), CELDA_ALTO):
                rect = pygame.Rect(x, y, CELDA_ANCHO, CELDA_ALTO)
                pygame.draw.rect(pantalla, BLANCO, rect, 1)
                
                # Ésto es para ver las coordenadas de las cuadrillas, no es necesario que el jugador lo vea
                #text = FONT.render(f"{x // CELDA_ANCHO}, {y // CELDA_ALTO}", True, BLANCO)
                #pantalla.blit(text, (x + 5, y + 5))
        
        # Menú de acciones
        if estado_turno == "seleccion_accion":
            menu_y = 550
            turno_text = f"Turno {globals_var.turno_actual}: {campeon1_modelo.name}" if turno_campeon1 else f"Turno {globals_var.turno_actual}: {campeon2_modelo.name}"
            pantalla.blit(FONT.render(turno_text, True, BLANCO),(100, menu_y - 40))
            for i, accion in enumerate(acciones):
                color = BLANCO if i == accion_seleccionada else GRIS
                text = FONT.render(accion, True, color)
                pantalla.blit(text, (100, menu_y + i * 40))
        elif estado_turno == "seleccion_habilidad":
            """
            Lo siguiente es que en éste menú se muestre el icono y nombre de la habilidad.
            Al seleccionar alguna se muestra otra "ventana" con la descripción detallada de la habilidad con una opcion de confirnar o volver.
            """
            menu_y = 550
            pantalla.blit(FONT.render("Elige habildad: ", True, BLANCO), (100, menu_y - 40))
            for i, hab in enumerate(habilidades):
                color = BLANCO if i == habilidad_seleccionada else GRIS
                text = FONT.render(hab, True, color)
                pantalla.blit(text, (100, menu_y + i * 40))
        
        
        # Bloques de información de campeones
        bloque_ancho = 350
        bloque_alto = 170
        margen = 30
        x_bloque1 = PANTALLA_ANCHO - bloque_ancho - margen - 400
        x_bloque2 = PANTALLA_ANCHO - bloque_ancho - margen
        y_bloque1 = PANTALLA_ALTO - bloque_alto - margen
        y_bloque2 = PANTALLA_ALTO - bloque_alto - margen
        
        # Campeón 1 (arriba)
        tipo_recurso1 = "mana" if hasattr(campeon1_modelo, "actual_max_mana") and campeon1_modelo.actual_max_mana > 0 else "energy"
        dibujar_bloque_campeon(
            pantalla, x_bloque1, y_bloque1, bloque_ancho, bloque_alto,
            campeon1_vista, campeon1_modelo,
            color_vida=(0, 200, 0),
            color_recurso=(0, 120, 255) if tipo_recurso1 == "mana" else (255, 220, 0),
            tipo_recurso=tipo_recurso1
        )

        # Campeón 2 (abajo)
        tipo_recurso2 = "mana" if hasattr(campeon2_modelo, "actual_max_mana") and campeon2_modelo.actual_max_mana > 0 else "energy"
        dibujar_bloque_campeon(
            pantalla, x_bloque2, y_bloque2, bloque_ancho, bloque_alto,
            campeon2_vista, campeon2_modelo,
            color_vida=(0, 200, 0),
            color_recurso=(0, 120, 255) if tipo_recurso2 == "mana" else (255, 220, 0),
            tipo_recurso=tipo_recurso2
        )
        
        
        # Dibuja el icono de la Q como cursos de la habilidad
        if estado_turno == "seleccion_casilla_q" and campeon1_modelo.name == "Karthus":
            campeon1_vista.dibujar_cursor_q(pantalla, q_cursor_x, q_cursor_y, CELDA_ANCHO, CELDA_ALTO)
        
        # Dibujo la animación de la Q
        if estado_turno == "animacion_q" and q_anim_en_progreso:
            campeon1_vista.dibujar_animacion_q(pantalla, q_anim_pos[0], q_anim_pos[1], q_anim_frame, CELDA_ANCHO, CELDA_ALTO)
            # Avanza los frames cada 80ms
            if pygame.time.get_ticks() - q_anim_timer > 80:
                q_anim_frame += 1
                q_anim_timer = pygame.time.get_ticks()
                if q_anim_frame >= q_anim_duracion:
                    q_anim_en_progreso = False
                    estado_turno = "esperando"
        
        pygame.display.update()

def dibujar_bloque_campeon(pantalla, x, y, ancho, alto, campeon_vista, campeon_modelo, color_vida, color_recurso, tipo_recurso):
    # Fondo del bloque
    fondo_color = (30, 30, 30)
    pygame.draw.rect(pantalla, fondo_color, (x, y, ancho, alto), border_radius=10)

    # Icono del campeón
    icono = pygame.image.load(campeon_vista.icon_path)
    icono = pygame.transform.scale(icono, (64, 64))
    pantalla.blit(icono, (x + 20, y + 20))

    # Nombre
    nombre_text = FONT.render(f"{campeon_modelo.name}", True, BLANCO)
    pantalla.blit(nombre_text, (x + 100, y + 20))
    
    # Nivel
    nivel_text = FONT.render(f"{campeon_modelo.level}", True, BLANCO)
    pantalla.blit(nivel_text, (x + 100, y + 50))

    # --- Barra de vida ---
    vida_actual = campeon_modelo.actual_hp
    vida_max = campeon_modelo.actual_max_hp
    vida_regen = campeon_modelo.actual_hp_regen
    barra_ancho = ancho - 40
    barra_alto = 24
    barra_x = x + 20
    barra_y = y + 100

    # Fondo barra vida
    pygame.draw.rect(pantalla, (40, 60, 40), (barra_x, barra_y, barra_ancho, barra_alto), border_radius=6)
    # Barra vida
    vida_width = int(barra_ancho * vida_actual / vida_max)
    pygame.draw.rect(pantalla, color_vida, (barra_x, barra_y, vida_width, barra_alto), border_radius=6)
    # Texto vida
    vida_text = FONT.render(f"{round(vida_actual)}/{round(vida_max)} +{round(vida_regen,1)}", True, BLANCO)
    pantalla.blit(vida_text, (barra_x + 10, barra_y - 3))

    # --- Barra de recurso ---
    if tipo_recurso == "mana":
        recurso_actual = campeon_modelo.actual_mana
        recurso_max = campeon_modelo.actual_max_mana
        recurso_regen = campeon_modelo.actual_mana_regen
        color_fondo = (30, 40, 60)
    else:  # energia
        recurso_actual = campeon_modelo.actual_energy
        recurso_max = campeon_modelo.actual_max_energy
        recurso_regen = campeon_modelo.actual_energy_regen
        color_fondo = (60, 60, 30)

    barra_y2 = barra_y + barra_alto + 10
    # Fondo barra recurso
    pygame.draw.rect(pantalla, color_fondo, (barra_x, barra_y2, barra_ancho, barra_alto), border_radius=6)
    # Barra recurso
    if recurso_max > 0:
        recurso_width = int(barra_ancho * recurso_actual / recurso_max)
    else:
        recurso_width = 0
    pygame.draw.rect(pantalla, color_recurso, (barra_x, barra_y2, recurso_width, barra_alto), border_radius=6)
    # Texto recurso
    recurso_text = FONT.render(f"{round(recurso_actual)}/{round(recurso_max)} +{round(recurso_regen,1)}", True, BLANCO)
    pantalla.blit(recurso_text, (barra_x + 10, barra_y2 - 3))

def pantalla_ganador(campeon_ganador):
    mensaje_ganador = f"¡Ganador {campeon_ganador.name}!"
    texto = FONT.render(mensaje_ganador, True, BLANCO)
    rect = texto.get_rect(center = (pantalla.get_width()//2, pantalla.get_height()//2))
    
    # Fondo semitransparente
    overlay = pygame.Surface(pantalla.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0 , 180)) #Negro con transparencia

    pantalla.blit(overlay, (0,0))
    pantalla.blit(texto, rect)
    
    pygame.display.update()
    
    espera = True
    while espera:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                espera = False
                main()


if __name__ == '__main__':
    main()