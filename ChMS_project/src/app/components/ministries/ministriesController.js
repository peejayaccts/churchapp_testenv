'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.ministries:MinistriesCtrl
 * @description
 * # MinistriesCtrl
 * Controller of the appsApp
 */
angular.module('appsApp')
  .controller('MinistriesCtrl',['$scope','ministriesFactory',
      function ($scope,ministriesFactory) {

          $scope.addStatus;
          $scope.delStatus;
          $scope.searchStatus;
          $scope.ministries;
          $scope.ministry;

          getMinistries();

        function getMinistries(){
              ministriesFactory.getMinistries()
                .then(function(response){
                    $scope.ministries = response.data; 
                },function(error){
                    $scope.status = error.message;
                });
        }

        $scope.searchMinistry = function(){
            var id =  $scope.searchID;
                  ministriesFactory.getMinistry(id)
                    .then(function(response){
                        $scope.searchStatus = response.data; 
                    },function(error){
                        $scope.searchStatus = error.message;
                    });
        }


        $scope.newMinistry = function(){
            var data = { 'name' : $scope.addMinistry};
                 ministriesFactory.insertMinistry(data)
                    .then(function(response){

                      $scope.addStatus= response.data;
                      //fetch all list to table
                      getMinistries();
                    }, 
                    function(error){
                      $scope.addStatus= error.data;
                    });

        }

        $scope.deleteMinistry = function(id){
             ministriesFactory.deleteMinistry(id)
                .then(function(response){
                  $scope.ministry = response.data;
                  getMinistries();
                }, 
                function(error){
                  $scope.status = error;
                });
        }


        $scope.updateModal = function(data){
            $scope.ministryName = data.name;
            $scope.ministryID = data.id;
        }

        $scope.updateMinistry = function(id,name){
            var data  = { id: id, 
                          value : { 
                          'name': name} 
                        };

             ministriesFactory.updateMinistry(data)
                .then(function(response){
                  $scope.ministry = response.data;
                  //fetch all list to table
                  getMinistries();
                }, 
                function(error){
                  $scope.status = error;
                });
        }


      }
  ]);
