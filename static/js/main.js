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

    $scope.last_hash = null;

    $scope.choiceRepository = function() {
        $scope.repository = $scope.repository_buf;
        $cookies.put('last-repository', $scope.repository);
        $scope.updateLogs();
    }

    $scope.updateLogs = function() {
        gitModelLog.getLogAll(0, $scope.repository).then(function(res) {
            $scope.logs = res.data['logs'];

            if ($scope.last_hash !== null && $scope.last_hash == res.data['hash']) {
                var notify_opt = {
                    body: res.data['author'] + "\n" + res.data['message']
                };
                var notification = new Notification("新着コミット ", notify_opt);

            }

            $scope.last_hash = res.data['hash'];
            console.log($scope.last_hash);
        });
    };


});