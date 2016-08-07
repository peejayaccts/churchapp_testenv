'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:PeopleCtrl
 * @description
 * # PeopleCtrl
 * Controller of the appsApp
 */
angular.module('appsApp')
  .controller('PeopleCtrl',['$scope','dataFactory',
      function ($scope,dataFactory) {
          dataFactory.success(function(data){
              $scope.people = data;
          })
  /*.controller('PeopleCtrl',['$scope',
              function ($scope) {*/

          /*$scope.people;

          getPeople();

          function getPeople(){
              dataFactory.getPeople()
                  .then(function(response){
                      $scope.people = response;
              }), function (error){
                      $scope.status = 'error'; 
              }
          }*/
          /*$scope.people = 'test';*/

      }
  ]);
