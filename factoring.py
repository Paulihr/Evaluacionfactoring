import streamlit as st

# Definimos las clases

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre

class Deudor(Empresa):
    def __init__(self, nombre, anos_en_mercado, historial_crediticio, ingresos_anuales, endeudamiento, sector):
        super().__init__(nombre)
        self.anos_en_mercado = anos_en_mercado
        self.historial_crediticio = historial_crediticio
        self.ingresos_anuales = ingresos_anuales
        self.endeudamiento = endeudamiento
        self.sector = sector

    def calcular_score(self):
        score = 0
        if self.anos_en_mercado > 10:
            score += 30
        elif self.anos_en_mercado > 5:
            score += 20
        else:
            score += 10

        if self.historial_crediticio == 'bueno':
            score += 40
        elif self.historial_crediticio == 'regular':
            score += 20

        if self.ingresos_anuales > 500000:  # suponiendo un valor en moneda local
            score += 15

        if self.endeudamiento < 0.5:  # ratio de endeudamiento
            score += 15

        return score

def evaluar_credito(deudor, proveedor, monto_solicitado):
    if monto_solicitado <= 0:
        return "Monto solicitado inválido"
    elif deudor.calcular_score() < 70:  # Modifiqué el score mínimo a 70 como ejemplo
        return "Solicitud rechazada: El deudor no cumple con el score mínimo"
    else:
        return "Solicitud aprobada"

# Diseño de la app con Streamlit

st.title('Evaluación de Crédito de Factoring')

# Datos del Proveedor
st.subheader('Datos del Proveedor')
nombre_proveedor = st.text_input('Nombre del Proveedor', '')

# Datos del Deudor
st.subheader('Datos del Deudor')
nombre_deudor = st.text_input('Nombre del Deudor', '')
anos_en_mercado = st.slider('Años en el mercado', 1, 20, 5)
historial_crediticio = st.selectbox('Historial Crediticio', ['bueno', 'regular', 'malo'])
ingresos_anuales = st.number_input('Ingresos Anuales del Deudor', min_value=0.0)
endeudamiento = st.slider('Ratio de Endeudamiento (0 a 1)', 0.0, 1.0, 0.5)
# Puedes agregar más campos según las necesidades

# Monto solicitado
monto_solicitado = st.number_input('Monto solicitado', min_value=1.0)

# Evaluar solicitud
if st.button('Evaluar Solicitud'):
    proveedor = Empresa(nombre_proveedor)
    deudor = Deudor(nombre_deudor, anos_en_mercado, historial_crediticio, ingresos_anuales, endeudamiento, None)
    resultado = evaluar_credito(deudor, proveedor, monto_solicitado)
    st.write(resultado)


