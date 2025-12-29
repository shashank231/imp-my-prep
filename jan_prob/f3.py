from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Any
import csv
import json

@dataclass
class Sale:
    date: str
    product: str
    quantity: float
    price: float

class CSVProcessor:
    def __init__(self):
        self.revenue_by_product = defaultdict(float)
        self.total_revenue = 0.0
        self.total_orders = 0
        self.skipped_rows = 0
    
    def parse_sale_row(self, row: List[str], line_num: int) -> Sale | None:
        """Parse CSV row, return None on error."""
        try:
            if len(row) != 4:
                return None
            date, product, qty_str, price_str = row
            # Handle missing fields
            if not product or qty_str == '' or price_str == '':
                return None
            quantity = float(qty_str)
            price = float(price_str)
            return Sale(date, product.strip(), quantity, price)
        except (ValueError, IndexError):
            return None

    def process_row(self, sale: Sale):
        """Aggregate single valid sale."""
        revenue = sale.quantity * sale.price
        self.revenue_by_product[sale.product] += revenue
        self.total_revenue += revenue
        self.total_orders += 1
    
    def process_csv(self, filepath: str) -> Dict[str, Any]:
        """Main orchestrator: stream + parse + aggregate."""
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"{filepath} not found")
        
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Skip header
            next(reader, None)
            for line_num, row in enumerate(reader, 2):  # line 2+
                sale = self.parse_sale_row(row, line_num)
                if sale:
                    self.process_row(sale)
                else:
                    self.skipped_rows += 1
        
        return self._generate_report()
    
    def _generate_report(self) -> Dict[str, Any]:
        """Format final results."""
        top_products = sorted(
            self.revenue_by_product.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:3]
        
        avg_order_value = self.total_revenue / self.total_orders if self.total_orders else 0
        
        return {
            "revenue_by_product": dict(self.revenue_by_product),
            "top_products": [
                {"product": product, "revenue": revenue}
                for product, revenue in top_products
            ],
            "avg_order_value": round(avg_order_value, 2),
            "total_orders": self.total_orders,
            "skipped_rows": self.skipped_rows,
            "total_revenue": round(self.total_revenue, 2)
        }

# Usage
if __name__ == "__main__":
    processor = CSVProcessor()
    result = processor.process_csv("sales.csv")
    print(json.dumps(result, indent=2))
