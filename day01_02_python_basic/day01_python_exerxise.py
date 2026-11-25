import json


# Step 1: Simulate SAP payload
materials = [
    {
        "material": "MAT-1001",
        "plant": "P001",
        "stock": 120,
        "demand": 150,
        "lead_time_days": 12
    },
    {
        "material": "MAT-1002",
        "plant": "P001",
        "stock": 250,
        "demand": 100,
        "lead_time_days": 5
    },
    {
        "material": "MAT-1003",
        "plant": "P002",
        "stock": 40,
        "demand": 90,
        "lead_time_days": 20
    }
]


# Step 2: Inventory analysis function
def calculate_inventory_risk(data):

    shortage = data["demand"] - data["stock"]

    if shortage > 0:
        status = "REORDER_REQUIRED"
    else:
        status = "NO_ACTION_NEEDED"

    return {
        data["material"], max(shortage, 0), status
    }


# Step 3: Safe processing
def safe_inventory_analysis(data):

    try:
        stock = data["stock"]
        demand = data["demand"]

        if not isinstance(stock, (int, float)):
            raise ValueError("Stock must be numeric")

        if not isinstance(demand, (int, float)):
            raise ValueError("Demand must be numeric")

        return calculate_inventory_risk(data)

    except KeyError as error:
        return {"error": f"Missing field: {error}"}

    except ValueError as error:
        return {"error": str(error)}


# Step 4: Execute
for material in materials:
    result = safe_inventory_analysis(material)
#    print("Inventory Analysis:")
    print(result)
    # Step 5: Convert to JSON
#    json_output = json.dumps(result, indent=4)
#    print("\nJSON Output:")
#    print(json_output)
