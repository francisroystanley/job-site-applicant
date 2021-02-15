(function(angular) {
  'use strict';
  angular
    .module('metis')
    .factory('UserSrvc', UserService)
    .factory('UserPhotoSrvc', UserPhotoService);

  function UserService($http) {
    var headers = { 'Content-Type': 'application/json' };
    return {
      changePassword: changePassword,
      getParams: getParams,
      getMe: getMe,
      locationGet: locationGet,
      loginStatus: loginStatus,
      me: me,
      save: save,
      setParams: setParams,
      setPassword: setPassword
    };

    function changePassword(data) {
      return $http.patch('/api/user/change_password', data, { headers: headers });
    }

    function getMe(data) {
      return $http.get('/api/me', { params: data });
    }

    function getParams(data) {
      return $http.get('/api/user/' + data.uuid + '/parameters', { params: data });
    }

    function locationGet() {
      return $http.get('/api/location');
    }

    function loginStatus() {
      return $http.get('/api/login_status');
    }

    function me(data) {
      return $http.get('/api/user/me', { params: data });
    }

    function save(data) {
      return $http.post('/api/user', data, { headers: headers });
    }

    function setParams(data) {
      return $http.patch('/api/user/' + data.uuid + '/parameters', data, { headers: headers });
    }

    function setPassword(data) {
      return $http.post('/api/user/' + data.uuid + '/password', data, { headers: headers });
    }
  }

  function UserPhotoService($http) {
    var headers = { 'Content-Type': 'application/json' };
    return {
      get: get,
      save: save,
    };

    function get(data) {
      return $http.get('/api/user/' + data.id + '/photo');
    }

    function save(data) {
      return $http.post('/api/user/' + data.id + '/photo', data, { headers: headers });
    }
  }
})(angular);
