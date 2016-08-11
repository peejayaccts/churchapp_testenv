var peopleModule = angular.module('PeopleModule', []);

peopleModule.controller('PeopleController', ['$scope', '$http',
		function($scope, $http) {
			$scope.message = 'You are in the People page!';
		}
]);
