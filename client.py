import time
import json
import paho.mqtt.client as mqtt

from models.Sensor import Sensor


MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "inatel/c115/plant_project"

def __create_json_to_send(data):
    return json.dumps(data)


if __name__ == "__main__":
    # Setting mqtt
    mqtt_client = mqtt.Client("FarmerClient")
    mqtt_client.connect(MQTT_BROKER)

    # Creating Sensors
    humidity_sensor = Sensor(name="Humidity", bounds=(0, 1))
    temperature_sensor = Sensor(name="Temperature", bounds=(-10, 85), gauss=True, mean=30, sigma=5)
    ph_sensor = Sensor(name="Humidity", bounds=(0, 14), integer=True)

    # Main loop
    while 42:
        values_data = {
            "humidity_value": humidity_sensor.read_value(),
            "temperature_value": temperature_sensor.read_value(),
            "ph_value": ph_sensor.read_value(),
        }

        json_to_send = __create_json_to_send(values_data)

        # Sending data
        mqtt_client.publish(topic=MQTT_TOPIC, payload=json_to_send)
        print(f"The json {json_to_send} was published")

        time.sleep(1)

