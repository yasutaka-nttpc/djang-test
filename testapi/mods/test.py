class Stub:
  def ret_data(self):
    return 'test module'

  def get_pop3(self):
    return '0.0.0.0'

  def get_imap(self):
    return '255.255.255.255'

  def get_smtpauth(self):
    return True

  def get_submission(self):
    return '1.2.3.4, 5.6.7.8'

  def post_pop3(self, ip):
    return '255.255.255.255/32'

  def post_imap(self, ip):
    return '1.2.3.4/32, 5.6.7.8/32'

  def post_smtpauth(self, ip):
    return False

  def post_submission(self, ip):
    return '0.0.0.0/32'


if __name__ == '__main__':
  a = Stub()
  print(a.ret_data())
