class ProductParserAgent:
    """
    Responsibility:
    - Parse raw product input data
    - Normalize it into the internal ProductModel format
    """

    def run(self, raw_data: dict) -> dict:
        return {
            "name": raw_data["Product Name"],
            "active_concentration": int(raw_data["Concentration"].replace("%", "")),
            "skin_type": [s.strip() for s in raw_data["Skin Type"].split(",")],
            "ingredients": [i.strip() for i in raw_data["Key Ingredients"].split(",")],
            "benefits": [b.strip() for b in raw_data["Benefits"].split(",")],
            "usage": raw_data["How to Use"],
            "side_effects": raw_data["Side Effects"],
            "price_inr": int(raw_data["Price"].replace("₹", ""))
        }

