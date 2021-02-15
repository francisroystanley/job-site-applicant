(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('OrganizationJobtitleSrvc', OrganizationJobtitleService);

  function OrganizationJobtitleService($http) {
    return {
      get: get
    };

    function get(data) {
      return $http.get('/api/organization/jobtitle/' + data.id);
    }
  }
})(angular);
