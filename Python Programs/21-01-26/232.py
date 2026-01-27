def n_largest_items(dataset, n):
    if n <= 0:
        return []
    
    sorted_dataset = sorted(dataset, reverse=True)
    return sorted_dataset[:n]
