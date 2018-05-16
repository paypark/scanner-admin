(function () {

  class RecordingPageActions {

    constructor() {
      this.START_RECORDING = 'RECORDING_PAGE_START_RECORDING';
      this.STOP_RECORDING = 'RECORDING_PAGE_STOP_RECORDING';
      this.SET_USB_MOUNTED = 'RECORDING_PAGE_SET_USB_MOUNTED';
      this.SET_CAMERA_SETTINGS = 'RECORDING_PAGE_SET_CAMERA_SETTINGS';
      this.SET_SHOW_STREAM = 'RECORDING_PAGE_SET_SHOW_STREAM';
    }

    startRecording() {
      return {
        type: this.START_RECORDING,
        payload: null,
      };
    }

    stopRecording() {
      return {
        type: this.STOP_RECORDING,
        payload: null,
      };
    }

    setUsbMounted(isUsbMounted) {
      return {
        type: this.SET_USB_MOUNTED,
        payload: { isUsbMounted, },
      };
    }

    setCameraSettings(cameraSettings) {
      return {
        type: this.SET_CAMERA_SETTINGS,
        payload: { cameraSettings, },
      };
    }

    setShowStream(isStreamShowing) {
      return {
        type: this.SET_SHOW_STREAM,
        payload: { isStreamShowing, },
      }
    }

  }

  angular.module('app').service('recordingPageActions', RecordingPageActions);

})();