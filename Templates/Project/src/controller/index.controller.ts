import { Request, Response } from "express";

export const hi = (req: Request, res: Response) => {
    res.send("hello");
};

export const hello = (req: Request, res: Response) => {
    res.send("how's it going?");
};

export const awesome = (req: Request, res: Response) => {
    res.send("EVERYTHING IS AWESOME");
};


export const validatorAndSanitizer = (req: Request, res: Response) => {
    res.status(201).send(`You were sanitized and passed the validator ${req.body.tested_string}`);
};
