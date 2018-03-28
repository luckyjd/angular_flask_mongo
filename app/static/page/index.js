var app = angular.module('index_page', []);
app.controller('index_data', function($scope, $http) {
    $http.get('http://127.0.0.1:5000/api/index').then(function(response){
        if (response.data['user'] != None &&  response.data['type'] == 'logged') {
            $scope.username = response.data['user'];
        } else { $scope.username = "No One"; }
    });
});