
CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,        -- No PostgreSQL, "SERIAL" cria o ID auto-incrementável
    nome VARCHAR(100) NOT NULL,   -- Atributo nome do tipo varchar
    email VARCHAR(100),           -- Atributo e-mail do tipo varchar
    endereco VARCHAR(255)         -- Atributo endereço do tipo varchar
);

-- Inserindo dados de teste
INSERT INTO aluno (nome, email, endereco) VALUES 
('Ana Souza', 'ana.souza@email.com', 'Rua das Flores, 123'),
('Carlos Lima', 'carlos.lima@email.com', 'Avenida Central, 456');

-- Consultando os dados
SELECT * FROM aluno;
