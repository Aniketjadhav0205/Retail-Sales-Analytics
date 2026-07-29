# 🛍️ Retail Sales Analytics

An end-to-end data analytics portfolio project that simulates the sales operations of a multi-city retail chain — from **synthetic data generation** in Python, to **relational schema design & analysis** in SQL, to an interactive **Power BI dashboard**.

---

## 📌 Project Overview

This project models a fictional retail business operating across 10 Indian cities, with customers, stores, products, orders, and order-level transactions. The goal is to demonstrate a full analytics workflow: generating realistic (and realistically messy) data, structuring it in a relational database, writing SQL to answer business questions, and visualizing key metrics in a BI dashboard.

**Business questions explored:**
- Which customer segments and regions drive the most orders?
- What are the best-selling and highest-margin product categories?
- How do sales channels (Online / In-Store / Mobile App) compare?
- Which customers or products have zero activity (churn / dead stock)?
- What does the order fulfillment funnel look like (Completed / Returned / Cancelled / Pending)?

---

## 🧰 Tech Stack

| Layer | Tools |
|---|---|
| Data Generation | Python (`pandas`, `numpy`, `Faker`) |
| Database & Analysis | SQL (MySQL) |
| Visualization | Power BI |

---

## 🗂️ Dataset

Synthetic data was generated with realistic imperfections (missing values, outliers) to mimic real-world data cleaning challenges.

| Table | Rows | Description |
|---|---|---|
| `customers` | 10,000 | Customer profile, region, signup date, and segment (VIP / Regular / New / At-Risk) |
| `products` | 500 | Product catalog across 5 categories with cost, profit, and selling price |
| `stores` | 50 | Store locations across 10 Indian cities with store type (Mall / Outlet / Franchise / Flagship) |
| `orders` | 100,000 | Order-level records with channel and fulfillment status |
| `order_items` | 250,000 | Line-item detail per order — quantity, unit price, discount |

**Entity relationships:**

```
customers ─┐
           ├─< orders >─┐
stores ────┘            ├─< order_items >─ products
```

---

## 📁 Repository Structure

```
Retail-Sales-Analytics/
├── Data/               # Generated CSV datasets
│   ├── customers.csv
│   ├── products.csv
│   ├── stores.csv
│   ├── orders.csv
│   └── order_items.csv
├── Python/             # Synthetic data generation scripts
│   ├── customers.py
│   ├── Products.py
│   ├── store.py
│   ├── orders.py
│   └── order_items.py
├── SQL/                # Schema creation + analysis queries
│   └── retail_analysis.sql
└── Dashboard/          # Power BI dashboard
    └── retail_dashboard.pbix
```

---

## ⚙️ How It Works

1. **Data Generation** (`Python/`) — Each script generates one table using `Faker` and `numpy`, seeding realistic distributions (e.g. 70% of customers are "Regular" segment, 5% "VIP") and deliberately injecting nulls and outliers for cleaning practice.
2. **Schema & Analysis** (`SQL/`) — Tables are created with primary/foreign key constraints linking customers → orders → order_items → products, and stores → orders. Analysis queries cover aggregations, joins across all five tables, and left-join "gap" queries (e.g. customers with no orders).
3. **Dashboard** (`Dashboard/`) — The cleaned data is visualized in Power BI to surface sales trends, regional performance, and customer segmentation.

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Aniketjadhav0205/Retail-Sales-Analytics.git
cd Retail-Sales-Analytics

# Install dependencies
pip install pandas numpy faker

# Generate the datasets (run in order — orders.py and order_items.py depend on earlier outputs)
python Python/store.py
python Python/customers.py
python Python/Products.py
python Python/orders.py
python Python/order_items.py
```

Then load the CSVs into MySQL using the schema in `SQL/retail_analysis.sql`, and open `Dashboard/retail_dashboard.pbix` in Power BI Desktop.

---

## 📊 Dashboard Preview

*(Add a screenshot of your Power BI dashboard here — drag an image into this section on GitHub, e.g.)*

```
![Dashboard Preview](Dashboard/dashboard_preview.png)
```

---

## 🔮 Future Improvements

- Parameterize file paths (currently hardcoded to local `C:/Users/...` paths) using relative paths or a config file
- Add a `requirements.txt`
- Automate the SQL schema + load with a single setup script
- Add data validation / unit tests for the generation scripts

---

## 👤 Author

**Aniket Jadhav**
📎 [GitHub](https://github.com/Aniketjadhav0205)
