import app from "./app";
import https from 'https';
import http from 'http';
import path from "path";

import fs from 'fs';
import API_APPINESS from "./config/config";


const banner = `     
 █████╗ ██████╗ ██╗       █████╗ ██╗   ██╗████████╗██╗  ██╗       █████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██║      ██╔══██╗██║   ██║╚══██╔══╝██║  ██║      ██╔══██╗██╔══██╗██╔══██╗
███████║██████╔╝██║█████╗███████║██║   ██║   ██║   ███████║█████╗███████║██████╔╝██████╔╝
██╔══██║██╔═══╝ ██║╚════╝██╔══██║██║   ██║   ██║   ██╔══██║╚════╝██╔══██║██╔═══╝ ██╔═══╝ 
██║  ██║██║     ██║      ██║  ██║╚██████╔╝   ██║   ██║  ██║      ██║  ██║██║     ██║     
╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝      ╚═╝  ╚═╝╚═╝     ╚═╝ `;

if (API_APPINESS.API.getInstance().SSL) {
    const httpsServer = https.createServer({
        key: fs.readFileSync(path.join(__dirname.replace("dist", API_APPINESS.API.getInstance().Key))),
        cert: fs.readFileSync(path.join(__dirname.replace("dist", API_APPINESS.API.getInstance().Cert))),
        passphrase: 'BE HAPPY'
    }, app);

    httpsServer.listen(app.get("port"), () => {
        console.log(banner);
        console.log(`\n\n\t    🚀🚀🚀 https://localhost:${app.get("port")} in ${app.get("env")} mode`);
    });

} else {
    const httpServer = http.createServer(app);

    httpServer.listen(app.get("port"), () => {
        console.log(banner);
        console.log(`\n\n\t    🚀🚀🚀 http://localhost:${app.get("port")} in ${app.get("env")} mode`);
    });
} 
