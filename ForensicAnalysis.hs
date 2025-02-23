module ForensicAnalysis where

import Data.Time.Clock
import Data.Time.Format
import System.IO
import System.Process

data SystemInfo = SystemInfo {
    timestamp :: UTCTime,
    cpuUsage :: Float,
    memoryInfo :: String,
    diskUsage :: String,
    networkConnections :: String,
    runningProcesses :: String
} deriving (Show)

parseSystemInfo :: String -> IO SystemInfo
parseSystemInfo logData = do
    let [timestampStr, cpuUsageStr, memoryInfoStr, diskUsageStr, networkConnectionsStr, runningProcessesStr] = lines logData
    let timestamp = parseTimeOrError True defaultTimeLocale (iso8601DateFormat (Just "%H:%M:%S")) timestampStr
    let cpuUsage = read cpuUsageStr :: Float
    return $ SystemInfo timestamp cpuUsage memoryInfoStr diskUsageStr networkConnectionsStr runningProcessesStr

analyzeLogs :: String -> IO ()
analyzeLogs logs = do
    putStrLn "Analisi dei log completata"

main :: IO ()
main = do
    let sampleLogData = "2025-02-23T11:41:51Z\n15.0\nMemory Info\nDisk Usage\nNetwork Connections\nRunning Processes"
    systemInfo <- parseSystemInfo sampleLogData
    putStrLn $ "Parsed system info: " ++ show(systemInfo)
    let sampleLogs = "Sample log data..."
    analyzeLogs(sampleLogs)