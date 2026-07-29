from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)

input_dir = Path(r"C:/Users/artist/Desktop/data/raw")
input_dir.mkdir(parents=True, exist_ok=True)

stores_path = input_dir / "stores.csv"
if stores_path.exists():
    stores = pd.read_csv(stores_path)
    store_ids = stores["store_id"].astype(str).tolist()
else:
    store_ids = [f"S{i:05d}" for i in range(1, 51)]

customer_ids = [f"C{i:05d}" for i in range(1, 10001)]
channels = ["Online", "In-Store", "Mobile App"]
channel_probs = [0.45, 0.35, 0.20]
statuses = ["Completed", "Returned", "Cancelled", "Pending"]
status_probs = [0.78, 0.10, 0.07, 0.05]


def generate_orders(num_rows=100000):
    rng = np.random.default_rng(42)

    order_dates = pd.date_range(start="2022-01-01", end="2024-12-31", freq="D")
    selected_dates = pd.to_datetime(rng.choice(order_dates, size=num_rows))

    rows = []
    for i in range(1, num_rows + 1):
        rows.append(
            {
                "order_id": f"O{i:05d}",
                "customer_id": rng.choice(customer_ids),
                "store_id": rng.choice(store_ids),
                "order_date": selected_dates[i - 1].strftime("%Y-%m-%d"),
                "channel": rng.choice(channels, p=channel_probs),
                "status": rng.choice(statuses, p=status_probs),
            }
        )

    return pd.DataFrame(rows)

    
if __name__ == "__main__":
    df = generate_orders(100000)

    #  Add missing values HERE — after df is defined
    for col in ["channel", "status"]:
        mask = np.random.random(len(df)) < 0.05
        df.loc[mask, col] = np.nan

    output_file = input_dir / "orders.csv"
    df.to_csv(output_file, index=False)

    print(df.head())
    print(f"\nSaved {len(df)} orders to: {output_file}")
    print("\nNull counts:")
    print(df.isnull().sum())

