{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqOwjvQMvSWvbAZO9ymcFM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/usmangul23/Scientific-Calculator/blob/main/unit_conversion_tool.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hgZGUNeR504u",
        "outputId": "4dfb0baf-6a20-4529-f773-085659457d4c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Unit Conversion Tool\n",
            "1. Length\n",
            "2. Weight\n",
            "3. Pressure\n",
            "4. Temperature\n",
            "Select conversion type (1-4): 1\n",
            "1. Meters to Feet\n",
            "2. Feet to Meters\n",
            "Select unit (1-2): 1\n",
            "Enter the value: 1\n",
            "1.0 meters is equal to 3.28084 feet.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Conversion functions\n",
        "\n",
        "# Length Conversion (meters <-> feet)\n",
        "def meters_to_feet(meters):\n",
        "    return meters * 3.28084\n",
        "\n",
        "def feet_to_meters(feet):\n",
        "    return feet / 3.28084\n",
        "\n",
        "# Weight Conversion (kilograms <-> pounds)\n",
        "def kg_to_pounds(kg):\n",
        "    return kg * 2.20462\n",
        "\n",
        "def pounds_to_kg(pounds):\n",
        "    return pounds / 2.20462\n",
        "\n",
        "# Pressure Conversion (Pascal <-> PSI)\n",
        "def pascal_to_psi(pascal):\n",
        "    return pascal * 0.000145038\n",
        "\n",
        "def psi_to_pascal(psi):\n",
        "    return psi / 0.000145038\n",
        "\n",
        "# Temperature Conversion (Celsius <-> Fahrenheit)\n",
        "def celsius_to_fahrenheit(celsius):\n",
        "    return (celsius * 9/5) + 32\n",
        "\n",
        "def fahrenheit_to_celsius(fahrenheit):\n",
        "    return (fahrenheit - 32) * 5/9\n",
        "\n",
        "# Streamlit app\n",
        "st.title(\"Unit Conversion Tool\")\n",
        "\n",
        "# Select the type of conversion\n",
        "conversion_type = st.selectbox(\"Select conversion type\",\n",
        "                               [\"Length\", \"Weight\", \"Pressure\", \"Temperature\"])\n",
        "\n",
        "if conversion_type == \"Length\":\n",
        "    # Length conversion\n",
        "    length_unit = st.selectbox(\"Select unit\", [\"Meters to Feet\", \"Feet to Meters\"])\n",
        "    length_value = st.number_input(\"Enter the value\", format=\"%.2f\")\n",
        "\n",
        "    if st.button(\"Convert\"):\n",
        "        if length_unit == \"Meters to Feet\":\n",
        "            result = meters_to_feet(length_value)\n",
        "            st.write(f\"{length_value} meters is equal to {result} feet.\")\n",
        "        else:\n",
        "            result = feet_to_meters(length_value)\n",
        "            st.write(f\"{length_value} feet is equal to {result} meters.\")\n",
        "\n",
        "elif conversion_type == \"Weight\":\n",
        "    # Weight conversion\n",
        "    weight_unit = st.selectbox(\"Select unit\", [\"Kilograms to Pounds\", \"Pounds to Kilograms\"])\n",
        "    weight_value = st.number_input(\"Enter the value\", format=\"%.2f\")\n",
        "\n",
        "    if st.button(\"Convert\"):\n",
        "        if weight_unit == \"Kilograms to Pounds\":\n",
        "            result = kg_to_pounds(weight_value)\n",
        "            st.write(f\"{weight_value} kg is equal to {result} pounds.\")\n",
        "        else:\n",
        "            result = pounds_to_kg(weight_value)\n",
        "            st.write(f\"{weight_value} pounds is equal to {result} kg.\")\n",
        "\n",
        "elif conversion_type == \"Pressure\":\n",
        "    # Pressure conversion\n",
        "    pressure_unit = st.selectbox(\"Select unit\", [\"Pascal to PSI\", \"PSI to Pascal\"])\n",
        "    pressure_value = st.number_input(\"Enter the value\", format=\"%.2f\")\n",
        "\n",
        "    if st.button(\"Convert\"):\n",
        "        if pressure_unit == \"Pascal to PSI\":\n",
        "            result = pascal_to_psi(pressure_value)\n",
        "            st.write(f\"{pressure_value} Pascal is equal to {result} PSI.\")\n",
        "        else:\n",
        "            result = psi_to_pascal(pressure_value)\n",
        "            st.write(f\"{pressure_value} PSI is equal to {result} Pascal.\")\n",
        "\n",
        "elif conversion_type == \"Temperature\":\n",
        "    # Temperature conversion\n",
        "    temp_unit = st.selectbox(\"Select unit\", [\"Celsius to Fahrenheit\", \"Fahrenheit to Celsius\"])\n",
        "    temp_value = st.number_input(\"Enter the value\", format=\"%.2f\")\n",
        "\n",
        "    if st.button(\"Convert\"):\n",
        "        if temp_unit == \"Celsius to Fahrenheit\":\n",
        "            result = celsius_to_fahrenheit(temp_value)\n",
        "            st.write(f\"{temp_value} Celsius is equal to {result} Fahrenheit.\")\n",
        "        else:\n",
        "            result = fahrenheit_to_celsius(temp_value)\n",
        "            st.write(f\"{temp_value} Fahrenheit is equal to {result} Celsius.\")\n"
      ]
    }
  ]
}