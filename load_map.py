"""
    Loads the map of the given level.
"""
from csv import reader


levels = {
    "1": {
        "walls": ""
    }
}


def load_map(path, level):
    """
    :param path: Must be the path of the folder, not the level itself.
    :param level: The level whose map you want to load.
    :return: IDK inca
    """
    level_folder = "".join(["Level ", str(level)])
    blocks = ["dots", "pacman spawn", "walls"]
    for block in blocks:
        csv_file_path = "".join([str(path), "/", level_folder, "/", level_folder, "_", str(block), ".csv"])
        block_layout = import_csv_layout(csv_file_path)


def import_csv_layout(file):
    terrain_map = []
    try:
        with open(file) as t_map:
            level_map = reader(t_map, delimiter=",")
            for row in level_map:
                terrain_map.append(list(row))
            return terrain_map
    except FileNotFoundError:
        pass



load_map("Levels", 1)
