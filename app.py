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
  st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
  st.title("Modelo de Predicción para el abastecimiento periódico (modelo LSTM)")
  st.write("Autor: Umer Avila - Avance01-Grupo03 | ISIL")
  st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")
  # URLs de imágenes en GitHub
  base_url = "https://raw.githubusercontent.com/umeravila12/timeline_s1/main/timeline_images/"
  imagenes = {
     1: base_url + "timeline1.png",
     2: base_url + "timeline2.png",
     3: base_url + "timeline3.png",
     4: base_url + "timeline4.png",
     5: base_url + "timeline5.png"
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
  if opcion == 1:
   st.info(" **1943 – La Neurona Formal** | Warren McCulloch y Walter Pitts publican el modelo de la Neurona MCP.")
  if opcion == 2:
   st.info(" **1957 – La Invención del Perceptrón** | Frank Rosenblatt crea el Perceptrón.")
  if opcion == 3:
   st.info(" **1986 – La Superación del Estancamiento con Retropropagación** | Geoffrey Hinton, David Rumelhart y Ronald Williams popularizan la Retropropagación.")
  if opcion == 4:
   st.info(" **2009 – El Auge de las Redes Convolucionales (CNN) y GPUs** | Yann LeCun desarrolla LeNet-5 (1998) y el posterior uso de GPUs (a partir de 2009) para acelerar el entrenamiento.")
  if opcion == 5:
   st.info(" **2012 – El Momento de AlexNet en ImageNet** | Alex Krizhevsky, Ilya Sutskever y Geoffrey Hinton (el equipo de AlexNet) ganan la competencia de reconocimiento visual ImageNet (ILSVRC) por un margen abrumador.")  

#############################Pagina 4############################## 
def page4():
  st.info("A")

#############################Pagina 5############################## 
def page5():
  st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
  st.title("Evolución de Equipos de Cómputo | Timeline")
  st.write("Autores: Franco Palacios, Sebastian Gamarra, Daniel Garcia, Gabriel Chipana | ISIL")
  st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de los Equipos de Cómputo.")
  # URLs de imágenes en GitHub
  base_url = "https://raw.githubusercontent.com/francopalacios0599-byte/Timeline_S1/main/timeline_images/"
  imagenes = {
  1: base_url + "Timeline1.png",
  2: base_url + "Timeline2.png",
  3: base_url + "Timeline3.png",
  4: base_url + "Timeline4.png",
  5: base_url + "Timeline5.png"
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
  
  if opcion == 1:
    st.info("""
      **Periodo 1: Las Primeras Computadoras Electrónicas (Años 40 - 50)**  
      En este período, las computadoras eran máquinas masivas que ocupaban habitaciones enteras. Estaban construidas con miles de tubos de vacío, lo que las hacía muy grandes, costosas y propensas a fallas.
      
      **Recursos Computacionales:**  
      • Hardware: Tubos de vacío, relés electromecánicos, tambores magnéticos.  
      • Velocidad: Medida en milisegundos por operación.  
      • Memoria: Muy limitada, apenas unos pocos KB.  
      • Programación: En lenguaje máquina o ensamblador, usando tarjetas perforadas.  
  
      **Aplicaciones Soportadas:**  
      • Cálculos científicos y militares (trayectorias, descifrado de códigos).  
      • Procesamiento de datos para censos o contabilidad.  
      • Simulaciones básicas.
      """)
  if opcion == 2:
      st.info("""
      ### **Periodo 2: La Era de los Transistores y los Mainframes (Años 50 - 60)**  
      La invención del transistor revolucionó la computación, reemplazando los voluminosos tubos de vacío. Esto permitió computadoras más pequeñas, rápidas y fiables, dando origen a los mainframes.
  
      **Recursos Computacionales:**  
      • Hardware: Transistores discretos, memorias de núcleo magnético, cintas magnéticas y discos para almacenamiento masivo.  
      • Velocidad: Medida en microsegundos por operación.  
      • Memoria: Cientos de KB a pocos MB.  
      • Programación: FORTRAN y COBOL; surgen los primeros sistemas operativos.  
  
      **Aplicaciones Soportadas:**  
      • Procesamiento bancario y de seguros.  
      • Gestión de inventarios y nóminas.  
      • Análisis científicos y de ingeniería.  
      • Sistemas de reservación aérea.
      """)
  if opcion == 3:
      st.info("""
      ### **Periodo 3: Los Circuitos Integrados y las Minicomputadoras (Años 60 - 70)**  
      Los circuitos integrados permitieron miniaturizar componentes y aumentar la potencia de cómputo, dando paso a las minicomputadoras.
  
      **Recursos Computacionales:**  
      • Hardware: Circuitos integrados SSI/MSI; procesadores de 8 a 16 bits.  
      • Velocidad: Medida en nanosegundos por operación.  
      • Memoria: Varios MB.  
      • Programación: Sistemas multiusuario como UNIX; surge el lenguaje C.  
  
      **Aplicaciones Soportadas:**  
      • Control industrial.  
      • Sistemas departamentales.  
      • Investigación científica y simulaciones.  
      • Edición de texto y desarrollo de software.  
      • Primeros videojuegos.
      """)
  if opcion == 4:
      st.info("""
      ### **Periodo 4: La Computadora Personal y el Microprocesador (Años 70 - 90)**  
      El microprocesador permitió que la computación llegara a hogares y oficinas, dando inicio a la era de la PC.
  
      **Recursos Computacionales:**  
      • Hardware: Microprocesadores de 8, 16 y 32 bits; RAM en MB; discos duros; pantallas a color.  
      • Velocidad: Medida en MHz.  
      • Memoria: Cientos de KB a decenas de MB.  
      • Programación: Sistemas operativos gráficos (Windows, Mac OS); lenguajes orientados a objetos.  
  
      **Aplicaciones Soportadas:**  
      • Procesadores de texto, hojas de cálculo, bases de datos personales.  
      • Diseño gráfico y publicación de escritorio.  
      • Videojuegos avanzados.  
      • Navegación temprana por Internet (finales de los 90).  
      • Desarrollo de software.
      """)
  if opcion == 5:
      st.info("""
      ### **Periodo 5: La Era de la Computación Ubicua e Internet (Años 2000 - Actualidad)**  
      La computación está presente en todos los dispositivos: móviles, nube, IA y entornos conectados.
  
      **Recursos Computacionales:**  
      • Hardware: CPUs multinúcleo de 64 bits, GPUs, RAM de GB a TB, SSD, móviles, dispositivos IoT.  
      • Velocidad: Medida en GHz, MOPS y FLOPS.  
      • Memoria: GB en móviles; TB y PB en servidores.  
      • Programación: iOS, Android, desarrollo web, Python para IA, contenedores y APIs.  
  
      **Aplicaciones Soportadas:**  
      • Redes sociales y streaming.  
      • Apps móviles de todo tipo.  
      • IA y Machine Learning (voz, imagen, chatbots, autos autónomos).  
      • Realidad Virtual y Aumentada.  
      • Computación en la nube (SaaS, PaaS, IaaS).  
      • IoT y domótica.  
      • Big Data y análisis masivo.
      """)

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
