(function () {

  const SETTINGS_PATH = '/settings';
  const INSCREASE_PATH = '/increase';
  const DECREASE_PATH = '/decrease';
  const RECORDING_PATH = '/recording';

  class NetworkService {

    constructor($http) {
      this.$http = $http;

    }

    recordingStart() {
      const options = {
        method: 'GET',
        url: RECORDING_PATH + '/start',
      };
      return this
        .$http(options)
        .then(response => response.data);
    }

    recordingEnd() {
      const options = {
        method: 'GET',
        url: RECORDING_PATH + '/stop',
      };
      return this
        .$http(options)
        .then(response => response.data);
    }

    status() {
      const options = {
        method: 'GET',
        url: '/status',
      };
      return this
        .$http(options)
        .then(response => response.data);
    }

    increase() {
      const options = {
        method: 'GET',
        url: INSCREASE_PATH,
      };
      return this
        .$http(options)
        .then(response => response.data);
    }

    decrease() {
      const options = {
        method: 'GET',
        url: DECREASE_PATH,
      };
      return this
        .$http(options)
        .then(response => response.data);
    }

    getSettings() {
      const options = {
        method: 'GET',
        url: SETTINGS_PATH,
      };
      return this
        .$http(options)
        .then(response => response.data);
    }

    patchSettings(settings) {
      const options = {
        method: 'POST',
        url: SETTINGS_PATH,
        data: settings,
      };
      return this
        .$http(options)
        .then(response => response.data);
    }

  }

  NetworkService.$inject = ['$http'];

  angular.module('app').service('networkService', NetworkService);

})();