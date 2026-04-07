import joblib
import os
import pandas as pd
from sklearn.metrics import accuracy_score

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_PATH = os.path.join(BASE_DIR, "..", "archive", "data.csv")

def test_model_performance():
    """
    Assegura que o modelo atenda aos requisitos de desempenho estabelecidos.
    Requisito: Acurácia deve ser superior a 40% (considerando 5 classes e features subjetivas).
    """
    # 1. Carregar modelo dinamicamente
    assert os.path.exists(MODELS_DIR), f"Diretório {MODELS_DIR} não encontrado."
    pkl_files = [f for f in os.listdir(MODELS_DIR) if f.endswith('.pkl')]
    assert len(pkl_files) > 0, "Nenhum arquivo de modelo .pkl encontrado para teste."
    
    MODEL_PATH = os.path.join(MODELS_DIR, pkl_files[0])
    model = joblib.load(MODEL_PATH)
    print(f"Testando modelo: {pkl_files[0]}")
    
    # 2. Carregar dados de teste (usaremos uma amostra do dataset original)
    df = pd.read_csv(DATA_PATH, sep='\t').head(500)
    
    # Repetir o pré-processamento do notebook para o target
    dep_items = ['Q3A', 'Q5A', 'Q10A', 'Q13A', 'Q16A', 'Q17A', 'Q21A', 'Q24A', 'Q26A', 'Q31A', 'Q34A', 'Q37A', 'Q38A', 'Q42A']
    raw_score = df[dep_items].sum(axis=1) - 14
    y_true = raw_score.apply(lambda s: 0 if s<=9 else 1 if s<=13 else 2 if s<=20 else 3 if s<=27 else 4)
    
    X = df[[f'TIPI{i}' for i in range(1, 11)] + ['education', 'urban', 'gender', 'age', 'married']]
    
    # 3. Predição
    y_pred = model.predict(X)
    
    # 4. Cálculo da Métrica
    acc = accuracy_score(y_true, y_pred)
    print(f"Acurácia do modelo no teste: {acc:.4f}")
    
    # 5. Threshold (Limite aceitável)
    THRESHOLD = 0.40
    assert acc >= THRESHOLD, f"O modelo não atingiu a acurácia mínima de {THRESHOLD}. Acurácia atual: {acc:.4f}"

if __name__ == "__main__":
    test_model_performance()
