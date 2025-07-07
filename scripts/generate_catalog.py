import csv
import random

materials = ["Steel", "Stainless Steel", "Brass", "Aluminum", "PVC", "Nylon"]
finishes = ["Zinc-Plated", "Black Oxide", "Unfinished", "Nickel-Plated"]
sizes = ["1/4\"", "3/8\"", "1/2\"", "5/8\"", "3/4\"", "1\""]
thread_types = ["UNC", "UNF", "Metric"]
tubing_ids = ["1/4\"", "3/8\"", "1/2\"", "3/4\"", "1\""]
angles = ["90°", "45°", "Straight"]
head_styles = ["Flat", "Pan", "Round", "Hex"]

def make_parts():
    parts = []
    part_number = 1000

    def add_part(name, desc, category):
        nonlocal part_number
        parts.append({
            "part_number": part_number,
            "name": name,
            "description": desc,
            "category": category
        })
        part_number += 1

    for _ in range(200):
        size = random.choice(sizes)
        mat = random.choice(materials)
        thread = random.choice(thread_types)
        finish = random.choice(finishes)
        add_part(
            "Hex Bolt",
            f"{mat} hex bolt {size}, {thread} thread, {finish} finish",
            "Bolts"
        )

    for _ in range(200):
        size = random.choice(sizes)
        mat = random.choice(materials)
        type_ = random.choice(["Flat", "Split Lock", "Tooth"])
        add_part(
            f"{type_} Washer",
            f"{mat} {type_.lower()} washer for {size} bolts",
            "Washers"
        )

    for _ in range(200):
        id_ = random.choice(tubing_ids)
        mat = random.choice(["PVC", "Nylon", "Silicone", "Rubber"])
        pressure = random.randint(60, 300)
        add_part(
            "Flexible Tubing",
            f"{mat} tubing {id_} ID, rated for {pressure} PSI",
            "Tubing"
        )

    for _ in range(200):
        type_ = random.choice(["Elbow", "Tee", "Straight"])
        angle = random.choice(angles)
        mat = random.choice(["Brass", "Stainless Steel", "Plastic"])
        connection = random.choice(["Compression", "Threaded", "Push-to-Connect"])
        add_part(
            f"{type_} Fitting",
            f"{mat} {type_.lower()} fitting ({angle}) with {connection} connections",
            "Fittings"
        )

    for _ in range(200):
        type_ = random.choice(["Rivet", "Clip", "Screw"])
        head = random.choice(head_styles)
        mat = random.choice(materials)
        add_part(
            f"{type_}",
            f"{mat} {type_.lower()} fastener with {head.lower()} head",
            "Fasteners"
        )

    return parts

def save_to_csv(parts, path="data/parts_catalog.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["part_number", "name", "description", "category"])
        writer.writeheader()
        writer.writerows(parts)
    print(f"✅ Saved {len(parts)} parts to {path}")

if __name__ == "__main__":
    parts = make_parts()
    save_to_csv(parts)
