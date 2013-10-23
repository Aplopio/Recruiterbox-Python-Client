import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from recruiterbox_api import recruiterbox_api as recruiterbox

recruiterbox.SITE = "https://app.recruiterbox.com"
recruiterbox.api_key = "******************"
recruiterbox.username = "demoaccount@recruiterbox.com"
recruiterbox.SCHEMA_DUMP_URI = recruiterbox.SITE+"/static/schema_dump.json"

openings = recruiterbox.openings.all()
for opening in openings:
    new_stage = opening.stages.create()
    new_stage.name = 'new_stage'
    new_stage.save()
