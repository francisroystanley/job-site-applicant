(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('JobAdSrvc', JobAdService)
    .factory('JobAdApplicationSrvc', JobAdApplicationService)
    .factory('JobAdApplicationQuickSrvc', JobAdApplicationQuickService)
    .factory('JobAdSearchTagSrvc', JobAdSearchTagService);

  function JobAdService($http) {
    return {
      get: get
    };

    function get(data) {
      if (data && data.id) {
        return $http.get('/api/job_ad/' + data.id, { params: data });
      } else {
        return $http.get('/api/job_ad', { params: data });
      }
    }
  }

  function JobAdApplicationService($http) {
    return {
      get: get,
      save: save,
      update: update
    };

    function get(data) {
      if (data && data.id) {
        return $http.get('/api/job_ad_application/' + data.id, { params: data });
      } else {
        return $http.get('/api/job_ad_application', { params: data });
      }
    }

    function save(data) {
      return $http.post('/api/job_ad_application', data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/job_ad_application', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function JobAdApplicationQuickService($http) {
    return {
      get: get
    };

    function get(data) {
      return $http.get('/api/job_ad_application_quick', { params: data });
    }
  }

  function JobAdSearchTagService($http) {
    return {
      get: get,
      getTag: getTag
    };

    function get(data) {
      return $http.get('/api/job_ad_search_tag', { params: data });
    }

    function getTag(data) {
      return $http.get('/api/job_ad/' + data.job_ad_id + '/search_tag', { params: data });
    }
  }
})(angular);
