'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.core:coreFactory
 * @description
 * # coreSrvc
 * Controller of the appsApp
 */

angular.module('appsApp')
  .factory('coreFactory',['$http','$API','$HTTP', function ($http, $API, $HTTP){ 
      var coreFactory = {};

      coreFactory.getAll = function (url){
          return $http({
              url    : url,
              method : 'GET',
              params : $HTTP.fields 
              })
                  .success(function (data, status, headers, config){
                      return data;
                  })
                  .error(function (err){
                      return err;
                  });
      }

      coreFactory.searchID = function (url, id){
          return $http({
              url    : url + id + '/',
              method : 'GET',
              params : $HTTP.fields 
              })
                  .success(function (data, status, headers, config){
                      return data;
                  })
                  .error(function (err){
                      return err;
                  });
      }

      coreFactory.insert = function (url, searchCriteria){
          return $http({ 
              url    : url,
              method : 'POST',
              params : $HTTP.fields,
              data   : searchCriteria 
          })
                  .success(function (data, status, headers, config){
                      return data;
                  })
                  .error(function (err){
                      return err;
                  });
      }

      coreFactory.del = function (url, id){
          return $http({ 
              url    : url + id + '/',
              method : 'DELETE',
              params : $HTTP.fields
          })
                  .success(function (data, status, headers, config){
                      return data;
                  })
                  .error(function (err){
                      return err;
                  });
      }

      coreFactory.update = function(url,data){

          return $http({ 
              url    : url + data.id + '/', 
              method : 'PATCH',
              params : $HTTP.fields,
              data   : data.value 
          })
                  .success(function (data, status, headers, config){
                      return data;
                  })
                  .error(function (err){
                      return err;
                  });
      }

      return coreFactory;
  }]); 
