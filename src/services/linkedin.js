(function (angular) {
  'use strict';
  angular
    .module('metis')
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
