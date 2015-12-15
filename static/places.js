angular.module('getAhead',[]);

angular.module('getAhead').controller('MainController', function($scope, $http) {

	$scope.f = {name:"",col:""};

	$scope.o1 = {name:"",col:""};

	$scope.o2 = {name:"",col:""};

	$scope.families = ['1 Adult', '1 Adult + 1 Child', '1 Adult + 2 Children', '1 Adult + 3 Children', '2 Adults (One Working)',
       				'2 Adults (One Working) + 1 Child', '2 Adults (One Working) + 2 Children', '2 Adults (One Working) + 3 Children',
       				'2 Adults', '2 Adults + 1 Child', '2 Adults + 2 Children', '2 Adults + 3 Children'];

	$scope.occupations = ['Management', 'Business & Financial Operations', 'Computer & Mathematical', 'Architecture & Engineering',
     'Life, Physical, & Social Science', 'Community & Social Service', 'Legal', 'Education, Training, & Library',
     'Arts, Design, Entertainment, Sports, & Media', 'Healthcare Practitioners & Technical', 'Healthcare Support',
     'Protective Service', 'Food Preparation & Serving Related', 'Building & Grounds Cleaning & Maintenance',
		 'Personal Care & Service', 'Sales & Related', 'Office & Administrative Support', 'Farming, Fishing, & Forestry',
		 'Construction & Extraction', 'Installation, Maintenance, & Repair', 'Production', 'Transportation & Material Moving'];

	$scope.places = [];

	for (var i = 0; i < 20; i++) {
		$scope.places.push({site:'.',state:'.',dollars:'.'});
		};

	$scope.oneAdult = function() {
		return $scope.f.col < 'i';
	};

	$scope.mapInd = function(i) {
		return String.fromCharCode(97+i);
	};

	$scope.postReady = function() {
		if (!$scope.f.name.length || !$scope.o1.name.length) {return};
		if ($scope.oneAdult()) {
			$http.post('/data',{f:$scope.f.col, o1:$scope.o1.col}).success(function(data) {
				$scope.places = data;
			});
		} else if ($scope.o2.name.length) {
			$http.post('/data',{f:$scope.f.col, o1:$scope.o1.col, o2:$scope.o2.col}).success(function(data) {
				$scope.places = data;
			});
		};
	};
});