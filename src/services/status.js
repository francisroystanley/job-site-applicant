(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('StatusSrvc', StatusService)
    .factory('StatusActionSrvc', StatusActionService);

  function StatusService($http) {
    return {
      get: get,
      getAction: getAction
    };

    function get(data) {
      if (data && data.id) {
        return $http.get('/api/status/' + data.id, { params: data });
      }
      return $http.get('/api/status', { params: data });
    }

    function getAction(data) {
      if (data && data.id) {
        return $http.get('/api/status/' + data.status_id + '/action/' + data.id, { params: data });
      }
      return $http.get('/api/status/' + data.status_id + '/action', { params: data });
    }
  }

  function StatusActionService($http) {
    return {
      get: get
    };

    function get(data) {
      return $http.get('/api/status_action', { params: data });
    }
  }
})(angular);
