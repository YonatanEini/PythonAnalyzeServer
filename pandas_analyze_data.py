import pandas


class DecodedData:
    def __init__(self, decoded_items, hour, date):
        self.decoded_items = decoded_items
        self.hour = hour
        self.date = date

    def convert_to_frame_data(self):
        data = []
        for element in self.decoded_items:
            data.append(element)
        data_frame = pandas.DataFrame(data)
        return data_frame

    def extract_property_value(self, data_frame, property_name):
        for index in range(len(data_frame)):
            if data_frame.iloc[index]['Name'] == property_name:
                return data_frame.iloc[index]['Value']

    def analyze_data_frame(self, data_object):
        data_frame = self.convert_to_frame_data()
        velocity = self.extract_property_value(data_frame, 'Velocity')
        height = self.extract_property_value(data_frame, 'Height')
        wind_speed = self.extract_property_value(data_frame, 'Wind Speed')
        light_eng = self.extract_property_value(data_frame, 'Light - Eng Cut')
        light_ready = self.extract_property_value(data_frame, 'Light - Ready')
        light_copilot = self.extract_property_value(data_frame, 'Light - Copilot')
        data_object.update_properties(wind_speed, height, velocity, light_eng,
                                      light_ready, light_copilot,
                                      self.hour, self.date)


def main():
    data = DecodedData(
        [{"Name": "Sync", "Value": 195}, {"Name": "Height", "Value": 111}, {"Name": "Wind Speed", "Value": 4},
         {"Name": "Fit Mode", "Value": 1}, {"Name": "Test Result", "Value": 0}, {"Name": "Control", "Value": 0}
            , {"Name": "Comm Fail", "Value": 1}, {"Name": "Busy", "Value": 0}, {"Name": "Stick Alieron", "Value": 160},
         {"Name": "Stick Elevator", "Value": 74}, {"Name": "Stick Rubber", "Value": 222},
         {"Name": "Stick Throttle", "Value": 124}, {"Name": "Select Stick", "Value": 2},
         {"Name": "Engine", "Value": 0}, {"Name": "DNL_Undefined 1", "Value": 0},
         {"Name": "Autopilot", "Value": 1}, {"Name": "Brakes", "Value": 0},
         {"Name": "DNL_Undefined 2", "Value": 0}, {"Name": "Fit/To-id", "Value": 0}, {"Name": "Light On", "Value": 1},
         {"Name": "DNL_Undefined 3", "Value": 1}, {"Name": "Flaps", "Value": 0}, {"Name": "Flaps Selector", "Value": 1},
         {"Name": "Starter", "Value": 0}, {"Name": "DNL_Undefined 4", "Value": 0}, {"Name": "Ldg Gear", "Value": 3},
         {"Name": "Cal Correlator", "Value": 171}, {"Name": "Cal Data", "Value": 63}], "11:23:54")
    # data_analyzed = DataAnalyzedObjectDto(0, 0, 0, 0, [], [], 0)
    # data.analyze_data_frame(data_analyzed)


if __name__ == '__main__':
    main()
