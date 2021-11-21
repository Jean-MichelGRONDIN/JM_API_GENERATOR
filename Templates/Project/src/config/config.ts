import * as dotenv from 'dotenv';

dotenv.config();

namespace API_APPINESS {
    class Security {
        constructor() {
            this.AccessTokenDuration = this.getEnvNumber("API_ACCESS_TOKEN");
            this.OAuthID = this.getEnvString("API_OAUTH_ID");
            this.OAuthSecret = this.getEnvString("API_OAUTH_SECRET");
            this.RefreshTokenDuration = this.getEnvNumber("API_REFRESH_TOKEN");
            this.Secret = this.getEnvString("API_SECRET");
        }

        private getEnvNumber(key: string): number {
            const env: (string | undefined) = process.env[key];
            let result: number;

            if (env) {
                result = parseInt(env);
            } else {
                return 0;
            }
            return result;
        }

        private getEnvString(key: string): string {
            const env: (string | undefined) = process.env[key];
            let result: string;

            if (env) {
                result = env;
            } else {
                return "";
            }
            return result;
        }
        public Secret: string;
        public AccessTokenDuration: number;
        public RefreshTokenDuration: number;
        public OAuthID: string;
        public OAuthSecret: string;
    }

    class Database {
        constructor() {
            this.Database = this.getEnvString("POSTGRES_DB");
            this.Host = this.getEnvString("POSTGRES_HOST");
            this.Password = this.getEnvString("POSTGRES_PASSWORD");
            this.Port = this.getEnvNumber("POSTGRES_PORT");
            this.User = this.getEnvString("POSTGRES_USER");
        }

        private getEnvNumber(key: string): number {
            const env: (string | undefined) = process.env[key];
            let result: number;

            if (env) {
                result = parseInt(env);
            } else {
                return 0;
            }
            return result;
        }

        private getEnvString(key: string): string {
            const env: (string | undefined) = process.env[key];
            let result: string;

            if (env) {
                result = env;
            } else {
                return "";
            }
            return result;
        }

        public Host: string;
        public Database: string;
        public User: string;
        public Password: string;
        public Port: number;
    }

    class Mail {
        constructor() {
            this.From = this.getEnvString("API_MAIL_FROM");
            this.Host = this.getEnvString("API_MAIL_HOST");
            this.Password = this.getEnvString("API_MAIL_PASSWORD");
            this.Port = this.getEnvNumber("API_MAIL_PORT");
            this.User = this.getEnvString("API_MAIL_USER");
        }

        private getEnvNumber(key: string): number {
            const env: (string | undefined) = process.env[key];
            let result: number;

            if (env) {
                result = parseInt(env);
            } else {
                return 0;
            }
            return result;
        }

        private getEnvString(key: string): string {
            const env: (string | undefined) = process.env[key];
            let result: string;

            if (env) {
                result = env;
            } else {
                return "";
            }
            return result;
        }
    
        public From: string;
        public User: string;
        public Password: string;
        public Host: string;
        public Port: number;
    }

    class Version {
        constructor() {
            this.Android = this.getEnvString("VERSION_ANDROID");
            this.IOS = this.getEnvString("VERSION_IOS");
            this.PWA = this.getEnvString("VERSION_PWA");
        }

        private getEnvString(key: string): string {
            const env: (string | undefined) = process.env[key];
            let result: string;

            if (env) {
                result = env;
            } else {
                return "";
            }
            return result;
        }

        public IOS: string;
        public Android: string;
        public PWA: string;
    }

    export class API {
        private static insrance: API
        private constructor() {

            this.Mode = this.getEnvString("API_MODE");
            this.Domain = this.getEnvString("API_DOMAIN");
            this.Port = this.getEnvNumber("API_PORT");
            this.Host = this.getEnvString("API_HOST");
            this.FrontHost = this.getEnvString("FRONT_HOST");
            this.TimeZone = this.getEnvString("API_TZ");
            this.Cors = this.getEnvArrayString("API_CORS");
            this.SSL = this.getEnvBoolean("API_SSL");
            this.Cert = this.getEnvString("API_CERT");
            this.Key = this.getEnvString("API_KEY");

            this.Security = new Security();
            this.Database = new Database();
            this.Mail = new Mail();
            this.Version = new Version();
        }
    
        private getEnvNumber(key: string): number {
            const env: (string | undefined) = process.env[key];
            let result: number;

            if (env) {
                result = parseInt(env);
            } else {
                return 0;
            }
            return result;
        }

        private getEnvArrayString(key: string): string[] {
            const env: (string | undefined) = process.env[key];
            let result: string[];

            if (env) {
                result = env.split(",");
            } else {
                return [""];
            }
            return result;
        }

        private getEnvBoolean(key: string): boolean {
            const env: (string | undefined) = process.env[key];
            let result: boolean;

            if (env) {
                if (env === "true") {
                    result = true;
                } else {
                    result = false;
                }
            } else {
                return false;
            }
            return result;
        }

        private getEnvString(key: string): string {
            const env: (string | undefined) = process.env[key];
            let result: string;

            if (env) {
                result = env;
            } else {
                return "";
            }
            return result;
        }

        public static getInstance(): API {
            if (!API.insrance) {
                API.insrance = new API();
            }
    
            return API.insrance;
        }

        public Mode: string;
        public Domain: string;
        public Port: number;
        public Host: string;
        public FrontHost: string;
        public TimeZone: string;
        public Cors: string[];
        public SSL: boolean;
        public Cert: string;
        public Key: string;
        public Security: Security;
        public Database: Database;
        public Mail: Mail;
        public Version: Version;
    }
}

export default API_APPINESS;