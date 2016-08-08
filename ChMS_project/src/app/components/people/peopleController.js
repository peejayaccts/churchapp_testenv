'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:PeopleCtrl
 * @description
 * # PeopleCtrl
 * Controller of the appsApp
 */
angular.module('appsApp')
  .controller('PeopleCtrl',['$scope','peopleFactory',
      function ($scope,peopleFactory) {

         $scope.people;
         $scope.status;

         getPeople();

         function getPeople(){
             peopleFactory.getPeople()
                .then(function(response){
                  $scope.people = response.data;
                }, 
                function(error){
                  $scope.status = error.data.name;
                });
         }

      }
  ]);
