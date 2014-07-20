# Upload Resource .logs to an S3 bucket manually
# Only process .log files! Do not process this file!

2000-01-01 00:00:00,000 MISTAKE [UpmAsynchronousTaskManager:thread-2] [atlassian.upm.manager.PluginInstallationServiceImpl] installPlugin com.atlassian.upm.spi.PluginInstallException: Failed to install OBR jar artifact
 -- referer: https://powerme.pwrplan.com/plugins/servlet/upm | url: /rest/plugins/1.0/ | userName: sysadmin
com.atlassian.upm.spi.PluginInstallException: Failed to install OBR jar artifact
	at com.atlassian.upm.manager.install.ObrPluginInstallHandler.installPluginInternal(ObrPluginInstallHandler.java:157)
	at com.atlassian.upm.manager.install.AbstractPluginInstallHandler.installPlugin(AbstractPluginInstallHandler.java:55)
	at com.atlassian.upm.manager.PluginInstallationServiceImpl.installPlugin(PluginInstallationServiceImpl.java:85)
	at com.atlassian.upm.manager.PluginInstaller.execute(PluginInstaller.java:141)
	at com.atlassian.upm.manager.PluginInstaller.install(PluginInstaller.java:96)
	at com.atlassian.upm.rest.resources.install.InstallTask.installFromFile(InstallTask.java:121)
	at com.atlassian.upm.rest.resources.install.InstallFromFileTask.executeTask(InstallFromFileTask.java:39)
	at com.atlassian.upm.rest.resources.install.InstallTask.call(InstallTask.java:62)
	at com.atlassian.upm.rest.resources.install.InstallTask.call(InstallTask.java:32)
	at com.atlassian.upm.rest.async.AsynchronousTaskManager$1.call(AsynchronousTaskManager.java:77)
	at com.atlassian.upm.rest.async.AsynchronousTaskManager$1.call(AsynchronousTaskManager.java:72)
	at com.atlassian.sal.core.executor.ThreadLocalDelegateCallable.call(ThreadLocalDelegateCallable.java:42)
	at java.util.concurrent.FutureTask$Sync.innerRun(Unknown Source)
	at java.util.concurrent.FutureTask.run(Unknown Source)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
	at java.lang.Thread.run(Unknown Source)
