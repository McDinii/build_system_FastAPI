import yaml
from collections import deque


def load_data():
    """
    Function to load tasks and builds data from yaml files.
    """
    try:
        with open("builds/tasks.yaml") as task_file:
            # If 'dependencies' key is missing, an empty list will be returned
            tasks = {task_data['name']: task_data.get(
                'dependencies', []) for task_data in yaml.safe_load(task_file)['tasks']}
    except (FileNotFoundError, yaml.YAMLError) as e:
        raise e

    try:
        with open("builds/builds.yaml") as build_file:
            builds = {build_data['name']: build_data.get(
                'tasks', []) for build_data in yaml.safe_load(build_file)['builds']}
    except (FileNotFoundError, yaml.YAMLError) as e:
        raise e

    return tasks, builds


def topo_sort(build_name: str, tasks: dict, builds: dict):
    """
    Function to get the topological sorting of tasks.

    Parameters
    ----------
    build_name : str
        Name of the build
    tasks : dict
        Dictionary of tasks mapping from task name to its dependencies
    builds : dict
        Dictionary of builds mapping from build name to its tasks

    Returns
    -------
    List of tasks in topological order.
    """
    if build_name not in builds:
        raise KeyError

    build_tasks = set(builds[build_name])

    for task in list(build_tasks):
        try:
            build_tasks.update(tasks[task])
        except KeyError:
            raise KeyError

    sorted_tasks = deque()
    queue = deque()
    indegree = {task: 0 for task in build_tasks}

    for task in build_tasks:
        for dependency in tasks.get(task, []):
            indegree[dependency] = indegree.get(dependency, 0) + 1

    for task, in_degree in indegree.items():
        if in_degree == 0:
            queue.append(task)

    while queue:
        task = queue.popleft()
        sorted_tasks.appendleft(task)
        for dependency in tasks.get(task, []):
            indegree[dependency] -= 1
            if indegree[dependency] == 0:
                queue.append(dependency)

    if len(sorted_tasks) != len(indegree):
        raise ValueError("Circular dependency detected!")

    return list(sorted_tasks)