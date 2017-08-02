
import sys
import json
import platform
import subprocess
import requests

from splunk.clilib.bundle_paths import make_splunkhome_path

sys.path.append(make_splunkhome_path(['etc', 'apps', 'SA-ITOA', 'lib']))

from ITOA.fix_appserver_import import FixAppserverImports
from ITOA.setup_logging import setup_logging
from itsi.event_management.sdk.eventing import Event
from itsi.event_management.sdk.custom_event_action_base import CustomEventActionBase

class Email(CustomEventActionBase):
    def execute(self):
     
        self.logger.debug('Received settings from splunkd=`%s`',json.dumps(self.settings))
        self.logger.info('Executed action. Processed events count=`%s`.', count)
  
if __name__ == "__main__":
    logger = setup_logging("itsi_event_management.log", "itsi.event_action.trelloboard")
    logger.info("Starting Board Post ")
    if len(sys.argv) > 1 and sys.argv[1] == '--execute':
	input_params = sys.stdin.read()
        logger.info(input_params)
        payload = json.loads(input_params)
        logger.info(payload)
        event_id = payload['result']['event_id']
        session_key = payload['session_key']
	myboard="4978c0fb1d5db6908f3e618e" 
        urlstring = "https://api.trello.com/1/lists/"+myboard+"/cards"
        logger.info("Session Key:"+session_key+" event id:"+event_id)
	title=payload['result']['title']
	description=payload['result']['description']
	mykey = 'f1b83a540065a0aa7d4e1b2c0199c3e8'
        mytoken='14ac1c8ac6950f0d666cf8f6db7c59ffb92c49412f55cf6942f5368d7ab05936'
        payload = {'descData':'MyDescData','dueComplete':'true','due':'2017-04-07T21:26:00.365Z','name':title,'desc':description,'key':mykey,'token':mytoken}
	r = requests.post(urlstring, data=payload)
	event = Event(session_key, logger)
        event.create_comment(event_id, "Trello Message has been created")

