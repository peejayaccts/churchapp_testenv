// Home module
var homeModule = angular.module('HomeModule', []);

homeModule.controller('HomeController', ['$scope', '$http',
		function($scope, $http) {
			$scope.message = 'You are in the Home page!';
		}
]);
