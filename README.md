
private void Form1_Load(object sender, EventArgs e) {
client = new SoapClient(); ServicePointManager.Expect100Continue = true;
ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
string acctName = "youraccountemail@xxx.com"; //"YOUR DEVORG USERNAME"; string acctPw = "YourPassword”+”Yoursecuritytoken";
try
{
loginResult = client.login(null, acctName, acctPw);
}
catch (Exception ex) {
MessageBox.Show(ex.Message+ " and "+ ex.StackTrace);
if (ex.Data != null) {
MessageBox.Show("You failed to login");
Close(); }
}
MessageBox.Show("Congratulations: Login succeeded "); // success
}

SystInt20242U2NB4W1al22qUqVIakjbqZjM
------


MessageBox.Show("Username: " + loginResult.userInfo.userName + "\n" + "Organization Id " + loginResult.userInfo.organizationId + "\n"
+ "Organization Name " + loginResult.userInfo.organizationName + "\n" + "User full Name " + loginResult.userInfo.userFullName + "\n"
+ "User Type " + loginResult.userInfo.userType + "\n"
+ "User Email " + loginResult.userInfo.userEmail + "\n"
+ "Profile ID " + loginResult.userInfo.profileId + "\n",
"User Information for " + loginResult.userInfo.userFullName + "\n", MessageBoxButtons.OKCancel, MessageBoxIcon.Information);
