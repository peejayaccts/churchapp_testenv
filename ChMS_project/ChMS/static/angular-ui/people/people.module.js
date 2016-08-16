// People module

(function() {

  angular
    .module('PeopleModule', [])
  
    .controller('PeopleController', ['$scope', '$http',
      PeopleController
    ]);

  function PeopleController($scope, $http) {
  	$scope.message = 'You are in the People page!';
  };

}());

