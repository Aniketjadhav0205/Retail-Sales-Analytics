from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)

store_types = ["Mall", "Outlet", "Franchise", "Flagship"]

locations = [
    ("Mumbai", "Maharashtra", "West"),
    ("Delhi", "Delhi", "North"),
    ("Bengaluru", "Karnataka", "South"),
    ("Chennai", "Tamil Nadu", "South"),
    ("Kolkata", "West Bengal", "East"),
    ("Hyderabad", "Telangana", "South"),
    ("Pune", "Maharashtra", "West"),
    ("Ahmedabad", "Gujarat", "West"),
    ("Jaipur", "Rajasthan", "North"),
    ("Lucknow", "Uttar Pradesh", "North"),
]


def generate_stores(num_rows=50):
    rows = []
    for i in range(1, num_rows + 1):
        city, state, region = locations[(i - 1) % len(locations)]
        store_type = np.random.choice(store_types)
        store_name = f"{city} {'Central' if store_type == 'Mall' else 'Express' if store_type == 'Outlet' else 'Hub' if store_type == 'Franchise' else 'Prime'} Store"

        rows.append(
            {
                "store_id": f"S{i:05d}",
                "store_name": store_name,
                "city": city,
                "state": state,
                "region": region,
                "store_type": store_type,
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = generate_stores(50)

    output_path = Path(r"C:/Users/artist/Desktop/data/raw")
    output_path.mkdir(parents=True, exist_ok=True)

    output_file = output_path / "stores.csv"
    df.to_csv(output_file, index=False)

    print(df.head())
    print(f"\nSaved {len(df)} stores to: {output_file}")
