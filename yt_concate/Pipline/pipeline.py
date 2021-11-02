from .steps.step import StepException


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self, Input):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, Input)
            except StepException:
                print(Exception, "happened in steps")
                break
