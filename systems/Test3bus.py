from power.models.electricity_models import *

class test3bus(Network):
    def __init__(self):
        super().__init__(id=1, name="Simple 3-Bus System")
        self._create_buses()
        self._create_loads()
        self._create_generators()
        self._create_lines()

    def _create_buses(self):
        # Create buses
        self.buses = [
            Bus(self, id=1, bus_type='Slack', v=1.00, theta=0.0, Sh=1),
            Bus(self, id=2, bus_type='PV', v=1.00, theta=0.0, Sh=0),
            Bus(self, id=3, bus_type='PQ', v=1.00, theta=0.0), 
        ]

    def _create_loads(self):
        # Create loads
        self.loads = [
            Load(id=1, bus=self.buses[2], p_input=1, q_input=0),  # Bus 2
        ]

    def _create_generators(self):
        # Create generators
        self.generators = [
            Generator(id=1, bus=self.buses[0]),  # Slack (bus 1)
            Generator(id=2, bus=self.buses[1], p_input=0.5, q_input=0),  # PV (bus 2)
        ]

    def _create_lines(self):
        # Create lines
        self.lines = [
            Line(id=1, from_bus=self.buses[0], to_bus=self.buses[1], r=0.1, x=0.5, b_half=0),
            Line(id=2, from_bus=self.buses[0], to_bus=self.buses[2], r=0.1, x=0.5, b_half=0),
            Line(id=3, from_bus=self.buses[1], to_bus=self.buses[2], r=0.1, x=0.5, b_half=0),
        ]