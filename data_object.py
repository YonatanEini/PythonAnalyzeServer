import json


class DataAnalyzedObjectDto:
    def __init__(self, current_velocity, current_wind_speed, current_height, light_eng, light_ready, light_copilot,
                 time, date):
        self.current_velocity = current_velocity
        self.current_wind_speed = current_wind_speed
        self.current_height = current_height
        self.light_eng = light_eng
        self.light_ready = light_ready
        self.light_Copilot = light_copilot
        self.time = time
        self.date = date

    def to_Json(self):
        data_analyzed = DataAnalyzedObjectDto(int(self.current_velocity), int(self.current_wind_speed),
                                              int(self.current_height), int(self.light_eng), int(self.light_ready),
                                              int(self.light_Copilot),
                                              self.time, self.date)
        return json.dumps(data_analyzed, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def update_properties(self, current_wind_speed, current_height, current_velocity, light_eng, light_ready,
                          light_copilot, current_time, current_date):
        self.current_velocity = current_velocity
        self.current_height = current_height
        self.current_wind_speed = current_wind_speed
        self.light_eng = light_eng
        self.light_ready = light_ready
        self.light_Copilot = light_copilot
        self.time = current_time
        self.date = current_date
