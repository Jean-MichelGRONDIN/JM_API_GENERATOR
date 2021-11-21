import { requestSanitizer } from '../requests';
import { NextFunction, Request, Response } from "express";

export let validatorAndSanitizerSanitizer = (req: Request, res: Response, next: NextFunction) => {
    const rules = {
        tested_string: 'strip_tags',
    }

    requestSanitizer(rules, req, res, next);
};
