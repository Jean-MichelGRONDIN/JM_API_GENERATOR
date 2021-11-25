export let $CONTROLLER_CONTROLLER_NAME$ = (req: Request, res: Response) => {
    $CONTROLLER_CONTROLLER_DTO_FUNC_NAME$(req)
    .then((data: $CONTROLLER_CONTROLLER_DTO_STRUC_NAME$) => {
        $CONTROLLER_CONTROLLER_ACTION_NAME$(data).then((resDB: $CONTROLLER_CONTROLLER_ACTION_RET_TYPE$) => {
            $CONTROLLER_CONTROLLER_SUCESS_RES$
        }).catch((error: ErrorDB) => {
            $CONTROLLER_CONTROLLER_DB_ERROR_RES$
        });
    })
    .catch((error: ErrorDataFromRequest) => {
        $CONTROLLER_CONTROLLER_DTO_ERROR_RES$
    });
};

$CONTROLLER_PLACEHOLDER$