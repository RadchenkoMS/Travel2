from trains.models import Train


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_town_id, set())
        graph[q.from_town_id].add(q.to_town_id)
    return graph


def route_finder(request, form) -> dict:
    context = {'form': form}
    qs = Train.objects.all().select_related('from_town', 'to_town')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_town = data['from_town']
    to_town = data['to_town']
    towns = data['towns']
    travel_time = data['travel_time']
    all_paths = list(dfs_path(graph, from_town.id, to_town.id))
    if len(all_paths) == 0:
        a = 1
        raise ValueError("Маршруту не існує")
    if towns:
        _cities = [city.id for city in towns]
        right_path = []
        for path in all_paths:
            if all(city in path for city in _cities):
                right_path.append(path)
        if not right_path:
            raise ValueError("Маршруту не існує помилка з містами")
    else:
        right_path = all_paths
    trains = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_town_id, q.to_town_id), [])
        all_trains[(q.from_town_id, q.to_town_id)].append(q)
    for path in right_path:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(path) - 1):
            qs = all_trains[(path[i], path[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if travel_time >= total_time:
            trains.append(tmp)
    if not trains:
        raise ValueError('Немає маршруту за заданим часом')
    sorted_trains = []
    if len(trains) == 1:
        sorted_trains = trains
    else:
        time = list(set(train['total_time'] for train in trains))
        time = sorted(time)
        for t in time:
            for train in trains:
                if t == train['total_time']:
                    sorted_trains.append(train)
    context['trains'] = sorted_trains
    context['cities'] = {'from_town': from_town, 'to_town': to_town}
    return context
