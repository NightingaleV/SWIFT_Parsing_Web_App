// External imports
import React, {useEffect} from 'react';
// import classNames from 'classnames';
import {SourceFileList} from '../molecules'
// Assets

export function DataframeDashboard(props) {

    return (
        <>
            <div className="row">
                <div className="col-xl-4">
<SourceFileList/>
                </div>
            </div>
        </>
    );
}