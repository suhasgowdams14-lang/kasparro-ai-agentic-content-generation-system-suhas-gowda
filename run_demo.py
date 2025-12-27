from agents.product_page_agent import ProductPageAgent
from agents.faq_page_agent import FAQPageAgent


if __name__ == "__main__":
    sample_product = {
        "name": "Vitamin C Serum",
        "active_concentration": 10,
        "skin_type": ["oily", "dry", "normal"],
        "ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "benefits": ["Brightens skin", "Reduces pigmentation"],
        "usage": "Apply twice daily after cleansing.",
        "side_effects": "May cause mild irritation for sensitive skin.",
        "price_inr": 799
    }

    product_page = ProductPageAgent().run(sample_product)
    faq_page = FAQPageAgent().run(sample_product)

    print("PRODUCT PAGE OUTPUT")
    print(product_page)

    print("\nFAQ PAGE OUTPUT")
    print(faq_page)

