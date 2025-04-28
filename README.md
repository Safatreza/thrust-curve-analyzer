# Thrust Curve Analyzer for UAV Engines

This project analyzes thrust data from UAV engines by reading CSV or sensor logs, detecting anomalies, and calculating key metrics such as total impulse, burn time, and average thrust. It also provides real-time plots of thrust vs. time, with anomaly detection highlighted.

## Features

- **Real-time thrust vs. time plot**: Visualizes the thrust data over time.
- **Anomaly detection**: Detects anomalies in thrust data based on standard deviation thresholds.
- **Metrics calculation**: Calculates total impulse (Ns), burn time (s), and average thrust (N).
- **Data cleaning and processing**: Includes automated handling of anomalies and other data inconsistencies.

## Requirements

- Python 3.7 or higher
- `pandas`
- `matplotlib`
- `numpy`

You can install the necessary dependencies using `pip`:

```bash
pip install pandas matplotlib numpy
