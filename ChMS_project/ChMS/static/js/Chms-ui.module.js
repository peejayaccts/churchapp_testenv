var chmsUi = angular.module('Chms-ui', []);

chmsUi.controller('IndexController', ['$scope',
		function($scope) {
			$scope.names = [
				{ name: 'Jon' },
				{ name: 'Pj' },
				{ name: 'Pao' },
				{ name: 'Chan' },
			];
		}
]);
