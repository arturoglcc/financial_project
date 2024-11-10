# start.sh
#!/bin/bash
source ~/mi_entorno/bin/activate  # Activa el entorno virtual
alembic revision --autogenerate -m "Add curp, rfc, and nombre columns to users"  # Ejecuta el comando de Alembic
