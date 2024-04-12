from aoc_meta import *
aoc_init(2023, 20)

data = get_input().split("\n")
# data = get_test_input().split("\n")

import math

class Pulse:
    low = 0
    high = 0
    queue = []
    def __init__(self, value, output):
        self.value = value
        self.output = output
        if self.value == True:
            Pulse.high += len(self.output)
        elif self.value == False:
            Pulse.low += len(self.output)
    def fulfill(self):
        for module in self.output:
            pulse = module.recieve(self)
            if pulse:
                Pulse.queue.append(pulse)
    def __repr__(self):
        return f"{self.value} -> {self.output}"
    @classmethod
    def get_pulses(self):
        return Pulse.low * Pulse.high

class Module:
    def __init__(self, name):
        self.name = name
    def set_output(self, output):
        self.output = output
    def __repr__(self):
        return f"{self.name}: {self.value}"
    @classmethod
    def module_factory(self, module_info):
        module_string, output_string = module_info.split(" -> ")
        module_type = ""
        if module_string == "broadcaster":
            module_type = "Broadcaster"
        elif module_string.startswith("%"):
            module_type = "FlipFlop"
        elif module_string.startswith("&"):
            module_type = "Conjunction"

        module = None
        match module_type:
            case "Broadcaster":
                module = Broadcast(module_string)
            case "FlipFlop":
                name = module_string[1:]
                module = FlipFlop(name)
            case "Conjunction":
                name = module_string[1:]
                module = Conjunction(name)

        output = output_string.split(", ")
        module.set_output(output)

        return module
    @classmethod
    def map_outputs(self):
        modules_to_add = {}
        for name, module in modules.items():
            new_output = []
            for output in module.output:
                if output not in modules.keys():
                    new_module = None
                    if not output in modules_to_add.keys():
                        new_module = Untyped(output)
                        modules_to_add[output] = new_module
                    else:
                        new_module = modules_to_add[output]
                    new_output.append(new_module)
                else:
                    new_output.append(modules[output])
                    if isinstance(modules[output], Conjunction):
                        modules[output].add_input(module)
            module.output = new_output
        for name, module in modules_to_add.items():
            modules[name] = module
            
    
class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)
        self.value = False
    def recieve(self, parent):
        if not parent.value:
            self.value = not self.value
            return Pulse(self.value, self.output)
    
class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.value = False
        self.input = []
        self.high_recieved = False
    def recieve(self, _):
        self.value = any([not parent.value for parent in self.input])
        if self.value == True:
            self.high_recieved = True
        return Pulse(self.value, self.output)
    def add_input(self, module):
        self.input.append(module)

class Broadcast(Module):
    def __init__(self, name):
        super().__init__(name)
        self.value = False
    def recieve(self, parent):
        self.value = parent.value
        return Pulse(self.value, self.output)

class Button(Module):
    def __init__(self, name):
        super().__init__(name)
        self.value = False
    def push(self):
        output = [broadcaster]
        initial_pulse = Pulse(self.value, output)
        initial_pulse.fulfill()
        while len(Pulse.queue) > 0:
            pulse = Pulse.queue.pop(0)
            pulse.fulfill()
    
class Untyped(Module):
    def __init__(self, name):
        super().__init__(name)
        self.value = False
        self.low_recieved = False
    def recieve(self, parent):
        self.value = parent.value
        if self.value == False:
            self.low_recieved = True
        # print(f"Module {self.name} has value {self.value}")


cycles = [0, 0, 0, 0]

for i in range(4):
    broadcaster = None
    button = None
    modules = {}
    for line in data:
        module = Module.module_factory(line)
        if isinstance(module, Broadcast):
            broadcaster = module
        name = module.name
        modules[name] = module
    Module.map_outputs()

    button = Button("button")

    relevant_modules = []
    nand_module = None
    for name, module in modules.items():
        if modules["rx"] in module.output:
            nand_module = module
            break
    for name, module in modules.items():
        if not isinstance(module, Untyped) and nand_module in module.output:
            relevant_modules.append(module)

    module = relevant_modules[i]
    button_pushes = 0
    while not module.high_recieved:
        button.push()
        button_pushes += 1
    cycles[i] = button_pushes

answer = math.lcm(*cycles)
p2(answer)