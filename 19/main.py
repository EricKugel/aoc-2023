from aoc_meta import *
aoc_init(2023, 19)

def generate_workflow(steps):
    def workflow(parts, step_i):
        step = steps[step_i]
        if ":" in step:
            condition, value = step.split(":")
            operand, operator, *num = condition
            num = int("".join(num))
            valid = []
            invalid = []
            for part in parts:
                application = part[operand]
                new_part = part.copy()
                new_part[operand] = (num + 1, application[1]) if operator == ">" else (application[0], num)
                valid.append(new_part)
                new_part = part.copy()
                new_part[operand] = (application[0], num + 1) if operator == ">" else (num, application[1])
                invalid.append(new_part)
            return workflows[value](valid.copy(), 0) + workflow(invalid.copy(), step_i + 1)
        else:
            return workflows[step](parts.copy(), 0)
    return workflow

workflows_data, parts_data = [section.split("\n") for section in get_input().split("\n\n")]

workflows = {"A": lambda part, step_i : part, "R": lambda part, step_i : []}
for workflow_string in workflows_data:
    name = workflow_string[0:workflow_string.index("{")]
    workflow_data = workflow_string[workflow_string.index("{") + 1:workflow_string.index("}")]
    steps = workflow_data.split(",")
    workflows[name] = generate_workflow(steps)

parts = [{"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}]
parts = workflows["in"](parts.copy(), 0)

total = 0
for part in parts:
    sub_total = 1
    for start, end in part.values():
        sub_total *= (end - start)
    total += sub_total

p2(total)