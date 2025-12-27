from agents.product_parser_agent import ProductParserAgent
from logic_blocks.benefits_block import generate_benefits_block
from logic_blocks.usage_block import generate_usage_block
from logic_blocks.safety_block import generate_safety_block


class ProductPageAgent:
    """
    Responsibility:
    - Generate a structured product page using reusable logic blocks
    """

    def run(self, raw_product: dict) -> dict:
        product = ProductParserAgent().run(raw_product)

        return {
            "page_type": "Product",
            "overview": {
                "name": product["name"],
                "active_concentration": product["active_concentration"],
                "skin_type": product["skin_type"]
            },
            "benefits": generate_benefits_block(product["benefits"]),
            "usage": generate_usage_block(product["usage"]),
            "safety": generate_safety_block(product["side_effects"]),
            "price": product["price_inr"]
        }
