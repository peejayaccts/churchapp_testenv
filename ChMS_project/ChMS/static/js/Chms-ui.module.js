var chmsUi = angular.module('Chms-ui', []);

chmsUi.controller('IndexController', ['$scope', '$http',
		function($scope, $http) {
			$scope.churches = [];

			var churchData = {
				'name' : 'New World Order Church',
				'vision' : 'I want to be... the very best.. like no one ever was...',
				'logo' : 'NWO logo',
				'banner': 'NWO banner'
			};

			$http.get('/api/churches', {format : 'json'})
				.then(function(result) {
					console.log(result.data);
					angular.forEach(result.data, function(data) {
						$scope.churches.push(data);
					});
				});

			$scope.addChurch = function(){
				console.log('Added Church');
				console.log(churchData);

				$http.post('/api/churches/', churchData).then(
						function(response) {
							console.log('Success: ' + response.status);
						},
						function(response) {
							console.log('Error: ' + response.status);
							console.log(response.data)
						});
			}
			$scope.deleteChurch = function(){
				console.log('Delete Church');
			}
			$scope.editChurch = function(){
				console.log('Edit Church');
			}
		}
]);
