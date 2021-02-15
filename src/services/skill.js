(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('SkillSrvc', SkillService);

  function SkillService($http) {
    return {
      get: get
    };

    function get(data) {
      return $http.get('/api/skill', { params: data });
    }
  }
})(angular);
