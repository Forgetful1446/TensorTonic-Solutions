def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    
    # Tổng số mẫu
    ref_total = sum(reference_counts)
    prod_total = sum(production_counts)
    
    # Chuẩn hóa thành xác suất
    ref_dist = [x / ref_total for x in reference_counts]
    prod_dist = [x / prod_total for x in production_counts]
    
    # Tính Total Variation Distance
    tvd = 0.5 * sum(abs(p - q) for p, q in zip(ref_dist, prod_dist))
    
    # Kiểm tra drift
    return {
        "score": tvd,
        "drift_detected": tvd > threshold
    }