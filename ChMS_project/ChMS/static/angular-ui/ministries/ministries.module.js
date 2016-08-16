// Ministries module

(function() {

  angular
    .module('MinistriesModule', [])
  
    .controller('MinistriesController', ['$scope', '$http',
      MinistriesController
    ]);

  function MinistriesController($scope, $http) {
  	$scope.message = 'You are in the Ministries page!';
  };

}());

