'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.ministries:ministriesFactory
 * @description
 * # ministriesSrvc
 * Controller of the appsApp
 */

angular.module('appsApp')
  .factory('ministriesFactory',function($http){ 
       var ministriesFactory = {};

      var apiUrl = 'http://127.0.0.1:8000/api/ministries/';

      var configs = {
              withCredentials: true,
              headers: {'Content-Type' : 'application/json'}
      };

      ministriesFactory.getMinistries = function (){
          return $http({
              url: apiUrl,
              method: 'GET',
              configs
              })
                  .success(function(response){
                      return response;
                  })
                  .error(function(err){
                      return err;
                  });
      }

      ministriesFactory.getMinistry = function (id){
          return $http({
              url: apiUrl + id,
              method: 'GET',
              configs
              })
                  .success(function(response){
                      return response;
                  })
                  .error(function(err){
                      return err;
                  });
      }

      ministriesFactory.insertMinistry = function (data){
          return $http({ 
              url: apiUrl,
              method: 'POST',
              configs,
              data : data 
          })
                  .success(function(response){
                      return response;
                  })
                  .error(function(err){
                      return err;
                  });
      }

      ministriesFactory.deleteMinistry = function (id){
          return $http({ 
              url: apiUrl + id + '/',
              method: 'DELETE',
              configs
          })
                  .success(function(response){
                      return response;
                  })
                  .error(function(err){
                      return err;
                  });
      }

       return ministriesFactory;
  }); 
