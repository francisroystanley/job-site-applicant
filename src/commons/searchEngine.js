import PropTypes from 'prop-types';
import { useState } from 'react';


const SearchEngine = props => {
  // vm.enable_department = env.department_01;
  const [entities, SetEntities] = useState([{ code: 'ALL', name: 'All' }]);
  // vm.env = env.client_code;
  const isCareer = window.location.pathname.includes('career');
  const [jobAds, setJobAds] = useState([]);
  const [jobClass, setJobClass] = useState([]);
  const [pageitem, setPageItem] = useState(JSON.parse(sessionStorage.getItem("JobAdSearchPage")) || {});
  const [param, setParam] = useState({});
  const [provinces, setProvinces] = useState([]);

  const changeJobTitle = () => {

  };

  const changeProvince = () => {

  };

  const getProvince = () => {

  };

  const searchViaBusinessUnit = () => {

  };

  const searchViaJobClass = () => {

  };

  const searchJobAd = () => {

  };

  return (
    <div className="px-2 px-md-1 px-lg-2 px-xl-5">
      <div id="advanced-search" className="advanced-search wow fadeInUp"
        // ng-class="{'open': search_engine.is_search_open}"
        data-wow-delay="0.2s">
        <form className="d-md-flex"
        // ng-submit="search_engine.searchJobAd(search_engine.search)"
        >
          <div className="departmentWrap"
          // ng-if="search_engine.enable_department"
          >
            <button id="departmentButton" className="btn btn-outline departmentButton dropdown-toggle mega-dropdown" type="button" aria-haspopup="true" aria-expanded="false"
            // ng-click="search_engine.is_search_open=!search_engine.is_search_open"
            >
              <span className="departmentName"
              // ng-bind="search_engine.param.entity.name"
              ></span>
            </button>
            <div id="departmentList" className="departmentList dropdown-menu w-100"
            // ng-class="{'show': search_engine.is_search_open}"
            >
              <div className="container-fluid">
                <div className="row overflow-auto">
                  <div className="departmentList-parentList col-5 col-sm-4 col-md-3 pl-3 pr-2 pb-2">
                    <div className="d-block nav nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                      <a className="nav-link pointer px-0 text-truncate"
                        // ng-class="{'active': search_engine.param.entity.code == entity.code}"
                        id="v-pills-tab-{{$index}}" data-toggle="pill" role="tab" aria-controls="v-pills-{{$index}}"
                      // ng-click="search_engine.searchViaBusinessUnit(entity, search_engine.search)"
                      // ng-repeat="entity in search_engine.entities"
                      // ng-bind="entity.name"
                      ></a>
                    </div>
                  </div>
                  <div className="departmentList-childrenList col-7 col-sm-8 col-md-9 pt-4 pb-2 px-2">
                    <div className="tab-content" id="v-pills-tabContent">
                      <div className="tab-pane fade active show" id="v-pills-0" role="tabpanel" aria-labelledby="v-pills-tab-0">
                        <div className="row">
                          <ul className="col-md-6 col-lg-4 col-xl-3"
                          // ng-repeat="job_class in search_engine.job_class"
                          >
                            <li>
                              <a className="pt-0 text-truncate" href=""
                              // ng-bind="job_class.job_class_name"
                              // ng-click="search_engine.searchViaJobClass(job_class)"
                              ></a>
                            </li>
                          </ul>
                          <ul className="col-md-12">
                            <li><a className="pt-0" href="/career/search">All Jobs</a></li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="input-group form-control-wrap mt-lg-3 px-md-1 px-lg-0 px-xl-3 align-items-center"
          // ng-class="!search_engine.enable_department && 'border-0'"
          >
            <input type="text" className="form-control" placeholder="Search job title or keywords"
            // ng-model="search_engine.param.job_title"
            // ng-change="search_engine.changeJobTitle()"
            />
          </div>
          <div className="input-group form-control-wrap pl-2 align-items-center">
            <div className="input-group-prepend inputIcon">
              <span className="input-group-text px-1 py-0 mr-2">
                <i className="fas fa-map-marker-alt"></i>
              </span>
            </div>
            <input type="text" className="form-control mt-lg-1 mt-0"
              // ng-model="search_engine.param.province"
              // uib-typeahead="province as province.province_name for province in search_engine.getProvince($viewValue)" typeahead-on-select="search_engine.changeProvince(search_engine.param.province)" typeahead-editable="false"
              className="form-control input-no-border"
              // typeahead-min-length="1"
              autoComplete="off" />
          </div>
          <button className="btn btn-secondary advancedSearchButton" type="submit">
            <i className="fas fa-search"></i>
            <span className="d-md-none">Search</span>
          </button>
        </form>
      </div>
    </div>
  );
};

SearchEngine.propTypes = {};

export default SearchEngine;
