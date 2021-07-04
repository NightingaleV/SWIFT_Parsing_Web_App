// External imports
import React, {useState, useEffect} from 'react';
import classNames from 'classnames';
import axios from 'axios';
import moment from 'moment'

import {truncate} from '../../../utils';

// Assets

export function SourceFileList(props) {
    const {sourceFiles} = props

    // return (
    //     <>
    //         <div className="card">
    //             <div className="card-header border-0">
    //                 <div className="row align-items-center">
    //                     <div className="col">
    //                         <h3 className="mb-0">Source Files</h3>
    //                     </div>
    //
    //                     <div className="col text-right">
    //                         <a href="#!" className="btn btn-sm btn-primary">See all</a>
    //                     </div>
    //                 </div>
    //             </div>
    //             <div className="table-responsive">
    //                 <table className="table align-items-center table-flush">
    //                     <thead className="thead-light">
    //                     <tr>
    //                         <th scope="col">File Name</th>
    //
    //                         <th scope="col">Created At</th>
    //                         <th scope="col">Size (Msgs)</th>
    //                     </tr>
    //                     </thead>
    //                     <tbody>
    //                     {sourceFiles.map(({created_at, file_name, total_msg_ctn}) =>
    //                         <tr key={file_name}>
    //                             <th scope="row">
    //                                 {truncate(file_name, 18)}
    //                             </th>
    //                             <td>
    //                                 {moment(created_at).format('DD. MM. HH:MM')}
    //                             </td>
    //                             <td>
    //                                 {total_msg_ctn}
    //                             </td>
    //                         </tr>
    //                     )}
    //                     </tbody>
    //                 </table>
    //             </div>
    //         </div>
    //     </>
    // );

    return (
        <>

            <div className="card">
                <div className="card-header border-0">
                    <div className="row align-items-center">
                        <div className="col">
                            <h3 className="mb-0">Source Files</h3>
                        </div>

                        <div className="col text-right">
                            <a href="#!" className="btn btn-sm btn-primary">See all</a>
                        </div>
                    </div>
                </div>
                <div className="list-group">
                    {sourceFiles.map(({created_at, file_name, total_msg_ctn}) =>
                        <a href=""
                           className="list-group-item list-group-item-action  d-flex justify-content-between align-items-center">
                            <span>{truncate(file_name, 20)} </span>
                            {/*<span>{moment(created_at).format('DD. MM. HH:MM')}</span>*/}
                            <span
                                className="badge badge-lg badge-floating text-pwc-medium-grey bg-pwc-light-grey border-white badge-pill">{total_msg_ctn}</span>
                        </a>
                    )}

                </div>
            </div>
        </>
    );
}