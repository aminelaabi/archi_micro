const sio = io();

sio.on('connect', () => {
  console.log('connected');
  sio.emit('sum_io', {numbers: [1, 2]}, (result) => {
    console.log(result);
  });
});



function change_img(result) {
  const dataUrl = 'data:image/jpg;base64,' + result.toString('base64');
  let img = document.getElementById("img");
  img.src = dataUrl;
}


function getBase64video(img) {
  var canvas = document.createElement("canvas");
  canvas.width = 640;
  canvas.height = 480;
  var ctx = canvas.getContext("2d");
  ctx.drawImage(img, 0, 0, 640, 480);
  return canvas.toDataURL("image/jpeg", 1.0).replace(/^data:image\/\w+;base64,/, "");
}


navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    let videoElement = document.getElementById("video");
    videoElement.srcObject = stream;
    videoElement.play();
    setInterval(() => {
      let img = getBase64video(videoElement);
      sio.emit("video", {video: img}, () => {
        console.log("Video sent");
      });
    }, 1000 / 5); // Send frames at 3 FPS
});



sio.on('video', (frame_res) => {
  change_img(frame_res);
});