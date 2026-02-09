from simpleai.search import SearchProblem, breadth_first


class WaterJug(SearchProblem):

    def __init__(self, jug1, jug2, target):
        self.jug1 = jug1
        self.jug2 = jug2
        self.target = target
        super().__init__(initial_state=(0, 0))

    def actions(self, state):
        x, y = state
        actions = []

        if x < self.jug1:
            actions.append("fill_x")
        if y < self.jug2:
            actions.append("fill_y")
        if x > 0:
            actions.append("empty_x")
        if y > 0:
            actions.append("empty_y")
        if x > 0 and y < self.jug2:
            actions.append("pour_x_y")
        if y > 0 and x < self.jug1:
            actions.append("pour_y_x")

        return actions

    def result(self, state, action):
        x, y = state

        if action == "fill_x":
            return (self.jug1, y)
        if action == "fill_y":
            return (x, self.jug2)
        if action == "empty_x":
            return (0, y)
        if action == "empty_y":
            return (x, 0)
        if action == "pour_x_y":
            t = min(x, self.jug2 - y)
            return (x - t, y + t)
        if action == "pour_y_x":
            t = min(y, self.jug1 - x)
            return (x + t, y - t)

    def is_goal(self, state):
        return state[0] == self.target or state[1] == self.target


jug1 = int(input("Enter Jug 1 size: "))
jug2 = int(input("Enter Jug 2 size: "))
target = int(input("Enter Target amount: "))

problem = WaterJug(jug1, jug2, target)
result = breadth_first(problem)

print("\nSteps:\n")
for step in result.path():
    print(step)
