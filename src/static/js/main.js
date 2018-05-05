// handlers

function onIncreaseButtonClick() { increase(); }
function onDecreaseButtonClick() { decrease(); }
function onSnapshotButtonClick() { snapshot(); }
function onShowStreamButtonClick() { showStream(); }
function onHideStreamButtonClick() { hideStream(); }
function onSaveSettingsButtonClick() { saveSettings(); }

// controllers

function increase() {
console.log('increase()');
fetch('/increase');
} 
function decrease() {
console.log('decrase()');
fetch('/decrease');
}
function snapshot() {
console.log('snapshot()');
fetch('/snapshot', { method: 'PUT' })
    .then(response => response.json())
    .then(({ filename }) => snapshotShow(filename));
}
function getSettings() {
fetch('/settings')
    .then(response => response.json())
    .then(settings => updateSettings(settings));
}
function saveSettings() {
console.log('saveSettings()');
const shutterSpeedInputElement = document.querySelector('.shutter-speed');
const frameRateInputElement = document.querySelector('.frame-rate');
const isoInputElement = document.querySelector('.iso');

const settings = {
    shutterSpeed: parseInt(shutterSpeedInputElement.value, 10),
    frameRate: parseInt(frameRateInputElement.value, 10),
    iso: parseInt(isoInputElement.value, 10),
};

fetch('/settings', { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(settings) })
    .then(() => console.log('success!!!'));
}

// view manipulators

function snapshotShow(fileName) {
const snapshotContainerElement = document.querySelector('.snapshot-container');
snapshotContainerElement.innerHTML = `<img src="/snapshot/${fileName}" class="snapshot" />`;
}
function snapshotHide() {
const snapshotContainerElement = document.querySelector('.snapshot-container');
snapshotContainerElement.innerHTML = '';
}
function showStream() {
const streamContainerElement = document.querySelector('.stream-container');
streamContainerElement.innerHTML = '<img class="video-stream" src="/video_feed" >';
}
function hideStream() {
const streamContainerElement = document.querySelector('.stream-container');
streamContainerElement.innerHTML = '';
}
function updateSettings(settings) {
const shutterSpeedInputElement = document.querySelector('.shutter-speed');
shutterSpeedInputElement.value = settings.shutterSpeed;

const frameRateInputElement = document.querySelector('.frame-rate');
frameRateInputElement.value = settings.frameRate;

const isoInputElement = document.querySelector('.iso');
isoInputElement.value = settings.iso;
}

function initialize() {
getSettings();
}

initialize();