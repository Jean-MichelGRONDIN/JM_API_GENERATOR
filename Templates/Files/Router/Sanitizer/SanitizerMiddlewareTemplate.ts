export let $SANITIZER_MIDDLEWARE_NAME$ = (req: Request, res: Response, next: NextFunction) => {
    const rules = {
        $SANITIZER_MIDDLEWARE_RULES$
    };

    requestSanitizer(rules, req, res, next);
};

$SANITIZER_MIDDLEWARES$