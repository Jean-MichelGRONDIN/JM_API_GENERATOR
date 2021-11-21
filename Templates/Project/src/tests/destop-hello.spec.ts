// import app from "../app";
import * as chai from "chai";
import chaiHttp from "chai-http";
import {expect, request} from 'chai';
import {Response} from 'superagent';

import "mocha";
import API_APPINESS from "../config/config";

chai.use(chaiHttp);

describe(`Hello API Request on ${process.env.API_PORT} ${API_APPINESS.API.getInstance().SSL ? "https://" : "http://"}${API_APPINESS.API.getInstance().Domain}:${API_APPINESS.API.getInstance().Port}`, () => {
    it("should return how's it going? on call", async() => {
        const res: Response =  await request(`${API_APPINESS.API.getInstance().SSL ? "https://" : "http://"}${API_APPINESS.API.getInstance().Domain}:${API_APPINESS.API.getInstance().Port}`).get(`/desktop/hello`);
        console.log(res.text);
        expect(res).to.have.status(200);
        expect(res.text).to.eql("how's it going?");
    });
});

describe(`Test request's validator and sanitizer route`, () => {
    it("work", async() => {
        let arg = 'test string that work for the validator';
        const res: Response =  await request(`${API_APPINESS.API.getInstance().SSL ? "https://" : "http://"}${API_APPINESS.API.getInstance().Domain}:${API_APPINESS.API.getInstance().Port}`)
            .post(`/testValidatorAndSanitizer`).type('form').send({
                tested_string: arg
            });
        expect(res).to.have.status(201);
        expect(res.text).to.eql(`You were sanitized and passed the validator ${arg}`);
    });
    it("work and the string was sanitized", async() => {
        let arg = '<script>test string that work for the validator</script>';
        let argSanitized = 'test string that work for the validator';
        const res: Response =  await request(`${API_APPINESS.API.getInstance().SSL ? "https://" : "http://"}${API_APPINESS.API.getInstance().Domain}:${API_APPINESS.API.getInstance().Port}`)
            .post(`/testValidatorAndSanitizer`).type('form').send({
                tested_string: arg
            });
        expect(res).to.have.status(201);
        expect(res.text).to.eql(`You were sanitized and passed the validator ${argSanitized}`);
    });
    it("doesn\'t work, missing body arg", async() => {
        const res: Response = await request(`${API_APPINESS.API.getInstance().SSL ? "https://" : "http://"}${API_APPINESS.API.getInstance().Domain}:${API_APPINESS.API.getInstance().Port}`)
            .post(`/testValidatorAndSanitizer`).type('form').send({});
        expect(res).to.have.status(400);
        expect(res.body).to.have.property('message');
        expect(res.body.message).to.eql("Bad request, tested_string is required.");
    });
});
