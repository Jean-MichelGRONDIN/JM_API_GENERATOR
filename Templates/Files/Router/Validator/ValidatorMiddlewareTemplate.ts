export let $VALIDATOR_MIDDLEWARE_NAME$ = (req: Request, res: Response, next: NextFunction) => {
    const rules = {
        $VALIDATOR_MIDDLEWARE_RULES$
    };

    requestValidator(rules, req, res, next);
};

$VALIDATOR_MIDDLEWARES$