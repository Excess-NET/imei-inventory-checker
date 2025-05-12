import streamlit as st
import pandas as pd
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
import io

st.set_page_config(page_title="IMEI Inventory Checker", layout="centered")
st.title("📱 IMEI Inventory Checker")

# Step 1: Upload Excel File
uploaded_file = st.file_uploader("Step 1: Upload your Excel (.xlsx) file", type="xlsx")

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, dtype=str).fillna("")
        st.success("Excel file loaded successfully!")

        imei_input = st.text_input("Step 2: Enter IMEI")

        if imei_input:
            imei_input = imei_input.strip()
            result = df[df.apply(lambda row: row.astype(str).str.contains(imei_input).any(), axis=1)]

            if not result.empty:
                item = result.iloc[0]
                st.subheader("🔍 Item Details")

                for col in result.columns:
                    st.write(f"**{col}:** {item[col]}")

                # Generate barcode
                imei_val = next((item[c] for c in result.columns if "imei" in c.lower()), "")
                if imei_val:
                    barcode = Code128(imei_val, writer=ImageWriter())
                    buffer = io.BytesIO()
                    barcode.write(buffer)
                    buffer.seek(0)
                    st.image(buffer, caption="Barcode for IMEI", use_column_width=True)
                else:
                    st.warning("No IMEI value found for barcode generation.")
            else:
                st.error("IMEI not found in the inventory.")

    except Exception as e:
        st.error(f"Failed to read Excel file: {e}")
else:
    st.info("Upload an Excel file to begin.")
