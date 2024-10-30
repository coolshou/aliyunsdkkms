# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkkms.endpoint import endpoint_data

class UpdateKmsInstanceBindVpcRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Kms', '2016-01-20', 'UpdateKmsInstanceBindVpc','kms')
		self.set_protocol_type('https')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_KmsInstanceId(self): # String
		return self.get_query_params().get('KmsInstanceId')

	def set_KmsInstanceId(self, KmsInstanceId):  # String
		self.add_query_param('KmsInstanceId', KmsInstanceId)
	def get_BindVpcs(self): # String
		return self.get_query_params().get('BindVpcs')

	def set_BindVpcs(self, BindVpcs):  # String
		self.add_query_param('BindVpcs', BindVpcs)
