// App routing
(function() {

  angular
    .module('ChMS-ui')

    .config(['$routeProvider',
  		function($routeProvider) {
  			var static_dir = 'static/angular-ui/';
  			$routeProvider
  				.when('/', {
  				templateUrl : static_dir.concat('login/login.template.html'),
  				controller : 'LoginController',
  				})
  				.when('/home', {
  					templateUrl : static_dir.concat('home/home.template.html'),
  					controller : 'HomeController'
  				})
  				.when('/login', {
  					templateUrl : static_dir.concat('/login/login.template.html'),
  					controller : 'LoginController'
  				})
  				.when('/people', {
  					templateUrl : static_dir.concat('/people/people.template.html'),
  					controller : 'PeopleController',
            controllerAs : 'peopleCtrl'
  				})
  				.when('/ministries', {
  					templateUrl : static_dir.concat('/ministries/ministries.template.html'),
  					controller : 'MinistriesController'
  				})
  				.when('/admin', {
  					templateUrl : static_dir.concat('/admin/admin.template.html'),
  					controller : 'AdminController'
  				})
  		}

    ]);

}());
