import { requestValidator } from '../requests';
import { NextFunction, Request, Response } from "express";

export let validatorAndSanitizerRequest = (req: Request, res: Response, next: NextFunction) => {
    const request = {
        tested_string: 'required|string',
    }

    requestValidator(request, req, res, next);
};