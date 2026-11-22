# Accepts material and plant.
#Checks whether the material exists.
#Returns inventory information.
#Does not modify the source data.

# inventory_agent.py

MOCK_INVENTORY = {
    ("MAT-1001", "P100"): {
        "material": "MAT-1001",
        "plant": "P100",
        "available_stock": 120,
        "safety_stock": 100,
    },
    ("MAT-1002", "P100"): {
        "material": "MAT-1002",
        "plant": "P100",
        "available_stock": 20,
        "safety_stock": 50,
    },
}

def validate_input(material, plant):
    """Validate business input before calling the API."""

    if not isinstance(material, str) or not material.strip():
        raise ValueError("Material is required")

    if not isinstance(plant, str) or not plant.strip():
        raise ValueError("Plant is required")

def get_stock(material, plant):
    """Existing capability enhanced with safety stock."""

    validate_input(material, plant)

    key = (material, plant)

    if key not in MOCK_INVENTORY:
        raise ValueError("Material or plant not found")

    return MOCK_INVENTORY[key].copy()

def get_inventory_risk(material, plant):
    """New read-only action to assess inventory risk."""

    stock = get_stock(material, plant)

    available = stock["available_stock"]
    safety_stock = stock["safety_stock"]

    below_safety_stock = available < safety_stock

    return {
        "material": material,
        "plant": plant,
        "available_stock": available,
        "safety_stock": safety_stock,
        "below_safety_stock": below_safety_stock,
        "risk_status": (
            "HIGH"
            if below_safety_stock
            else "NORMAL"
        ),
    }

if __name__ == "__main__":

    result = get_inventory_risk(
        "MAT-1001",
        "P100"
    )

    print(result)