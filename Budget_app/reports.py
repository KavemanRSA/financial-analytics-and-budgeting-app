"""Text-based financial reporting functions."""


def create_spend_chart(categories):
    """Return a text chart showing each category's share of total spending."""
    title = "Percentage spent by category"
    spent_by_category = [
        sum(-record["amount"] for record in category.ledger if record["amount"] < 0)
        for category in categories
    ]
    total_spent = sum(spent_by_category)

    percentages = [
        int((spent / total_spent * 100) // 10 * 10) if total_spent else 0
        for spent in spent_by_category
    ]

    y_axis = []
    for level in range(100, -1, -10):
        row = f"{level:>3}| "
        row += "".join("o  " if percent >= level else "   " for percent in percentages)
        y_axis.append(row)

    horizontal_line = "    " + "-" * (len(categories) * 3 + 1)

    names = [category.name for category in categories]
    x_axis = []
    for letter_index in range(max((len(name) for name in names), default=0)):
        row = ""
        for name_index, name in enumerate(names):
            row += (name[letter_index] if letter_index < len(name) else " ") + "  "
        x_axis.append(row.rstrip())

    y_axis_text = "\n".join(y_axis)
    x_axis_text = "     " + "\n     ".join(x_axis)
    return f"{title}\n{y_axis_text}\n{horizontal_line}\n{x_axis_text}"
