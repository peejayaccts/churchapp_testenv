'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:PeopleCtrl
 * @description
 * # PeopleCtrl
 * Controller of the appsApp
 */
angular.module('appsApp')
  .controller('PeopleCtrl',['$scope', 'PeopleFactory',
      function ($scope,PeopleFactory) {


          function getPeople(){
              PeopleFactory.getPeople()
                 .then(function(response){
                     $scope.people = response.data;
                 },
                 function(error){
                     $scope.status = error.data.name;
                 });
          }

          getPeople();

  }]);
