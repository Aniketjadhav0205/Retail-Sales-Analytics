from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)

input_dir = input_dir = Path(r"C:/Users/artist/Desktop/DA project 1/data/raw")

input_dir.mkdir(parents=True, exist_ok=True)

orders = pd.read_csv(input_dir / "orders.csv")
products = pd.read_csv(input_dir / "products.csv")

order_ids = orders["order_id"].astype(str).tolist()
product_ids = products["product_id"].astype(str).tolist()
price_map = dict(zip(products["product_id"].astype(str), products["selling_price"]))

num_items = 250_000
rng = np.random.default_rng(42)

selected_order_ids = rng.choice(order_ids, size=num_items)
selected_product_ids = rng.choice(product_ids, size=num_items)
selected_quantities = rng.integers(1, 6, size=num_items)
selected_unit_prices = [price_map[pid] for pid in selected_product_ids]
selected_discounts = rng.choice([0.0, 0.05, 0.10, 0.15], size=num_items, p=[0.70, 0.15, 0.10, 0.05])

order_items = pd.DataFrame(
    {
        "item_id": [f"I{i:05d}" for i in range(1, num_items + 1)],
        "order_id": selected_order_ids,
        "product_id": selected_product_ids,
        "quantity": selected_quantities,
        "unit_price": selected_unit_prices,
        "discount": selected_discounts,
    }
)

# Add outliers in quantity (~3%)
outlier_mask = np.random.random(num_items) < 0.03
order_items.loc[outlier_mask, "quantity"] = np.random.randint(20, 50, outlier_mask.sum())

# Add missing values in discount (~5%)
mask = np.random.random(len(order_items)) < 0.05
order_items.loc[mask, "discount"] = np.nan

output_file = input_dir / "order_items.csv"
order_items.to_csv(output_file, index=False)

print(order_items.head())
print(f"\nSaved {len(order_items)} order items to: {output_file}")
print("\nNull counts:")
print(order_items.isnull().sum())
