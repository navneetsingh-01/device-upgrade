import time
import sys
import ansible_runner

# precheck_out, precheck_err, precheck_rc = ansible_runner.run_command(
#     executable_cmd='ansible-playbook',
#     cmdline_args=['/home/singhnavneet.su/device-upgrade/project/precheck.yaml',
#                   '-i', 'inventory', '-vvvv', '--tags', '9k', '--vault-id', 'vault_password'],
#     input_fd=sys.stdin,
#     output_fd=sys.stdout,
#     error_fd=sys.stderr,
# )
# print("rc: {}".format(precheck_out))
# print("out: {}".format(precheck_err))
# print("err: {}".format(precheck_rc))

# if precheck_rc == 0:
prestage_out, prestage_err, prestage_rc = ansible_runner.run_command(
    executable_cmd='ansible-playbook',
    cmdline_args=['/home/singhnavneet.su/device-upgrade/project/prestage.yaml',
                  '-i', 'inventory', '-vvvv', '--tags', '9k', '--vault-id', 'vault_password', '--extra-vars', 'rsync_host', 'syd-netft-lp001'],
    input_fd=sys.stdin,
    output_fd=sys.stdout,
    error_fd=sys.stderr,
)
print("rc: {}".format(prestage_out))
print("out: {}".format(prestage_err))
print("err: {}".format(prestage_rc))

# if precheck_rc == 0 and prestage_rc == 0:
#     os_install_out, os_install_err, os_install_rc = ansible_runner.run_command(
#         executable_cmd='ansible-playbook',
#         cmdline_args=['/home/singhnavneet.su/device-upgrade/project/os_install.yaml',
#                       '-i', 'inventory', '-vvvv', '--tags', '9k'],
#         input_fd=sys.stdin,
#         output_fd=sys.stdout,
#         error_fd=sys.stderr,
#     )
#     print("rc: {}".format(os_install_out))
#     print("out: {}".format(os_install_err))
#     print("err: {}".format(os_install_rc))

# time.sleep(600)

# if precheck_rc == 0 and prestage_rc == 0 and os_install_rc == 0:
#     postcheck_out, postcheck_err, postcheck_rc = ansible_runner.run_command(
#         executable_cmd='ansible-playbook',
#         cmdline_args=['/home/singhnavneet.su/device-upgrade/project/postcheck.yaml',
#                       '-i', 'inventory', '-vvvv', '--tags', '9k'],
#         input_fd=sys.stdin,
#         output_fd=sys.stdout,
#         error_fd=sys.stderr,
#     )
#     print("rc: {}".format(postcheck_out))
#     print("out: {}".format(postcheck_err))
#     print("err: {}".format(postcheck_rc))

# if prestage_err == 0 and os_install_err == 0 and postcheck_err == 0:
# if os_install_err == 0 and postcheck_err == 0:
# if postcheck_err == 0:
#     epld_install_out, epld_install_err, epld_install_rc = ansible_runner.run_command(
#         executable_cmd='ansible-playbook',
#         cmdline_args=['/home/singhnavneet.su/device-upgrade/project/epld_install.yaml',
#                       '-i', 'inventory', '-vvvv', '--tags', '7k'],
#         input_fd=sys.stdin,
#         output_fd=sys.stdout,
#         error_fd=sys.stderr,
#     )
#     print("rc: {}".format(epld_install_out))
#     print("out: {}".format(epld_install_err))
#     print("err: {}".format(epld_install_rc))
