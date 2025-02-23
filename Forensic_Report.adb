with Ada.Text_IO;

procedure Forensic_Report is
   procedure Write_HTML_Report (System_Info : String; Logs : String; Analysis : String) is
   begin
      Ada.Text_IO.Put_Line ("<html>");
      Ada.Text_IO.Put_Line ("<head><title>SilentAutopsy Report</title></head>");
      Ada.Text_IO.Put_Line ("<body>");
      Ada.Text_IO.Put_Line ("<h1>SilentAutopsy Report</h1>");
      Ada.Text_IO.Put_Line ("<h2>Developed by Jashin L.</h2>");
      Ada.Text_IO.Put_Line ("<h1>System Information</h1>");
      Ada.Text_IO.Put_Line (System_Info);
      Ada.Text_IO.Put_Line ("<h1>Logs</h1>");
      Ada.Text_IO.Put_Line (Logs);
      Ada.Text_IO.Put_Line ("<h1>AI Analysis</h1>");
      Ada.Text_IO.Put_Line (Analysis);
      Ada.Text_IO.Put_Line ("</body>");
      Ada.Text_IO.Put_Line ("</html>");
   end Write_HTML_Report;

begin
   Write_HTML_Report ("<ul><li>Timestamp: 2025-02-23T11:41:51Z</li></ul>", "<pre>Log data...</pre>", "<pre>AI Analysis data...</pre>");
end Forensic_Report;