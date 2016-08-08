'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:peopleFactory
 * @description
 * # PeopleSrvc
 * Controller of the appsApp
 */

angular.module('appsApp')
  .factory('peopleFactory',['$http',function($http){ 

      var peopleFactory = {};

      peopleFactory.getPeople = function (){
          return $http({
              withCredentials: true,
              headers: {'Content-Type' : 'application/json'},
              method: 'GET',
              url: 'http://127.0.0.1:8000/api/people/'})
                  .success(function(response){
                      return response;
                  })
                  .error(function(err){
                      return err;
                  });
      }

      peopleFactory.insertPeople = function (){
          return $http({
              withCredentials: true,
              headers: {'Content-Type' : 'application/json'},
              method: 'POST',
              data: { "name" : "xxxFFFFFFFFFeeeFFFFF"},
              url: 'http://127.0.0.1:8000/api/spiritual_milestones/'})
                  .success(function(response){
                      return response;
                  })
                  .error(function(err){
                      console.log(err);
                      return err;
                  });
      }

      return peopleFactory;

  }]); 
