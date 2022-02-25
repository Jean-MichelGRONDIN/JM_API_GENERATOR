    let data: ($CONTROLLER_CONTROLLER_DTO_STRUC_NAME$|ErrorDataFromRequest) = await $CONTROLLER_CONTROLLER_DTO_FUNC_NAME$(req);
    if (data instanceof ErrorDataFromRequest) {
        $CONTROLLER_CONTROLLER_DTO_ERROR_RES$
        return;
    }

