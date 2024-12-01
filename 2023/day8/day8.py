from cProfile import Profile
from pstats import SortKey, Stats

def main() -> None:
    total_steps = 0
    instructions = list()
    
    node_graph = dict()
    
    with open('input.txt') as f:
        instructions = f.readline().rstrip()
        f.readline()  # white line
        
        for line in f:
            node = line.rstrip().split(" ")[0]
            left = line.rstrip().split(" ")[2][1:-1]
            right = line.rstrip().split(" ")[3][:-1]
            node_graph[node] = (left, right, node.endswith("Z"))

    print(f"Instructions {instructions}")
    print(f"Node Graph {node_graph}")
    
    all_paths_current_node = [each_node for each_node in node_graph.keys() if each_node.endswith("A")]
    how_many_paths = len(all_paths_current_node)
    instructions_len = len(instructions)
    # with Profile() as profile:
    i = 0
    while i < instructions_len:
        total_steps += 1
        # all_paths_next_node = list()
        all_paths_next_node = [None] * how_many_paths
        
        all_nodes_are_final_nodes = True
        for path_i, each_current_node in enumerate(all_paths_current_node):
            next_node = node_graph[each_current_node][0 if instructions[i] == "L" else 1]
            
            if node_graph[next_node][2] is False:
                all_nodes_are_final_nodes = False

            # all_paths_next_node.append(next_node)
            all_paths_next_node[path_i] = next_node
        
        if all_nodes_are_final_nodes is True:
            break
        # if False not in [node_graph[each_node][2] for each_node in all_paths_next_node]:
        #     break

        all_paths_current_node = all_paths_next_node
        
        # back to the beginning
        if i == instructions_len - 1:
            i = -1
        i += 1
        if total_steps % 1000000 == 0:
            # break
            print(total_steps)
        # (
        #     Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()
        # )
    
    print(f"Total steps: {total_steps}")
            

if __name__ == "__main__":
    main()
    