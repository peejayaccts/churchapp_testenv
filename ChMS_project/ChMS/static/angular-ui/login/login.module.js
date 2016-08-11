// login module
var loginModule = angular.module('LogInModule',[]);

loginModule.controller('LoginController', ['$scope', '$http',
		function($scope, $http) {
			$scope.message = 'You are in the login page!';
		}
]);
