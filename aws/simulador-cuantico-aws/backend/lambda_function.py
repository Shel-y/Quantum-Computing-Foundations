import json
import numpy as np

def lambda_handler(event, context):
    # 1. EL QUBIT
    qubit = np.array([[1], [0]])
    
    # 2. LA MATRIZ
    H = (1/np.sqrt(2)) * np.array([[1, 1],
                                   [1, -1]])
    
    # 3. LA SIMULACIÓN
    estado_final = np.dot(H, qubit)
    
    # RESULTADOS
    probabilidades = {
        "0": float(np.abs(estado_final[0][0])**2),
        "1": float(np.abs(estado_final[1][0])**2)
    }

    # AWS se encarga del CORS automáticamente
    return {
        'statusCode': 200,
        'body': json.dumps(probabilidades)
    }
