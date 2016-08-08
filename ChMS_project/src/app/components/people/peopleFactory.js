'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:peopleFactory
 * @description
 * # PeopleFactory
 * Controller of the appsApp
 */

angular.module('appsApp')
  .factory('peopleFactory',['$http',function($http){ 

      var peopleFactory = {};
      var apiUrl = 'http://127.0.0.1:8000/api/spiritual_milestones/';

      var configs = {
              withCredentials: true,
              headers: {'Content-Type' : 'application/json'}
      };


      peopleFactory.getPeople = function (){
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


      return peopleFactory;

  }]); 
