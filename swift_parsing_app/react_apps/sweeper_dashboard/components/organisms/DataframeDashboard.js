// External imports
import React, {useEffect, useState} from 'react';
// import classNames from 'classnames';
import {SourceFileList, MessageList} from '../molecules'
import axios from "axios";
import {requestConfig} from "../../../utils";

// Assets

export function DataframeDashboard(props) {

    const [sourceFiles, setSourceFiles] = useState([]);
    const [sourceFileDetail, setSourceFileDetail] = useState({swiftMessageList: []});
    const [pageNumber, setPageNumber] = useState(0);
    const [totalPageCtn, setTotalPageNumbers] = useState(0);

    const fetchSourceFiles = async () => {
        try {
            const res = await axios.get('/api/source-files/', requestConfig);
            // setUserGroups(res.data);
            // setSourceFiles(res.data.results)
        } catch (err) {
            console.log(err);
        }
    };

    const fetchSourceFileMessages = async (fileId, pageNumber) => {
        try {
            const res = await axios.get('/api/source-files/6/related_messages/?page=' + pageNumber, requestConfig);
            // console.log(res.data);
            console.log(res.data);
            setTotalPageNumbers(res.data.total_pages)
            setSourceFileDetail({swiftMessageList: res.data.results})
            // setUserGroups(res.data);
            // setSourceFileDetail(res.data)
        } catch (err) {
            console.log(err);
        }
    };
    //
    useEffect(() => {
        fetchSourceFiles();
        fetchSourceFileMessages(6, 1);
    }, []);


    useEffect(() => {
        fetchSourceFileMessages(6, pageNumber);
    }, [pageNumber]);

    return (
        <>
            <div className="row">
                <div className="col-xl-2">
                    <SourceFileList sourceFiles={sourceFiles}/>
                </div>
                <div className="col-xl-6">
                    <MessageList
                        setPageNumber={setPageNumber}
                        totalPageCtn={totalPageCtn}
                        swiftMessageList={sourceFileDetail.swiftMessageList}/>
                </div>
            </div>
        </>
    );
}