(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('RecaptchaSrvc', RecaptchaService);

  function RecaptchaService($http) {
    return {
      get: get,
      save: save
    };

    function get() {
      return $http.get('/api/recaptcha');
    }

    function save(data) {
      return $http.post('/api/recaptcha', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }
})(angular);
