class State():
    def __init__(self):
        self.game = None
        self.previous_state = None

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.previous_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()