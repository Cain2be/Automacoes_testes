async function camposExistentes(campos) {
  const existentes = [];

  for (const campo of campos) {
    if (await campo.count() > 0) {
      existentes.push(campo);
    }
  }
  
  console.log(existentes)
  return existentes;
}

module.exports = {
  camposExistentes,
};
