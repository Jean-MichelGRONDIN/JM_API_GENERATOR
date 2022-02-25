export const $CONTROLLER_CONTROLLER_NAME$ = $DTO_ASYNC_PLACEHOLDER$(req: Request, res: Response) => {
    let data: ($CONTROLLER_CONTROLLER_DTO_STRUC_NAME$|ErrorDataFromRequest) = await $CONTROLLER_CONTROLLER_DTO_FUNC_NAME$(req);
    if (data instanceof ErrorDataFromRequest) {
        $CONTROLLER_CONTROLLER_DTO_ERROR_RES$
        return;
    }

    let resDB = await $CONTROLLER_CONTROLLER_ACTION_NAME$(data);
    if (resDB instanceof ErrorDB) {
        $CONTROLLER_CONTROLLER_DB_ERROR_RES$
        return;
    }

    $CONTROLLER_CONTROLLER_SUCESS_RES$
};

$CONTROLLER_PLACEHOLDER$