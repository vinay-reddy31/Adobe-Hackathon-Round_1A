from collections import Counter

def find_common_font_sizes(font_data):
    """
    Returns the most common font sizes sorted in descending order.
    """
    sizes = [round(span['size'], 1) for span in font_data]
    return sorted(list(set(sizes)), reverse=True)

def classify_heading(size, font_hierarchy):
    """
    Classifies a font size into H1, H2, H3 based on hierarchy.
    """
    if size == font_hierarchy[0]:
        return "H1"
    elif len(font_hierarchy) > 1 and size == font_hierarchy[1]:
        return "H2"
    elif len(font_hierarchy) > 2 and size == font_hierarchy[2]:
        return "H3"
