def generate_benefits_block(benefits: list) -> list:
    """
    Convert a list of benefits into a structured format.
    """
    return [{"benefit": benefit} for benefit in benefits]
