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

                <td>
                    <a className="" data-toggle="collapse" href={'#' + trans_id_strip_num}
                       role="button" aria-expanded="false" aria-controls={message_type}>
                        <i className="fas fa-chevron-right text-primary mr-3"/>
                    </a>
                </td>
                <td scope="row">
                    0551665IWOAJIEJGF
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
                <th>
                    Mandatory
                </th>
                <th>
                    Field Name
                </th>
                <th>
                    Field Tag
                </th>
                <th>
                    Content Options
                </th>
                <th>
                    Field Value
                </th>
            </tr>
            <tr className="collapse" id={trans_id_strip_num}>
                <td>

                </td>
                <td>
                    20
                </td>
                <td>
                    Sender's Reference
                </td>
                <td>
                    16x
                </td>
                <td>
                    0000000000000000
                </td>
            </tr>
            <tr className="collapse" id={trans_id_strip_num}>
                <td>

                </td>
                <td>
                    32B
                </td>
                <td>
                    Currency/Transaction Amount
                </td>
                <td>
                    3!a15d
                </td>
                <td>
                    20100622
                </td>
            </tr>

        </>
    );
}