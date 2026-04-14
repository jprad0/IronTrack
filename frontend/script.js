function clicou() {
    alert('Funcionando!')
};

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
  });
}

// carrega automaticamente quando abrir a pagina
window.onload = carregarTabela;

function registrarTreino() {
  const exercicio = document.getElementById("exercicio").value;
  const peso = document.getElementById("peso").value;
  const reps = document.getElementById("reps").value;

  fetch("http://127.0.0.1:8000/salvar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      exercicio: exercicio,
      peso: Number(peso),
      reps: Number(reps)
    })
  })
  .then(res => res.json())
  .then(data => {
    console.log("Resposta:", data);
    carregarTabela();
  })
  .catch(err => {
    console.error("Erro:", err);
  });
}

function registrarRm() {
  const peso = document.getElementById("peso_calc").value
  const reps = document.getElementById("reps_calc").value

  fetch(`http://127.0.0.1:8000/calcular?peso=${peso}&reps=${reps}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("resultado").innerText =
        "1RM estimado: " + data["1rm"]
    })
}