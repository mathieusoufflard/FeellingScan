import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import morgan from "morgan"
import {connectToDatabase} from "./src/config/databaseConnection";
import {dataPicturePlaylistRoute} from "./src/routes/dataPicturePlaylist.route";


dotenv.config();

const port = parseInt(process.env.PORT || "8080");
const app = express();


app.use(morgan('dev'));
app.use(cors({}));


app.use("/", dataPicturePlaylistRoute);

app.listen(port,  async () => {
    await connectToDatabase()
    console.log(`Application started on URL http://localhost:${port}`);
});
