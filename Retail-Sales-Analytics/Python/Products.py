from pathlib import Path
import numpy as np
import pandas as pd

np.random.seed(42)

categories = {
    "Electronics": ["Smartphone", "Laptop", "Tablet", "Headphones", "Smartwatch"],
    "Home": ["Furniture", "Kitchen", "Decor", "Bedding", "Storage"],
    "Clothing": ["Shirt", "T-Shirt", "Jeans", "Shoes", "Jacket"],
    "Sports": ["Cricket", "Football", "Gym", "Cycling", "Swimming"],
    "Beauty": ["Skincare", "Makeup", "Haircare", "Fragrance", "Personal Care"],
}

product_names = {
    "Smartphone": ["iPhone 15", "Samsung Galaxy S24", "Google Pixel 9", "OnePlus 13", "Nothing Phone 3"],
    "Laptop": ["HP Pavilion", "Dell Inspiron 15", "Lenovo ThinkPad", "ASUS VivoBook", "Acer Aspire"],
    "Tablet": ["iPad Air", "Samsung Galaxy Tab S9", "Lenovo Tab P12", "Xiaomi Pad 6", "Microsoft Surface Go"],
    "Headphones": ["Sony WH-1000XM5", "AirPods Pro", "JBL Tune 770NC", "Boat Rockerz 550", "Sennheiser HD 450BT"],
    "Smartwatch": ["Apple Watch Series 10", "Samsung Galaxy Watch 7", "Garmin Venu 3", "Amazfit GTR 4", "Fitbit Sense 2"],
    "Furniture": ["Wooden Chair", "Office Desk", "Dining Table", "Bookshelf", "TV Cabinet"],
    "Kitchen": ["Mixer Grinder", "Pressure Cooker", "Non-Stick Pan", "Electric Kettle", "Microwave Oven"],
    "Decor": ["Wall Clock", "Table Lamp", "Flower Vase", "Photo Frame", "Canvas Painting"],
    "Bedding": ["Bedsheet", "Blanket", "Comforter", "Pillow", "Mattress Protector"],
    "Storage": ["Plastic Storage Box", "Wardrobe Organizer", "Drawer Unit", "Laundry Basket", "Shoe Rack"],
    "Shirt": ["Formal Shirt", "Casual Shirt", "Linen Shirt", "Denim Shirt", "Oxford Shirt"],
    "T-Shirt": ["Polo T-Shirt", "Graphic T-Shirt", "Round Neck T-Shirt", "V-Neck T-Shirt", "Oversized T-Shirt"],
    "Jeans": ["Slim Fit Jeans", "Straight Fit Jeans", "Relaxed Fit Jeans", "Skinny Jeans", "Bootcut Jeans"],
    "Shoes": ["Running Shoes", "Sneakers", "Formal Shoes", "Loafers", "Boots"],
    "Jacket": ["Leather Jacket", "Denim Jacket", "Bomber Jacket", "Puffer Jacket", "Hooded Jacket"],
    "Cricket": ["Cricket Bat", "Cricket Ball", "Batting Gloves", "Cricket Helmet", "Stumps"],
    "Football": ["Football", "Football Boots", "Goalkeeper Gloves", "Shin Guards", "Training Cones"],
    "Gym": ["Dumbbells", "Yoga Mat", "Resistance Bands", "Skipping Rope", "Kettlebell"],
    "Cycling": ["Mountain Bike", "Helmet", "Bike Pump", "Cycling Gloves", "Water Bottle Cage"],
    "Swimming": ["Swimming Goggles", "Swim Cap", "Kickboard", "Swimming Fins", "Pool Towel"],
    "Skincare": ["Face Wash", "Moisturizer", "Sunscreen", "Vitamin C Serum", "Night Cream"],
    "Haircare": ["Shampoo", "Conditioner", "Hair Oil", "Hair Serum", "Hair Mask"],
    "Makeup": ["Foundation", "Lipstick", "Mascara", "Eyeliner", "Compact Powder"],
    "Fragrance": ["Eau de Parfum", "Body Mist", "Roll-On Perfume", "Deodorant", "Cologne"],
    "Personal Care": ["Body Wash", "Face Razor", "Hand Cream", "Toothbrush", "Electric Trimmer"],
}

