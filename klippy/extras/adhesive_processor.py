class AdhesiveParser:
    def __init__(self, config):
        self.printer = config.get_printer()
        # Read config
        # Note: 'minval' is >=, whereas 'above' is >
        self.buffer_distance = config.getfloat('buffer_distance', 5, minval=0.)
        self.spray_diameter = config.getfloat('spray_diameter', 10, minval=0.)
        self.travel_speed = config.getint('travel_speed', 7000, above=0.)
        self.extrude_speed = config.getint('extrude_speed', 7000, above=0.)
        self.extrude_distance = config.getint('extrude_distance', 50000, above=0.)

        # Register macros
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command(
            'RUN_ADHESIVE', self.cmd_RUN_ADHESIVE, desc=self.cmd_RUN_ADHESIVE_help
        )

    
    # TODO
    def cmd_GET_PARSER_PARAMETERS(self, gcmd):
        pass

    cmd_RUN_ADHESIVE_help = "Run adhesive processor"
    def cmd_RUN_ADHESIVE(self, gcmd):
        pass

def load_config(config):
    return AdhesiveParser(config)
