import React, { useState } from 'react';
import type { Route } from "./+types/home";
import "../app.css";

interface PredictionResponse {
  prediction_class: number;
  label: string;
}

const TIPI_QUESTIONS = [
  "Extrovertido, entusiasmado",
  "Crítico, briguento",
  "Confiável, autodisciplinado",
  "Ansioso, chateia-se facilmente",
  "Aberto a novas experiências, complexo",
  "Reservado, quieto",
  "Simpático, caloroso",
  "Desorganizado, descuidado",
  "Calmo, emocionalmente estável",
  "Convencional, não criativo"
];

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Predição DASS-42 - MVP PUC-Rio" },
    { name: "description", content: "Sistema inteligente de predição de níveis de depressão." },
  ];
}

export default function Home() {
  const [formData, setFormData] = useState<any>({
    TIPI1: 4, TIPI2: 4, TIPI3: 4, TIPI4: 4, TIPI5: 4,
    TIPI6: 4, TIPI7: 4, TIPI8: 4, TIPI9: 4, TIPI10: 4,
    education: 2, urban: 2, gender: 1, age: 25, married: 1
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: parseInt(value) });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Falha na comunicação com o servidor');
      
      const data = await response.json();
      setResult(data);
    } catch (err: any) {
      setError(err.message || 'Ocorreu um erro inesperado.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>DASS-42: Predição de Depressão</h1>
      <p className="subtitle">
        MVP de Inteligência Artificial para Classificação de Saúde Emocional baseada em Personalidade.
      </p>

      <form onSubmit={handleSubmit}>
        <div className="section">
          <h2>1. Traços de Personalidade (TIPI)</h2>
          <p style={{ fontSize: '0.8rem', color: '#666' }}>
            Eu me vejo como: (1: Discordo totalmente | 7: Concordo totalmente)
          </p>
          {TIPI_QUESTIONS.map((q, index) => (
            <div key={index} className="tipi-item">
              <span className="tipi-label">{index + 1}. {q}</span>
              <select 
                name={`TIPI${index + 1}`} 
                value={formData[`TIPI${index + 1}`]} 
                onChange={handleChange}
              >
                {[1, 2, 3, 4, 5, 6, 7].map(v => <option key={v} value={v}>{v}</option>)}
              </select>
            </div>
          ))}
        </div>

        <div className="section">
          <h2>2. Dados Demográficos</h2>
          <div className="grid">
            <div className="form-group">
              <label>Idade</label>
              <input type="number" name="age" value={formData.age} onChange={handleChange} min="10" max="90" />
            </div>
            <div className="form-group">
              <label>Gênero</label>
              <select name="gender" value={formData.gender} onChange={handleChange}>
                <option value="1">Masculino</option>
                <option value="2">Feminino</option>
                <option value="3">Outro</option>
              </select>
            </div>
            <div className="form-group">
              <label>Educação</label>
              <select name="education" value={formData.education} onChange={handleChange}>
                <option value="1">Fundamental incompleto</option>
                <option value="2">Médio completo</option>
                <option value="3">Universitário (Graduação)</option>
                <option value="4">Pós-graduação</option>
              </select>
            </div>
            <div className="form-group">
              <label>Ambiente de Infância</label>
              <select name="urban" value={formData.urban} onChange={handleChange}>
                <option value="1">Rural</option>
                <option value="2">Suburbano</option>
                <option value="3">Urbano</option>
              </select>
            </div>
          </div>
        </div>

        <button type="submit" className="predict-btn" disabled={loading}>
          {loading ? 'Processando Predição...' : 'Analisar Resultados'}
        </button>
      </form>

      {error && <div style={{ color: 'red', marginTop: '1rem', textAlign: 'center' }}>{error}</div>}

      {result && (
        <div className={`result-card severity-${result.prediction_class}`}>
          <h3>Resultado da Predição</h3>
          <p style={{ fontSize: '1.4rem', fontWeight: 'bold' }}>{result.label}</p>
          <p style={{ fontSize: '0.9rem' }}>
            {result.label === 'Normal' ? 'Seus níveis estão dentro da média populacional.' : 
             'Recomenda-se acompanhamento especializado para maiores esclarecimentos.'}
          </p>
        </div>
      )}
    </div>
  );
}
