class QuestionGenerationAgent:
    """
    Responsibility:
    - Generate categorized user questions based on ProductModel
    """

    def run(self, product: dict) -> dict:
        return {
            "informational": [
                f"What is {product['name']}?",
                "What are the key ingredients?",
                "What skin types is it suitable for?"
            ],
            "usage": [
                "How should this product be used?",
                "When should it be applied?",
                "Can it be used daily?",
                "Can it be used along with sunscreen?"
            ],
            "safety": [
                "Are there any side effects?",
                "Is it safe for sensitive skin?",
                "Does it cause irritation?"
            ],
            "purchase": [
                "What is the price of the product?",
                "Is it worth the price?",
                "How long does one bottle last?"
            ],
            "comparison": [
                "How does it compare with other Vitamin C serums?",
                "Is it better than similar products?"
            ]
        }

