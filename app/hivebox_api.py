import requests
import logging

logger = logging.getLogger(__name__)


senseBox_api_base_url = "https://api.opensensemap.org/boxes/"
senseBox_ids = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c",
]


def get_senseBox_data(box_id):
    url = f"{senseBox_api_base_url}{box_id}"
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f"Successfully fetched data for box ID: {box_id}")
        return response.json()
    else:
        logging.info(
            f"Failed to fetch data for box ID: {box_id}. Status code: {response.status_code}"
        )
        return None


def get_senseBox_temp(box_id):
    senseBox_data = get_senseBox_data(box_id)
    if senseBox_data:
        all_sensor_data = senseBox_data.get("sensors")
        for sensor_data in all_sensor_data:
            if sensor_data.get("title") == "Temperatur":
                logging.info(
                    f"Successfully fetched temperature for box ID: {box_id} with temperature: {sensor_data.get('lastMeasurement').get('value')}"
                )
                return float(sensor_data.get("lastMeasurement").get("value"))
    logging.info(f"Failed to fetch temperature for box ID: {box_id}")
    return None


def get_avg_senseBox_temp():
    logging.info("Fetching data for all senseBox IDs:")
    senseBox_temp = []
    for senseBox_id in senseBox_ids:
        senseBox_temp.append(get_senseBox_temp(senseBox_id))
    logging.info(f"Found total of {len(senseBox_temp)} sensebox temp points")
    if len(senseBox_temp) > 0:
        return sum(senseBox_temp) / len(senseBox_temp)
    logging.info("Failed to fetch temperature for any senseBox")
    return None
