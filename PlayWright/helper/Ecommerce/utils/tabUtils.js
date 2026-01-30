async function tabAteSairDoCampoData(page, inputDate) {
  const idInicial = await inputDate.getAttribute('id');

  for (let i = 0; i < 5; i++) {
    await page.keyboard.press('Tab');

    const idAtual = await page.evaluate(() => {
      return document.activeElement?.id;
    });

    if (idAtual !== idInicial) {
      return;
    }
  }

  throw new Error('Não foi possível sair do campo de data com TAB');
}

module.exports = {
  tabAteSairDoCampoData,
};
