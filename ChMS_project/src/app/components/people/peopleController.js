'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:PeopleCtrl
 * @description
 * # PeopleCtrl
 * Controller of the appsApp
 */
angular.module('appsApp')
  /*.controller('PeopleCtrl',['$scope','peopleService',
      function ($scope,peopleService) {*/
  .controller('PeopleCtrl',['$scope','peopleFactory',
      function ($scope,peopleFactory) {

         $scope.people;
         $scope.status;

         /*$scope.people = peopleService.query();*/

         /*getPeople();*/
         insertPeople();

         function getPeople(){
             peopleFactory.getPeople()
                .then(function(response){
                    console.log(response.data[0].name)
                  $scope.people = response.data;
                }, 
                function(error){
                });
         }

         function insertPeople(){
             peopleFactory.insertPeople()
                .then(function(response){
                  $scope.people = response.data;
                }, 
                function(error){
                });
         }


      }
  ]);
