(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('LinkedInSrvc', LinkedInService);

  function LinkedInService($http) {
    return {
      'request': request
    };

    function request() {
      return $http.get('/auth/linkedin/request');
    }
  }
})(angular);
