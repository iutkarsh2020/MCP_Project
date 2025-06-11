# we will add on some new tools and will create a new server for that

from mcp.server.fastmcp import FastMCP


mcp = FastMCP('Simple_Server')

@mcp.tool()
def add(a: int, b: int):
    ''' Adds two numbers
    Args: 
    a: First Argument
    b: Second Argument

    Return: sum of the numbers
    '''
    return a+b

@mcp.tool()
def multiply(a: int, b: int):
    ''' Multiplies two numbers
    Args: 
    a: First Argument
    b: Second Argument

    Return: sum of the numbers
    '''
    return a*b


if __name__ == '__main__':
    mcp.run(transport='stdio')
