(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('ForgotPasswordSrvc', ForgotPasswordService);

  function ForgotPasswordService($http) {
    return {
      save: save
    };

    function save(data) {
      return $http.post('/api/forgotpassword', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }
})(angular);
