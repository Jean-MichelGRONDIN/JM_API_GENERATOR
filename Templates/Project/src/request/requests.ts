import { validate } from "indicative/validator";
import { sanitize } from "indicative/sanitizer";
import { NextFunction, Request, Response } from "express";

const messages = {
    required: (field: any) => `${field} is required`,
    alpha_numeric: (field: any) => `${field} contains unallowed characters`,
    alpha: (field: any) => `${field} contains unallowed characters`,
    email: (field: any) => `${field} enter a valid email address`,
    min: (field: any) => `${field} is too short`,
    max: (field: any) => `${field} is too long`,
    string: (field: any) => `${field} must be a string`,
}

export let requestValidator = (rules: any, req: Request, res: Response, next: NextFunction) => {
    validate(req.body, rules, messages)
        .then(() => next())
        .catch((e: Error[]) => res.status(400).json({ status: 400, message: "Bad request, " + e[0].message + ".", data: {} }))
};

export let requestSanitizer = (rules: any, req: Request, res: Response, next: NextFunction) => {
    sanitize(req.body, rules);
    next()
};
