import React from 'react';
import { BrowserRouter, Route, Switch } from "react-router-dom";
import './App.css';

function App() {
  return (
    <React.Fragment>
      <BrowserRouter
      basename={process.env.REACT_APP_rOUTER_BASE || ""}>
        <layout>
          <Switch>
            <Route exact path="/" component={HomeView} />
          </Switch>
        </layout>
      </BrowserRouter>
    </React.Fragment>
  );
}

export default App;
