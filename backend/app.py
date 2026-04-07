from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="MVP", version="1.0.0")

# Habilitar CORS para comunicação com o Front-end (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. CARGA DO MODELO (Item 4 do Trabalho)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
model = None
MODEL_PATH = "Não identificado"

@app.on_event("startup")
def load_model():
    global model, MODEL_PATH
    try:
        if os.path.exists(MODELS_DIR):
            pkl_files = [f for f in os.listdir(MODELS_DIR) if f.endswith('.pkl')]
            if pkl_files:
                MODEL_PATH = os.path.join(MODELS_DIR, pkl_files[0])
                model = joblib.load(MODEL_PATH)
                print(f">>> SUCESSO: Modelo {pkl_files[0]} carregado!")
            else:
                print(f">>> AVISO: Nenhum arquivo .pkl encontrado em {MODELS_DIR}")
        else:
            print(f">>> AVISO: Diretório {MODELS_DIR} não encontrado.")
    except Exception as e:
        print(f">>> ERRO ao carregar o modelo: {e}")

# Mapeamento para labels legíveis
LABEL_MAPPING = {
    0: "Normal",
    1: "Leve",
    2: "Moderado",
    3: "Grave",
    4: "Extremamente Grave"
}

# 2. DEFINIÇÃO DA ENTRADA DE DADOS (Pydantic)
class PredictionInput(BaseModel):
    TIPI1: int; TIPI2: int; TIPI3: int; TIPI4: int; TIPI5: int
    TIPI6: int; TIPI7: int; TIPI8: int; TIPI9: int; TIPI10: int
    education: int; urban: int; gender: int; age: int; married: int

# 3. ENDPOINT DE PREDIÇÃO (Item 4 do Trabalho)
@app.post("/predict")
def predict(data: PredictionInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo não carregado no servidor.")
    
    try:
        # Converter entrada em DataFrame (o Pipeline espera o formato original do treinamento)
        input_df = pd.DataFrame([data.dict()])
        
        # Realizar a predição através do Pipeline (que já contém o pré-processamento)
        prediction = model.predict(input_df)[0]
        
        return {
            "prediction_class": int(prediction),
            "label": LABEL_MAPPING.get(prediction, "Desconhecido")
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
