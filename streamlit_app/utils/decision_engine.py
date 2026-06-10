def credit_decision(
    pd_value,
    stress,
    loan_ratio
):

    if pd_value > 0.75:
        return "REJECT"

    if stress > 8:
        return "REJECT"

    if loan_ratio > 15:
        return "REJECT"

    if pd_value > 0.50:
        return "MANUAL REVIEW"

    return "APPROVED"