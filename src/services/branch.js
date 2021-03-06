(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('BranchSrvc', BranchService);

  function BranchService($http) {
    return {
      get: get
    };

    function get(data) {
      return $http.get('/api/branch', { params: data });
    }
  }
})(angular);
