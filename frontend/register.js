function registrar() {
  const nome = document.getElementById("nome").value
  const senha = document.getElementById("senha").value


  console.log("Nome:", nome)
  console.log("Senha:", senha)
  fetch("http://127.0.0.1:8000/registro", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ nome, senha })
  })
  .then(res => res.json())
  .then(data => {
    if (data.user_id) {
      localStorage.setItem("usuario_id", data.user_id)
      window.location.href = "app.html"
    } else {
      alert("Usuario Registrado com Sucesso!")
    }
  })
}