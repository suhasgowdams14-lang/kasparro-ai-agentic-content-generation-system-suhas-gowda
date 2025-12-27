from agents.question_generation_agent import QuestionGenerationAgent


class FAQPageAgent:
    """
    Responsibility:
    - Generate FAQ page content using questions from QuestionGenerationAgent
    """

    def run(self, product: dict) -> dict:
        questions = QuestionGenerationAgent().run(product)

        faq_items = []
        for category, qs in questions.items():
            for q in qs:
                faq_items.append({
                    "question": q,
                    "answer": "Answer generated based on product data."
                })

        return {
            "page_type": "FAQ",
            "faqs": faq_items
        }
