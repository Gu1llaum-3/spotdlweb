function startDownload() {
  var downloadButton = document.getElementById('download-button');
  var downloadLocalButton = document.getElementById('downloadlocal-button');

  if (downloadButton.style.display !== 'none') {
    downloadButton.style.display = 'none';
    downloadLocalButton.style.display = 'block';
  } else {
    downloadButton.style.display = 'block';
    downloadLocalButton.style.display = 'none';
  }

  downloadLocalButton.innerHTML = 'Téléchargement en cours...';
}

function startLocalDownload() {
  var downloadButton = document.getElementById('download-button');
  var downloadLocalButton = document.getElementById('downloadlocal-button');

  if (downloadLocalButton.style.display !== 'none') {
    downloadLocalButton.style.display = 'none';
    downloadButton.style.display = 'block';
  } else {
    downloadLocalButton.style.display = 'block';
    downloadButton.style.display = 'none';
  }

  downloadButton.innerHTML = 'Téléchargement en cours...';
}

function refreshPage() {
  window.location.reload();
  }