// login module

(function() {

  angular
    .module('LogInModule',[])
  
    .controller('LoginController', ['$scope', '$http', '$window',
      LoginController
    ]);

    function LoginController($scope, $http, $window) {
      $scope.message = 'You are in the login page!';
      //$scope.user = {username: 'demo', password: 'demodemos'};
      $scope.message = '';
      $scope.submit = function () {
	  $http
	      .post(app.apiLogin, $scope.user)
	      .success(function (data, status, headers, config) {
		  $window.sessionStorage.token = data.token;
		  //console.log(data.token);
		  $scope.message = 'Welcome';
		  //console.log("Welcome");
		  alert('Welcome');
	      })
	      .error(function (data, status, headers, config) {
		  // Erase the token if the user fails to log in
		  delete $window.sessionStorage.token;

		  // Handle login errors here
		  $scope.message = 'Error: Invalid user or password';
		  //console.log("Error");
		  alert("Invalid credentials");
	      });
      };
  };

}());

