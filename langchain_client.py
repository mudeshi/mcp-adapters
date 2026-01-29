from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from mcp import ClientSession, StdioServerParameters
from dotenv import load_dotenv
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
import asyncio

load_dotenv()

llm = ChatOllama(model="llama3.2",temperature=0,)
server_params = StdioServerParameters(
    command="python", 
    args=["/Users/malayudeshi/Projects/langchain-course/mcp-adapters/servers/math_server.py"]
)

async def main():
    print("Hello from langchain_mcp!")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            print("Connected to MCP server.")
            # Get tools
            #tools = await session.list_tools()
            #print("Available tools:", tools)

            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_agent(llm, tools)
            agent_response = await agent.ainvoke({"messages": "what's 54 + 2 * 3?"})
            print("Agent response:", agent_response)

if __name__ == "__main__":
    asyncio.run(main())