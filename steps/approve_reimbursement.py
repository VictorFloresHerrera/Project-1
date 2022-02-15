import time
from behave import Given, When, Then


@Given(u'The manager is in the manager page')
def manager_log_in(context):
    context.driver.get(r"C:\Users\itsvi\Desktop\Project1\web_files\html\manager_page.html")


@When(u'the manager enter the reimbursement id in the reimbursement id input box')
def enter_reimbursement_id(context):
    context.approve_reimbursement.select_reimbursement_id().send_keys("85")


@When(u'the manager enter the employee id in the employee id input box')
def enter_employee_id(context):
    context.approve_reimbursement.select_employee_id().send_keys("1")


@When(u'the manager enter the manager id in the manager id input box')
def enter_manager_id(context):
    context.approve_reimbursement.select_manager_id().send_keys("1")


@When(u'the manager enter the reimbursement amount in the reimbursement amount input box')
def enter_reimbursement_amount_requested(context):
    context.approve_reimbursement.select_reimbursement().send_keys("100")


@When(u'the manager enter the reason in the reason input box')
def enter_employee_reason(context):
    context.approve_reimbursement.select_reason().send_keys("food")


@When(u'the manager enter the approval in the approval input box')
def enter_approval(context):
    context.approve_reimbursement.select_approval().send_keys("Approve")


@When(u'the manager enter the manager comment in the manager comment input box')
def enter_manager_comment(context):
    context.approve_reimbursement.select_manager_comment().send_keys("?")


@When(u'the manager clicks the approve button')
def click_approve_button(context):
    context.approve_reimbursement.select_approve_button().click()


@Then(u'one reimbursement is approved and sent to the previous reimbursements')
def manager_refreshes_page(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Manager Page"
