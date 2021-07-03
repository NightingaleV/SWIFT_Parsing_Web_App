// External imports
import React from 'react';
import ReactDOM from 'react-dom';
// Internal imports
import {TopHeader, DataframeDashboard} from "./sweeper_dashboard/components/organisms";
//
// // function AllProviders({ children }) {
// //   return (
// //     <AuthProvider>
// //       <TimerProvider>
// //         <BrowserRouter>{children}</BrowserRouter>
// //       </TimerProvider>
// //     </AuthProvider>
// //   );
// // }
//
function App() {
    return (
        <>
            <header className="dashboard-header">
                <TopHeader/>
            </header>
            <main className="dashboard-content">
                <DataframeDashboard/>
            </main>
            <div className="modals-container">

            </div>
        </>
    );
}

ReactDOM.render(<App/>, document.getElementById('sweeper-dashboard-app'));