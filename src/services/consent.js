(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('ConsentSrvc', ConsentService);

  function ConsentService($http) {
    return {
      get: get
    };

    function get(data) {
      return $http.get('/api/consent', { params: data });
    }
  }
})(angular);
