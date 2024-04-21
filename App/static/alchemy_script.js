function openFilterMenu(id)
{
  // alert(id);
  let overlay = document.getElementById(id).style.display = "flex";
}

function closeFilterMenu(id)
{
  document.getElementById(id).style.display = "none";
}

function switchTabs(id)
{
  if(id == "project-tab")
  {  
    document.getElementById("project-tab").classList.add("selected");
    document.getElementById("student-tab").classList.remove("selected");

    document.getElementById("project-pane").style.display = "flex";
    document.getElementById("student-pane").style.display = "none";
  }
  else if(id == "student-tab")
  {
    document.getElementById("student-tab").classList.add("selected");
    document.getElementById("project-tab").classList.remove("selected");

    document.getElementById("student-pane").style.display = "flex";
    document.getElementById("project-pane").style.display = "none";
  }
}

function addDiscipline()
{  
  let field_area = document.getElementById("discipline-field");

  let course = document.createElement('div');

  course.id = `discipline-${field_area.childElementCount}`;

  course.style.display = 'flex';
  course.style.flexDirection = 'row';
  course.style.alignItems = 'center';

  course.innerHTML =
  `
  <label for="discipline-list" class ="form-field-item">Discipline ${field_area.childElementCount}:</label>

  <select id="discipline-list" name="disciplines[]" class="form-field-item" required>

    <option value="" disabled selected>[select]</option>
    <option value="Discipline1" class="select">Discipline1</option>
    <option value="Discipline2" class="select">Discipline2</option>
    <option value="Discipline3" class="select">Discipline3</option>
    <option value="Discipline4" class="select">Discipline4</option>
    <option value="Discipline5" class="select">Discipline5</option>

  </select>

  <div class = "button-compound" style="width:10vw; height:40px;"> 

    <div class="button-compound contrast" onclick="removeDiscipline('discipline-${field_area.childElementCount}')">

      <img src ="/static/icons/close_black.svg" class="button-compound-image">
      <div class="button-compound-text">
        REMOVE
      </div>

    </div>

  </div>
  `;

  let button = document.createElement('div');

  button.setAttribute ('id', 'add-discipline-button');
  button.classList.add("button-compound");
  button.style.width = '10vw';

  button.innerHTML =
  `
  <div class = "pane-header-button"> 

    <div class="button-compound contrast" onclick="addDiscipline()">

      <img src ="/static/icons/add_black.svg" class="button-compound-image">
      <div class="button-compound-text">
        ADD
      </div>

    </div>

  </div>
  `;

  document.getElementById("add-discipline-button").remove();
  field_area.appendChild(course);
  field_area.appendChild(button);

  document.getElementById("form").scrollBy(0, 70);

  //alert(`Field area now has ${field_area.childElementCount} children`);
}

function removeDiscipline(id)
{
  document.getElementById(id).remove();

  let disciplines = document.getElementById("discipline-field").children;

  let count = 0;

  for (let i = 0; i < disciplines.length-1; i++)
  {
    let discipline = disciplines[i];

    //alert(`${course.children[0].innerHTML} vs Course ${i+1}:`);

    if(discipline.children[0].innerHTML != `Discipline ${i+1}:`)
    {

      discipline.children[0].innerHTML = `Discipline ${i+1}:`;
      count++;
    }
  }

  document.getElementById("form").scrollBy(0, -70);
  //alert(count);
}

function addCourse()
{  
  let field_area = document.getElementById("course-field");
  
  let course = document.createElement('div');
  
  course.id = `course-${field_area.childElementCount}`;
  
  course.style.display = 'flex';
  course.style.flexDirection = 'row';
  course.style.alignItems = 'center';
  
  course.innerHTML =
  `
  <label for="course-list" class ="form-field-item">Course ${field_area.childElementCount}:</label>
  
  <select id="course-list" name="courses[]" class="form-field-item" required>
    
    <option value="" disabled selected>[select]</option>
    <option value="Course1" class="select">Course1</option>
    <option value="Course2" class="select">Course2</option>
    <option value="Course3" class="select">Course3</option>
    <option value="Course4" class="select">Course4</option>
    <option value="Course5" class="select">Course5</option>

  </select>

  <div class = "button-compound" style="width:10vw; height:40px;"> 

    <div class="button-compound contrast" onclick="removeCourse('course-${field_area.childElementCount}')">

      <img src ="/static/icons/close_black.svg" class="button-compound-image">
      <div class="button-compound-text">
        REMOVE
      </div>

    </div>

  </div>
  `;

  let button = document.createElement('div');

  button.setAttribute ('id', 'add-course-button');
  button.classList.add("button-compound");
  button.style.width = '10vw';
  
  button.innerHTML =
  `
  <div class = "pane-header-button"> 

    <div class="button-compound contrast" onclick="addCourse()">

      <img src ="/static/icons/add_black.svg" class="button-compound-image">
      <div class="button-compound-text">
        ADD
      </div>

    </div>

  </div>
  `;
  
  document.getElementById("add-course-button").remove();
  field_area.appendChild(course);
  field_area.appendChild(button);

  document.getElementById("form").scrollBy(0, 70);

  //alert(`Field area now has ${field_area.childElementCount} children`);
}

function removeCourse(id)
{
  document.getElementById(id).remove();

  let courses = document.getElementById("course-field").children;

  let count = 0;

  for (let i = 0; i < courses.length-1; i++)
  {
    let course = courses[i];

    //alert(`${course.children[0].innerHTML} vs Course ${i+1}:`);

    if(course.children[0].innerHTML != `Course ${i+1}:`)
    {

      course.children[0].innerHTML = `Course ${i+1}:`;
      count++;
    }
  }

  document.getElementById("form").scrollBy(0, -70);

  //alert(count);
}

// function addCourseToFormOld()
// {
//   let field_area = document.getElementById("course-field");
  
//   let course = 
//   `
//     <div id = "course-${field_area.childElementCount}" style="display:flex; flex-direction:row; align-items:center;">
    
//       <label for="course_filter" class ="form-field-item">
//         Course ${field_area.childElementCount}:
//       </label>
      
//       <select id="minor2" name="minor2" class="form-field-item" required>
        
//         <option value="" disabled selected>[select]</option>
//         <option value="Course1" class="select">Course1</option>
//         <option value="Course2" class="select">Course2</option>
//         <option value="Course3" class="select">Course3</option>
//         <option value="Course4" class="select">Course4</option>
//         <option value="Course5" class="select">Course5</option>
  
//       </select>

//       <div class = "button-compound" style="width:10vw; height:40px;"> 

//         <div class="button-compound contrast" onclick="remove('course-${field_area.childElementCount}')">

//           <img src ="close_black.svg" class="button-compound-image">
//           <div class="button-compound-text">
//             REMOVE
//           </div>

//         </div>

//       </div>
      
//     </div>
//   `;
  
//   let add_button =
//   `
//   <div class ="button-compound" id= "add-course-button" style="width:10vw;">
                    
//     <div class = "pane-header-button"> 
  
//       <div class="button-compound contrast" onclick="addCourseToForm()">
  
//         <img src ="add_black.svg" class="button-compound-image">
//         <div class="button-compound-text">
//           ADD
//         </div>
  
//       </div>
  
//     </div>
    
//   </div>
//   `;

//   document.getElementById("add-course-button").remove();
//   field_area.innerHTML+= course + add_button;
//   document.getElementById("add-course-button").scrollIntoView();

//   // alert(field_area.childElementCount);
// }