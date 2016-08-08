var chmsUi = angular.module('Chms-ui', []);

chmsUi.controller('IndexController', ['$scope', '$http',
		function($scope, $http) {
			$scope.names = [
				{ name: 'Jon' },
				{ name: 'Pj' },
				{ name: 'Pao' },
				{ name: 'Chan' },
			];
			$scope.churches = [];
			$http.get('http://localhost:8000/api/churches/')
				.then(function(result) {
					// angular.forEach(result.data) {
					// 	// $scope.churches.push()
					// };
				});
		}
]);
