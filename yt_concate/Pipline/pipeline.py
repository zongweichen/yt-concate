from .steps.step import StepException


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self, Input, utils):
        data = None
        for step in self.steps:
            try:
                 data = step.process(data, Input, utils)
            except StepException:
                print(Exception, "happened in steps")
                break
