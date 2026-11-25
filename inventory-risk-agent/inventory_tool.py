import json

# Mock data for our Inventory Risk Agent.
# In a real SAP integration, this would come
# from an authorized API or service.

INVENTORY_JSON = """
[
  {
    "material_id": "MAT-1001",
    "material_name": "Steel Sheet",
    "stock_qty": 120,
    "daily_demand": 30,
    "lead_time_days": 5
  },
  {
    "material_id": "MAT-1002",
    "material_name": "Industrial Bearing",
    "stock_qty": 300,
    "daily_demand": 20,
    "lead_time_days": 7
  },
  {
    "material_id": "MAT-1003",
    "material_name": "Copper Wire",
    "stock_qty": 50,
    "daily_demand": 25,
    "lead_time_days": 4
  }
]
"""

def get_inventory(material_id):
    """Read one material from mock inventory data."""
    records = json.loads(INVENTORY_JSON)

    for record in records:
        if record["material_id"] == material_id:
            return {
                "success": True,
                "data": record
            }

    return {
        "success": False,
        "error": "Material not found"
    }

if __name__ == "__main__":
    requested_material = input(
        "Enter material ID (e.g. MAT-1001): "
    ).strip().upper()

    result = get_inventory(requested_material)

    print("\nTool response:")
    print(json.dumps(result, indent=2))