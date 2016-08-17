// Admin module

(function() {

  angular
    .module('AdminModule', [])
  
    .controller('AdminController', ['$scope', '$http',
      AdminController
    ]);

    function AdminController($scope, $http) {
      $scope.message = 'You are in the Admin page!';
    }

}());

