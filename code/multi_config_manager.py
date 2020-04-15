#!/usr/bin/env python3
#allows to read input (feedback) from robots (i.e. a client for API running on robot)
#uses a Docker client to communicate with a Docker server

#DESCRIPTION:
#This file is part of the remote controller that needs to be set up in dt-town-interface

import yaml
import docker
import os
import git
import glob
import numpy as np

#Import from base image dt-commons
from dt_class_utils import DTProcess #only if code incl. running, e.g. API, ...
from dt_town_interface_utils import multiArchAPIClient as multi


class multiConfiguration:
    def __init__(self):

        if os.path.isfile("some/directory/where/desired/robot/hostnames/are/stored"):
            self.available_robots = open("directory/robot/hostnames/for/this/exercise").readline()
        else:
            self.available_robots = open("default/directory/robot/hostnames").readline()

        self.robot = []
        for i in len(available_robots):
            self.robot(i) = available_robots(i) #used as input for multiArchAPIClient?

            #else do self.robot(i) = multiArchAPIClient(available_robots(i))

        #specify/import variables unknown from library (robots, types, docker.client.swarm)
        self.robot_type = "unknown"
        self.robot_name = os.environ['VEHICLE_NAME']

        self.docker_client =  docker.DockerClient(base_url='unix://var/run/docker.sock')
        self.active_config = None
        self.config_path = None
        self.module_path = "/data/assets/dt-architecture-data/modules/"
        self.current_configuration = "none"
        self.dt_version = "ente"

        self.robot = multi.get_robot_list
        self.robot_type = multi.get_robot_type_list
        self.robot_count = multi.get_robot_count


    def endpoint_1(self):
        self.docker_client.configs = 'something'

    def endpoint_2(self):
        self.docker_client.configs = 'something'

    def status(self):
        for i in [0, self.robot_count]:
            if self.status[i] == 'something':
                return 'single ok'
            else:
                return 'single NOT ok --> send error msg'
