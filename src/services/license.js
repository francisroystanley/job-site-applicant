(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('LicenseSrvc', LicenseService);

  function LicenseService($http) {
    return {
      get: get
    };

    function get(data) {
      if (data && data.id) {
        return $http.get('/api/license/' + data.id, { params: data });
      }
      return $http.get('/api/license', { params: data });
    }
  }
})(angular);
