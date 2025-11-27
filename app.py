import streamlit as st

##############
st.sidebar.image("imagenes/logo_isil_principal.jpg", caption="Actividad #1 | Contenido del Curso")

#############################Pagina 1############################## 

def page1():
  # --- Estética: Usamos layout="wide" para una mejor visualización de la línea de tiempo ---
  st.set_page_config(page_title="Detección de Fraude | ISIL", layout="wide") 
  
  st.title("Detección de Transacciones Fraudulentas | Línea de Tiempo de Hitos Clave")
  st.markdown("---")
  # Autor actualizado según la solicitud del usuario
  st.write("Autor: GRUPO 1 | ISIL") 
  st.write("Explora los 5 eventos tecnológicos que transformaron la lucha contra el fraude bancario, desde la modelización estadística hasta la inteligencia artificial en tiempo real.")
  st.markdown("---")
  
  # --- URLs y Definición de Hitos con Información Ampliada ---
  
  # Se usa la URL de GitHub proporcionada por el usuario
  base_url = "https://raw.githubusercontent.com/adrianticonatapia-debug/timeline_s1/main/timeline_images/"
  
  hitos = {
      1: {
          "año": "Finales del S. XX",
          "nombre": "Sistemas de Puntuación de Riesgo (FICO)",
          "concepto": "Implementación de modelos estadísticos para asignar una puntuación de riesgo a individuos, sentando las bases de la detección predictiva.",
          "descripcion": "El desarrollo de modelos como el FICO Score introdujo la metodología de usar datos históricos y algoritmos para evaluar el riesgo en tiempo real. Aunque inicialmente se centró en la solvencia crediticia, el concepto fue adaptado rápidamente para identificar comportamientos anómalos en transacciones bancarias, migrando de reglas fijas a modelos predictivos.",
          "figura_clave": "Fair Isaac Corporation (FICO) y pioneros de la estadística.",
          "imagen_url": base_url + "timeline1.png"
      },
      2: {
          "año": "Inicios del 2000",
          "nombre": "Autenticación de Doble Factor (2FA)",
          "concepto": "Requerir dos o más factores de verificación (algo que se sabe, algo que se tiene) para el acceso a cuentas y la ejecución de transacciones.",
          "descripcion": "Este desarrollo cambió el enfoque de la detección a la prevención activa. Al exigir un segundo código de verificación (a menudo enviado al móvil del usuario), se hizo mucho más difícil para los defraudadores realizar un 'Account Takeover' (ATO) o completar transacciones no autorizadas, incluso si habían robado la contraseña principal.",
          "figura_clave": "Pioneros de la seguridad en banca online y SMS/Token.",
          "imagen_url": base_url + "timeline2.png"
      },
      3: {
          "año": "2000 - 2015",
          "nombre": "Adopción Global del Chip EMV",
          "concepto": "Transición de la banda magnética fácilmente clonable a tarjetas con un chip que genera un código criptográfico único para cada transacción.",
          "descripcion": "El chip EMV (Europay, Mastercard, Visa) eliminó casi por completo el fraude físico por clonación ('skimming') en el punto de venta. Este éxito tuvo el efecto secundario de forzar a los criminales a migrar sus esfuerzos hacia las transacciones 'Card-Not-Present' (CNP), como las compras en línea, acelerando la necesidad de soluciones avanzadas en el comercio electrónico.",
          "figura_clave": "Consorcio EMV (Europay, Mastercard, Visa).",
          "imagen_url": base_url + "timeline3.png"
      },
      4: {
          "año": "Década de 2010",
          "nombre": "El Auge de Machine Learning (ML) y Deep Learning (DL)",
          "concepto": "Uso de algoritmos de Aprendizaje Automático para analizar patrones de comportamiento y datos masivos con el fin de identificar anomalías sutiles en tiempo real.",
          "descripcion": "Los modelos de IA y ML superaron las limitaciones de las reglas fijas. Son capaces de procesar la hora, ubicación, monto, producto y comportamiento histórico del usuario para detectar transacciones que se desvían de la norma con una precisión mucho mayor, reduciendo drásticamente tanto el fraude como los falsos positivos.",
          "figura_clave": "Científicos de datos y equipos de riesgo bancario.",
          "imagen_url": base_url + "timeline4.png"
      },
      5: {
          "año": "Presente",
          "nombre": "Detección de Huellas Digitales de Dispositivos (Device Fingerprinting)",
          "concepto": "Creación de un identificador único y persistente de un dispositivo basado en sus características técnicas para evaluar su nivel de confianza.",
          "descripcion": "Esta tecnología recopila cientos de parámetros técnicos (tipo de fuente, resolución, OS, etc.) para crear una 'huella' que persiste incluso si el usuario borra cookies o cambia de IP. Es una herramienta crítica para combatir el fraude CNP y de 'mulas de dinero' al identificar instantáneamente si un dispositivo es sospechoso o si ha sido visto en transacciones fraudulentas previas.",
          "figura_clave": "Empresas de ciberseguridad y plataformas antifraude.",
          "imagen_url": base_url + "timeline5.png"
      }
  }
  
  # --- Interfaz de Streamlit ---
  
  # Slider para seleccionar el hito
  opcion = st.slider(
      "Selecciona un punto del timeline",
      min_value=1,
      max_value=5,
      value=1,
      step=1,
      format="HITO N° %d" # Formato para mejor estética
  )
  
  st.markdown("---")
  
  # Obtener los datos del hito seleccionado
  data_hito = hitos[opcion]
  
  # Uso de columnas para una mejor estética (Imagen a la izquierda, Texto a la derecha)
  col1, col2 = st.columns([1, 2.5])
  
  with col1:
      # Muestra el año/periodo de manera destacada
      st.header(data_hito["año"])
      
      # Mostrar la imagen
      st.image(data_hito["imagen_url"], caption=data_hito["nombre"], use_column_width=True)
  
  with col2:
      # Título y Subtítulo
      st.subheader(f":lock: {data_hito['nombre']}")
      st.caption(f"**Concepto Central:** {data_hito['concepto']}")
  
      # Información detallada
      st.markdown("---")
      st.write(data_hito["descripcion"])
      
      # Figura clave destacada
      st.markdown(f"**🛡️ Actores Clave:** *{data_hito['figura_clave']}*")


