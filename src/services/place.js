(function (angular) {
  'use strict';
  angular
    .module('metis')
    .factory('PlaceSrvc', PlaceService);

  function PlaceService($http) {
    return {
      city: city,
      province: province
    };

    function city(data) {
      return $http.get('/api/city', { params: data });
    }

    function province(data) {
      return $http.get('/api/province', { params: data });
    }
  }
})(angular);