price_ranges = {
    "Smartphone": {"cost": (12000, 70000), "margin_pct": (0.12, 0.30)},
    "Laptop": {"cost": (20000, 60000), "margin_pct": (0.15, 0.35)},
    "Tablet": {"cost": (10000, 40000), "margin_pct": (0.10, 0.25)},
    "Headphones": {"cost": (2000, 15000), "margin_pct": (0.20, 0.40)},
    "Smartwatch": {"cost": (4000, 25000), "margin_pct": (0.18, 0.35)},
    "Furniture": {"cost": (3000, 30000), "margin_pct": (0.20, 0.45)},
    "Kitchen": {"cost": (1000, 15000), "margin_pct": (0.15, 0.35)},
    "Decor": {"cost": (500, 6000), "margin_pct": (0.20, 0.40)},
    "Bedding": {"cost": (700, 8000), "margin_pct": (0.18, 0.35)},
    "Storage": {"cost": (800, 7000), "margin_pct": (0.15, 0.30)},
    "Shirt": {"cost": (500, 4000), "margin_pct": (0.20, 0.45)},
    "T-Shirt": {"cost": (300, 2500), "margin_pct": (0.20, 0.40)},
    "Jeans": {"cost": (700, 5000), "margin_pct": (0.18, 0.35)},
    "Shoes": {"cost": (1000, 6000), "margin_pct": (0.20, 0.38)},
    "Jacket": {"cost": (1500, 8000), "margin_pct": (0.22, 0.42)},
    "Cricket": {"cost": (500, 8000), "margin_pct": (0.15, 0.35)},
    "Football": {"cost": (400, 6000), "margin_pct": (0.18, 0.35)},
    "Gym": {"cost": (300, 5000), "margin_pct": (0.20, 0.40)},
    "Cycling": {"cost": (1500, 12000), "margin_pct": (0.18, 0.35)},
    "Swimming": {"cost": (400, 4000), "margin_pct": (0.20, 0.35)},
    "Skincare": {"cost": (200, 2500), "margin_pct": (0.25, 0.50)},
    "Haircare": {"cost": (150, 2200), "margin_pct": (0.25, 0.45)},
    "Makeup": {"cost": (300, 3000), "margin_pct": (0.22, 0.42)},
    "Fragrance": {"cost": (250, 3500), "margin_pct": (0.25, 0.50)},
    "Personal Care": {"cost": (100, 1800), "margin_pct": (0.20, 0.40)},
}


def generate_product_data(num_rows=500):
    rows = []
    for i in range(1, num_rows + 1):
        category = np.random.choice(list(categories.keys()))
        subcategory = np.random.choice(categories[category])
        product_name = np.random.choice(product_names[subcategory])

        cost_min, cost_max = price_ranges[subcategory]["cost"]
        margin_min, margin_max = price_ranges[subcategory]["margin_pct"]

        cost_price = np.random.randint(cost_min, cost_max + 1)
        profit_margin = np.random.uniform(margin_min, margin_max)
        profit = round(cost_price * profit_margin, 2)
        selling_price = round(cost_price + profit, 2)

        rows.append(
            {
                "product_id": f"P{i:05d}",
                "product_name": product_name,
                "category": category,
                "subcategory": subcategory,
                "cost_price": cost_price,
                "profit": profit,
                "selling_price": selling_price,
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = generate_product_data(500)

    output_path = Path(r"C:/Users/artist/Desktop/data/raw")
    output_path.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path / "products.csv", index=False)

    print(df.head())
    print("\nSaved product table to:", output_path / "products.csv")