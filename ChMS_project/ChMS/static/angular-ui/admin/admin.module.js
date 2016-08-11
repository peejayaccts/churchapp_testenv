var adminModule = angular.module('AdminModule', []);

adminModule.controller('AdminController', ['$scope', '$http',
		function($scope, $http) {
			$scope.message = 'You are in the Admin page!';
		}
]);
