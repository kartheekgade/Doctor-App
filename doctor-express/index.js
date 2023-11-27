const express = require('express');
const multer = require('multer');
const app = express();
const port = 3001;

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.post('/upload-audio', upload.single('audio'), (req, res) => {
  const audioFile = req.file;
  // Process the audio file (e.g., save it to disk, database, etc.)

  res.json({ message: 'Audio uploaded successfully!' });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
