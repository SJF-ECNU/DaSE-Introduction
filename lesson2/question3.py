def DFS_find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:
            new_paths = DFS_find_all_paths(graph, neighbor, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


if __name__ == "__main__":
    my_graph = {
        "人-羊-狼-菜": {"狼-菜"},
        "狼-菜": {"人-狼-菜"},
        "人-狼-菜": {"狼", "菜"},
        "狼": {"人-羊-狼"},
        "菜": {"人-羊-菜"},
        "人-羊-狼": { "羊"},
        "人-羊-菜": {"羊"},
        "羊": {"人-羊"},
        "人-羊": {"成功"}
    }

    start_address = "人-羊-狼-菜"
    end_address = "成功"
    all_paths = DFS_find_all_paths(my_graph, start_address, end_address)
    for path in all_paths:
        print("->".join(path))
