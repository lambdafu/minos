/* Imports */
var Navbar = ReactBootstrap.Navbar;
var Nav = ReactBootstrap.Nav;
var NavItem = ReactBootstrap.NavItem;
var NavDropdown = ReactBootstrap.NavDropdown;
var MenuItem = ReactBootstrap.MenuItem;
var Button = ReactBootstrap.Button;
var Grid = ReactBootstrap.Grid;
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;
var PageHeader = ReactBootstrap.PageHeader;
var Table = ReactBootstrap.Table;

var Provider = ReactRedux.Provider;

var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var IndexRoute = ReactRouter.IndexRoute;
var hashHistory = ReactRouter.hashHistory;
var Link = ReactRouter.Link;

var LinkContainer = ReactRouterBootstrap.LinkContainer;

/* Redux state.  */

function actionInfoSet(data) {
    let payload = { data: data };
    return { type: 'actionInfoSet', payload: payload };
}

/* Reducer */
function minos_info(state, action) {
    if (state === undefined) {
	return {
	    name: "minos",
	    version: "0.0.0",
	};
    }
    
    switch (action.type) {
    case 'actionInfoSet':
	let data = action.payload.data;
	state = { ...state,
		  name: data.name,
		  version: data.version
		};
	break;
    default:
	break;
    }
    
    return state;
}

function minos_data(state, action) {
    if (state === undefined) {
	return {
	    experiments: [ { id: 1, name: "apn5", dim: 5, jobs: 12 },
			   { id: 2, name: "apn6", dim: 6, jobs: 27 } ],
	    jobs: [ { id: 1, name: "apn5", jobs: 12 },
		    { id: 2, name: "apn6", jobs: 27 } ]
	};
    }
    
    return state;
}

var minos_reducer = Redux.combineReducers({ info: minos_info, data: minos_data });
var store = Redux.createStore(minos_reducer);

axios.get('/api/status')
    .then((response) => {
	store.dispatch(actionInfoSet(response.data));
    });


/* VIEW */
const mapStateToProps = (state) => {
    return {
	name: state.info.name,
	version: state.info.version,
	experiments: state.data.experiments,
	jobs: state.data.jobs
    }
};

const MinosNav_ = (props) => (
<Navbar fluid={true}>
  <Navbar.Header>
    <Navbar.Brand>
      <Link to="/">{ props.name } { props.version }</Link>
    </Navbar.Brand>
  </Navbar.Header>
  <Nav>
    <LinkContainer to="/experiment">
      <NavItem eventKey={1}>Experiments</NavItem>
    </LinkContainer>
    <LinkContainer to="/job">
      <NavItem eventKey={2}>Jobs</NavItem>
    </LinkContainer>
  </Nav>
</Navbar>
);
/* https://github.com/react-bootstrap/react-router-bootstrap/issues/152 */
const MinosNav = ReactRedux.connect(mapStateToProps, null, null, { pure: false })(MinosNav_);

const Status_ = (props) => <div><h1>Status</h1><p>All systems fully operational.</p></div>;
const Status = ReactRedux.connect(mapStateToProps, null, null, { pure: false })(Status_);

const Experiments_ = (props) => (
<div>
  <h1>All Experiments</h1>
  <Table>
    <thead>
      <tr><th>#</th><th>Name</th><th>Dimension</th><th>Jobs</th></tr>
    </thead>
    <tbody>
	{ props.experiments.map((item) => (
		<tr>
		  <td>{ item.id }</td>
		  <td><Link to={"/experiment/" + item.id}>{item.name}</Link></td>
		  <td>{ item.dim }</td>
		  <td>{ item.jobs }</td>
		</tr>
	)) }
    </tbody>
  </Table>
</div>
);
const Experiments = ReactRedux.connect(mapStateToProps, null, null, { pure: false })(Experiments_);

const Experiment_ = (props) => <div><h1>Experiment { props.params.id }</h1></div>;
const Experiment = ReactRedux.connect(mapStateToProps, null, null, { pure: false })(Experiment_);

const Jobs_ = (props) => <div><h1>All Jobs</h1></div>;
const Jobs = ReactRedux.connect(mapStateToProps, null, null, { pure: false })(Jobs_);

const Job_ = (props) => <div><h1>Job { props.params.id }</h1></div>;
const Job = ReactRedux.connect(mapStateToProps, null, null, { pure: false })(Job_);

const Minos = (props) => (
<Provider store={store}>
<div>
  <MinosNav />
  <Grid fluid={true}>
    {props.children}
  </Grid>
</div>
</Provider>
);
      
ReactDOM.render((
  <Router history={hashHistory}>
    <Route path="/" component={Minos}>
      <IndexRoute component={Status} />
      <Route path="experiment">
        <IndexRoute component={Experiments} />
        <Route path=":id" component={Experiment} />
      </Route>
      <Route path="job">
        <IndexRoute component={Jobs} />
        <Route path=":id" component={Job} />
      </Route>
    </Route>
  </Router>
), document.getElementById("content"))
