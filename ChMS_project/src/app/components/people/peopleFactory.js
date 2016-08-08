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
      return $http({
          withCredentials: true,
          //headers: {'Content-Type': 'application/json; charset=uft-8'},
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          method: 'GET',
          /*dataType: 'jsonp',*/
          url: 'http://127.0.0.1:8000/api/people/?format=json'})
          /*url: 'http://127.0.0.1:8000/api/people/'})*/
          /*url: 'http://www.pinoymountaineer.com/api/get_recent_posts/'})*/
              .success(function(data){
                  return data;
              })
              .error(function(err){
                  return err;
              });
  }]); 
