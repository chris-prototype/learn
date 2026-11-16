from typing import TypedDict, Annotated

# run time libraries like pydantic will throw errors for the annotation
# however, they require the pydantic library not shown here
# static analysis tools will catch the int requirement
ValidAge = Annotated[int, "Must be greater than 0"]
user_age: ValidAge = 1

'''

example taken from MVF
note the second field, is just metadata, it can be used for advanced type checking in validation libries or it can be use for reducer functions in graph libraries
for example in langraph, this allows two separate branches ( a series of nodes and edges ) to merge without crashing on simultaneous updates for an execution step ( a langgraph superstep )
https://reference.langchain.com/python/langgraph/graph/state/StateGraph

'''

def _last(a: str, b: str) -> str:
    return b if b else a
  
class FactoryState(TypedDict):
    ticket_id: Annotated[str, _last]