(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('JobClassSrvc', JobClassService);

  function JobClassService($http) {
    return {
      get: get
    };

    function get(data) {
      return $http.get('/api/job_class', { params: data });
    }
  }
})(angular);
