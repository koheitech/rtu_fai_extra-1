from itertools import combinations
import copy

"""Problem description

Create a state space graph for the problem given below:
-----------------------------------------------------------
Three travellers (let's call them A, B and C) met at night at a narrow bridge (let's call the meeting point P1). 
They all have to cross the bridge and get to the other side (let's call it P2).
Nothing can be seen around. At the bridge, the travellers have access to one torch which, once lit, burns for 12 minutes. 
It must be used when crossing the bridge. 
Each of the travellers is able to cross the bridge in a certain time: A - 1 minute, B - 3 minutes, C - 5 minutes. 
Thus, for all travellers to cross safely from P1 to P2, the following conditions must be met:
- The bridge can only be crossed from P1 to P2 by two travellers carrying the torch
- The bridge is crossed alone in the opposite direction from P2 to P1, carrying the torch
- When two travellers cross the bridge, the time of the slowest traveller is taken as the time of crossing the bridge
- The torch burning time decreases according to the bridge crossing time
- If the torch burning time is less than the bridge crossing time, the bridge may not be crosse
-----------------------------------------------------------
"""

INITIAL_STATE = {
    "P1": ["A", "B", "C"],
    "P2": [],
    "torch": "P1",
    "elapsed_time": 0
}

DURATION = {"A": 1, "B": 3, "C": 5}
TORCH_TIME = 12

def solve_bridge_and_torch(state):
    """
    Solve the bridge and torch problem with recursive approach
    """

    if not is_valid(state):
        return
    
    print_state(state)
    
    possible_moves = get_possible_moves(state)
    
    for move in possible_moves:
        # `new_state` has to be deepcopy so that intermediate state can be preseved for each stack call
        new_state = copy.deepcopy(state)
        move_bridge(new_state, move)
        solve_bridge_and_torch(new_state)

def is_completed(state):
    """
    Check if the move of the traverllers is completed
    """
    return all(traveler in state["P2"] for traveler in ["A", "B", "C"]) and state["torch"] == "P2" and state["elapsed_time"] <= TORCH_TIME

def is_valid(state):
    """
    Check the validity of the movement of traveller/travellers
    In the given problem, the move differs depending on whether the torch is at P1 or P2.
    If the torch is at P2, only one traveller is moving. Thus, it calculates the duration for each of the possbile travellers
    If the torch is at P1, a pair of travellers are moveing. Thus, it calculates the slowest duration out of 2 travellers using `max`
    """
    if is_completed(state):
        return True

    possible_moves = get_possible_moves(state)
    
    if not possible_moves:
        return False
    
    if state["torch"] == "P2":    
        for move in possible_moves:
            if DURATION[move] > (TORCH_TIME - state["elapsed_time"]):
                return False 
        return True
    else:
        for pair_move in possible_moves:
            if max(DURATION[pair_move[0]], DURATION[pair_move[1]]) > (TORCH_TIME - state["elapsed_time"]):
                return False
    return True


def get_possible_moves(state):
    """
    Get all possible moves from the current state
    In the given problem, the move differs depending on whether the torch is at P1 or P2.
    If the torch is at P2:
        Only one traveller is moving. 
        Thus, it returns list of possible travellers
    If the torch is at P1: 
        A pair of travellers are moveing. 
        Thus, it returns list of set of 2 travellers using `combinations` method
    """
    if state["torch"] == "P2":
        return state["P2"]
    
    return list(combinations(state["P1"], 2)) # pair of 2 travellers
    
    
def move_bridge(state, travellers):
    """
    Move specified travellers from one side of the bridge to the other
    """
    
    dept = state["torch"]
    dest = "P2" if dept == "P1" else "P1"

    if dept == "P2":
        state[dept].remove(travellers)
        state[dest].append(travellers)
        state["elapsed_time"] += DURATION[travellers]
        state["torch"] = dest
    else:
        for traveller in travellers:
            state[dept].remove(traveller)
            state[dest].append(traveller)
        state["elapsed_time"] += max(DURATION[travellers[0]], DURATION[travellers[1]])
        state["torch"] = dest
    
def print_state(state):
    """
    Print the current state
    """
    if state["torch"] == "P1":
        print("|-----------------------------------------------------")
        print(f"|P1: {state['P1']}, Torch: {TORCH_TIME - state['elapsed_time']} min left")
        print("|-------------------------bridge----------------------")
        print(f"|P2: {state['P2']}")
        print("|-----------------------------------------------------\n\n")
    else:
        print("|-----------------------------------------------------")
        print(f"|P1: {state['P1']}")
        print("|-------------------------bridge----------------------")
        print(f"|P2: {state['P2']}, Torch: {TORCH_TIME - state['elapsed_time']} min left")
        print("|-----------------------------------------------------\n\n")

solve_bridge_and_torch(INITIAL_STATE)