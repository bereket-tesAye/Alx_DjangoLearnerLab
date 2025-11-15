Permissions and Groups Setup:

- Book model permissions:
    can_view, can_create, can_edit, can_delete
- Groups:
    Viewers: can_view
    Editors: can_create, can_edit
    Admins: all permissions
- Views enforce permissions using @permission_required
- To test:
    - Assign users to groups
    - Log in and try accessing different views
    - Users without permissions will get 403 Forbidden
