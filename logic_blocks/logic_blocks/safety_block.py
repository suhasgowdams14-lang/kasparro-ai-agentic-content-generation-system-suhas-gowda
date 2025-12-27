def generate_safety_block(side_effects: str) -> dict:
    """
    Format safety and side-effect information into a structured block.
    """
    return {
        "notice": side_effects
    }
