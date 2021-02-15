(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('SignInSrvc', SignInService);

  function SignInService($http) {
    return {
      login: login
    };

    function login(data) {
      return $http.post('/api/login', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }
})(angular);
