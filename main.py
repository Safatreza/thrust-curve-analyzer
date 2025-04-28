# main.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    """
    Create sample thrust data programmatically (dummy data).

    Returns:
        pd.DataFrame: DataFrame with 'time' and 'thrust' columns.
    """
    # Create a simple dataset with time and thrust data (for testing purposes)
    time = np.linspace(0, 10, 100)  # 100 data points from 0 to 10 seconds
    thrust = 10 * np.sin(time) + 15  # Simulated thrust values with some sine wave behavior
    
    # Create a DataFrame
    df = pd.DataFrame({'time': time, 'thrust': thrust})
    
    return df

def detect_anomalies(df, threshold_std=3):
    """
    Detects anomalies in thrust data based on standard deviation threshold.

    Args:
        df (pd.DataFrame): DataFrame with 'thrust' column.
        threshold_std (float): How many standard deviations from the mean to consider an anomaly.

    Returns:
        pd.DataFrame: DataFrame of anomalous points.
    """
    if df.empty:
        return pd.DataFrame()

    thrust = df['thrust']

    mean = thrust.mean()
    std = thrust.std()

    # Identify points where thrust deviates too much from the mean
    anomalies = df[(thrust > mean + threshold_std * std) | (thrust < mean - threshold_std * std)]

    return anomalies

def calculate_metrics(df):
    """
    Calculate total impulse, burn time, and average thrust.

    Args:
        df (pd.DataFrame): DataFrame with 'time' and 'thrust' columns.
        
    Returns:
        tuple: Total impulse (Ns), burn time (s), average thrust (N)
    """
    # Total impulse: Area under the curve (thrust * time)
    total_impulse = np.trapz(df['thrust'], df['time'])

    # Burn time: Time from start to end
    burn_time = df['time'].iloc[-1] - df['time'].iloc[0]

    # Average thrust: Mean thrust
    average_thrust = df['thrust'].mean()

    return total_impulse, burn_time, average_thrust

def main():
    # 1. Load thrust data (using dummy data since no CSV file)
    df = load_data()
    
    # 2. Detect anomalies in the thrust data
    anomalies_df = detect_anomalies(df)
    if not anomalies_df.empty:
        print("Anomalies detected:")
        print(anomalies_df)
    
    # 3. Calculate metrics: total impulse, burn time, average thrust
    total_impulse, burn_time, average_thrust = calculate_metrics(df)

    print(f"Total Impulse: {total_impulse} Ns")
    print(f"Burn Time: {burn_time} seconds")
    print(f"Average Thrust: {average_thrust} N")

    # 4. Plot thrust vs time
    plt.plot(df['time'], df['thrust'], label='Thrust')
    plt.xlabel('Time (s)')
    plt.ylabel('Thrust (N)')
    plt.title('Thrust vs Time')
    
    # Highlight anomalies if any
    if not anomalies_df.empty:
        plt.scatter(anomalies_df['time'], anomalies_df['thrust'], color='red', label='Anomalies', zorder=5)
    
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
