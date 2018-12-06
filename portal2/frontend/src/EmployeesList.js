import React, {  Component  } from 'react';

import EmployeeService from './EmployeeService';

const employeeService = new EmployeeService();


class EmployeeList extends Component {

  constructor(props) {
    super(props);
    this.state = {
      employees: [],
      nextPageURL: ''
    };
    this.nextPage = this.nextPage.bind(this);
    this.handleDelete = this.handleDelete.bind(this);
  }

  componentDidMount() {
    var self = this;
    employeeService.getEmployees().then(function (result) {
      self.setState({  employees: result.data, nextPageURL: result.nextLink})
    });
  }

  handleDelete(e, pk) {
    var self = this;
    employeeService.deleteEmployee({pk: pk}).then(()=>{
      var newArr = self.state.employees.filter(function(obj) {
        return obj.pk !== pk;
      });
      self.setState({employees: newArr})
    });
  }

  nextPage(){
    var self = this;
    EmployeeService.getEmployeesByURL(this.state.nextPageURL).then((result)=> {
      self.setState({ employees: result.data, nextPageURL: result.nextLink})
    });
  }

  render() {
    return (
      <div className="employees--list">
        <table className="table">
          <thead key="thead">
          <tr>
            <th>#</th>
    )
  }

}
export default EmployeeList;
