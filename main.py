from itertools import product


def reflex_vacuum_agent(configuration, size, position, iterations):
    """
    simple reflex agent to 

    :param configuration: current configuration area
    :param size: current working size area
    :param position: current vaccum position
    :param iterations: iterations count
    :return: current performance report
    """
    agent_performance = 0
    for _ in range(iterations):
        if configuration[position] == 0: # CLEAN FLOOR
            if position + 1 == size: # LEFT POSITION
                position -= 1
            elif position == 0: # RIGHT POSITION
                position += 1
        elif configuration[position] == 1: # DIRTY FLOOR
            configuration[position] = 0
            
        agent_performance += size - sum(configuration) # calculate performance report

    return agent_performance

def get_each_performance(iterations, size):
    """
    get simple performance report for all size and iterations 

    :param size: current working size area
    :param iterations: iterations count
    :return: performance report for all
    """
    performances = []
    for position in range(size):
        for configuration in list(product([0, 1], repeat=size)):
            agent_performance = reflex_vacuum_agent(list(configuration), size, position, iterations)
            performances.append(agent_performance)
            print("Position: " + str(position) + ", Area Config: " + str(configuration) + ", Performance: " + str(agent_performance))
    print("Average: " + str(sum(performances)/len(performances)))


if __name__ == "__main__":
    # change iterations and size right here for the arguments
    get_each_performance(100, 2)
