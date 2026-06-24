import numpy as np

# ── Seed for reproducibility ──────────────────────────────────────────────────
np.random.seed(42)

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

# ── Simulate a full year of daily data ───────────────────────────────────────
# Temperature (°C): Kathmandu seasonal pattern + noise
base_temps = np.array([
    10, 13, 18, 23, 26, 27, 26, 26, 25, 21, 15, 11  # monthly averages
])
daily_temps = np.repeat(base_temps, [31,28,31,30,31,30,31,31,30,31,30,31])
daily_temps = daily_temps + np.random.normal(0, 3, size=365)   # ±3°C noise

# Rainfall (mm): monsoon-heavy (Jun–Sep), dry otherwise
monthly_rain = np.array([
    15, 20, 35, 60, 120, 240, 365, 310, 180, 50, 10, 8
])
daily_rain_base = np.repeat(monthly_rain / np.array([31,28,31,30,31,30,31,31,30,31,30,31]), 
                             [31,28,31,30,31,30,31,31,30,31,30,31])
daily_rain = np.maximum(0, daily_rain_base + np.random.exponential(2, size=365))

# Humidity (%) correlated with rain
daily_humidity = np.clip(40 + daily_rain * 0.8 + np.random.normal(0, 5, 365), 20, 100)

# ── Build monthly index boundaries ───────────────────────────────────────────
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_ends    = np.cumsum(days_in_month)
month_starts  = np.concatenate([[0], month_ends[:-1]])

def monthly_stat(data, func):
    return np.array([func(data[s:e]) for s, e in zip(month_starts, month_ends)])

monthly_avg_temp  = monthly_stat(daily_temps,    np.mean)
monthly_max_temp  = monthly_stat(daily_temps,    np.max)
monthly_min_temp  = monthly_stat(daily_temps,    np.min)
monthly_total_rain = monthly_stat(daily_rain,    np.sum)
monthly_avg_humid = monthly_stat(daily_humidity, np.mean)

# ── Annual statistics ─────────────────────────────────────────────────────────
print("=" * 52)
print("   KATHMANDU WEATHER REPORT — 2024 (Simulated)")
print("=" * 52)

print("\n── Annual Temperature (°C) ──────────────────────")
print(f"  Mean      : {np.mean(daily_temps):.1f}°C")
print(f"  Hottest   : {np.max(daily_temps):.1f}°C")
print(f"  Coldest   : {np.min(daily_temps):.1f}°C")
print(f"  Std Dev   : {np.std(daily_temps):.1f}°C")

print("\n── Annual Rainfall ──────────────────────────────")
print(f"  Total     : {np.sum(daily_rain):.1f} mm")
print(f"  Avg/day   : {np.mean(daily_rain):.2f} mm")
print(f"  Wettest month : {MONTHS[np.argmax(monthly_total_rain)]} "
      f"({np.max(monthly_total_rain):.0f} mm)")
print(f"  Driest month  : {MONTHS[np.argmin(monthly_total_rain)]} "
      f"({np.min(monthly_total_rain):.0f} mm)")

print("\n── Humidity ─────────────────────────────────────")
print(f"  Mean      : {np.mean(daily_humidity):.1f}%")
print(f"  Max       : {np.max(daily_humidity):.1f}%")
print(f"  Min       : {np.min(daily_humidity):.1f}%")

# ── Monthly breakdown ─────────────────────────────────────────────────────────
print("\n── Monthly Breakdown ────────────────────────────")
print(f"  {'Month':<6} {'Avg°C':>6} {'Max°C':>6} {'Min°C':>6} {'Rain mm':>8} {'Humid%':>7}")
print("  " + "-" * 42)
for i, month in enumerate(MONTHS):
    print(f"  {month:<6} {monthly_avg_temp[i]:>6.1f} {monthly_max_temp[i]:>6.1f} "
          f"{monthly_min_temp[i]:>6.1f} {monthly_total_rain[i]:>8.1f} {monthly_avg_humid[i]:>7.1f}")

# ── Seasonal analysis ─────────────────────────────────────────────────────────
# Winter: Dec–Feb (indices 11,0,1)  Spring: Mar–May (2–4)
# Summer/Monsoon: Jun–Sep (5–8)     Autumn: Oct–Nov (9–10)
season_indices = {
    "Winter (Dec-Feb)" : [11, 0, 1],
    "Spring (Mar-May)" : [2, 3, 4],
    "Monsoon (Jun-Sep)": [5, 6, 7, 8],
    "Autumn (Oct-Nov)" : [9, 10],
}

print("\n── Seasonal Averages ────────────────────────────")
print(f"  {'Season':<22} {'Avg Temp':>9} {'Total Rain':>11}")
print("  " + "-" * 44)
for season, idx in season_indices.items():
    temps = np.concatenate([daily_temps[month_starts[i]:month_ends[i]] for i in idx])
    rain  = np.concatenate([daily_rain[month_starts[i]:month_ends[i]]  for i in idx])
    print(f"  {season:<22} {np.mean(temps):>8.1f}°C {np.sum(rain):>10.1f} mm")

# ── Anomaly detection ─────────────────────────────────────────────────────────
temp_mean = np.mean(daily_temps)
temp_std  = np.std(daily_temps)
hot_days  = np.sum(daily_temps > temp_mean + 2 * temp_std)
cold_days = np.sum(daily_temps < temp_mean - 2 * temp_std)
heavy_rain_days = np.sum(daily_rain > 20)

print("\n── Notable Days ─────────────────────────────────")
print(f"  Unusually hot days  (>mean+2σ): {hot_days}")
print(f"  Unusually cold days (<mean-2σ): {cold_days}")
print(f"  Heavy rain days     (>20 mm)  : {heavy_rain_days}")

# ── Temperature–rainfall correlation ─────────────────────────────────────────
corr = np.corrcoef(monthly_avg_temp, monthly_total_rain)[0, 1]
print(f"\n── Temperature vs Rainfall Correlation : {corr:.3f}")
if corr > 0.5:
    print("  Warmer months tend to receive more rainfall (monsoon pattern).")
elif corr < -0.5:
    print("  Cooler months tend to receive more rainfall.")
else:
    print("  Weak correlation between temperature and rainfall.")

print("\n" + "=" * 52)