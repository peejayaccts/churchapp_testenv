var ministriesModule = angular.module('MinistriesModule', []);

ministriesModule.controller('MinistriesController', ['$scope', '$http',
		function($scope, $http) {
			$scope.message = 'You are in the Ministries page!';
		}
]);
