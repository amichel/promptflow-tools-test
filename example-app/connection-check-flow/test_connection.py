from promptflow.core import tool
from test_tools.tools.test_connection import TestConnection

#this script tool works as expected, with the same connection type from the tools package
@tool
def validate(connection: TestConnection) -> bool: 
    return len(connection.test_key)>0 and len(connection.test_secret)>0
