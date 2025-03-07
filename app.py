# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:13:59 2025

@author: sala4
"""

import streamlit as st

# Título de la aplicación
st.title("Cálculo de Balance de Masa para la Producción de Néctar")

# Ingreso de datos interactivos
pulpa_kg = st.number_input("Ingrese la cantidad de pulpa (kg):", min_value=0.0, step=0.1)
brix_pulpa = st.number_input("Ingrese los grados Brix de la pulpa:", min_value=0.0, step=0.1)
nectar_kg = st.number_input("Ingrese la cantidad de néctar a producir (kg):", min_value=0.0, step=0.1)
brix_nectar = st.number_input("Ingrese los grados Brix del néctar:", min_value=0.0, step=0.1)

# Verificar si los inputs son válidos
if pulpa_kg > 0 and brix_pulpa > 0 and nectar_kg > 0 and brix_nectar > 0:
    
    # Cálculo de la cantidad de sólidos solubles en la pulpa
    solidos_pulpa_kg = (brix_pulpa / 100) * pulpa_kg

    # Cálculo de la cantidad de sólidos solubles en el néctar
    solidos_nectar_kg = (brix_nectar / 100) * nectar_kg

    # Cálculo de la cantidad de azúcar a agregar
    azucar_kg = solidos_nectar_kg - solidos_pulpa_kg

    # Cálculo de la cantidad de agua a agregar
    agua_kg = nectar_kg - pulpa_kg - azucar_kg

    # Mostrar los resultados
    st.subheader("Resultados del Balance de Masa")
    st.write(f"Cantidad de azúcar a agregar: {azucar_kg:.2f} kg")
    st.write(f"Cantidad de agua a agregar: {agua_kg:.2f} kg")

    # Validación de los resultados
    st.subheader("Validación del Balance de Masa")
    st.write(f"Masa inicial (pulpa): {pulpa_kg} kg")
    st.write(f"Masa de azúcar agregada: {azucar_kg:.2f} kg")
    st.write(f"Masa de agua agregada: {agua_kg:.2f} kg")
    st.write(f"Masa final (néctar): {pulpa_kg + azucar_kg + agua_kg:.2f} kg")
    st.write(f"Masa esperada de néctar: {nectar_kg} kg")

    # Validación de los grados Brix
    brix_final = (solidos_nectar_kg / (pulpa_kg + azucar_kg + agua_kg)) * 100
    st.subheader("Validación de los Grados Brix")
    st.write(f"Grados Brix finales calculados: {brix_final:.2f} °Brix")
    st.write(f"Grados Brix esperados: {brix_nectar} °Brix")

else:
    st.warning("Por favor, ingrese todos los valores correctamente.")
