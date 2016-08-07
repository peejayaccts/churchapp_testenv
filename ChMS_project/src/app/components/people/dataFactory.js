'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:dataFactory
 * @description
 * # PeopleSrvc
 * Controller of the appsApp
 */

angular.module('appsApp')
  .factory('dataFactory',['$http',function($http){ 
      /*return $http.get('http://127.0.0.1:8000/api/people/?format=json')*/
      return $http({
          withCredentials: true,
          headers: {'Content-Type': 'application/json; charset=uft-8'},
          method: 'GET',
          url: 'http://127.0.0.1:8000/api/people/?format=json'})
                  .success(function(data){
                      return data;
                  })
                  .error(function(err){
                      return err;
                  });
       /*var url = 'http://127.0.0.1:8000/api/people/?format=json';
       var dataFactory = {};

       dataFactory.getPeople = function (){
           return $http.get(url);
       }
       return dataFactory;*/
  }]); 
