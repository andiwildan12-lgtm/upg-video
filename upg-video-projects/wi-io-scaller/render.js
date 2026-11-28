const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const f of ['WI-IO', 'WI-Scaler']) {
    const p = await b.newPage({viewport: {width: 794, height: 1123}, deviceScaleFactor: 3});
    await p.goto('file://' + __dirname + '/' + f + '.html');
    await p.evaluate(() => document.fonts.ready);
    const pages = await p.$$('.page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({path: `${__dirname}/hasil/${f}-hal${i + 1}.png`});
    await p.pdf({path: `${__dirname}/hasil/${f}.pdf`, format: 'A4', printBackground: true});
    console.log(f, await p.evaluate(() => [...document.querySelectorAll('main')].map(m => m.scrollHeight > m.clientHeight + 1 ? 'OVERFLOW' : 'ok').join(',')));
  }
  await b.close();
})();
