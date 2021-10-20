import {Picture} from "../models/dataPicture";
import {Playlist} from "../models/dataPlaylist";


const getPicture =  (request, response) => {
     Picture.find((error, picture) => {
        if (error) {
            return response.status(500).json(
                {
                    success: false,
                }
            );
        } else {
            return response.status(201).json(
                {
                    data: picture,
                    success: true,
                }
            );
        }
    })
}

const getPlaylist = async (request, response, next) => {
    await Playlist.find((error, playlist) => {
        if (error) {
            return response.status(500).json(
                {
                    success: false,
                }
            );
        } else {
            return response.status(201).json(
                {
                    data: playlist,
                    success: true,
                }
            );
        }
    })

}

export {
    getPicture
}

export {
    getPlaylist
}
