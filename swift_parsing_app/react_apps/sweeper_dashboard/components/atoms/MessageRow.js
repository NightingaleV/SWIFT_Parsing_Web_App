// External imports
import React, {useState, useEffect} from 'react';
import ReactPaginate from "react-paginate";
import classNames from 'classnames';
import {SourceFileList} from '../molecules'
import {truncate} from "../../../utils";

// Assets

export function MessageRow({message}) {
    const {transaction_id, message_type, direction} = message
    const trans_id_strip_num = transaction_id.replace(/[0-9]/g, '');

    return (
        <>
            <tr key={transaction_id}>
                <th scope="row">
                    0551665IWOAJIEJGF
                </th>
                <td>
                    <a className="btn" data-toggle="collapse" href={'#' + trans_id_strip_num}
                       role="button" aria-expanded="false" aria-controls={message_type}>
                        <i className="fas fa-chevron-left text-primary mr-3"/>
                    </a>
                </td>
                <td>
                    {transaction_id}
                </td>
                <td>
                    <i className={classNames('fas mr-3',
                        direction === 'Incoming' && 'fa-arrow-left text-primary',
                        direction === 'Outgoing' && 'fa-arrow-right text-secondary'
                    )}/> {direction}
                </td>
                <td>
                    {message_type}
                </td>
            </tr>
            <tr className="collapse" id={trans_id_strip_num}>
                <th scope="row">
                    <i className="fas fa-long-arrow-alt-right text-primary ml-5"></i>
                </th>
                <td>
awd
                </td>
                 <td>
awd
                </td>
                <td>
awd
                </td>
                <td>
awd
                </td>
            </tr>
        </>
    );
}