'use strict';

/**
 * @ngdoc function
 * @name appsApp.components.ministries:MinistriesCtrl
 * @description
 * # MinistriesCtrl
 * Controller of the appsApp
 */
angular.module('appsApp')
  .controller('MinistriesCtrl',['$scope', 'coreFactory', '$API',
      function ($scope, coreFactory, $API) {

          var url = $API.ministries;

          $scope.addStatus;
          $scope.delStatus;
          $scope.searchStatus;
          $scope.ministries;
          $scope.ministry;

          getMinistries();

        function getMinistries(){

          coreFactory.getAll(url)
            .then(function (response){
                $scope.ministries = response.data; 
            },
            function (error){
                $scope.status = error.message;
            });
        }

        $scope.searchMinistry = function (){

          var id =  $scope.searchID;

          coreFactory.searchID(url, id)
            .then(function (response){
                $scope.searchStatus = response.data; 
            },
            function (error){
                $scope.searchStatus = error.message;
            });
        }


        $scope.newMinistry = function (){

          var searchCriteria = { 'name' : $scope.addMinistry};

          coreFactory.insert(url, searchCriteria)
             .then(function (response){
                $scope.addStatus= response.data;
                //fetch all list to table
                getMinistries(url);
            }, 
            function (error){
                $scope.addStatus= error.data;
            });
        }

        $scope.deleteMinistry = function (id){

         coreFactory.del(url, id)
            .then(function (response){
               $scope.ministry = response.data;
               //fetch all list to table
               getMinistries(url);
            }, 
            function (error){
               $scope.status = error;
            });
        }


        $scope.updateModal = function (data){
            $scope.ministryName = data.name;
            $scope.ministryID = data.id;
        }

        $scope.updateMinistry = function (id, name){
            var data  = { id: id, 
                          value : { 
                          'name': name} 
                        };

             coreFactory.update(url, data)
                .then(function (response){
                    $scope.ministry = response.data;
                    //fetch all list to table
                    getMinistries(url);
                }, 
                function(error){
                    $scope.status = error;
                });
        }


      }
  ]);
