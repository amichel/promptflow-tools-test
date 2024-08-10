from promptflow.core import tool
from test_tools.tools.test_connection import TestConnection

@tool
def validate(connection: TestConnection) -> bool: 
    return len(connection.test_key)>0 and len(connection.test_secret)>0
