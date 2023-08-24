import streamlit as st

# Definimos las clases como antes

class Empresa:
    def __init__(self, ruc, nombre, direccion):
        self.ruc = ruc
        self.nombre = nombre
        self.direccion = direccion

class Deudor(Empresa):
    def __init__(self, ruc, nombre, direccion, anos_en_mercado, historial_crediticio, indicadores_financieros, sector):
        super().__init__(ruc, nombre, direccion)
        self.anos_en_mercado = anos_en_mercado
        self.historial_crediticio = historial_crediticio
        self.indicadores_financieros = indicadores_financieros
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
        return score

def evaluar_credito(deudor, proveedor, monto_solicitado):
    if monto_solicitado <= 0:
        return "Monto solicitado inválido"
    elif deudor.calcular_score() < 50:  # Ejemplo: Requiere un score mínimo
        return "Solicitud rechazada: El deudor no cumple con el score mínimo"
    else:
        return "Solicitud aprobada"

# Diseño de la app con Streamlit

st.title('Evaluación de Crédito de Factoring')

# Datos del Proveedor
st.subheader('Datos del Proveedor')
ruc_proveedor = st.text_input('RUC', '')
nombre_proveedor = st.text_input('Nombre', '')
direccion_proveedor = st.text_input('Dirección', '')

# Datos del Deudor
st.subheader('Datos del Deudor')
ruc_deudor = st.text_input('RUC del Deudor', '')
nombre_deudor = st.text_input('Nombre del Deudor', '')
direccion_deudor = st.text_input('Dirección del Deudor', '')
anos_en_mercado = st.slider('Años en el mercado', 1, 20, 5)
historial_crediticio = st.selectbox('Historial Crediticio', ['bueno', 'regular', 'malo'])
# Aquí puedes agregar más campos para los indicadores financieros y otros datos

# Monto solicitado
monto_solicitado = st.number_input('Monto solicitado', min_value=1.0)

# Evaluar solicitud
if st.button('Evaluar Solicitud'):
    proveedor = Empresa(ruc_proveedor, nombre_proveedor, direccion_proveedor)
    deudor = Deudor(ruc_deudor, nombre_deudor, direccion_deudor, anos_en_mercado, historial_crediticio, None, None)
    resultado = evaluar_credito(deudor, proveedor, monto_solicitado)
    st.write(resultado)

