def samitleri_al(text):
    samitler = set()
    for herf in text:
        if herf.isalpha() and herf.lower() not in {'a','ı','o','u','e','ə', 'i', 'ö','ü' }:
            samitler.add(herf.lower())
    return samitler
