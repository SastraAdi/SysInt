ServiceReference1.Service1Client sc = new ServiceReference1.Service1Client();

lblResult.Text = "";
double x = 0,y=0;
if (double.TryParse(txtNumber1.Text, out x) && double.TryParse(txtNumber2.Text, out y))
lblResult.Text = sc.Add(x, y).ToString();
else
{
MessageBox.Show("Please enter valid number");
}




    double x = 0, y = 0;
lblResult.Text = "";
    if (double.TryParse(txtNumber1.Text, out x) && double.TryParse(txtNumber2.Text, out y))
      lblResult.Text = sc.Subtract(x, y).ToString();
    else
    {
      MessageBox.Show("Please enter valid number");
    }
