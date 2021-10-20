import { Router } from "express";
import {getPicture, getPlaylist} from "../controllers/dataPicturePlaylist.controller";

const dataPicturePlaylistRoute = () =>{

    const router = Router();
    router.get('/data-picture', getPicture);
    router.get('/data-playlist',getPlaylist);

}


export {
    dataPicturePlaylistRoute
}
