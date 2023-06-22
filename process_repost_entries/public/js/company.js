frappe.ui.form.on("Company", "refresh", function(frm) {
    frm.add_custom_button(__("Repost Item Valuation"), () => {
        frappe.confirm(__("This action will create background job. Are you certain?"), function() {
            frappe.call({
                method: "process_repost_entries.process_repost_entries.uses_cases.repost_item_valuation.processing_documents_repost_entries",
                args: {
                    company: frm.doc.name
                },
                freeze: true,
                callback: () => {
                    frappe.msgprint({
                        title: __("Sync Started"),
                        message: __("The process has started in the background."),
                        alert: 1
                    });
                }
            });
        });
    });
    });
