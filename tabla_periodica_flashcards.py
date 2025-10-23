import streamlit as st
import random

# -- DATOS DE LOS ELEMENTOS (sin lantánidos ni actínidos)
elementos = [
    (1, "H", "Hidrógeno", 1, 1), (2, "He", "Helio", 18, 1),
    (3, "Li", "Litio", 1, 2), (4, "Be", "Berilio", 2, 2), (5, "B", "Boro", 13, 2), (6, "C", "Carbono", 14, 2),
    (7, "N", "Nitrógeno", 15, 2), (8, "O", "Oxígeno", 16, 2), (9, "F", "Flúor", 17, 2), (10, "Ne", "Neón", 18, 2),
    (11, "Na", "Sodio", 1, 3), (12, "Mg", "Magnesio", 2, 3), (13, "Al", "Aluminio", 13, 3), (14, "Si", "Silicio", 14, 3),
    (15, "P", "Fósforo", 15, 3), (16, "S", "Azufre", 16, 3), (17, "Cl", "Cloro", 17, 3), (18, "Ar", "Argón", 18, 3),
    (19, "K", "Potasio", 1, 4), (20, "Ca", "Calcio", 2, 4), (21, "Sc", "Escandio", 3, 4), (22, "Ti", "Titanio", 4, 4),
    (23, "V", "Vanadio", 5, 4), (24, "Cr", "Cromo", 6, 4), (25, "Mn", "Manganeso", 7, 4), (26, "Fe", "Hierro", 8, 4),
    (27, "Co", "Cobalto", 9, 4), (28, "Ni", "Níquel", 10, 4), (29, "Cu", "Cobre", 11, 4), (30, "Zn", "Zinc", 12, 4),
    (31, "Ga", "Galio", 13, 4), (32, "Ge", "Germanio", 14, 4), (33, "As", "Arsénico", 15, 4), (34, "Se", "Selenio", 16, 4),
    (35, "Br", "Bromo", 17, 4), (36, "Kr", "Kriptón", 18, 4),
    (37, "Rb", "Rubidio", 1, 5), (38, "Sr", "Estroncio", 2, 5), (39, "Y", "Itrio", 3, 5), (40, "Zr", "Circonio", 4, 5),
    (41, "Nb", "Niobio", 5, 5), (42, "Mo", "Molibdeno", 6, 5), (43, "Tc", "Tecnecio", 7, 5), (44, "Ru", "Rutenio", 8, 5),
    (45, "Rh", "Rodio", 9, 5), (46, "Pd", "Paladio", 10, 5), (47, "Ag", "Plata", 11, 5), (48, "Cd", "Cadmio", 12, 5),
    (49, "In", "Indio", 13, 5), (50, "Sn", "Estaño", 14, 5), (51, "Sb", "Antimonio", 15, 5), (52, "Te", "Telurio", 16, 5),
    (53, "I", "Yodo", 17, 5), (54, "Xe", "Xenón", 18, 5),
    (55, "Cs", "Cesio", 1, 6), (56, "Ba", "Bario", 2, 6),
    (72, "Hf", "Hafnio", 4, 6), (73, "Ta", "Tantalio", 5, 6), (74, "W", "Wolframio", 6, 6), (75, "Re", "Renio", 7, 6), (76, "Os", "Osmio", 8, 6),
    (77, "Ir", "Iridio", 9, 6), (78, "Pt", "Platino", 10, 6), (79, "Au", "Oro", 11, 6), (80, "Hg", "Mercurio", 12, 6), (81, "Tl", "Talio", 13, 6),
    (82, "Pb", "Plomo", 14, 6), (83, "Bi", "Bismuto", 15, 6), (84, "Po", "Polonio", 16, 6), (85, "At", "Astato", 17, 6), (86, "Rn", "Radón", 18, 6),
    (87, "Fr", "Francio", 1, 7), (88, "Ra", "Radio", 2, 7),
    (104, "Rf", "Rutherfordio", 4, 7), (105, "Db", "Dubnio", 5, 7), (106, "Sg", "Seaborgio", 6, 7), (107, "Bh", "Bohrio", 7, 7),
    (108, "Hs", "Hassio", 8, 7), (109, "Mt", "Meitnerio", 9, 7), (110, "Ds", "Darmstatio", 10, 7), (111, "Rg", "Roentgenio", 11, 7),
    (112, "Cn", "Copernicio", 12, 7), (113, "Nh", "Nihonio", 13, 7), (114, "Fl", "Flerovio", 14, 7), (115, "Mc", "Moscovio", 15, 7), (116, "Lv", "Livermorio", 16, 7), (117, "Ts", "Tenesino", 17, 7), (118, "Og", "Oganesón", 18, 7)
]

M, N = 7, 18  # filas, columnas de la tabla
tabla = [[None for c in range(N)] for f in range(M)]
for num, z, nombre, g, p in elementos:
    tabla[p-1][g-1] = (num, z, nombre)

st.title("FlashCards de la Tabla Periódica (sin lantánidos ni actínidos)")
st.markdown("Haz clic en *Siguiente Flashcard* para practicar. Los números de arriba son **grupos**, los de la izquierda son **periodos**.")

# -- Selección aleatoria de un cuadro que contenga un elemento
elementos_disponibles = [(f, c) for f in range(M) for c in range(N) if tabla[f][c]]
if "pos_inq" not in st.session_state:
    st.session_state["pos_inq"] = random.choice(elementos_disponibles)
if st.button("Siguiente Flashcard"):
    st.session_state["pos_inq"] = random.choice(elementos_disponibles)

ff, cc = st.session_state["pos_inq"]

# -- Dibuja la tabla con leyendas de grupo y periodo
st.subheader("¿Qué elemento es?")

# Encabezado de grupos (números de columna)
cols = st.columns(N + 1)
cols[0].markdown(" ")  # Esquina vacía
for c in range(N):
    cols[c + 1].markdown(f"**{c+1}**")

for f in range(M):
    cols = st.columns(N + 1)
    cols[0].markdown(f"**{f+1}**")  # Número de periodo al inicio de la fila
    for c in range(N):
        if tabla[f][c]:
            if (f, c) == (ff, cc):
                # Cuadro incógnita
                cols[c + 1].markdown(
                    "<div style='border:1px solid #444; border-radius:7px; background:#FFFCE0; text-align:center; font-size:28px; height:60px; display:flex; align-items:center; justify-content:center;'>❓</div>",
                    unsafe_allow_html=True
                )
            else:
                # Otros cuadros, vacíos pero con borde
                cols[c + 1].markdown(
                    "<div style='border:1px solid #bbb; border-radius:7px; background:#f8f8f8; height:60px;'>&nbsp;</div>",
                    unsafe_allow_html=True
                )
        else:
            cols[c + 1].markdown(" ")  # Celda vacía (sin elemento)

# -- Mostrar el reverso si el usuario pulsa un botón
if st.button("Mostrar respuesta"):
    num, z, nombre = tabla[ff][cc]
    st.success(f"Elemento: **{nombre}**\n\nSímbolo: **{z}**\n\nNúmero atómico: **{num}**")

st.markdown("*Desarrollado por ChatGPT y Streamlit*")

