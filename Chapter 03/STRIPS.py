#Experiment 13: STRIPS in Classical AI
#Description: STRIPS (Stanford Research Institute Problem Solver) is an AI planning technique used to achieve a
#goal by performing a sequence of actions. It uses preconditions, delete lists, and add lists to modify the current state.
# Blocks World Problem using STRIPS

state = {
    "ON(B,TABLE)",
    "ON(A,TABLE)",
    "ON(C,A)",
    "HAND_EMPTY",
    "CLEAR(C)",
    "CLEAR(B)"
}

def move_C_to_table():
    if "ON(C,A)" in state and "CLEAR(C)" in state:
        state.remove("ON(C,A)")
        state.add("ON(C,TABLE)")
        state.add("CLEAR(A)")
        print("Action: Move C to Table")

def move_B_on_C():
    if "ON(B,TABLE)" in state and "CLEAR(B)" in state \
       and "CLEAR(C)" in state and "HAND_EMPTY" in state:

        state.remove("ON(B,TABLE)")
        state.remove("CLEAR(C)")

        state.add("ON(B,C)")
        state.add("CLEAR(B)")
        print("Action: Move B on C")

def move_A_on_B():
    if "ON(A,TABLE)" in state and "CLEAR(A)" in state \
       and "CLEAR(B)" in state and "HAND_EMPTY" in state:

        state.remove("ON(A,TABLE)")
        state.remove("CLEAR(B)")

        state.add("ON(A,B)")
        state.add("CLEAR(A)")
        print("Action: Move A on B")

print("Initial State:", state)

move_C_to_table()
move_B_on_C()
move_A_on_B()

goal = {
    "ON(C,TABLE)",
    "ON(B,C)",
    "ON(A,B)",
    "HAND_EMPTY",
    "CLEAR(A)"
}

print("\nFinal State:", state)
print("Goal Achieved:", goal.issubset(state))