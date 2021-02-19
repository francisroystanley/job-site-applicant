(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('RequestSrvc', RequestService);

  function RequestService($http) {
    return {
      save: save
    };

    function save(data) {
      return $http.post('/api/request/purge_person', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }
})(angular);
