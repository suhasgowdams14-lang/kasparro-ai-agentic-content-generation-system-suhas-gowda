class ProductParserAgent:
    """
    Responsibility:
    - Parse raw product input data
    - Normalize it into the internal ProductModel format
    """

    def run(self, raw_data: dict) -> dict:
        return {
            "name": raw_data["name"],
            "active_concentration": raw_data["active_concentration"],
            "skin_type": raw_data["skin_type"],
            "ingredients": raw_data["ingredients"],
            "benefits": raw_data["benefits"],
            "usage": raw_data["usage"],
            "side_effects": raw_data["side_effects"],
            "price_inr": raw_data["price_inr"]
        }
