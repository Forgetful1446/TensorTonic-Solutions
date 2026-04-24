def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    groups = {}
    order = []

    for record in records:
        key = tuple(record[col] for col in key_columns)

        if key not in groups:
            groups[key] = record
            order.append(key)
        else:
            if strategy == "last":
                groups[key] = record

            elif strategy == "most_complete":
                current_none = sum(v is None for v in groups[key].values())
                new_none = sum(v is None for v in record.values())

                if new_none < current_none:
                    groups[key] = record

    return [groups[key] for key in order]