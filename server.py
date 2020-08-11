import time
from fastapi import FastAPI
from pydantic import (BaseModel)
import os
import sys
import os.path
sys.path.append(os.getcwd())
from factorial import Factorial

#Defining the pydantic request and response

class FactorialRequest(BaseModel):
    input_number: int = None

class FactorialResponse(BaseModel):
    input: int = None
    factorial: int = None
    time_taken: str = None


app = FastAPI()

factorial_object = Factorial()

@app.post("/compute/factorial", response_model=FactorialResponse)
async def return_factorial( request: FactorialRequest ):

    start = time.time()
    output = factorial_object.compute(request.input_number)
    end = time.time()
    time_taken = ( end - start )
    msec_string = str(time_taken*1000) + "ms"

    response = FactorialResponse( input = request.input_number, factorial = output, time_taken= msec_string)

    return response

# @app.post("/compute/factorial")
# async def return_factorial( input_num: int ):

#     start = time.time()
#     output = factorial_object.compute(input_num)
#     end = time.time()
#     time_taken = ( end - start )
#     msec_string = str(time_taken*1000) + "ms"

#     #Note- I could have used pydantic model here to define the format and return accordingly, but going along with defining json on the fly for simplicity
#     return {
#         "input": input_num,
#         "factorial": output,
#         "time_taken": msec_string
#     }