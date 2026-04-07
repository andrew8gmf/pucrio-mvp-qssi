import pandas as pd
import joblib
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "archive", "data.csv")
MODEL_SAVE_PATH = os.path.join(BASE_DIR, "models", "data.pkl")

def train_official_model():
    print("\n" + "="*50)
    print("INICIANDO TREINAMENTO DO MODELO OFICIAL (LOCAL)")
    
    # 1. Carga
    if not os.path.exists(DATA_PATH):
        print(f"ERRO: Dataset não encontrado em {DATA_PATH}")
        return
    
    df = pd.read_csv(DATA_PATH, sep='\t')
    
    # 2. Limpeza (Data Quality)
    df_clean = df[(df['VCL6'] == 0) & (df['VCL9'] == 0) & (df['VCL12'] == 0)].copy()
    df_clean = df_clean[(df_clean['age'] >= 10) & (df_clean['age'] <= 90)]

    # 3. Target
    dep_items = ['Q3A', 'Q5A', 'Q10A', 'Q13A', 'Q16A', 'Q17A', 'Q21A', 'Q24A', 'Q26A', 'Q31A', 'Q34A', 'Q37A', 'Q38A', 'Q42A']
    raw_score = df_clean[dep_items].sum(axis=1) - 14
    y = raw_score.apply(lambda s: 0 if s<=9 else 1 if s<=13 else 2 if s<=20 else 3 if s<=27 else 4)

    # 4. Features
    features_tipi = [f'TIPI{i}' for i in range(1, 11)]
    features_demo = ['education', 'urban', 'gender', 'age', 'married']
    X = df_clean[features_tipi + features_demo]

    # 5. Pré-processamento (Pipeline e ColumnTransformer)
    numeric_features = features_tipi + ['age']
    categorical_features = ['education', 'urban', 'gender', 'married']

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

    # 6. Pipeline Completo
    model_pipeline = Pipeline([
        ('pre', preprocessor),
        ('clf', DecisionTreeClassifier(max_depth=10, random_state=42))
    ])

    # 7. Treino
    print("Treinando o Pipeline (StandardScaler + OneHotEncoder + DecisionTree)...")
    model_pipeline.fit(X, y)

    # 8. Exportação
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    joblib.dump(model_pipeline, MODEL_SAVE_PATH)
    
    print(f"SUCESSO: Modelo Oficial exportado para {MODEL_SAVE_PATH}")
    print("="*50 + "\n")

if __name__ == "__main__":
    train_official_model()
