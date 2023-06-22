import frappe
from frappe import _
from frappe.utils.background_jobs import get_jobs
from erpnext.stock.doctype.repost_item_valuation.repost_item_valuation import repost_entries


@frappe.whitelist()
def processing_documents_repost_entries(company):

    try:

        processing_repost_entries()

        return "okay"


    except Exception as error:

        frappe.log_error(message=frappe.get_traceback(), title="processing_documents_repost_entries")

        pass

    return "error"


def processing_repost_entries():

    # Validar duplicacion de ejecución de proceso
    enqueued_method = 'process_repost_entries.process_repost_entries.uses_cases.repost_item_valuation.ejecutar_proceso' 
    jobs = get_jobs()

    if not jobs or enqueued_method not in jobs[frappe.local.site]:

        frappe.enqueue(enqueued_method, queue='long', is_async=True, timeout=28800)


def ejecutar_proceso():

    repost_entries(bandera=True)

    return
