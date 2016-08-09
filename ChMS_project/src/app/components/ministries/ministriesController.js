'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.people:MinistriesCtrl
 * @description
 * # MinistriesCtrl
 * Controller of the appsApp
 */
angular.module('appsApp')
  .controller('MinistriesCtrl',['$scope','ministriesService',
      function ($scope,ministriesService) {

          $scope.status;
          $scope.ministries;

          getMinistries();

          function getMinistries(){
              ministriesService.getMinistries()
                .then(function(response){
                    $scope.ministries = response.data; 
                },function(error){
                    $scope.status = error.message;
                });
          }



      }
  ]);
