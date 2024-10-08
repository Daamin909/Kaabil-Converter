const { app, BrowserWindow } = require('electron')
const path = require('path');

const createWindow = () => {
  const { width, height } = require('electron').screen.getPrimaryDisplay().workAreaSize;
  const win = new BrowserWindow({
    width: width,
    height: height,
    autoHideMenuBar: true,
    icon: path.join(__dirname, 'images/android-chrome-512x512.ico'), 
  })

  win.loadURL('http://127.0.0.1:8000');
  win.maximize();
}
app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});