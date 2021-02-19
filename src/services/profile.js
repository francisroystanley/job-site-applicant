(function (angular) {
  'use strict';
  angular
    .module('ponos')
    .factory('ProfileSrvc', ProfileService)
    .factory('ProfilePersonSrvc', ProfilePersonService)
    .factory('ProfilePersonAffiliationSrvc', ProfilePersonAffiliationService)
    .factory('ProfilePersonAttachmentSrvc', ProfilePersonAttachmentService)
    .factory('ProfilePersonCertificateSrvc', ProfilePersonCertificateService)
    .factory('ProfilePersonConsentSrvc', ProfilePersonConsentService)
    .factory('ProfilePersonDetailSrvc', ProfilePersonDetailService)
    .factory('ProfilePersonEducationSrvc', ProfilePersonEducationService)
    .factory('ProfilePersonIdentificationSrvc', ProfilePersonIdentificationService)
    .factory('ProfilePersonLicenseSrvc', ProfilePersonLicenseService)
    .factory('ProfilePersonPortfolioSrvc', ProfilePersonPortfolioService)
    .factory('ProfilePersonPreferenceSrvc', ProfilePersonPreferenceService)
    .factory('ProfilePersonSkillSrvc', ProfilePersonSkillService)
    .factory('ProfilePersonSocialLinksSrvc', ProfilePersonSocialLinksService)
    .factory('ProfilePersonTrainingSrvc', ProfilePersonTrainingService)
    .factory('ProfilePersonWorkHistorySrvc', ProfilePersonWorkHistoryService);

  function ProfileService($http) {
    return {
      citizenship: citizenship,
      religion: religion
    };

    function citizenship(data) {
      return $http.get('/api/citizenship', { params: data });
    }

    function religion(data) {
      return $http.get('/api/religion', { params: data });
    }
  }

  function ProfilePersonService($http) {
    return {
      get: get,
      update: update
    };

    function get(data) {
      return $http.get('/api/person', { params: data });
    }

    function update(data) {
      return $http.patch('/api/person', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonAffiliationService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_affiliation', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_affiliation/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_affiliation/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_affiliation', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonAttachmentService($http) {
    return {
      get: get,
      remove: remove,
      save: save,
      update: update
    };

    function get(data) {
      return $http.get('/api/person_attachment', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_attachment/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_attachment', data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_attachment/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonCertificateService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_certificate', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_certificate/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_certificate/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_certificate', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonConsentService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_consent', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_consent/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_consent/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_consent', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonDetailService($http) {
    return {
      get: get,
      save: save,
      remove: remove
    };

    function get(data) {
      return $http.get('/api/person_detail', { params: data });
    }

    function save(data) {
      return $http.post('/api/person_detail', data, { headers: { 'Content-Type': 'application/json' } });
    }

    function remove(data) {
      return $http.delete('/api/person_detail/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonEducationService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_education', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_education/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_education/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_education', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonIdentificationService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_identification', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_identification/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_identification/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_identification', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonLicenseService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_license', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_license/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_license/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_license', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonPortfolioService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_portfolio', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_portfolio/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_portfolio/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_portfolio', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonPreferenceService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_preference', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_preference/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_preference/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_preference', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonSkillService($http) {
    return {
      get: get,
      save: save,
      remove: remove
    };

    function get(data) {
      return $http.get('/api/person_skill', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_skill/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_skill', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonSocialLinksService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_social_link', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_social_link/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_social_link/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_social_link', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonTrainingService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_training', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_training/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_training/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_training', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }

  function ProfilePersonWorkHistoryService($http) {
    return {
      get: get,
      remove: remove,
      update: update,
      save: save
    };

    function get(data) {
      return $http.get('/api/person_work_history', { params: data });
    }

    function remove(data) {
      return $http.delete('/api/person_work_history/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function update(data) {
      return $http.patch('/api/person_work_history/' + data.id, data, { headers: { 'Content-Type': 'application/json' } });
    }

    function save(data) {
      return $http.post('/api/person_work_history', data, { headers: { 'Content-Type': 'application/json' } });
    }
  }
})(angular);
