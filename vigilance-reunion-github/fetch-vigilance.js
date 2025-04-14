const https = require('https');
const fs = require('fs');
const path = require('path');

const url = "https://vigilance.meteofrance.re/data/images/vigilance/vigilance_974.png";
const outputPath = path.join(__dirname, 'public', 'vigilance.png');

// Créer le dossier 'public' s'il n'existe pas
fs.mkdirSync(path.dirname(outputPath), { recursive: true });

// Télécharger l'image
https.get(url, res => {
  if (res.statusCode === 200) {
    const file = fs.createWriteStream(outputPath);
    res.pipe(file);
    file.on('finish', () => {
      file.close();
      console.log("Image téléchargée avec succès !");
    });
  } else {
    console.error(`Erreur HTTP: ${res.statusCode}`);
  }
}).on('error', err => {
  console.error(`Erreur de téléchargement: ${err.message}`);
});
