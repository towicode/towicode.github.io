'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope', function($scope) {


	var i = 0;
	var j = 0;
	//$scope = this;
	$scope.parsed = true;
	$scope.script = 'paste your script here';
	$scope.currentLine = "";
	$scope.arrScript = [];
	$scope.finished_script = "";


	$scope.parse = function(){

		//console.log($scope.script);
		$scope.s = $scope.script.split("\n");
		$scope.f = [];
		//console.log($scope.s);
		continueParsing();

		console.log($scope.f);

		var m = "";
		$scope.parsed = false;
		$scope.next();
	};

	var continueParsing = function(){

		if (i >= $scope.s.length)
			return;
		while (!contains($scope.s[i], "\"")){
			console.log("inloop");
			var line = $scope.s[i];
			if (line == undefined)
				return;
			if (line == ""){
				i++;
				if (i >= $scope.s.length)
					return;
				continue;
			}
			if (i >= $scope.s.length)
					return;

			$scope.f.push("\"" + line + "\"");
			i++;
		}

		var line = $scope.s[i];
		var split = line.split('"');
		var first = false;
		var narr = true;
		if(split[0] == ""){
			first = true;
			narr = false
		}

		for (var go = 0; go < split.length; go++){
			if (narr){
				if (split[go] == "")
					continue;
				$scope.f.push("\"" + split[go].trim() + "\"");
			}
			else {
				if (split[go] =="")
					continue;
				$scope.f.push("%ACTOR%" + " \"" + split[go].trim() + "\"")
			}
			narr = !narr;

		}
		i++;
		continueParsing();

	}

	$scope.next = function(joke){
		if (joke != undefined){
			$scope.f[j] = $scope.f[j].replace("%ACTOR%", joke);
			if ($scope.f[j] != undefined)
				$scope.addToScript($scope.f[j]);
			j++;
		}
		while (!contains($scope.f[j], "%ACTOR%")){
			if ($scope.f[j] == undefined)
				return;
			$scope.addToScript($scope.f[j]);
			j++;
		}
		var lo = $scope.f[j];
		if ($scope.f[j-1] != undefined)
			$scope.prevLine = $scope.f[j-1];
		else
			$scope.f[j-1] = "";

		if ($scope.f[j+1] != undefined)
			$scope.nextLine = $scope.f[j+1];
		else
			$scope.f[j+1] = "";
		
		$scope.currentLine = lo;
	}

	$scope.addToScript = function(mmm){
		$scope.finished_script += mmm + "\n";
	}


	$scope.previous = function(){

	}


	var contains = function(string, x){
		if (string == undefined)
			return false;
		if(string.indexOf(x) > -1 || string.indexOf("”") > -1)
			{
			return true;
			}
			return false;
	}

}]);