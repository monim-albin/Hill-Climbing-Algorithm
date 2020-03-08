__author__ = 'AMA'


def delete(queue):
    """
            This function is to delete a node with the lowest value and then return it.
            In this way it mimics the sytle of priority queue
            :param queue: a queue or list
            :return a node with lowest value
    """
        max = 0
        for i in range(len(queue)):
             if queue[i]> queue[min]:
                max = i
        item = queue[max]
        del queue[min]
        return item
   

if __name__ == "__main__":

    queue = []                                                                                
    visited = []                                                                            
    found = False
    queue.append(first_node)
    visited.append(first_node) 

    while len(queue) > 0:                                                                     
        current_node = delete(queue)                      # priority queue
        neighbor_list = neighboring_nodes(current_node)                                  
        for neighbor in neighbor_list:                                                      
            if neighbor not in visited:                                                     
                    if neighbor < current_node:
                        found = True
                que.append(neighbor)
         visited.append(neighbor)
            if found == True:                                                                                           
                return print(current_node)
