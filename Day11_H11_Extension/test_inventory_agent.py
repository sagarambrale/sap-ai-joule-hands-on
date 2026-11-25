import unittest

from inventory_agent import (
    get_stock,
    get_inventory_risk,
)

class InventoryAgentTests(unittest.TestCase):

    def test_existing_stock_capability(self):
        result = get_stock("MAT-1001", "P100")

        self.assertEqual(
            result["available_stock"], 120
        )

    def test_safety_stock_field(self):
        result = get_stock("MAT-1002", "P100")

        self.assertEqual(
            result["safety_stock"], 50
        )

    def test_high_inventory_risk(self):
        result = get_inventory_risk(
            "MAT-1002", "P100"
        )

        self.assertEqual(
            result["risk_status"], "HIGH"
        )

        self.assertTrue(
            result["below_safety_stock"]
        )

    def test_normal_inventory_risk(self):
        result = get_inventory_risk(
            "MAT-1001", "P100"
        )

        self.assertEqual(
            result["risk_status"], "NORMAL"
        )

    def test_invalid_material(self):
        with self.assertRaises(ValueError):
            get_stock("", "P100")

    def test_unknown_material(self):
        with self.assertRaises(ValueError):
            get_inventory_risk(
                "MAT-9999", "P100"
            )

if __name__ == "__main__":
    unittest.main()