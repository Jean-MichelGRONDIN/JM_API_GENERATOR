import express, {Request, Response, NextFunction} from 'express';
import API_APPINESS from './config/config';
import routes from './router/index';

// Our Express APP config
const app = express();
app.set('port', API_APPINESS.API.getInstance().Port || 3000);
app.set('env', API_APPINESS.API.getInstance().Mode);

//-- CORS
app.use((req: Request, res: Response, next: NextFunction) => {
    res.header('Access-Control-Allow-Origin', API_APPINESS.API.getInstance().Cors);
    res.header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS, PATCH');
    res.header('Access-Control-Allow-Headers', '*');
    next();
});

// middlewares

app.use(express.json());
app.use(express.urlencoded({extended: true}));

// API Endpoints
app.use(routes);

// export our app
export default app;