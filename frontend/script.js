function clicou() {
  alert('Funcionando!')
};

// ==========================
// TESTE API
// ==========================
function testarAPI() {
  fetch('http://127.0.0.1:8000/')
    .then(res => res.json())
    .then(data => {
      console.log(data)
      alert(data.msg)
    })
    .catch(err => {
      console.error("Erro:", err)
    })
}

// ==========================
// CARREGAR TABELA DE TREINOS
// ==========================
function carregarTabela() {
  fetch("http://127.0.0.1:8000/treinos")
    .then(res => res.json())
    .then(dados => {
      let tabela = "";

      dados.forEach(t => {
        tabela += `
          <tr>
            <td>${t.id}</td>
            <td>${t.exercicio}</td>
            <td>${t.peso}</td>
            <td>${t.reps}</td>
            <td>${t.data}</td>
          </tr>
        `;
      });

      document.getElementById("tabela").innerHTML = tabela;
    })
    .catch(err => {
      console.error("Erro ao carregar tabela:", err)
    });
}

// ==========================
// CARREGAR EXERCICIOS (DROPDOWN)
// ==========================
function carregarExercicios() {
  fetch("http://127.0.0.1:8000/exercicios")
    .then(res => res.json())
    .then(dados => {
      const select = document.getElementById("exercicio")

      select.innerHTML = ""

      dados.forEach(ex => {
        const option = document.createElement("option")
        option.value = ex.id
        option.textContent = ex.nome
        select.appendChild(option)
      })
    })
    .catch(err => {
      console.error("Erro ao carregar exercícios:", err)
    });
}

// ==========================
// REGISTRAR CONTA (TESTE)
// ==========================
function registrarAccount() {
  fetch("http://127.0.0.1:8000/registro", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      nome: "Joao",
      senha: "123"
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      alert(data.msg)
    })
    .catch(err => {
      console.error("Erro:", err)
    })
}

// ==========================
// REGISTRAR TREINO (NOVO MODELO)
// ==========================
function registrarTreino() {
  const exercicio_id = document.getElementById("exercicio").value;
  const peso = document.getElementById("peso").value;
  const reps = document.getElementById("reps").value;

  fetch("http://127.0.0.1:8000/treino_exercicios", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      treino_id: 1, // depois tu pode dinamizar
      exercicio_id: Number(exercicio_id),
      series: 3,
      repeticoes: Number(reps),
      peso: Number(peso)
    })
  })
    .then(res => res.json())
    .then(data => {
      console.log("Treino salvo:", data);
      carregarTabela();
    })
    .catch(err => {
      console.error("Erro ao salvar treino:", err);
    });
}

// ==========================
// CALCULAR 1RM
// ==========================
function registrarRm() {
  const peso = document.getElementById("peso_calc").value
  const reps = document.getElementById("reps_calc").value

  fetch(`http://127.0.0.1:8000/calcular?peso=${peso}&reps=${reps}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("resultado").innerText =
        "1RM estimado: " + data["1rm"]
    })
    .catch(err => {
      console.error("Erro ao calcular RM:", err)
    });
}

// ==========================
// LOAD INICIAL
// ==========================
window.onload = () => {
  carregarTabela()
  carregarExercicios()
}