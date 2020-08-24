let chrono = false;
let startChrono = Date.now()
const server = 'http://localhost:5000/'


const showStop = (seconds) => {
  const millis = seconds*1000;
  const minRender = document.querySelector('.min');
  const secRender = document.querySelector('.sec');
  const decRender = document.querySelector('.millis');

  min = (parseInt(millis/60000)).toString().padStart(2, "0");
  sec = (parseInt(millis/1000)).toString().padStart(2, "0");
  dec = Math.round(millis%1000).toString().padStart(3, "0");
  minRender.innerHTML = min;
  secRender.innerHTML = sec;
  decRender.innerHTML = dec;
}


const timer = () => {
  const minRender = document.querySelector('.min');
  const secRender = document.querySelector('.sec');
  const decRender = document.querySelector('.millis');

  let min = 0;
  let sec = 0;
  let dec = 0;

  const showChrono = (millis) => {
    min = (parseInt(millis/60000)).toString().padStart(2, "0");
    sec = (parseInt(millis/1000)).toString().padStart(2, "0");
    dec = parseInt(millis%1000).toString().padStart(3, "0");
    
    
    minRender.innerHTML = min;
    secRender.innerHTML = sec;
    decRender.innerHTML = dec;
  }
 
  const everyDec = () => {
    if (chrono){
      now = Date.now();
      diference = now-startChrono;
      showChrono(diference);
    }
  };

  setInterval(everyDec, 17);
  let now = 0;
  let diference = 0;
};

const send = () => {
  const buttonParent = document.querySelector('.is-fetching');
  const submitbutton = document.querySelector('.button');
  const fileInput = document.querySelector('.file-input');
  const sortMethod = document.querySelector('.sort-method');
  const sampleVolume = document.querySelector('.sample-volume');
  const fileError = document.querySelector('.file-error');
  const eventsLog = document.querySelector('.events');
  buttonParent.onclick = () => {
    fileError.textContent = ''
    if (fileInput.value == '') {
      fileError.textContent = 'Selecciona un archivo'
    } else{
      submitbutton.classList.toggle('is-loading');
      chrono = !chrono;
      startChrono = Date.now()
      if (chrono){
        const file = fileInput.value.split('\\')[2]
        const samples = sampleVolume.value
        const method = sortMethod.value
        fetch(server, {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'API-Key': 'secret'
          },
          body: JSON.stringify({samples, method}),
        })
        .then(response => response.json())
        .then(data => {
          chrono = !chrono;
          console.log(data)
          showStop(data['time']);
          eventsLog.appendChild(message(data['message'],'success'));
          submitbutton.classList.toggle('is-loading');
        })
        .catch((error) => {
          eventsLog.appendChild(message(`Error en el servidor Python`,'danger '))
          console.error('Error:', error);
          submitbutton.classList.toggle('is-loading');
          chrono = !chrono;
        });
      // send post to API return file size
      // send post to solve algoritm
      // Append what was done in the register
      }
    }
  }
};

const updateFile = () => {
  const eventsLog = document.querySelector('.events');
  const fileInput = document.querySelector('#file-upload input[type=file]');
  fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
      const fileName = document.querySelector('#file-upload .file-name');
      fileName.textContent = fileInput.files[0].name;
      const fileError = document.querySelector('.file-error');
      fileError.textContent = '';
      const data = { "file": fileInput.files[0].name }
      fetch(server, {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'API-Key': 'secret'
        },
        body: JSON.stringify(data),
      })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          eventsLog.appendChild(message(data['message'],'success'));
        })
        .catch(error => {
          console.log(error);
          eventsLog.appendChild(message('Error en el servidor de python, no pudo cargar archivo','danger'));
        });
    }
  }
};

const message = (text, type) => {
  const timestamp = moment().format('HH:MM:ss')
  const messagelog = document.createElement('p')
  const messageContent = document.createElement('span')
  const prompt = document.createElement('span')
  prompt.classList = 'has-text-link'
  prompt.textContent = `> ${timestamp}`
  messageContent.classList = `has-text-${type}`
  messageContent.innerHTML = ` - ${text}`
  messagelog.append(prompt, messageContent);
  return messagelog;
}

window.onload = () => {
  updateFile();
  timer();
  send();
};