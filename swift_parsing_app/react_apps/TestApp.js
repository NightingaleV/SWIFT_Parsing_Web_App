// External imports
import React from 'react';
import ReactDOM from 'react-dom';
// Internal imports
//
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
            <div className="alert alert-success" role="alert">
                <strong>It just works!</strong> React is working fine! Just fine!
            </div>
        </>
    );
}

ReactDOM.render(<App/>, document.getElementById('test-app'));