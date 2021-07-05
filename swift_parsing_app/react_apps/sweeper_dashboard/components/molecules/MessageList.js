// External imports
import React, {useState, useEffect} from 'react';
import ReactPaginate from "react-paginate";
// import classNames from 'classnames';
import {SourceFileList} from '../molecules'
import {truncate} from "../../../utils";

// Assets

export function MessageList(props) {

    const {swiftMessageList, setPageNumber, totalPageCtn} = props
    // const messageList = sourceFileDetail.swift_messages
    // const [pageNumber, setPageNumber] = useState(0);

    const changePage = ({selected}) => {
        // this component indexes from 0 so first page has index 0, that's why we increase by one to get real number
        const realPageNumber = selected + 1
        setPageNumber(realPageNumber);
        console.log(realPageNumber);
    };

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
                        {swiftMessageList.map(({transaction_id, direction, message_type}) =>
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
                    <nav aria-label="Page navigation example">
                        <ReactPaginate
                            previousLabel={<> <i className="fa fa-angle-left"></i>
                                <span className="sr-only">Previous</span></>}
                            nextLabel={<>  <i className="fa fa-angle-right"></i>
                                <span className="sr-only">Next</span></>}
                            pageCount={totalPageCtn}
                            onPageChange={changePage}
                            containerClassName={"pagination justify-content-center"}
                            pageClassName={'page-item'}
                            breakClassName={'page-item'}
                            previousClassName={'page-item'}
                            nextClassName={'page-item'}
                            pageLinkClassName={"page-link"}
                            breakLinkClassName={"page-link"}
                            previousLinkClassName={"page-link"}
                            nextLinkClassName={"page-link"}
                            disabledClassName={"disabled"}
                            activeClassName={"active"}/>
                    </nav>


                </div>
            </div>
        </>
    );
}