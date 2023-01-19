"""
Test client site
"""

import os
import sys
import json
import unittest


from nmdc.client.client import get_site_token, post_workflow_activities

class testClient(unittest.TestCase):

    def test_get_site_token(self):
        """
        Test get_site_token method
        """
        print(self.id())        
        
        try:
            client_name=os.environ['nmdc_client_id']
            client_password=os.environ['nmdc_client_credential']

        except KeyError:
            print('Cannot find site credential from environment.', file=sys.stderr)

        access_token = get_site_token(client_name, client_password)
        self.assertIsNotNone(access_token)
        self.nmdc_client_token = access_token
        
        print(f'Client token: {access_token}')

    def test_metadata_registration(self):
        print(self.id())
        
        # Had to remove the "version" field below since it is not in the schema.
        data = {
            "read_qc_analysis_activity_set": [
                {
                    "has_input": [
                        "nmdc:a1d8fff4b02719c4d0f9c442cf052f69"
                    ], 
                    "part_of": [
                        "nmdc:mgrqc0xxxx.1"
                    ], 
                  "input_read_bases": 1726196062, 
                  "name": "Read QC Activity for nmdc:mgrqc0xxxx.1", 
                  "output_read_count": 8312566, 
                  "output_read_bases": 1244017053, 
                  "git_url": "https://github.com/microbiomedata/mg_annotation/releases/tag/0.1", 
                  "ended_at_time": "2022-12-05T14:55:44+00:00", 
                  "has_output": [
                    "nmdc:b4023bf29269c9820e8f0682b82a8414", 
                    "nmdc:bd5d6090ddc03b181ffdae383f48b2c4"
                  ], 
              "started_at_time": "2022-10-26T22:59:32+00:00", 
              "was_informed_by": "gold:Gp0000000", 
              "input_read_count": 11431762, 
              "type": "nmdc:ReadQCAnalysisActivity", 
              "id": "nmdc:01d53e73571b35a505bf090b191164b3", 
              "execution_resource": "NERSC-Cori"
            }], 
            "data_object_set": [
                {
                  "file_size_bytes": 692638235, 
                  "name": "Reads QC result fastq (clean data)", 
                  "url": "https://data.microbiomedata.org/data/nmdc:mgrqc0xxxx.1/qa/nmdc_mgrqc0xxxx.1_filtered.fastq.gz", 
                  "data_object_type": "Filtered Sequencing Reads", 
                  "type": "nmdc:DataObject", 
                  "id": "nmdc:b4023bf29269c9820e8f0682b82a8414", 
                  "md5_checksum": "b4023bf29269c9820e8f0682b82a8414", 
                  "description": "Reads QC for nmdc:mgrqc0xxxx.1"
                }, 
                {
                  "file_size_bytes": 280, 
                  "name": "Reads QC summary statistics", 
                  "url": "https://data.microbiomedata.org/data/nmdc:mgrqc0xxxx.1/qa/nmdc_mgrqc0xxxx.1_filterStats.txt", 
                  "data_object_type": "QC Statistics", 
                  "type": "nmdc:DataObject", 
                  "id": "nmdc:bd5d6090ddc03b181ffdae383f48b2c3", 
                  "md5_checksum": "bd5d6090ddc03b181ffdae383f48b2c4", 
                  "description": "Reads QC summary for nmdc:mgrqc0xxxx.1"
                }]}

        client_name=os.environ['nmdc_client_id']
        client_password=os.environ['nmdc_client_credential']

        access_token = get_site_token(client_name, client_password)        
        print(json.dumps(post_workflow_activities(access_token, data).json()))
        
if __name__ == '__main__':
    unittest.main()



# if __name__ == '__main__':

    
    
#     obj_id = "gfs0nd80"


#     site_token = test_site()

#     if site_token is not None:
#         # list all the registered workflows
#         print(json.dumps(get_workflows(site_token).json()))

#         # sample metadata registration
#         print(json.dumps(get_v1_outputs(site_token, data).json()))

#         # get information about an objeect by its id.
#         print(json.dumps(get_objects_by_id(site_token, obj_id).json()))
    
