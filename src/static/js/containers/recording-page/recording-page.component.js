(function () {

  class RecordingPageController {

    constructor($interval, store, recordingPageActions, networkService) {
      this.store = store;
      this.recordingPageActions = recordingPageActions;
      this.networkService = networkService;

      this.store.subscribe(({ recordingPage }) => {
        this.recordingPage = recordingPage;
      });

      this.networkService
        .getSettings()
        .then(cameraSettings => this.store.dispatch(this.recordingPageActions.setCameraSettings(cameraSettings)));

      const updateStatus = () => {
        this.networkService
          .status()
          .then(({ isUsbConnected, isRecording }) => {
            this.store.dispatch(this.recordingPageActions.setUsbMounted(isUsbConnected));
            this.store.dispatch(
              isRecording
                ? this.recordingPageActions.startRecording()
                : this.recordingPageActions.stopRecording()
            );
          });
      };
      updateStatus();
      $interval(() => updateStatus(), 5000);
    }

    onRecordClick() {
      console.log('onRecordClick()');
      this.store.dispatch(this.recordingPageActions.startRecording());
    }

    onStopClick() {
      console.log('onStopClick()');
      this.store.dispatch(this.recordingPageActions.stopRecording());
    }

    onUnmountClick() {
      console.log('onUnmountClick()');
      this.store.dispatch(this.recordingPageActions.setUsbMounted(false));
    }

    onSettingsSaveClick() {
      console.log('onSettingsSaveClick()');
      const cameraSettingsClone = JSON.parse(JSON.stringify(this.recordingPage.cameraSettings));
      this.networkService
        .patchSettings(cameraSettingsClone)
        .then(() => this.store.dispatch(this.recordingPageActions.setCameraSettings(cameraSettingsClone)));
    }

  }

  RecordingPageController.$inject = ['$interval', 'store', 'recordingPageActions', 'networkService'];

  angular.module('app')
    .component('recordingPage', {
      templateUrl: '/js/containers/recording-page/recording-page.template.html',
      controller: RecordingPageController
    });
})();