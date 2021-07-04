// External imports
import React, {useEffect} from 'react';
// import classNames from 'classnames';
import {SourceFileList} from '../molecules'
import {truncate} from "../../../utils";

// Assets

export function MessageList(props) {

    const {sourceFileDetail} = props
    const messageList = sourceFileDetail.swift_messages


    return (
        <>
            <div className="card">
                <div className="card-header border-0">
                    <div className="row align-items-center">
                        <div className="col">
                            <h3 className="mb-0">Page visits</h3>
                        </div>
                        <div className="col text-right">
                            <a href="" className="btn btn-sm btn-primary">See all</a>
                        </div>
                    </div>
                </div>
                <div className="table-responsive">
                    <table className="table align-items-center table-flush">
                        <thead className="thead-light">
                        <tr>
                            <th scope="col">Ref ID</th>
                            <th scope="col">Transaction Id</th>
                            <th scope="col">Field</th>
                            <th scope="col">Values</th>
                        </tr>
                        </thead>
                        <tbody>
                        {messageList.map(({transaction_id, direction, message_type}) =>
                            <tr>
                                <th scope="row">
                                    0551665IWOAJIEJGF
                                </th>
                                <td>
                                    {transaction_id}
                                </td>
                                <td>
                                    <i className="fas fa-arrow-down text-danger mr-3"></i> {direction}
                                </td>
                                <td>
                                    {message_type}
                                </td>
                            </tr>
                        )}
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    );
}