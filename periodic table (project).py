


elements_data = [
    {"atomic_number": 1,   "symbol": "H",  "name": "Hydrogen",     "atomic_mass": 1.008},
    {"atomic_number": 2,   "symbol": "He", "name": "Helium",       "atomic_mass": 4.0026},
    {"atomic_number": 3,   "symbol": "Li", "name": "Lithium",      "atomic_mass": 6.94},
    {"atomic_number": 4,   "symbol": "Be", "name": "Beryllium",    "atomic_mass": 9.0122},
    {"atomic_number": 5,   "symbol": "B",  "name": "Boron",        "atomic_mass": 10.81},
    {"atomic_number": 6,   "symbol": "C",  "name": "Carbon",       "atomic_mass": 12.011},
    {"atomic_number": 7,   "symbol": "N",  "name": "Nitrogen",     "atomic_mass": 14.007},
    {"atomic_number": 8,   "symbol": "O",  "name": "Oxygen",       "atomic_mass": 15.999},
    {"atomic_number": 9,   "symbol": "F",  "name": "Fluorine",     "atomic_mass": 18.998},
    {"atomic_number": 10,  "symbol": "Ne", "name": "Neon",         "atomic_mass": 20.18},
    # ... [Continue filling through atomic_number 118]
    {"atomic_number": 118, "symbol": "Og", "name": "Oganesson",    "atomic_mass": 294},
]

def find_by_atomic_number(number: int):
    """Return the element dict for the given atomic number."""
    return next((e for e in elements_data if e["atomic_number"] == number), None)

def find_by_symbol(symbol: str):
    """Return the element dict matching the symbol (case-insensitive)."""
    return next((e for e in elements_data if e["symbol"].lower() == symbol.lower()), None)

def find_by_name(name: str):
    """Return the element dict matching the name (case-insensitive)."""
    return next((e for e in elements_data if e["name"].lower() == name.lower()), None)

def compare_elements(el1: dict, el2: dict, keys=None):
    """
    Compare two element dicts and return a dict mapping each key to a tuple of values.
    Bydefault, Bydefault compares atomic number, symbol, name, and atomic mass.
    """
    if keys is None:
        keys = ["atomic_number", "symbol", "name", "atomic_mass"]
    return {key: (el1.get(key), el2.get(key)) for key in keys}

def list_all_elements():
    """Return the full list of element dictionaries."""
    return elements_data.copy()
