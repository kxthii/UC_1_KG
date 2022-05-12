import logging
import json
import azure.functions as func
from azure.data.tables import TableServiceClient

#connection_string = "DefaultEndpointsProtocol=https;AccountName=kaffeemaschinefunktbd2a;AccountKey=FGmpEI0eI/zNNwIPjaHuVR84MH6kJGK/wIKHQ0Az1g9RWOWZn9Srd8ATAdJrmFKzjH94S0nztUCPKBLGgtS9kA==;EndpointSuffix=core.windows.net"
#service = TableServiceClient.from_connection_string(conn_str=connection_string)

def main(msg: func.ServiceBusMessage):
    
    #logging.info('Python ServiceBus queue trigger processed message: %s',msg.get_body().decode('utf-8'))
    #logging.info(json.dumps(msg.metadata))
    data = msg.get_body().decode('utf-8')
    bestellung = json.loads(data)
    sorte = bestellung["KaffeeSorte"]
    menge = bestellung["KaffeeMenge"]
    logging.info("Die Bestellung ist: "+sorte)
    logging.info("Die Menge ist: "+menge)
    

    #logging.info('Python ServiceBus queue trigger processed message: %s',
    #             msg.get_body().decode('utf-8'))
    #registry_manager = IoTHubModuleClient("HostName=iot3bhwii22-kg.azure-devices.net;DeviceId=Kaffeemaschine;SharedAccessKey=h9KYI+TPyjV5ovjiflBOSSuQ0GQZGg+g4MPdN87NWts=")
    
    
    #table_client = TableClient.from_connection_string(connection_string, table_name)
    #table_service_client = TableServiceClient.from_connection_string(conn_str=connection_string)
    #table_client = table_service_client.create_table(table_name=table_name)
    
    #entity = table_client.create_entity(entity=my_entity)

   


