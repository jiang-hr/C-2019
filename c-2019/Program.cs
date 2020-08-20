using System;
using System.IO;
using System.Net;
using System.Text.RegularExpressions;
using System.Threading;

namespace c_2019
{
    internal class ResourcePool
    {
        public static string HttpGet(string Url, string contentType)
        {
            try
            {
                string retString = string.Empty;

                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(Url);
                request.Method = "GET";
                request.ContentType = contentType;

                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                Stream myResponseStream = response.GetResponseStream();
                StreamReader streamReader = new StreamReader(myResponseStream);
                retString = streamReader.ReadToEnd();
                streamReader.Close();
                myResponseStream.Close();
                return retString;
            }
            catch (Exception ex)
            {
                return ex.Message;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string head = "time,numbers,enter,leave";
            Console.WriteLine(head);
            using (StreamWriter file = new StreamWriter(@"val.csv", true))
            {
                file.Write(head);
            }
            for (; ; )
            {
                string ans = NetworkAirport.getContent();
                Console.WriteLine(ans);
                using (StreamWriter file = new StreamWriter(@"val.csv", true))
                {
                    file.WriteLine(ans);
                }
                Thread.Sleep(5000);
            }
        }
    }

    class NetworkAirport
    {
        public static string getContent()
        {
            try
            {
                string ans = "";
                string head = "http://www.whalebj.com";
                string content = ResourcePool.HttpGet(head + "/xzjc/default.aspx", "");

                string pattern = "截止目前为止（[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*）";
                MatchCollection mc = Regex.Matches(content, pattern);
                string time = mc[0].Value.Substring(7, 19);
                ans += time + ",";

                pattern = "场内待运车辆数为：[0-9]*";
                mc = Regex.Matches(content, pattern);
                string vehiclesNumColl = mc[0].Value.Substring(9);
                ans += vehiclesNumColl + ",";

                pattern = "前半小时进场车辆数为：[0-9]*";
                mc = Regex.Matches(content, pattern);
                vehiclesNumColl = mc[0].Value.Substring(11);
                ans += vehiclesNumColl + ",";

                pattern = "前半小时离场车辆数为：[0-9]*";
                mc = Regex.Matches(content, pattern);
                vehiclesNumColl = mc[0].Value.Substring(11);
                ans += vehiclesNumColl;

                return ans;
            }
            catch (Exception e)
            {
                return "";
            }
        }
    }
}