#############################Pagina 2############################## 

def page2():
  st.set_page_config(page_title="Sesión 2 | ISIL", layout="centered")
  
  st.title("Segmentación de Clientes por Comportamiento Digital | Timeline")
  st.write("Autor: Christian Torres | ISIL")
  st.write(
      "Explora cómo ha evolucionado la segmentación y el análisis del comportamiento digital "
      "en marketing, data science y comercio electrónico."
  )
  
  # URLs de imágenes en GitHub (modifícalas según tus archivos)
    
  base_url = "https://raw.githubusercontent.com/christlv/Avance01-Grupo-2/main/timeline_segmentacion/"
    
  imagenes = {
     1: base_url + "segmentacion1.png",
     2: base_url + "segmentacion2.jpg",
     3: base_url + "segmentacion3.jpg",
     4: base_url + "segmentacion4.jpg",
     5: base_url + "segmentacion5.jpg"
  }
  
  # Slider
  opcion = st.slider(
      "Selecciona un punto del timeline",
      min_value=1,
      max_value=5,
      value=1,
      step=1
  )
  
  # Mostrar imagen según slider
  st.image(imagenes[opcion], use_container_width=True)
  
  # Información del timeline
  if opcion == 1:
      st.info(
          "**2000 – Inicio del análisis web (Web Analytics 1.0)** | "
          "Comienza el uso de métricas básicas como visitas, páginas vistas y tasa de rebote. "
          "Se sientan las bases del análisis de comportamiento digital."
      )
  
  if opcion == 2:
      st.info(
          "**2008 – Evolución hacia Web Analytics 2.0** | "
          "Aparecen métricas orientadas al usuario, segmentación por fuentes, embudos de conversión "
          "y análisis del customer journey."
      )
  
  if opcion == 3:
      st.info(
          "**2015 – Segmentación basada en Machine Learning** | "
          "Se masifica el uso de clustering (K-means, DBSCAN) para segmentar usuarios por comportamiento "
          "como frecuencia, valor, navegación o intención de compra."
      )
  
  if opcion == 4:
      st.info(
          "**2018 – Personalización en tiempo real** | "
          "Plataformas de e-commerce y marketing digital comienzan a personalizar contenido dinámicamente "
          "según el comportamiento histórico y actual del usuario."
      )
  
  if opcion == 5:
      st.info(
          "**2023 – Segmentación avanzada con IA generativa y big data** | "
          "La IA puede analizar interacciones a gran escala, generar perfiles de clientes, predecir comportamientos "
          "y optimizar campañas automáticamente."
      )


#############################Pagina 3############################## 
def page3():
  st.info("A")

#############################Pagina 4############################## 
def page4():
  st.info("A")

#############################Pagina 5############################## 
def page5():
  st.info("B")

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Grupo 01": page1,
  "Grupo 02": page2,
  "Grupo 03": page3,
  "Grupo 04": page4,
  "Grupo 05": page5,
}

selected_page = st.sidebar.selectbox("Selecciona", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
