import { validatorAndSanitizerRequest } from './../request/validator/indexRequest';
import { validatorAndSanitizerSanitizer } from './../request/sanitizer/indexSanitizer';
import { Router } from "express";
import { awesome, hello, hi, validatorAndSanitizer } from "../controller/index.controller";

const router = Router();

router.get("/authorization", (req, res) => {
    res.send("GET OAUTH");
});

router.get("/refresh", (req, res) => {
    res.send("REFRESH JWT");
});


// All request from mobile
router.get("/app/hi", hi);


// All request from web
router.get("/web/awesome", awesome);

// test the sanitizer and request's validator on one arg in the body (it's name => 'tested_string')
router.post("/testValidatorAndSanitizer", validatorAndSanitizerSanitizer, validatorAndSanitizerRequest, validatorAndSanitizer);

// All request from desktop
router.get("/desktop/hello", hello);


// hasJWT
// hasOAuth
// hasRole
// refresh
// storeRefresh |=> CRUD
// generateJWT
// currentUser
// currentRole
export default router;
