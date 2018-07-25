var app = angular.module('App', ['ngRoute', 'ngCookies']);

const api_log = '/api/log'


app.factory('gitModelLog', function($http) {
    return {
        getLogAll: function(limit, repository) {
            var url = api_log + '/' + limit + '/' + repository;

            return $http.get(url)
                .success(function(data, status, headers, config) {
                    return data;
                });
        },
    };
});

app.controller('gitCtrlLog', function($scope, $cookies, gitModelLog) {
    $scope.repository_buf = $cookies.get('last-repository');
    $scope.repository = "None";

    $scope.registRepository = function() {
        $scope.repository = $scope.repository_buf;
        $cookies.put('last-repository', $scope.repository);
    }

    $scope.updateLogs = function() {
        gitModelLog.getLogAll(0, $scope.repository).then(function(res) {
            $scope.logs = res.data['logs'];
        });
    };

    $scope.sendNortify = function() {

    };

});