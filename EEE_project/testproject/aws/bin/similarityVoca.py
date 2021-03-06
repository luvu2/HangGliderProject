# -*- coding:utf-8 -*-
import urllib3
import json
import numpy as np


class SimilarytyWord:
    def __init__(self):
        self.openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/WordRel"
        self.accessKey = "d15d1b57-ecc5-43e3-b0e6-e9200ce7e92c"
        pass

    def similarity_voca(self, w1, w2):

        firstWord = w1
        secondWord = w2

        requestJson = {
            "access_key": self.accessKey,
            "argument": {
                'first_word': firstWord,
                'second_word': secondWord
            }
        }

        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            self.openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)
        )

        return response


    def calc_similarity(self, true_word, ref_word):
        result_sim = []
        for i in range(len(ref_word)):
            response = self.similarity_voca(true_word, ref_word[i])
            response = json.loads(str(response.data, "utf-8"))
            sim = response["return_object"]["WWN WordRelInfo"]["WordRelInfo"]["Similarity"]
            for i in range(len(sim)):
                s = + sim[i]["SimScore"]

            a = s / len(sim)
            result_sim.append(a)
        if max(result_sim) <= 0.0:
            return -1
        return result_sim.index(max(result_sim))

