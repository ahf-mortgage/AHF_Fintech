const express = require("express");
const path = require("path");

const bodyParser = require("body-parser");
const app = express();
const fileUpload = require('express-fileupload');


const { cutVideo } = require("./controllers/editVideo.js");
const { addVideoToText } = require("./controllers/addTextToVideo.js");
const { addAudio } = require("./controllers/addAudio.js");
const {muteAudio} = require("./controllers/mute_video.js");

const port = process.env.PORT || 8080;

// Serve static files from the current directory
app.use(express.static(path.join(__dirname)));
// Configure body-parser middleware
app.use(bodyParser.json());

// Route all other requests to serve index.html
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});
app.use(fileUpload());



app.post('/upload', function(req, res) {
  let sampleFile;
  let uploadPath;

  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send('No files were uploaded.');
  }

  // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
  sampleFile = req.files.sampleFile;
  uploadPath = __dirname + '/uploads/' + sampleFile.name;

  // Use the mv() method to place the file somewhere on your server
  sampleFile.mv(uploadPath, function(err) {
    if (err)
      return res.status(500).send(err);

    res.send('File uploaded!');
  });

}
)
// Route all other requests to serve rindex.html
app.post("/crop/", (req, res) => {
  const sourcePath = req.body["sourcePath"];
  const outputPath = req.body["outputPath"];
  const startTime = req.body["startTime"];
  const duration = req.body["duration"];
  cutVideo(sourcePath, outputPath, startTime, duration);

  res.json({
    msg: "Video cutting completed successfully",
  });
});

app.post("/addText/", (req, res) => {
  const inputFile = req.body["inputFile"];
  const outputFile = req.body["outputFile"];
  const fontFile = req.body["fontFile"];
  const text = req.body["text"];
  const x = req.body["x"]; //10; // Position from left (pixels)
  const y = req.body["y"]; //50; // Position from top (pixels)
  const fontSize = req.body["fontsize"]; // 24;
  const color = req.body["color"]; // 'white';

  addVideoToText(inputFile, outputFile, fontFile, text, x, y, fontFile, color);

  res.json({
    msg: "Text added",
  });
});

app.post("/addAudioToVideo/", (req, res) => {
  const videoPath = req.body["videoPath"];
  const audioPath = req.body["audioPath"];
  const outputPath = req.body["outputPath"];
  try {
    addAudioOverlay(videoPath, audioPath, outputPath);
  } catch (error) {
    console.log(error);
  }

  res.json({
    msg: "audion added to text",
  });
});




app.post("/mutevideo/", (req, res) => {

    const inputPath =  req.body['inputPath']//'video_with_audio.mp4';
    const outputPath =req.body['outputPath'] //'video_without_audio.mp4';
    
    muteAudio(inputPath, outputPath)
      .then(() => {
        console.log('Audio muted successfully.');
      })
      .catch((err) => {
        console.error('Error muting audio:', err);
      });

  res.json({
    msg: "audion added to text",
  });
});


app.post("/combinevideowithVideo/",(req,res) => {

  // Example usage
  const inputVideos =  req.body['inputVideos'] // ['video1.mp4', 'video2.mp4'];
  const outputVideo =   req.body['outputVideos'] // 'output.mp4';
  
  combineVideos(inputVideos, outputVideo, (error) => {
    if (error) {
      console.error('Error combining videos:', error);
    } else {
      console.log('Videos combined successfully!');
    }
  })
  

})


app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
