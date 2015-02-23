#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random


class myApp(webapp.webApp):
    def process(self, parsedRequest):
        rand_num = random.randint(0, 1000000000)

        return ("200 OK", "<html><body>Hola.<a href=" +
                str(rand_num) + "> Dame otra</a></body></html>\r\n")

if __name__ == "__main__":
    testWebApp = myApp("localhost", 1234)
