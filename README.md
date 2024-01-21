# PythonLightService
Python Light Microservice using Kasa plug interface


git clone git@github.com:ThomasJay/PythonLightService.git


cd PythonLightService


python3 -m venv venv

source venv/bin/activate


Check end point

curl http://localhost:8086/


Check health

curl http://localhost:8086/api/v1/health

{
  "status": "Healthy"
}




Turn light on

curl http://localhost:8086/api/v1/on 

Status:

{
  "status": "Light On"
}


Turn light off

curl http://localhost:8086/api/v1/off

Status:

{
  "status": "Light Off"
}


