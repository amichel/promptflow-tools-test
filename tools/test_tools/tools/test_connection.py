from dataclasses import dataclass
from promptflow.core import tool
from promptflow.connections import CustomStrongTypeConnection
from promptflow.contracts.types import Secret
from promptflow._core.tools_manager import register_connections

class TestConnection(CustomStrongTypeConnection):
    test_key: str
    test_secret: Secret

#this workaround solves ResolveToolError: Tool load failed in 'Connection_Validate: (ValueTypeUnresolved), but then the tool stil fails on node 'Connection_Validate' of type 'CustomConnection' is not supported, valid types 
#register_connections(TestConnection)

@tool
def validate(connection: TestConnection) -> bool:  
    return len(connection.test_key)>0 and len(connection.test_secret)>0
