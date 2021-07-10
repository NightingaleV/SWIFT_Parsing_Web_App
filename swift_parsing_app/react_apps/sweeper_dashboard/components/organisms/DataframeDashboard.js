// External imports
import React, {useEffect, useState} from 'react';
// import classNames from 'classnames';
import {SourceFileList, MessageList} from '../molecules'
import axios from "axios";
import {requestConfig} from "../../../utils";

// Assets
export function DataframeDashboard(props) {

    const [sourceFiles, setSourceFiles] = useState([]);
    const [sourceFileDetail, setSourceFileDetail] = useState({
        fileId: 6,
        swiftMessageList: []
    });

    const fetchSourceFiles = async () => {
        try {
            const res = await axios.get('/api/source-files/', requestConfig);
            setSourceFiles(res.data.results)
        } catch (err) {
            console.log(err);
        }
    };

    // PAGINATION
    const [pageNumber, setPageNumber] = useState(1);
    const [totalPageCtn, setTotalPageNumbers] = useState(0);
    const fetchSourceFileMessages = async (fileId, pageNumber) => {
        try {
            const res = await axios.get('/api/source-files/' + fileId + '/related_messages/?page=' + pageNumber, requestConfig);
            const {total_pages, results} = res.data
            setTotalPageNumbers(total_pages)
            setSourceFileDetail({...sourceFileDetail, swiftMessageList: results})
        } catch (err) {
            console.log(err);
        }
    };

    const selectSourceFile = (file_id) => {
        setSourceFileDetail({...sourceFileDetail, fileId: file_id});
    };

    //
    useEffect(() => {
        fetchSourceFiles();
        // fetchSourceFileMessages(6, 1);
    }, []);


    useEffect(() => {
        fetchSourceFileMessages(sourceFileDetail.fileId, pageNumber);
    }, [pageNumber, sourceFileDetail.fileId]);

    return (
        <>
            <div className="row">
                <div className="col-xl-3">
                    <SourceFileList sourceFiles={sourceFiles}
                                    selectSourceFile={selectSourceFile}/>
                </div>
                <div className="col-xl-9">
                    <MessageList
                        setPageNumber={setPageNumber}
                        totalPageCtn={totalPageCtn}
                        swiftMessageList={sourceFileDetail.swiftMessageList}/>
                </div>
            </div>
        </>
    );
}