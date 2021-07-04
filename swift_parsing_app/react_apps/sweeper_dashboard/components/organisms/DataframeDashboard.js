// External imports
import React, {useEffect, useState} from 'react';
// import classNames from 'classnames';
import {SourceFileList, MessageList} from '../molecules'
import axios from "axios";
import {requestConfig} from "../../../utils";

// Assets

export function DataframeDashboard(props) {

    const [sourceFiles, setSourceFiles] = useState([]);
    const [sourceFileDetail, setSourceFileDetail] = useState({swift_messages:[]});

    const fetchSourceFiles = async () => {
        try {
            const res = await axios.get('/api/source-files/', requestConfig);
            // setUserGroups(res.data);
            setSourceFiles(res.data.results)
        } catch (err) {
            console.log(err);
        }
    };

    const fetchSourceFileMessages = async (fileId) => {
        try {
            const res = await axios.get('/api/source-files/' + 6, requestConfig);
            // console.log(res.data);
            // console.log(res.data);
            // setUserGroups(res.data);
            setSourceFileDetail(res.data)
        } catch (err) {
            console.log(err);
        }
    };
    //
    useEffect(() => {
        fetchSourceFiles();
        fetchSourceFileMessages();
    }, []);


    return (
        <>
            <div className="row">
                <div className="col-xl-2">
                    <SourceFileList sourceFiles={sourceFiles}/>
                </div>
                <div className="col-xl-6">
                    <MessageList sourceFileDetail={sourceFileDetail}/>
                </div>
            </div>
        </>
    );
}