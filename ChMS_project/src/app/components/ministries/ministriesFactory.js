'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.ministries:ministriesService
 * @description
 * # ministriesSrvc
 * Controller of the appsApp
 */

angular.module('appsApp')
  .factory('ministriesService',function($http){ 
       var ministriesService = {};

      ministriesService.getMinistries = function (){
          return $http({
              withCredentials: true,
              headers: {'Content-Type' : 'application/json'},
              method: 'GET',
              url: 'http://127.0.0.1:8000/api/ministries/'})
                  .success(function(response){
                      return response;
                  })
                  .error(function(err){
                      return err;
                  });
      }

       return ministriesService;
  }); 
