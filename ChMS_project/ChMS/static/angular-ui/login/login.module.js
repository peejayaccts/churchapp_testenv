// login module

(function() {

  angular
    .module('LogInModule',[])
  
    .controller('LoginController', ['$scope', '$http',
      LoginController
    ]);

  function LoginController($scope, $http) {
  	$scope.message = 'You are in the login page!';
  };

}());

