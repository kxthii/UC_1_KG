import json
import azure.functions as func
import azure.iot.hub as IotHubRegistryManager
from azure.iot.device import IoTHubModuleClient
from random import randint
from KaffeeMaschineMesswerte import KaffeeMaschine

KaffeeSorte = ["Espresso", "Café double", "Verlängerter", "Café crème", "Cappuccino", "Café frappé", "Caffè latte", "Latte macchiato" , "Café au Kirsch", "Almkaffee", "Eiskaffee"]
KaffeeMenge = ["120ml", "200ml", "250ml", "300ml", "500ml"]
 

def main ():
   
    regestry_manager = "HostName=iot3bhwii22-kg.azure-devices.net;DeviceId=Kaffeemaschine;SharedAccessKey=h9KYI+TPyjV5ovjiflBOSSuQ0GQZGg+g4MPdN87NWts="
    
    client = IoTHubModuleClient.create_from_connection_string(regestry_manager)
    client.connect()
    KaffeeMaschinen = KaffeeMaschine(KaffeeSorte[randint(0,10)],KaffeeMenge[randint(0,4)])
    KaffeeDatenJson = json.dumps(KaffeeMaschinen.__dict__)
    
    client.send_message(KaffeeDatenJson) 

    client.disconnect()
    client.shutdown()
    print("successfully sent")
main()