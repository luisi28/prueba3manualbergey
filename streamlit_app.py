if busqueda:
    resultado = [b for b in data if busqueda.lower() in b["nombre"].lower()]
    if resultado:
        for b in resultado:
            st.subheader(b["nombre"])
            st.write(f"**Morfología:** {b['morfologia']}")
            st.write(f"**Metabolismo:** {b['metabolismo']}")
            st.write(f"**Hábitat:** {b['habitat']}")
            st.write(f"**Importancia:** {b['importancia']}")
            if b["imagen"].startswith("http"):
                st.image(b["imagen"], caption=b["nombre"], use_container_width=True)
            else:
                st.image(b["imagen"], caption=b["nombre"], use_container_width=True)
    else:
        st.warning("No se encontró la bacteria buscada.")
else:
    st.info("Ingresa el nombre de una bacteria para ver su información.")
