import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import morgan from "morgan"


dotenv.config();

const port = parseInt(process.env.PORT || "8080");
const app = express();


app.use(morgan('dev'));
app.use(cors({origin: 'http://localhost:3000'}));




app.listen(port,  () => {
    console.log(`Application started on URL http://localhost:${port}`);
});
