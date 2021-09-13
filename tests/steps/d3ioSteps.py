from behave import *
import time

use_step_matcher("re")


@Given("User navigates to d3io page")
def step_impl(context):
    context.helperfunc.open('https://www.d3a.io/login')
    context.helperfunc.maximize()


@When('User enters the credentials with username as "(.*)" and password as "(.*)"')
def step_impl(context, username, password):
    username_ele = context.helperfunc.find_by_id("email")
    username_ele.send_keys(username)
    password_ele = context.helperfunc.find_by_id("password")
    password_ele.send_keys(password)


@Then('User clicks submit button')
def step_impl(context):
    submit_ele = context.helperfunc.find_by_xpath("//button/span[text()='Login']")
    submit_ele.click()


@Then('User verifies login success')
def step_impl(context):
    home_page_title_ele = context.helperfunc.find_by_xpath("//h1[text()='Home']")
    assert home_page_title_ele.text == 'Home'


@Then('User creates a project named "(.*)" after successful login')
def step_impl(context, project_name):
    project_ele = context.helperfunc.find_by_xpath("//*[@class='icon-projects ']")
    project_ele.click()
    new_project_ele = context.helperfunc.find_by_xpath("//button/span[text()='new project']")
    new_project_ele.click()
    project_name_ele = context.helperfunc.find_by_id("input-field-name")
    project_name_ele.send_keys(project_name)
    project_desc_ele = context.helperfunc.find_by_id("textarea-field-nameTextArea")
    project_desc_ele.send_keys("This is my first project")
    add_button_ele = context.helperfunc.find_by_xpath("//button/span[text()='Add']")
    add_button_ele.click()


@Then('User validates that the "(.*)" is created successfully')
def step_impl(context, project_name):
    created_proj_ele = context.helperfunc.find_by_xpath("//span[text()='" + project_name + "']")
    assert created_proj_ele.text == project_name


@Then('User creates the simulation for the "(.*)"')
def step_impl(context, project_name):
    project_ele = context.helperfunc.find_by_xpath("//*[@class='icon-projects ']")
    project_ele.click()
    created_proj_ele = context.helperfunc.find_by_xpath("//span[text()='" + project_name + "']")
    created_proj_ele.click()
    new_simulation_ele = context.helperfunc.find_by_xpath("//button/span[text()='new simulation']")
    new_simulation_ele.click()
    simu_desc_ele = context.helperfunc.find_by_id("textarea-field-description")
    simu_desc_ele.send_keys("default")
    next_button_ele = context.helperfunc.find_by_xpath("//button/span[text()='Next']")
    next_button_ele.click()
    time.sleep(2)


@Then('User validates the simulation is created successfully')
def step_impl(context):
    project_ele = context.helperfunc.find_by_xpath("//*[@class='icon-projects ']")
    project_ele.click()
    time.sleep(2)
    created_simulation = context.helperfunc.find_by_xpath("//p[text()='default simulation']")
    assert created_simulation.text == "default simulation"


@Then('User deletes the project')
def step_impl(context):
    settings_ele = context.helperfunc.find_by_xpath("//div[@class='saved-project__cog']")
    settings_ele.click()
    delete_ele = context.helperfunc.find_by_xpath("//button/p[text()='Delete']")
    delete_ele.click()
    sure_ele = context.helperfunc.find_by_xpath("//*[text()=\"I'm sure\"]")
    sure_ele.click()
