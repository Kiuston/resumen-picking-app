
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análisis de cajas por técnico", layout="wide")

st.title("📦 Análisis de cajas completas y picking por técnico")
uploaded_file = st.file_uploader("📂 Subí tu archivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, sheet_name="LASER", header=None)
        st.success("✅ Hoja 'LASER' encontrada correctamente.")
        
        # Muestra previa por si hace falta revisar
        st.subheader("👁️ Vista previa de los primeros datos:")
        st.dataframe(df.head(10))
        
        # Aquí iría el análisis real por técnico...
        st.info("🔧 Aquí se mostrarán las estadísticas y gráficos por técnico automáticamente.")
        
    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {e}")
