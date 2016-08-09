var chmsUi = angular.module('Chms-ui', []);

chmsUi.controller('IndexController', ['$scope', '$http',
		function($scope, $http) {
			$scope.churches = [];

			var churchData = {
				name : 'New World Order Church 2',
				vision : 'I want to be... the very best.. like no one ever was...',
				logo : 'NWO logo',
				banner: 'NWO banner',
        regional_info : null
			};

			$http.get('/api/churches', {format : 'json'})
				.then(function(result) {
					console.log(result.data);
					// angular.forEach(result.data, function(data) {
					// 	$scope.churches.push(data);
					// });
					$scope.churches = result.data;
				});

			$scope.addChurch = function(){
				console.log('Added Church');
				console.log(churchData);

				$http.post('/api/churches/', churchData, {format: 'json'})
          .then(
						function(response) {
							console.log('Success: ' + response.status);
              // TODO: Does not update and refresh the ui for the newly added
              // church! Try makeing this into a service. or use $Promise or
              // something
              $http.get('/api/churches', {format : 'json'})
                .then(function(result) {
                  console.log(result.data);
									$scope.churches = result.data
                  // angular.forEach(result.data, function(data) {
                  //   $scope.churches.push(data);
                  // });
                });
						},
						function(response) {
							console.log('Error: ' + response.status);
							console.log(response.data)
						});
			}
			$scope.deleteChurch = function(){
				console.log('Delete Church');
				var church_id = $scope.churches.pop().links['self'];
				$http.delete(church_id,
						{format: 'json'})
					.then(function(response) {
						console.log('Delete Success');
						console.log(response.status);
						console.log(church_id);
					}, function(response) {
						console.log('Delete Failed');
						console.log(response.status);
				});
				
			}
			$scope.editChurch = function(){
				console.log('Edit Church');
			}
		}
]);
