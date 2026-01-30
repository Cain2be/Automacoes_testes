export function gerarCPF() {
  const rand = () => Math.floor(Math.random() * 9);

  const n = Array.from({ length: 9 }, rand);

  // primeiro dígito verificador
  let d1 =
    n.reduce((acc, num, idx) => acc + num * (10 - idx), 0) % 11;
  d1 = d1 < 2 ? 0 : 11 - d1;

  // segundo dígito verificador
  let d2 =
    [...n, d1].reduce((acc, num, idx) => acc + num * (11 - idx), 0) % 11;
  d2 = d2 < 2 ? 0 : 11 - d2;

  return `${n.join('')}${d1}${d2}`;
}