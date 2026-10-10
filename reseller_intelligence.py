import json

# Simulate a 'base' intelligence product that analyzes sales data.
# This is the core product that a reseller would purchase and potentially rebrand.
class BaseIntelligenceProduct:
    def __init__(self, product_name):
        self.product_name = product_name

    def analyze_sales(self, sales_data):
        # Simulate complex analysis: calculate total sales, average sale value, and identify top products.
        total_sales = sum(item['price'] * item['quantity'] for item in sales_data)
        num_transactions = len(sales_data)
        average_sale_value = total_sales / num_transactions if num_transactions > 0 else 0

        product_counts = {}
        for item in sales_data:
            product_counts[item['product']] = product_counts.get(item['product'], 0) + item['quantity']

        top_products = sorted(product_counts.items(), key=lambda item: item[1], reverse=True)

        return {
            "analysis_title": f"Sales Analysis for {self.product_name}",
            "total_revenue": round(total_sales, 2),
            "average_transaction_value": round(average_sale_value, 2),
            "top_selling_products": top_products[:3] # Top 3
        }

# Simulate a reseller who buys the base product and offers it to their own clients.
# The reseller adds their own branding and potentially a markup.
class Reseller:
    def __init__(self, name, markup_percentage):
        self.name = name
        self.markup_percentage = markup_percentage
        # The reseller 'buys' the base product, perhaps at a wholesale price.
        # In a real scenario, this would involve licensing or API access.
        self.intelligence_product = BaseIntelligenceProduct("Core Analytics Engine")

    def offer_to_clients(self, sales_data):
        # Reseller uses the base product's analysis capabilities.
        base_analysis = self.intelligence_product.analyze_sales(sales_data)

        # Reseller applies their markup to the perceived value or adds their own service layer.
        # For simplicity, we'll just present the analysis with their branding.
        reseller_branded_analysis = {
            "reseller_name": self.name,
            "product_offering_name": f"{self.name} Insights",
            "original_analysis": base_analysis,
            "reseller_notes": "Leveraging advanced analytics to boost your business!"
        }
        return reseller_branded_analysis

# --- Demonstration ---

# Sample sales data
sales_records = [
    {"product": "Widget A", "quantity": 5, "price": 10.50},
    {"product": "Gadget B", "quantity": 2, "price": 25.00},
    {"product": "Widget A", "quantity": 3, "price": 10.50},
    {"product": "Thingamajig C", "quantity": 1, "price": 100.00},
    {"product": "Gadget B", "quantity": 4, "price": 25.00},
    {"product": "Widget A", "quantity": 2, "price": 10.50},
]

# Instantiate a reseller
"""
This is where the core concept is demonstrated:
Instead of selling the 'BaseIntelligenceProduct' directly to end-users (analysts),
we have a 'Reseller' who purchases or licenses it.
This reseller then packages and sells it to their own client base,
allowing the original product creator to reach a wider market indirectly
and potentially at a lower per-unit marketing cost.
"""
my_reseller = Reseller(name="DataSolutions Inc.", markup_percentage=20)

# Reseller offers their service to a client using the sales data
client_report = my_reseller.offer_to_clients(sales_records)

# Print the report as if the client received it
print(json.dumps(client_report, indent=2))
