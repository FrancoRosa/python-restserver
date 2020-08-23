let chrono = false;
let startChrono = Date.now()

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
        eventsLog.appendChild(message(`Enviando ${file} con ${samples} muestras para ordenar con el metodo ${method} al servidor Python`,'success'))
        fetch('http://localhost:5000/sort', {
          mode: 'no-cors',
          method: 'POST',
          body: JSON.stringify({file, samples, method}),
        })
          .then(response => response.json())
          .then(data => console.log(data))
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

const timer = () => {

  const minRender = document.querySelector('.min');
  const secRender = document.querySelector('.sec');
  const decRender = document.querySelector('.dec');

  let min = 0;
  let sec = 0;
  let dec = 0;
 
  const everyDec = () => {
    if (chrono){
      now = Date.now();
      diference = now-startChrono;
      diference = diference/100;
      min = (parseInt(diference/600)%60).toString().padStart(2, "0");
      sec = (parseInt(diference/10)%60).toString().padStart(2, "0");
      dec = parseInt(diference%10);
      minRender.innerHTML = min;
      secRender.innerHTML = sec;
      decRender.innerHTML = dec;
    }
  };

  setInterval(everyDec, 100);
  let now = 0;
  let diference = 0;
  
  return {
    everyDec,
  }
};

const updateFile = () => {
  const fileInput = document.querySelector('#file-upload input[type=file]');
    fileInput.onchange = () => {
      if (fileInput.files.length > 0) {
        const fileName = document.querySelector('#file-upload .file-name');
        fileName.textContent = fileInput.files[0].name;
        const fileError = document.querySelector('.file-error');
        fileError.textContent = '';
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
  messageContent.textContent = ` - ${text}`
  messagelog.append(prompt, messageContent);
  return messagelog;
}

window.onload = () => {
  updateFile();
  timer();
  send();
};