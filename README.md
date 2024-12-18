# Analiza Stężenia Zanieczyszczeń Powietrza (CO) z wykorzystaniem LSTM i Analizy Wizualnej

## Opis Projektu

Celem projektu jest analiza stężenia zanieczyszczeń powietrza (głównie **CO**) oraz stworzenie modelu predykcyjnego z użyciem **Long Short-Term Memory (LSTM)** do prognozowania poziomu zanieczyszczeń. Projekt obejmuje przetwarzanie danych, analizę korelacji między zmiennymi oraz tworzenie wizualizacji w celu lepszego zrozumienia trendów.

## Dane

Użyto zbioru danych `AirQuality.csv`, zawierającego informacje o:
- **CO(GT)** – Stężenie tlenku węgla (mg/m³)
- **NOx(GT)** – Stężenie tlenków azotu (ppb)
- **NO2(GT)** – Stężenie dwutlenku azotu (µg/m³)
- **C6H6(GT)** – Stężenie benzenu (µg/m³)
- **T** – Temperatura (°C)
- **RH** – Wilgotność względna (%)

## Wymagania

Aby uruchomić projekt, należy zainstalować poniższe biblioteki:
```bash
pip install pandas numpy matplotlib seaborn tensorflow scikit-learn statsmodels
# Analiza Stężenia Zanieczyszczeń Powietrza (CO) z wykorzystaniem LSTM i Analizy Wizualnej

## Struktura Projektu

### Przygotowanie danych
- Łączenie kolumn daty i czasu w jedną kolumnę `Datetime`.
- Usuwanie wartości ujemnych oraz brakujących danych (zamiana na średnią).
- Konwersja danych na wartości numeryczne.

### Analiza wizualna
- Wizualizacja zmienności stężenia **CO** w czasie.
- Wpływ temperatury i wilgotności na stężenie **CO**.
- Analiza korelacji między zmiennymi.
- Rozkład miesięczny i histogram stężenia **CO**.

### Modelowanie LSTM
- Przygotowanie danych czasowych (sekwencje o długości 12).
- Normalizacja danych za pomocą **MinMaxScaler**.
- Budowa i trenowanie modelu **LSTM** z warstwami Dropout dla regularizacji.
- Ocena wyników za pomocą **MAE**, **MSE** i **R²**.
- Wizualizacja wyników przewidywań w porównaniu z wartościami rzeczywistymi.

### Analiza dekompozycji sezonowej
- Dekompozycja stężenia **CO** na składowe: **trend**, **sezonowość** i **reszty**.

---

## Wyniki

### Wizualizacja danych:
- **Zmienność stężenia CO w czasie**  
![CO Trend](images/CO_plot.png)

- **Zależność CO od temperatury**  
![Temperature Impact](images/CO_vs_Temp.png)

- **Macierz korelacji**  
![Correlation Heatmap](images/correlation.png)

### Wyniki modelu:
- **Test Loss**: `wartość`
- **Metryki**:  
  - **Mean Squared Error (MSE):** `wartość`  
  - **Mean Absolute Error (MAE):** `wartość`  
  - **R² Score:** `wartość`  

---

## Uruchamianie Projektu

1. **Pobierz repozytorium**:
   ```bash
   git clone https://github.com/TwojeRepo/air-quality-lstm.git
   cd air-quality-lstm
