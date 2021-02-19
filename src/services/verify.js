(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('VerifySrvc', VerifyService);

  function VerifyService($http) {
    return {
      verify: verify
    };

    function verify(data) {
      return $http.post('/api/verify', data);
    }

  }
})(angular);
