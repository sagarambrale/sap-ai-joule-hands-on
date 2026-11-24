# material = "MAT-1001"
# print(type(material))
#def calculate_shortage(stock, demand):
#    shortage = demand - stock
#    return shortage

#result = calculate_shortage(120, 150)
#print(result)

#materials = ["MAT-1001", "MAT-1002", "MAT-1003"]

#print(materials[0])
#print(materials[1])

#for material in materials:
#    print(material)

#material_data = {
#    "material": "MAT-1001",
#    "plant": "P001",
#    "stock": 120,
#    "demand": 150
#}

#print(material_data["material"])
#print(material_data["stock"])

import json

sap_payload = {
    "material": "MAT-1001",
    "plant": "P001",
    "stock": 180,
    "demand": 150,
    "lead_time_days": 12
}

print("SAP Payload:")
print(sap_payload)

def calculate_inventory_risk(data):

    shortage = data["demand"] - data["stock"]

    if shortage > 0:
        status = "STOCK_SHORTAGE"
    else:
        status = "STOCK_AVAILABLE"

    return {
        "material": data["material"],
        "plant": data["plant"],
        "shortage": max(shortage, 0),
        "status": status
    }

result = calculate_inventory_risk(sap_payload)

print("\nInventory Analysis:")
print(result)

json_output = json.dumps(result, indent=4)

print("\nJSON Output:")
print(json_output)

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


bad_payload = {
    "material": "MAT-2001",
    "plant": "P002",
    "stock": "unknown",
    "demand": 100
}

print(safe_inventory_analysis(bad_payload))